#!/usr/bin/env python3
"""
Bottleneck Detection for Skill Workflows

Identifies potential bottlenecks:
- Skills requiring many tool calls
- Skills with conflicting approaches
- Skills loading large reference files
- Token budget concerns with multiple activations
"""

import json
import sys
from pathlib import Path
from typing import Dict, List
from collections import defaultdict

class BottleneckDetector:
    def __init__(self, skill_data: Dict):
        # Convert lists to sets for set operations
        self.skills = {}
        for name, data in skill_data.items():
            self.skills[name] = data.copy()
            self.skills[name]['tools'] = set(data.get('tools', []))
            self.skills[name]['formats'] = set(data.get('formats', []))
            self.skills[name]['domains'] = set(data.get('domains', []))
        
        self.bottlenecks = {
            'high_tool_usage': [],
            'conflicting_approaches': [],
            'large_references': [],
            'token_budget_risks': [],
            'sequential_dependencies': []
        }
    
    def detect_high_tool_usage(self, threshold: int = 3):
        """Identify skills that require many tool calls."""
        for name, data in self.skills.items():
            if len(data['tools']) >= threshold:
                self.bottlenecks['high_tool_usage'].append({
                    'skill': name,
                    'tool_count': len(data['tools']),
                    'tools': list(data['tools']),
                    'impact': 'May slow down workflows due to multiple tool calls'
                })
    
    def detect_conflicting_approaches(self):
        """Find skills handling same formats with different tools."""
        format_handlers = defaultdict(list)
        
        for name, data in self.skills.items():
            for fmt in data['formats']:
                format_handlers[fmt].append({
                    'skill': name,
                    'tools': data['tools'],
                    'complexity': data['complexity_score']
                })
        
        for fmt, handlers in format_handlers.items():
            if len(handlers) >= 2:
                # Check for tool differences
                all_tools = [set(h['tools']) for h in handlers]
                unique_tool_combos = set(map(frozenset, all_tools))
                
                if len(unique_tool_combos) > 1:
                    self.bottlenecks['conflicting_approaches'].append({
                        'format': fmt,
                        'skills': [h['skill'] for h in handlers],
                        'approaches': {h['skill']: list(h['tools']) for h in handlers},
                        'impact': 'Inconsistent handling may confuse workflow selection'
                    })
    
    def detect_large_references(self, size_threshold: int = 5000):
        """Identify skills with large SKILL.md files that consume tokens."""
        for name, data in self.skills.items():
            if data['size'] > size_threshold:
                self.bottlenecks['large_references'].append({
                    'skill': name,
                    'size': data['size'],
                    'has_references': data['has_references'],
                    'impact': f'Consumes ~{data["size"] // 4} tokens when loaded',
                    'recommendation': 'Consider splitting into reference files' if not data['has_references'] else 'Already uses references'
                })
    
    def detect_token_budget_risks(self, combined_threshold: int = 8000):
        """Find skill combinations that risk exceeding token budgets."""
        large_skills = {
            name: data for name, data in self.skills.items()
            if data['size'] > 3000
        }
        
        # Find skills that might activate together
        for name_a, data_a in large_skills.items():
            for name_b, data_b in large_skills.items():
                if name_a >= name_b:
                    continue
                
                # Check if they share domains (likely to co-activate)
                shared_domains = data_a['domains'] & data_b['domains']
                
                if shared_domains:
                    combined_size = data_a['size'] + data_b['size']
                    if combined_size > combined_threshold:
                        self.bottlenecks['token_budget_risks'].append({
                            'skills': [name_a, name_b],
                            'combined_size': combined_size,
                            'shared_domains': list(shared_domains),
                            'impact': f'Combined token load: ~{combined_size // 4} tokens',
                            'recommendation': 'May need sequential processing instead of parallel'
                        })
    
    def detect_sequential_dependencies(self):
        """Identify skills that must run in sequence."""
        # Look for skills that produce outputs consumed by other skills
        producers = {}
        consumers = {}
        
        for name, data in self.skills.items():
            # Skills that create files are producers
            if 'create_file' in data['tools'] or data['has_scripts']:
                for fmt in data['formats']:
                    if fmt not in producers:
                        producers[fmt] = []
                    producers[fmt].append(name)
            
            # Skills that read specific formats are consumers
            if 'view' in data['tools'] or data['formats']:
                for fmt in data['formats']:
                    if fmt not in consumers:
                        consumers[fmt] = []
                    consumers[fmt].append(name)
        
        # Find format chains
        for fmt in set(producers.keys()) & set(consumers.keys()):
            if producers[fmt] and consumers[fmt]:
                self.bottlenecks['sequential_dependencies'].append({
                    'format': fmt,
                    'producers': producers[fmt],
                    'consumers': consumers[fmt],
                    'impact': 'Sequential workflow required',
                    'optimization': 'Consider batching operations'
                })
    
    def generate_report(self) -> str:
        """Generate a markdown report of all detected bottlenecks."""
        report_lines = ["# Skill Workflow Bottleneck Analysis\n"]
        
        # High tool usage
        if self.bottlenecks['high_tool_usage']:
            report_lines.append("## High Tool Usage Bottlenecks\n")
            report_lines.append("Skills requiring multiple tool calls:\n")
            for item in sorted(self.bottlenecks['high_tool_usage'], 
                             key=lambda x: x['tool_count'], reverse=True):
                report_lines.append(f"- **{item['skill']}** ({item['tool_count']} tools)")
                report_lines.append(f"  - Tools: {', '.join(item['tools'])}")
                report_lines.append(f"  - Impact: {item['impact']}\n")
        
        # Conflicting approaches
        if self.bottlenecks['conflicting_approaches']:
            report_lines.append("## Conflicting Approach Bottlenecks\n")
            report_lines.append("Multiple skills handling the same format differently:\n")
            for item in self.bottlenecks['conflicting_approaches']:
                report_lines.append(f"- **{item['format']}** format conflict")
                report_lines.append(f"  - Skills: {', '.join(item['skills'])}")
                for skill, tools in item['approaches'].items():
                    report_lines.append(f"  - {skill}: {', '.join(tools) if tools else 'no specific tools'}")
                report_lines.append(f"  - Impact: {item['impact']}\n")
        
        # Large references
        if self.bottlenecks['large_references']:
            report_lines.append("## Token Budget Bottlenecks\n")
            report_lines.append("Skills with large SKILL.md files:\n")
            for item in sorted(self.bottlenecks['large_references'], 
                             key=lambda x: x['size'], reverse=True):
                report_lines.append(f"- **{item['skill']}** ({item['size']} chars)")
                report_lines.append(f"  - Impact: {item['impact']}")
                report_lines.append(f"  - Recommendation: {item['recommendation']}\n")
        
        # Token budget risks
        if self.bottlenecks['token_budget_risks']:
            report_lines.append("## Co-Activation Token Risks\n")
            report_lines.append("Skill pairs that may exceed token budgets when used together:\n")
            for item in sorted(self.bottlenecks['token_budget_risks'], 
                             key=lambda x: x['combined_size'], reverse=True)[:10]:
                report_lines.append(f"- **{' + '.join(item['skills'])}**")
                report_lines.append(f"  - Combined size: {item['combined_size']} chars")
                report_lines.append(f"  - Shared domains: {', '.join(item['shared_domains'])}")
                report_lines.append(f"  - Impact: {item['impact']}")
                report_lines.append(f"  - Recommendation: {item['recommendation']}\n")
        
        # Sequential dependencies
        if self.bottlenecks['sequential_dependencies']:
            report_lines.append("## Sequential Workflow Dependencies\n")
            report_lines.append("Format chains requiring sequential processing:\n")
            for item in self.bottlenecks['sequential_dependencies']:
                report_lines.append(f"- **{item['format']}** format chain")
                report_lines.append(f"  - Producers: {', '.join(item['producers'])}")
                report_lines.append(f"  - Consumers: {', '.join(item['consumers'])}")
                report_lines.append(f"  - Impact: {item['impact']}")
                report_lines.append(f"  - Optimization: {item['optimization']}\n")
        
        if not any(self.bottlenecks.values()):
            report_lines.append("No significant bottlenecks detected.\n")
        
        return '\n'.join(report_lines)
    
    def run_all_detections(self):
        """Run all bottleneck detection methods."""
        self.detect_high_tool_usage()
        self.detect_conflicting_approaches()
        self.detect_large_references()
        self.detect_token_budget_risks()
        self.detect_sequential_dependencies()


def main():
    """Run bottleneck detection on skill data."""
    if len(sys.argv) > 1:
        # Load skill data from JSON file
        with open(sys.argv[1], 'r') as f:
            skill_data = json.load(f)
    else:
        print("Usage: detect_bottlenecks.py <skill_data.json>")
        print("Or use in conjunction with analyze_skills.py")
        sys.exit(1)
    
    detector = BottleneckDetector(skill_data)
    detector.run_all_detections()
    
    print(detector.generate_report())


if __name__ == "__main__":
    main()
