#!/usr/bin/env python3
"""
Skill Dependency Analyzer

Scans available skills and extracts metadata about:
- Tool dependencies (bash, web_search, etc.)
- File format associations (docx, pdf, xlsx, etc.)
- Domain overlap and relationships
- Complexity indicators (token usage, tool call frequency)
"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Tuple

class SkillAnalyzer:
    def __init__(self, skills_dir: str = "/mnt/skills"):
        self.skills_dir = Path(skills_dir)
        self.skills = {}
        self.tool_patterns = [
            'bash_tool', 'web_search', 'web_fetch', 'drive_search',
            'google_drive_search', 'google_drive_fetch', 'conversation_search',
            'recent_chats', 'view', 'create_file', 'str_replace'
        ]
        self.format_patterns = [
            'docx', 'pdf', 'pptx', 'xlsx', 'csv', 'json', 'html', 'jsx',
            'markdown', 'svg', 'png', 'jpg', 'gif', 'xml', 'yaml'
        ]
        
    def scan_skills(self) -> Dict:
        """Scan all available skills and parse their metadata."""
        for skill_type in ['public', 'user', 'examples']:
            skill_path = self.skills_dir / skill_type
            if not skill_path.exists():
                continue
                
            for skill_dir in skill_path.iterdir():
                if not skill_dir.is_dir():
                    continue
                    
                skill_md = skill_dir / "SKILL.md"
                if skill_md.exists():
                    self.parse_skill(skill_md, skill_type)
        
        return self.skills
    
    def parse_skill(self, skill_path: Path, skill_type: str):
        """Parse a SKILL.md file and extract metadata."""
        with open(skill_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract YAML frontmatter
        frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not frontmatter_match:
            return
        
        frontmatter = yaml.safe_load(frontmatter_match.group(1))
        body = content[frontmatter_match.end():]
        
        skill_name = frontmatter.get('name', skill_path.parent.name)
        
        # Analyze skill content
        self.skills[skill_name] = {
            'type': skill_type,
            'name': skill_name,
            'description': frontmatter.get('description', ''),
            'path': str(skill_path.parent),
            'tools': self.extract_tools(body),
            'formats': self.extract_formats(body),
            'domains': self.extract_domains(body, frontmatter.get('description', '')),
            'size': len(body),
            'has_scripts': (skill_path.parent / 'scripts').exists(),
            'has_references': (skill_path.parent / 'references').exists(),
            'has_assets': (skill_path.parent / 'assets').exists(),
            'complexity_score': self.calculate_complexity(body),
            'bundled_files': self.count_bundled_files(skill_path.parent)
        }
    
    def extract_tools(self, content: str) -> Set[str]:
        """Extract tool dependencies mentioned in skill content."""
        tools = set()
        for tool in self.tool_patterns:
            # Look for tool usage patterns
            if re.search(rf'\b{tool}\b', content, re.IGNORECASE):
                tools.add(tool)
        return tools
    
    def extract_formats(self, content: str) -> Set[str]:
        """Extract file format associations."""
        formats = set()
        for fmt in self.format_patterns:
            # Look for format mentions (case-insensitive, whole word)
            if re.search(rf'\b{fmt}\b', content, re.IGNORECASE):
                formats.add(fmt.lower())
        return formats
    
    def extract_domains(self, content: str, description: str) -> Set[str]:
        """Extract domain keywords (heuristic-based)."""
        domains = set()
        
        # Domain keywords to look for
        domain_keywords = {
            'document': ['document', 'writing', 'text', 'report'],
            'presentation': ['presentation', 'slide', 'deck'],
            'spreadsheet': ['spreadsheet', 'excel', 'data', 'table'],
            'pdf': ['pdf'],
            'web': ['web', 'html', 'frontend', 'website'],
            'research': ['research', 'search', 'analysis'],
            'coding': ['code', 'programming', 'script', 'development'],
            'financial': ['financial', 'finance', 'revenue', 'budget'],
            'ai': ['ai', 'llm', 'model', 'prompt'],
            'business': ['business', 'strategy', 'pitch', 'startup']
        }
        
        combined_text = (content + ' ' + description).lower()
        
        for domain, keywords in domain_keywords.items():
            if any(kw in combined_text for kw in keywords):
                domains.add(domain)
        
        return domains
    
    def calculate_complexity(self, content: str) -> int:
        """Calculate a complexity score based on content characteristics."""
        score = 0
        
        # Length contributes to complexity
        score += len(content) // 1000
        
        # Multiple steps/sections increase complexity
        score += len(re.findall(r'##', content)) * 2
        
        # Code blocks indicate complexity
        score += len(re.findall(r'```', content))
        
        # Tool calls indicate complexity
        score += len(re.findall(r'<invoke', content)) * 3
        
        return score
    
    def count_bundled_files(self, skill_dir: Path) -> Dict[str, int]:
        """Count bundled resources in scripts/, references/, assets/."""
        counts = {'scripts': 0, 'references': 0, 'assets': 0}
        
        for resource_type in counts.keys():
            resource_dir = skill_dir / resource_type
            if resource_dir.exists():
                counts[resource_type] = len(list(resource_dir.glob('*')))
        
        return counts
    
    def find_dependencies(self) -> Dict[str, List[str]]:
        """Find skills that commonly work together based on shared characteristics."""
        dependencies = defaultdict(list)
        
        skills_list = list(self.skills.values())
        
        for i, skill_a in enumerate(skills_list):
            for skill_b in skills_list[i+1:]:
                # Check for shared tools
                shared_tools = skill_a['tools'] & skill_b['tools']
                
                # Check for shared formats
                shared_formats = skill_a['formats'] & skill_b['formats']
                
                # Check for shared domains
                shared_domains = skill_a['domains'] & skill_b['domains']
                
                # If they share multiple characteristics, they likely work together
                if len(shared_tools) >= 1 or len(shared_formats) >= 2 or len(shared_domains) >= 2:
                    dependencies[skill_a['name']].append(skill_b['name'])
                    dependencies[skill_b['name']].append(skill_a['name'])
        
        return dict(dependencies)
    
    def detect_format_conflicts(self) -> List[Dict]:
        """Detect skills that handle the same format with different approaches."""
        format_handlers = defaultdict(list)
        
        for skill_name, skill_data in self.skills.items():
            for fmt in skill_data['formats']:
                format_handlers[fmt].append({
                    'name': skill_name,
                    'tools': skill_data['tools'],
                    'complexity': skill_data['complexity_score']
                })
        
        conflicts = []
        for fmt, handlers in format_handlers.items():
            if len(handlers) > 1:
                # Check if they use different tools (potential conflict)
                tools_sets = [set(h['tools']) for h in handlers]
                if len(set(map(frozenset, tools_sets))) > 1:
                    conflicts.append({
                        'format': fmt,
                        'skills': [h['name'] for h in handlers],
                        'conflict_type': 'different_approaches'
                    })
        
        return conflicts
    
    def identify_token_heavy_combinations(self) -> List[Dict]:
        """Identify skill combinations that may cause token budget issues."""
        heavy_skills = [
            (name, data) for name, data in self.skills.items()
            if data['size'] > 3000 or data['complexity_score'] > 10
        ]
        
        combinations = []
        for i, (name_a, data_a) in enumerate(heavy_skills):
            for name_b, data_b in heavy_skills[i+1:]:
                # If they share domains, they might activate together
                if data_a['domains'] & data_b['domains']:
                    combinations.append({
                        'skills': [name_a, name_b],
                        'combined_size': data_a['size'] + data_b['size'],
                        'shared_domains': list(data_a['domains'] & data_b['domains'])
                    })
        
        return sorted(combinations, key=lambda x: x['combined_size'], reverse=True)
    
    def recommend_stacks(self, task_domain: str = None) -> List[Dict]:
        """Recommend optimal skill stacks for common workflows."""
        stacks = []
        
        # Document workflow stack
        doc_skills = [
            name for name, data in self.skills.items()
            if 'document' in data['domains'] or 'docx' in data['formats']
        ]
        if doc_skills:
            stacks.append({
                'name': 'Document Workflow',
                'skills': doc_skills,
                'use_case': 'Creating, editing, and analyzing documents'
            })
        
        # Presentation workflow stack
        pres_skills = [
            name for name, data in self.skills.items()
            if 'presentation' in data['domains'] or 'pptx' in data['formats']
        ]
        if pres_skills:
            stacks.append({
                'name': 'Presentation Workflow',
                'skills': pres_skills,
                'use_case': 'Creating and editing presentations'
            })
        
        # Research workflow stack
        research_skills = [
            name for name, data in self.skills.items()
            if 'research' in data['domains'] or 'web_search' in data['tools']
        ]
        if research_skills:
            stacks.append({
                'name': 'Research Workflow',
                'skills': research_skills,
                'use_case': 'Web research and information gathering'
            })
        
        # Data analysis stack
        data_skills = [
            name for name, data in self.skills.items()
            if 'spreadsheet' in data['domains'] or 'xlsx' in data['formats']
        ]
        if data_skills:
            stacks.append({
                'name': 'Data Analysis Workflow',
                'skills': data_skills,
                'use_case': 'Spreadsheet analysis and data processing'
            })
        
        return stacks


def main():
    """Run the skill analysis and output results."""
    analyzer = SkillAnalyzer()
    
    print("Scanning skills...")
    analyzer.scan_skills()
    
    print(f"\nFound {len(analyzer.skills)} skills\n")
    
    # Output basic skill information
    print("=== SKILL INVENTORY ===")
    for name, data in sorted(analyzer.skills.items()):
        print(f"{name} ({data['type']})")
        print(f"  Tools: {', '.join(data['tools']) if data['tools'] else 'none'}")
        print(f"  Formats: {', '.join(data['formats']) if data['formats'] else 'none'}")
        print(f"  Domains: {', '.join(data['domains']) if data['domains'] else 'none'}")
        print(f"  Complexity: {data['complexity_score']}")
        print()
    
    # Find dependencies
    print("\n=== SKILL DEPENDENCIES ===")
    dependencies = analyzer.find_dependencies()
    for skill, related in sorted(dependencies.items()):
        if related:
            print(f"{skill}: {', '.join(related[:5])}")
    
    # Detect conflicts
    print("\n=== FORMAT CONFLICTS ===")
    conflicts = analyzer.detect_format_conflicts()
    for conflict in conflicts:
        print(f"{conflict['format']}: {', '.join(conflict['skills'])}")
    
    # Token-heavy combinations
    print("\n=== TOKEN-HEAVY COMBINATIONS ===")
    heavy = analyzer.identify_token_heavy_combinations()
    for combo in heavy[:5]:
        print(f"{' + '.join(combo['skills'])}: {combo['combined_size']} tokens")
    
    # Recommended stacks
    print("\n=== RECOMMENDED STACKS ===")
    stacks = analyzer.recommend_stacks()
    for stack in stacks:
        print(f"{stack['name']}: {', '.join(stack['skills'][:5])}")


if __name__ == "__main__":
    main()
