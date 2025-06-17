import {
  Body,
  Container,
  Head,
  Html,
  Img,
  Link,
  Preview,
  Section,
  Text,
} from '@react-email/components';
import * as React from 'react';

interface CaiacEmailProps {
  title?: string;
  content?: {
    paragraph1?: string;
    paragraph2?: string;
    paragraph3?: string;
  };
  logoUrl?: string;
  websiteUrl?: string;
  githubUrl?: string;
  linkedinUrl?: string;
  address?: string;
  managePreferencesUrl?: string;
  unsubscribeUrl?: string;
}

export const CaiacEmail = ({
  title = "My Cool Template",
  content = {
    paragraph1: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam.",
    paragraph2: "Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta.",
    paragraph3: "Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos."
  },
  logoUrl = "https://raw.githubusercontent.com/cualignment/mailing-list/main/assets/logo.png",
  websiteUrl = "https://www.cualignment.org/",
  githubUrl = "https://github.com/cualignment",
  linkedinUrl = "https://www.linkedin.com/company/columbia-ai-alignment-club/",
  address = "Dorms of John Jay and East Campus <3, New York, NY, 10027",
  managePreferencesUrl = "https://LISTSERV.CUIT.COLUMBIA.EDU/scripts/wa.exe?SUBED1=CUALIGNMENT",
  unsubscribeUrl = "https://LISTSERV.CUIT.COLUMBIA.EDU/scripts/wa.exe?SUBED1=CUALIGNMENT"
}: CaiacEmailProps) => {
  return (
    <Html>
      <Head>
        <style>{`
          @import url('https://fonts.googleapis.com/css2?family=Fira+Sans:wght@400;500;600&display=swap');
          
          @media screen {
            @font-face {
              font-family: 'Fira Sans';
              font-style: normal;
              font-weight: 400;
              src: local('Fira Sans Regular'), local('FiraSans-Regular'), url(https://fonts.gstatic.com/s/firasans/v8/va9E4kDNxMZdWfMOD5Vvl4jLazX3dA.woff2) format('woff2');
              unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
            }
          }
        `}</style>
      </Head>
      <Preview>Template created by Designmodo.com</Preview>
      <Body
        style={{
          backgroundColor: '#f4f4f4',
          fontFamily: "'Fira Sans', Helvetica, Arial, sans-serif",
          fontSize: '16px',
          width: '100%',
          margin: '0',
          padding: '0',
          lineHeight: '1.5',
          WebkitFontSmoothing: 'antialiased',
          WebkitTextSizeAdjust: '100%',
          msTextSizeAdjust: '100%'
        }}
      >
        <Container
          style={{
            width: '100%',
            margin: '0 auto',
            maxWidth: '620px',
            padding: '20px 10px'
          }}
        >
          <Section
            style={{
              backgroundColor: '#ffffff',
              boxShadow: '0 2px 4px 0 rgba(0, 0, 0, 0.1)',
              borderRadius: '4px',
              overflow: 'hidden'
            }}
          >
            {/* Header Section */}
            <Section
              style={{
                backgroundColor: '#ffffff',
                padding: '34px 40px 55px'
              }}
            >
              {/* Logo */}
              <Section style={{ textAlign: 'center', marginBottom: '20px' }}>
                <Link href={websiteUrl} style={{ textDecoration: 'none' }}>
                  <Img
                    src={logoUrl}
                    alt="Logo"
                    width="80"
                    style={{
                      display: 'block',
                      margin: '0 auto'
                    }}
                  />
                </Link>
              </Section>

              {/* Content */}
              <Section style={{ padding: '20px 0' }}>
                <Text
                  style={{
                    fontFamily: "'Fira Sans', Helvetica, Arial, sans-serif",
                    fontSize: '24px',
                    color: '#333333',
                    textAlign: 'center',
                    margin: '0 0 20px 0',
                    fontWeight: '600'
                  }}
                >
                  {title}
                </Text>
                
                <Text
                  style={{
                    fontFamily: "'Fira Sans', Helvetica, Arial, sans-serif",
                    fontSize: '16px',
                    color: '#666666',
                    textAlign: 'left',
                    margin: '0 0 16px 0',
                    lineHeight: '1.5'
                  }}
                >
                  {content.paragraph1}
                </Text>
                
                <Text
                  style={{
                    fontFamily: "'Fira Sans', Helvetica, Arial, sans-serif",
                    fontSize: '16px',
                    color: '#666666',
                    textAlign: 'left',
                    margin: '0 0 16px 0',
                    lineHeight: '1.5'
                  }}
                >
                  {content.paragraph2}
                </Text>
                
                <Text
                  style={{
                    fontFamily: "'Fira Sans', Helvetica, Arial, sans-serif",
                    fontSize: '16px',
                    color: '#666666',
                    textAlign: 'left',
                    margin: '0 0 0 0',
                    lineHeight: '1.5'
                  }}
                >
                  {content.paragraph3}
                </Text>
              </Section>
            </Section>

            {/* Footer Section */}
            <Section
              style={{
                backgroundColor: '#ffffff',
                padding: '31px 40px',
                borderTop: '1px solid #f0f0f0'
              }}
            >
              {/* Social Media Icons */}
              <Section style={{ textAlign: 'center', marginBottom: '20px' }}>
                <Link href={websiteUrl} style={{ textDecoration: 'none', margin: '0 8px' }}>
                  <Img
                    src="https://raw.githubusercontent.com/cualignment/mailing-list/main/assets/web.png"
                    width="30"
                    height="30"
                    alt="Website"
                    style={{
                      border: '0',
                      lineHeight: '100%',
                      outline: '0',
                      fontSize: '14px',
                      color: '#151515',
                      display: 'inline-block'
                    }}
                  />
                </Link>
                
                <Link href={githubUrl} style={{ textDecoration: 'none', margin: '0 8px' }}>
                  <Img
                    src="https://raw.githubusercontent.com/cualignment/mailing-list/main/assets/github.png"
                    width="30"
                    height="30"
                    alt="GitHub"
                    style={{
                      border: '0',
                      lineHeight: '100%',
                      outline: '0',
                      fontSize: '14px',
                      color: '#151515',
                      display: 'inline-block'
                    }}
                  />
                </Link>
                
                <Link href={linkedinUrl} style={{ textDecoration: 'none', margin: '0 8px' }}>
                  <Img
                    src="https://raw.githubusercontent.com/cualignment/mailing-list/main/assets/linkedin.png"
                    width="30"
                    height="30"
                    alt="LinkedIn"
                    style={{
                      border: '0',
                      lineHeight: '100%',
                      outline: '0',
                      fontSize: '14px',
                      color: '#151515',
                      display: 'inline-block'
                    }}
                  />
                </Link>
              </Section>

              {/* Address */}
              <Text
                style={{
                  fontFamily: "'Fira Sans', Helvetica, Arial, sans-serif",
                  fontSize: '14px',
                  color: '#9B9B9B',
                  textAlign: 'center',
                  margin: '0 0 20px 0',
                  lineHeight: '1.43',
                  letterSpacing: '-0.2px'
                }}
              >
                {address}
              </Text>

              {/* Unsubscribe Links */}
              <Text
                style={{
                  fontFamily: "'Fira Sans', Helvetica, Arial, sans-serif",
                  fontSize: '14px',
                  color: '#9B9B9B',
                  textAlign: 'center',
                  margin: '0',
                  lineHeight: '1.43'
                }}
              >
                <Link
                  href={managePreferencesUrl}
                  style={{
                    textDecoration: 'none',
                    color: '#1595E7'
                  }}
                >
                  Manage Preferences
                </Link>
                <span style={{ margin: '0 8px' }}>•</span>
                <Link
                  href={unsubscribeUrl}
                  style={{
                    textDecoration: 'none',
                    color: '#1595E7'
                  }}
                >
                  Unsubscribe
                </Link>
              </Text>
            </Section>
          </Section>
        </Container>
      </Body>
    </Html>
  );
};

export default CaiacEmail;
