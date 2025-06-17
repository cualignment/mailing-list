#!/usr/bin/env python3
"""
CAIAC Email Template Generator

This script generates customized HTML email templates by replacing placeholders
in the template.html file with your content.

Usage:
    python generate_email.py --title "Your Title" --p1 "First paragraph" --p2 "Second paragraph" --p3 "Third paragraph"
    
Or use the interactive mode:
    python generate_email.py
"""

import argparse
import os
import sys
from datetime import datetime

# Default values
DEFAULT_VALUES = {
    'TITLE': 'My Cool Template',
    'PREVIEW_TEXT': 'Template created by Designmodo.com',
    'PARAGRAPH_1': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam.',
    'PARAGRAPH_2': 'Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta.',
    'PARAGRAPH_3': 'Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.',
    'LOGO_URL': 'https://raw.githubusercontent.com/cualignment/mailing-list/main/assets/logo.png',
    'WEBSITE_URL': 'https://www.cualignment.org/',
    'GITHUB_URL': 'https://github.com/cualignment',
    'LINKEDIN_URL': 'https://www.linkedin.com/company/columbia-ai-alignment-club/',
    'ADDRESS': 'Dorms of John Jay and East Campus <3, New York, NY, 10027',
    'MANAGE_PREFERENCES_URL': 'https://LISTSERV.CUIT.COLUMBIA.EDU/scripts/wa.exe?SUBED1=CUALIGNMENT',
    'UNSUBSCRIBE_URL': 'https://LISTSERV.CUIT.COLUMBIA.EDU/scripts/wa.exe?SUBED1=CUALIGNMENT'
}

def load_template():
    """Load the HTML template file."""
    template_path = os.path.join(os.path.dirname(__file__), 'template.html')
    
    if not os.path.exists(template_path):
        print(f"❌ Template file not found: {template_path}")
        sys.exit(1)
    
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()

def generate_email(values):
    """Generate HTML email by replacing placeholders in template."""
    template = load_template()
    
    # Replace all placeholders
    for key, value in values.items():
        placeholder = f'{{{{{key}}}}}'
        template = template.replace(placeholder, value)
    
    return template

def save_email(html_content, filename=None):
    """Save the generated HTML to a file."""
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"email_{timestamp}.html"
    
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(output_dir, exist_ok=True)
    
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return filepath

def interactive_mode():
    """Run in interactive mode to collect user input."""
    print("🎨 CAIAC Email Template Generator")
    print("=================================")
    print("Enter your content (press Enter to use defaults):")
    print()
    
    values = DEFAULT_VALUES.copy()
    
    # Collect user input
    title = input(f"Title [{DEFAULT_VALUES['TITLE']}]: ").strip()
    if title:
        values['TITLE'] = title
    
    preview = input(f"Preview text [{DEFAULT_VALUES['PREVIEW_TEXT']}]: ").strip()
    if preview:
        values['PREVIEW_TEXT'] = preview
    
    p1 = input(f"Paragraph 1 [{DEFAULT_VALUES['PARAGRAPH_1'][:50]}...]: ").strip()
    if p1:
        values['PARAGRAPH_1'] = p1
    
    p2 = input(f"Paragraph 2 [{DEFAULT_VALUES['PARAGRAPH_2'][:50]}...]: ").strip()
    if p2:
        values['PARAGRAPH_2'] = p2
    
    p3 = input(f"Paragraph 3 [{DEFAULT_VALUES['PARAGRAPH_3'][:50]}...]: ").strip()
    if p3:
        values['PARAGRAPH_3'] = p3
    
    return values

def main():
    parser = argparse.ArgumentParser(description='Generate CAIAC email templates')
    parser.add_argument('--title', help='Email title')
    parser.add_argument('--preview', help='Preview text')
    parser.add_argument('--p1', help='First paragraph')
    parser.add_argument('--p2', help='Second paragraph')
    parser.add_argument('--p3', help='Third paragraph')
    parser.add_argument('--output', '-o', help='Output filename')
    parser.add_argument('--interactive', '-i', action='store_true', help='Run in interactive mode')
    
    args = parser.parse_args()
    
    if args.interactive or (not args.title and not args.p1):
        values = interactive_mode()
    else:
        values = DEFAULT_VALUES.copy()
        if args.title:
            values['TITLE'] = args.title
        if args.preview:
            values['PREVIEW_TEXT'] = args.preview
        if args.p1:
            values['PARAGRAPH_1'] = args.p1
        if args.p2:
            values['PARAGRAPH_2'] = args.p2
        if args.p3:
            values['PARAGRAPH_3'] = args.p3
    
    # Generate email
    print("\n🔄 Generating email...")
    html_content = generate_email(values)
    
    # Save email
    filepath = save_email(html_content, args.output)
    
    print(f"✅ Email generated successfully!")
    print(f"📄 Saved to: {filepath}")
    print(f"📊 File size: {len(html_content)} characters")
    print("\n💡 You can now upload this HTML file to your email service provider.")

if __name__ == '__main__':
    main()
