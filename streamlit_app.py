import streamlit as st
import re
from pathlib import Path

def load_html_template():
    """Load the HTML template from index.html"""
    html_file = Path("index.html")
    if html_file.exists():
        return html_file.read_text(encoding='utf-8')
    else:
        st.error("index.html file not found!")
        return None

def extract_content_module(html_content):
    """Extract the content between START MODULE: Content and END MODULE: Content"""
    pattern = r'(<!-- START MODULE: Content -->)(.*?)(<!-- END MODULE: Content -->)'
    match = re.search(pattern, html_content, re.DOTALL)
    if match:
        return match.group(2).strip()
    return None

def replace_content_module(html_content, new_content):
    """Replace the content module with new content"""
    pattern = r'(<!-- START MODULE: Content -->)(.*?)(<!-- END MODULE: Content -->)'
    replacement = f'<!-- START MODULE: Content -->\n{new_content}\n                                              <!-- END MODULE: Content -->'
    return re.sub(pattern, replacement, html_content, flags=re.DOTALL)

def generate_html_element(element_type, content, extra_style=""):
    """Generate HTML elements with proper styling"""
    base_style = "font-family: 'Fira Sans', Helvetica, Arial, sans-serif; color: #666666; text-align: left;"
    
    if element_type == "h1":
        style = "font-family: 'Fira Sans', Helvetica, Arial, sans-serif; font-size: 24px; color: #333333; text-align: center;"
        return f'<h1 style="{style}">{content}</h1>'
    elif element_type == "h2":
        style = "font-family: 'Fira Sans', Helvetica, Arial, sans-serif; font-size: 20px; color: #333333; text-align: left; font-weight: bold;"
        return f'<h2 style="{style}">{content}</h2>'
    elif element_type == "h3":
        style = "font-family: 'Fira Sans', Helvetica, Arial, sans-serif; font-size: 18px; color: #333333; text-align: left; font-weight: bold;"
        return f'<h3 style="{style}">{content}</h3>'
    elif element_type == "p":
        style = f"font-family: 'Fira Sans', Helvetica, Arial, sans-serif; font-size: 16px; color: #666666; text-align: left; {extra_style}"
        return f'<p style="{style}">{content}</p>'
    elif element_type == "ul":
        style = "font-family: 'Fira Sans', Helvetica, Arial, sans-serif; font-size: 16px; color: #666666; text-align: left; padding-left: 20px;"
        items = content.split('\n')
        list_items = '\n'.join([f'<li>{item.strip()}</li>' for item in items if item.strip()])
        return f'<ul style="{style}">\n{list_items}\n</ul>'

def initialize_session_state():
    """Initialize session state variables"""
    if 'email_title' not in st.session_state:
        st.session_state.email_title = "Email Title"
    if 'email_greeting' not in st.session_state:
        st.session_state.email_greeting = "Hi CAIAC, <br><br> In today's email...Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    if 'email_sections' not in st.session_state:
        st.session_state.email_sections = []
    if 'email_signature' not in st.session_state:
        st.session_state.email_signature = "Sincerely,<br>The CAIAC Team"

def add_section():
    """Add a new section to the email"""
    section_id = len(st.session_state.email_sections)
    new_section = {
        'id': section_id,
        'type': 'paragraph',
        'title': '',
        'content': '',
        'items': []
    }
    st.session_state.email_sections.append(new_section)

def remove_section(section_id):
    """Remove a section from the email"""
    st.session_state.email_sections = [s for s in st.session_state.email_sections if s['id'] != section_id]

def move_section_up(section_id):
    """Move a section up in the order"""
    sections = st.session_state.email_sections
    for i, section in enumerate(sections):
        if section['id'] == section_id and i > 0:
            sections[i], sections[i-1] = sections[i-1], sections[i]
            break

def move_section_down(section_id):
    """Move a section down in the order"""
    sections = st.session_state.email_sections
    for i, section in enumerate(sections):
        if section['id'] == section_id and i < len(sections) - 1:
            sections[i], sections[i+1] = sections[i+1], sections[i]
            break

def generate_email_content():
    """Generate the complete email content from all sections"""
    content_parts = []
    
    # Add title
    if st.session_state.email_title:
        content_parts.append(generate_html_element("h1", st.session_state.email_title))
    
    # Add greeting
    if st.session_state.email_greeting:
        content_parts.append(generate_html_element("p", st.session_state.email_greeting))
    
    # Add all sections
    for section in st.session_state.email_sections:
        if section['type'] == 'heading' and section['title']:
            content_parts.append(generate_html_element("h2", section['title']))
        elif section['type'] == 'subheading' and section['title']:
            content_parts.append(generate_html_element("h3", section['title']))
        elif section['type'] == 'paragraph' and section['content']:
            content_parts.append(generate_html_element("p", section['content']))
        elif section['type'] == 'list' and section['items']:
            list_content = '\n'.join([item for item in section['items'] if item.strip()])
            if list_content:
                if section['title']:
                    content_parts.append(generate_html_element("h3", section['title']))
                if section['content']:
                    content_parts.append(generate_html_element("p", section['content']))
                content_parts.append(generate_html_element("ul", list_content))
    
    # Add signature
    if st.session_state.email_signature:
        content_parts.append(generate_html_element("p", st.session_state.email_signature))
    
    # Wrap in table structure
    content_html = '\n                                                  '.join(content_parts)
    return f'''
                                                <tr>
                                                <td style="vertical-align: top; padding: 20px 0;" valign="top">
                                                  {content_html}
                                                </td>
                                              </tr>'''

def main():
    st.set_page_config(
        page_title="Email Template Editor",
        page_icon="📧",
        layout="wide"
)
    
    st.title("📧 Email Template Content Editor")
    st.markdown("Create your email by adding and customizing sections one by one")
    
    # Initialize session state
    initialize_session_state()
    
    # Load the HTML template
    html_content = load_html_template()
    if not html_content:
        return
    
    # Create two columns
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("✏️ Edit Content")
        
        # Email basics section
        with st.expander("📝 Email Basics", expanded=True):
            st.session_state.email_title = st.text_input("Email Title", value=st.session_state.email_title)
            st.session_state.email_greeting = st.text_area("Greeting", value=st.session_state.email_greeting, height=68)
        
        # Sections management
        st.subheader("📋 Email Sections")
        
        # Add section buttons
        col_add1, col_add2, col_add3, col_add4 = st.columns(4)
        with col_add1:
            if st.button("➕ Add Heading", type="secondary"):
                add_section()
                st.session_state.email_sections[-1]['type'] = 'heading'
                st.rerun()
        with col_add2:
            if st.button("➕ Add Subheading", type="secondary"):
                add_section()
                st.session_state.email_sections[-1]['type'] = 'subheading'
                st.rerun()
        with col_add3:
            if st.button("➕ Add Paragraph", type="secondary"):
                add_section()
                st.session_state.email_sections[-1]['type'] = 'paragraph'
                st.rerun()
        with col_add4:
            if st.button("➕ Add List", type="secondary"):
                add_section()
                st.session_state.email_sections[-1]['type'] = 'list'
                st.rerun()
        
        # Display and edit sections
        for i, section in enumerate(st.session_state.email_sections):
            with st.expander(f"📑 Section {i+1}: {section['type'].title()}", expanded=True):
                col_controls1, col_controls2, col_controls3, col_controls4 = st.columns([1, 1, 1, 2])
                
                with col_controls1:
                    if st.button("⬆️", key=f"up_{section['id']}", help="Move up"):
                        move_section_up(section['id'])
                        st.rerun()
                
                with col_controls2:
                    if st.button("⬇️", key=f"down_{section['id']}", help="Move down"):
                        move_section_down(section['id'])
                        st.rerun()
                
                with col_controls3:
                    if st.button("🗑️", key=f"delete_{section['id']}", help="Delete section"):
                        remove_section(section['id'])
                        st.rerun()
                
                # Section content based on type
                if section['type'] in ['heading', 'subheading']:
                    section['title'] = st.text_input(f"{section['type'].title()} Text", 
                                                   value=section.get('title', ''), 
                                                   key=f"title_{section['id']}")
                
                elif section['type'] == 'paragraph':
                    section['content'] = st.text_area(f"Paragraph Content", 
                                                     value=section.get('content', ''), 
                                                     height=100,
                                                     key=f"content_{section['id']}")
                
                elif section['type'] == 'list':
                    section['title'] = st.text_input(f"List Title (optional)", 
                                                   value=section.get('title', ''), 
                                                   key=f"list_title_{section['id']}")
                    section['content'] = st.text_area(f"List Introduction (optional)", 
                                                     value=section.get('content', ''), 
                                                     height=68,
                                                     key=f"list_intro_{section['id']}")
                    
                    # List items management
                    st.write("List Items:")
                    if 'items' not in section:
                        section['items'] = []
                    
                    # Add item button
                    if st.button(f"➕ Add Item", key=f"add_item_{section['id']}"):
                        section['items'].append("")
                        st.rerun()
                    
                    # Edit existing items
                    for item_idx, item in enumerate(section['items']):
                        col_item, col_delete = st.columns([4, 1])
                        with col_item:
                            section['items'][item_idx] = st.text_input(
                                f"Item {item_idx + 1}", 
                                value=item, 
                                key=f"item_{section['id']}_{item_idx}",
                                label_visibility="collapsed"
                            )
                        with col_delete:
                            if st.button("🗑️", key=f"delete_item_{section['id']}_{item_idx}"):
                                section['items'].pop(item_idx)
                                st.rerun()
        
        # Signature section
        with st.expander("✍️ Email Signature", expanded=True):
            st.session_state.email_signature = st.text_area("Signature", value=st.session_state.email_signature, height=68)
        
        # Generate button
        if st.button("🚀 Generate Email", type="primary", use_container_width=True):
            # Generate the new content
            new_content = generate_email_content()
            
            # Replace content in HTML
            new_html = replace_content_module(html_content, new_content)
            
            # Store in session state
            st.session_state.generated_html = new_html
            st.success("✅ Email generated successfully!")
    
    with col2:
        st.header("👁️ Preview & Download")
        
        # Live preview section
        st.subheader("📱 Live Preview")
        preview_content = generate_email_content()
        preview_html = replace_content_module(html_content, preview_content)
        
        with st.container():
            st.components.v1.html(preview_html, height=600, scrolling=True)
        
        if 'generated_html' in st.session_state:
            st.divider()
            
            # Download button
            st.download_button(
                label="📥 Download HTML Email",
                data=st.session_state.generated_html,
                file_name=f"email_template_{st.session_state.get('download_counter', 1)}.html",
                mime="text/html",
                type="primary",
                use_container_width=True
            )
            
            # Update download counter
            if st.button("💾 Save as New Template", use_container_width=True):
                output_dir = Path("output")
                output_dir.mkdir(exist_ok=True)
                
                output_file = output_dir / f"email_template_{st.session_state.get('save_counter', 1)}.html"
                output_file.write_text(st.session_state.generated_html, encoding='utf-8')
                
                st.success(f"✅ Template saved as {output_file}")
                st.session_state.save_counter = st.session_state.get('save_counter', 0) + 1
        
        # Section summary
        st.divider()
        st.subheader("� Email Summary")
        st.write(f"**Total sections:** {len(st.session_state.email_sections)}")
        if st.session_state.email_sections:
            section_types = {}
            for section in st.session_state.email_sections:
                section_type = section['type']
                section_types[section_type] = section_types.get(section_type, 0) + 1
            
            for section_type, count in section_types.items():
                st.write(f"- {section_type.title()}s: {count}")
        
        # Tips section
        with st.expander("💡 Tips & Tricks"):
            st.markdown("""
            **Building your email:**
            - Start with basics: title, greeting, and introduction
            - Use headings to organize main topics
            - Add subheadings for subtopics
            - Use lists for multiple items or achievements
            - End with a conclusion paragraph and signature
            
            **Section management:**
            - Use ⬆️⬇️ arrows to reorder sections
            - Use 🗑️ to delete unwanted sections
            - Live preview updates automatically
            - Generate final version when ready
            """)

if __name__ == "__main__":
    main()
