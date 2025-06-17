import { CaiacEmail } from './caiac-email';

// Example with custom content
export const ExampleEmail = () => {
  return (
    <CaiacEmail
      title="Welcome to CAIAC Newsletter"
      content={{
        paragraph1: "Welcome to the Columbia AI Alignment Club newsletter! We're excited to share the latest updates and insights from our community.",
        paragraph2: "This month we're featuring research highlights, upcoming events, and opportunities to get involved in AI alignment research at Columbia.",
        paragraph3: "Stay tuned for exciting announcements about our upcoming speaker series and research collaborations."
      }}
    />
  );
};

// Example with event announcement
export const EventEmail = () => {
  return (
    <CaiacEmail
      title="Upcoming AI Alignment Workshop"
      content={{
        paragraph1: "Join us for an intensive workshop on AI alignment research methodologies. This hands-on session will cover current approaches and emerging techniques.",
        paragraph2: "Date: March 15th, 2025 | Time: 2:00 PM - 5:00 PM | Location: Computer Science Building, Room 451",
        paragraph3: "Registration is required. Please RSVP by March 10th to secure your spot. Light refreshments will be provided."
      }}
    />
  );
};

export default CaiacEmail;
