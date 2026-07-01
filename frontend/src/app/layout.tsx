import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

import { Toaster } from "sonner";

const inter = Inter({
    subsets: ["latin"],
    variable: "--font-inter",
    display: "swap",
});

export const metadata: Metadata = {
    title: "SecureGen",
    description: "AI Powered Intrusion Detection & Security Operations Center",
    applicationName: "SecureGen",
    authors: [{ name: "SecureGen Team" }],
    keywords: ["Cybersecurity", "AI", "Intrusion Detection", "SOC", "Threat Detection", "Machine Learning", "FastAPI"],
};

export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <html lang="en" suppressHydrationWarning>
            <body className={`${inter.variable} min-h-screen bg-background text-foreground antialiased`}>
                {children}

                <Toaster richColors position="top-right" closeButton theme="dark" />
            </body>
        </html>
    );
}
