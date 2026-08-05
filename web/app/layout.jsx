import "./globals.css";

export const metadata = {
  title: "Agent Email Router",
  description: "Web UI for Agent Email Router",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
