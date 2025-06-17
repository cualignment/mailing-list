# CAIAC Email Template - Quick Start Guide

## 🚀 Two Ways to Use This Template

### Option 1: Python Script (Recommended for Quick Use)

**Easiest way to generate HTML emails without needing Node.js**

1. **Simple command line usage:**
```bash
python3 generate_email.py --title "Your Title" --p1 "First paragraph" --p2 "Second paragraph" --p3 "Third paragraph"
```

2. **Interactive mode:**
```bash
python3 generate_email.py --interactive
```

3. **Find your generated HTML:**
Generated files are saved in the `output/` folder and ready to upload to any email service.

### Option 2: React Email (Advanced, requires Node.js)

**Best for developers who want full customization**

1. **Install dependencies:**
```bash
npm install
```

2. **Start development server:**
```bash
npm run dev
```

3. **Export HTML:**
```bash
npm run export
```

## 📝 Example Usage

### Newsletter Example
```bash
python3 generate_email.py \
  --title "CAIAC Monthly Newsletter - June 2025" \
  --p1 "Welcome to our monthly update! This month we're featuring exciting research developments and upcoming events." \
  --p2 "Join us for our AI Safety Workshop on June 20th. We'll be covering alignment techniques and current research methodologies." \
  --p3 "Don't forget to check out our new resource library and connect with fellow researchers in our community."
```

### Event Invitation
```bash
python3 generate_email.py \
  --title "AI Alignment Workshop - June 20th" \
  --p1 "You're invited to attend our hands-on AI Alignment Workshop featuring guest speakers from leading research institutions." \
  --p2 "Date: June 20th, 2025 | Time: 2:00 PM - 6:00 PM | Location: Computer Science Building, Room 451" \
  --p3 "Registration required by June 18th. Light refreshments will be provided. RSVP link: https://example.com/rsvp"
```

## 🎨 Customization Options

All these can be customized via command line arguments:

- `--title`: Main email heading
- `--preview`: Preview text (shown in email client previews)
- `--p1`, `--p2`, `--p3`: Content paragraphs
- `--output`: Custom filename for generated HTML

## 📱 Email Client Compatibility

This template works with:
- ✅ Gmail (Desktop & Mobile)
- ✅ Outlook (Desktop & Web)
- ✅ Apple Mail (Desktop & Mobile)
- ✅ Yahoo Mail
- ✅ Thunderbird
- ✅ Most other email clients

## 🔗 Included Features

- **Responsive design** - Works on all devices
- **Social media links** - Website, GitHub, LinkedIn
- **Professional styling** - Clean, modern look
- **Email-optimized** - Tested across major clients
- **Easy customization** - Simple placeholder system

## 📂 Files Explanation

```
react-email-template/
├── generate_email.py    # Python script for quick generation
├── template.html        # HTML template with placeholders
├── output/             # Generated email files go here
├── emails/             # React Email components (advanced)
└── README.md           # Full documentation
```

## 🆘 Troubleshooting

**Python script not working?**
- Make sure you have Python 3 installed: `python3 --version`
- Run from the correct directory: `cd react-email-template`

**Need to modify the template?**
- Edit `template.html` to change the overall design
- The Python script replaces `{{PLACEHOLDER}}` tags with your content

**Want more advanced features?**
- Use the React Email option (requires Node.js)
- Modify the `.tsx` files in the `emails/` folder

## 💡 Tips

1. **Test before sending**: Always preview the generated HTML in a browser first
2. **Keep it concise**: Email content should be scannable and brief
3. **Use clear CTAs**: If you need buttons or calls-to-action, add them to the template
4. **Mobile-first**: Most people read emails on mobile devices

## 🎯 Ready-to-Use Examples

The `output/` folder contains example generated emails you can use as starting points.
