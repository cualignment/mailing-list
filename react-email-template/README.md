# CAIAC React Email Template

This project provides an easily customizable email template for the Columbia AI Alignment Club (CAIAC) built with React Email.

## Features

- ✅ **Easy to customize**: Props-based configuration for all content
- ✅ **Responsive design**: Works on all email clients and devices
- ✅ **TypeScript support**: Full type safety for props
- ✅ **Export to HTML**: Generate pure HTML files for uploading to email services
- ✅ **Live preview**: Development server with hot reload

## Setup

1. Install dependencies:
```bash
cd react-email-template
npm install
```

2. Start the development server:
```bash
npm run dev
```

This will open a browser at `http://localhost:3000` where you can preview your emails in real-time.

## Usage

### Basic Template

The main template is in `emails/caiac-email.tsx`. You can customize it by passing props:

```tsx
import { CaiacEmail } from './caiac-email';

export const MyNewsletter = () => {
  return (
    <CaiacEmail
      title="Your Custom Title"
      content={{
        paragraph1: "Your first paragraph...",
        paragraph2: "Your second paragraph...",
        paragraph3: "Your third paragraph..."
      }}
    />
  );
};
```

### Available Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `title` | `string` | "My Cool Template" | Main heading of the email |
| `content.paragraph1` | `string` | Lorem ipsum... | First content paragraph |
| `content.paragraph2` | `string` | Lorem ipsum... | Second content paragraph |
| `content.paragraph3` | `string` | Lorem ipsum... | Third content paragraph |
| `logoUrl` | `string` | CAIAC logo URL | URL to the logo image |
| `websiteUrl` | `string` | https://www.cualignment.org/ | Website link |
| `githubUrl` | `string` | https://github.com/cualignment | GitHub link |
| `linkedinUrl` | `string` | LinkedIn URL | LinkedIn link |
| `address` | `string` | Dorms address | Footer address text |
| `managePreferencesUrl` | `string` | Listserv URL | Manage preferences link |
| `unsubscribeUrl` | `string` | Listserv URL | Unsubscribe link |

## Exporting HTML

To generate HTML files that you can upload to your email service:

```bash
npm run export
```

This creates HTML files in the `out` directory that are ready to use with any email service provider.

## Examples

Check `emails/examples.tsx` for sample implementations:

- Newsletter announcement
- Event invitation
- Custom content examples

## Email Client Compatibility

This template is designed to work with all major email clients including:
- Gmail
- Outlook
- Apple Mail
- Yahoo Mail
- Thunderbird
- Mobile email clients

## Development Tips

1. **Live Preview**: Use `npm run dev` to see changes in real-time
2. **HTML Export**: Always test the exported HTML in your target email client
3. **Image URLs**: Use absolute URLs for all images (already configured for CAIAC assets)
4. **Custom Styling**: Modify the inline styles in the component for design changes

## File Structure

```
react-email-template/
├── emails/
│   ├── caiac-email.tsx    # Main template component
│   └── examples.tsx       # Example implementations
├── package.json           # Dependencies and scripts
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Contributing

To add new email templates or modify existing ones:

1. Create new template files in the `emails/` directory
2. Follow the same prop-based pattern for customization
3. Test with `npm run dev` and `npm run export`
4. Ensure cross-client compatibility

## Support

For questions or issues with this template, please reach out to the CAIAC development team.
