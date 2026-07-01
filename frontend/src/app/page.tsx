"use client";

import { useState, useEffect, useRef, useCallback } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
    Shield,
    Brain,
    Database,
    Sparkles,
    Network,
    Server,
    Activity,
    CheckCircle2,
    AlertTriangle,
    Clock,
    FileText,
    Bug,
    ShieldCheck,
    BookOpen,
    ArrowRight,
    Upload,
    Download,
    Wifi,
    Zap,
    Terminal,
    Lock,
    ChevronRight,
    X,
    Layers,
} from "lucide-react";
import api from "@/lib/api";

// ─── Types ────────────────────────────────────────────────────────────────────

interface AppInfo {
    application: string;
    version: string;
    status: string;
}

interface HealthInfo {
    status: string;
}

interface MitreAttack {
    technique_id: string;
    technique_name: string;
    tactic: string;
}

interface IndicatorOfCompromise {
    type: string;
    value: string;
    description: string;
}

interface Mitigation {
    title: string;
    description: string;
}

interface Reference {
    title: string;
    url: string;
}

interface Prediction {
    attack_name: string;
    confidence: number;
    severity: "Critical" | "High" | "Medium" | "Low" | "Informational";
    executive_summary: string;
    technical_explanation: string;
    prediction_reason: string;
    mitre_attack: MitreAttack[];
    indicators_of_compromise: IndicatorOfCompromise[];
    business_impact: string[];
    mitigations: Mitigation[];
    references: Reference[];
}

interface PredictResponse {
    success: boolean;
    request_id: string;
    timestamp: string;
    latency_ms: number;
    model_version: string;
    prediction: Prediction;
}

type LoadingStep = "idle" | "input" | "features" | "model" | "mitre" | "report" | "done";
type InputSource = "sample" | "upload";

interface SampleEntry {
    id: string;
    emoji: string;
    title: string;
    description: string;
    accentColor: string;
    borderColor: string;
    bgColor: string;
    features: Record<string, number>;
}

// ─── Sample Library Data ───────────────────────────────────────────────────────

// Base feature template — exact keys the backend expects (spaces, slashes, dots)
const BASE_FEATURES: Record<string, number> = {
    "Destination Port": 0.0,
    "Flow Duration": 0.0,
    "Total Fwd Packets": 0.0,
    "Total Backward Packets": 0.0,
    "Total Length of Fwd Packets": 0.0,
    "Total Length of Bwd Packets": 0.0,
    "Fwd Packet Length Max": 0.0,
    "Fwd Packet Length Min": 0.0,
    "Fwd Packet Length Mean": 0.0,
    "Fwd Packet Length Std": 0.0,
    "Bwd Packet Length Max": 0.0,
    "Bwd Packet Length Min": 0.0,
    "Bwd Packet Length Mean": 0.0,
    "Bwd Packet Length Std": 0.0,
    "Flow Bytes/s": 0.0,
    "Flow Packets/s": 0.0,
    "Flow IAT Mean": 0.0,
    "Flow IAT Std": 0.0,
    "Flow IAT Max": 0.0,
    "Flow IAT Min": 0.0,
    "Fwd IAT Total": 0.0,
    "Fwd IAT Mean": 0.0,
    "Fwd IAT Std": 0.0,
    "Fwd IAT Max": 0.0,
    "Fwd IAT Min": 0.0,
    "Bwd IAT Total": 0.0,
    "Bwd IAT Mean": 0.0,
    "Bwd IAT Std": 0.0,
    "Bwd IAT Max": 0.0,
    "Bwd IAT Min": 0.0,
    "Fwd PSH Flags": 0.0,
    "Fwd URG Flags": 0.0,
    "Fwd Header Length": 0.0,
    "Bwd Header Length": 0.0,
    "Fwd Packets/s": 0.0,
    "Bwd Packets/s": 0.0,
    "Min Packet Length": 0.0,
    "Max Packet Length": 0.0,
    "Packet Length Mean": 0.0,
    "Packet Length Std": 0.0,
    "Packet Length Variance": 0.0,
    "FIN Flag Count": 0.0,
    "SYN Flag Count": 0.0,
    "RST Flag Count": 0.0,
    "PSH Flag Count": 0.0,
    "ACK Flag Count": 0.0,
    "URG Flag Count": 0.0,
    "CWE Flag Count": 0.0,
    "ECE Flag Count": 0.0,
    "Down/Up Ratio": 0.0,
    "Average Packet Size": 0.0,
    "Avg Fwd Segment Size": 0.0,
    "Avg Bwd Segment Size": 0.0,
    "Fwd Header Length.1": 0.0,
    "Subflow Fwd Packets": 0.0,
    "Subflow Fwd Bytes": 0.0,
    "Subflow Bwd Packets": 0.0,
    "Subflow Bwd Bytes": 0.0,
    "Init_Win_bytes_forward": 0.0,
    "Init_Win_bytes_backward": -1.0,
    "act_data_pkt_fwd": 0.0,
    "min_seg_size_forward": 20.0,
    "Active Mean": 0.0,
    "Active Std": 0.0,
    "Active Max": 0.0,
    "Active Min": 0.0,
    "Idle Mean": 0.0,
    "Idle Std": 0.0,
    "Idle Max": 0.0,
    "Idle Min": 0.0,
};

const benignFeatures: Record<string, number> = {
    ...BASE_FEATURES,
    "Destination Port": 54865.0,
    "Flow Duration": 3.0,
    "Total Fwd Packets": 2.0,
    "Total Length of Fwd Packets": 12.0,
    "Fwd Packet Length Max": 6.0,
    "Fwd Packet Length Min": 6.0,
    "Fwd Packet Length Mean": 6.0,
    "Flow Bytes/s": 4000000.0,
    "Flow Packets/s": 666666.6667,
    "Flow IAT Mean": 3.0,
    "Flow IAT Max": 3.0,
    "Flow IAT Min": 3.0,
    "Fwd IAT Total": 3.0,
    "Fwd IAT Mean": 3.0,
    "Fwd IAT Max": 3.0,
    "Fwd IAT Min": 3.0,
    "Fwd Header Length": 40.0,
    "Fwd Packets/s": 666666.6667,
    "Min Packet Length": 6.0,
    "Max Packet Length": 6.0,
    "Packet Length Mean": 6.0,
    "ACK Flag Count": 1.0,
    "Average Packet Size": 9.0,
    "Avg Fwd Segment Size": 6.0,
    "Fwd Header Length.1": 40.0,
    "Subflow Fwd Packets": 2.0,
    "Subflow Fwd Bytes": 12.0,
    "Init_Win_bytes_forward": 33.0,
    "Init_Win_bytes_backward": -1.0,
    "act_data_pkt_fwd": 1.0,
    "min_seg_size_forward": 20.0,
};

const ddosFeatures: Record<string, number> = {
    ...BASE_FEATURES,
    "Destination Port": 443.0,
    "Flow Duration": 5.0,
    "Total Fwd Packets": 9800.0,
    "Flow Bytes/s": 0.0,
    "Flow Packets/s": 1960000.0,
    "Flow IAT Mean": 0.51,
    "Flow IAT Std": 0.1,
    "Flow IAT Max": 1.0,
    "Flow IAT Min": 0.0,
    "Fwd IAT Total": 4.0,
    "Fwd IAT Mean": 0.51,
    "Fwd Header Length": 40.0,
    "Fwd Packets/s": 1960000.0,
    "SYN Flag Count": 9800.0,
    "Fwd Header Length.1": 40.0,
    "Subflow Fwd Packets": 9800.0,
    "Init_Win_bytes_forward": 0.0,
    "Init_Win_bytes_backward": -1.0,
    "min_seg_size_forward": 20.0,
};

const portScanFeatures: Record<string, number> = {
    ...BASE_FEATURES,
    "Destination Port": 80.0,
    "Flow Duration": 0.0,
    "Total Fwd Packets": 1.0,
    "Total Backward Packets": 1.0,
    "Total Length of Fwd Packets": 0.0,
    "Total Length of Bwd Packets": 0.0,
    "Fwd Packet Length Max": 0.0,
    "Fwd Packet Length Min": 0.0,
    "Fwd Packet Length Mean": 0.0,
    "Fwd Packet Length Std": 0.0,
    "Bwd Packet Length Max": 0.0,
    "Bwd Packet Length Min": 0.0,
    "Bwd Packet Length Mean": 0.0,
    "Bwd Packet Length Std": 0.0,
    "Flow Bytes/s": 0.0,
    "Flow Packets/s": 4000000.0,
    "Flow IAT Mean": 0.0,
    "Flow IAT Std": 0.0,
    "Flow IAT Max": 0.0,
    "Flow IAT Min": 0.0,
    "Fwd IAT Total": 0.0,
    "Fwd IAT Mean": 0.0,
    "Fwd IAT Std": 0.0,
    "Fwd IAT Max": 0.0,
    "Fwd IAT Min": 0.0,
    "Fwd Header Length": 20.0,
    "Bwd Header Length": 20.0,
    "Fwd Packets/s": 2000000.0,
    "Bwd Packets/s": 2000000.0,
    "Min Packet Length": 0.0,
    "Max Packet Length": 0.0,
    "Packet Length Mean": 0.0,
    "Packet Length Std": 0.0,
    "Packet Length Variance": 0.0,
    "SYN Flag Count": 1.0,
    "RST Flag Count": 1.0,
    "Fwd Header Length.1": 20.0,
    "Subflow Fwd Packets": 1.0,
    "Subflow Bwd Packets": 1.0,
    "Init_Win_bytes_forward": 0.0,
    "Init_Win_bytes_backward": 0.0,
    "min_seg_size_forward": 20.0,
};

const botFeatures: Record<string, number> = {
    ...BASE_FEATURES,
    "Destination Port": 6667.0,
    "Flow Duration": 60000.0,
    "Total Fwd Packets": 500.0,
    "Total Backward Packets": 480.0,
    "Total Length of Fwd Packets": 15000.0,
    "Total Length of Bwd Packets": 14400.0,
    "Fwd Packet Length Mean": 30.0,
    "Bwd Packet Length Mean": 30.0,
    "Flow Bytes/s": 490.0,
    "Flow Packets/s": 16.33,
    "Flow IAT Mean": 120.0,
    "Fwd Header Length": 40.0,
    "Bwd Header Length": 40.0,
    "Fwd Packets/s": 8.33,
    "Bwd Packets/s": 8.0,
    "ACK Flag Count": 980.0,
    "PSH Flag Count": 480.0,
    "Average Packet Size": 30.0,
    "Avg Fwd Segment Size": 30.0,
    "Avg Bwd Segment Size": 30.0,
    "Fwd Header Length.1": 40.0,
    "Subflow Fwd Packets": 500.0,
    "Subflow Fwd Bytes": 15000.0,
    "Subflow Bwd Packets": 480.0,
    "Subflow Bwd Bytes": 14400.0,
    "Init_Win_bytes_forward": 65535.0,
    "Init_Win_bytes_backward": 65535.0,
    "act_data_pkt_fwd": 480.0,
    "min_seg_size_forward": 20.0,
};

const sshBruteFeatures: Record<string, number> = {
    ...BASE_FEATURES,
    "Destination Port": 22.0,
    "Flow Duration": 3000.0,
    "Total Fwd Packets": 150.0,
    "Total Backward Packets": 120.0,
    "Total Length of Fwd Packets": 4500.0,
    "Total Length of Bwd Packets": 3600.0,
    "Fwd Packet Length Mean": 30.0,
    "Bwd Packet Length Mean": 30.0,
    "Flow Bytes/s": 2700.0,
    "Flow Packets/s": 90.0,
    "Flow IAT Mean": 20.0,
    "Flow IAT Std": 5.0,
    "Fwd Header Length": 40.0,
    "Bwd Header Length": 40.0,
    "Fwd Packets/s": 50.0,
    "Bwd Packets/s": 40.0,
    "SYN Flag Count": 30.0,
    "ACK Flag Count": 270.0,
    "Average Packet Size": 30.0,
    "Avg Fwd Segment Size": 30.0,
    "Avg Bwd Segment Size": 30.0,
    "Fwd Header Length.1": 40.0,
    "Subflow Fwd Packets": 150.0,
    "Subflow Fwd Bytes": 4500.0,
    "Subflow Bwd Packets": 120.0,
    "Subflow Bwd Bytes": 3600.0,
    "Init_Win_bytes_forward": 8192.0,
    "Init_Win_bytes_backward": 8192.0,
    "act_data_pkt_fwd": 120.0,
    "min_seg_size_forward": 20.0,
};

const SAMPLE_LIBRARY: SampleEntry[] = [
    {
        id: "benign",
        emoji: "🟢",
        title: "Benign Traffic",
        description: "Normal network communication",
        accentColor: "text-emerald-400",
        borderColor: "border-emerald-500/25",
        bgColor: "bg-emerald-500/5",
        features: benignFeatures,
    },
    {
        id: "ddos",
        emoji: "🔴",
        title: "DDoS Attack",
        description: "High-rate SYN Flood",
        accentColor: "text-red-400",
        borderColor: "border-red-500/25",
        bgColor: "bg-red-500/5",
        features: ddosFeatures,
    },
    {
        id: "portscan",
        emoji: "🟠",
        title: "Port Scan",
        description: "Reconnaissance traffic",
        accentColor: "text-orange-400",
        borderColor: "border-orange-500/25",
        bgColor: "bg-orange-500/5",
        features: portScanFeatures,
    },
    {
        id: "bot",
        emoji: "🟣",
        title: "Bot Activity",
        description: "Automated malicious behaviour",
        accentColor: "text-purple-400",
        borderColor: "border-purple-500/25",
        bgColor: "bg-purple-500/5",
        features: botFeatures,
    },
    {
        id: "ssh",
        emoji: "⚠",
        title: "SSH Brute Force",
        description: "Credential attack",
        accentColor: "text-yellow-400",
        borderColor: "border-yellow-500/25",
        bgColor: "bg-yellow-500/5",
        features: sshBruteFeatures,
    },
];

// ─── Loading Pipeline Stages ──────────────────────────────────────────────────

const LOADING_STAGES: { key: LoadingStep; label: string; icon: React.ElementType; duration: number }[] = [
    { key: "input",    label: "Input Loaded",           icon: Layers,   duration: 600  },
    { key: "features", label: "Feature Validation",     icon: Network,  duration: 900  },
    { key: "model",    label: "PyTorch Inference",      icon: Brain,    duration: 1100 },
    { key: "mitre",    label: "MITRE ATT&CK Mapping",   icon: Shield,   duration: 800  },
    { key: "report",   label: "AI Threat Report",       icon: Sparkles, duration: 900  },
];

const STAGE_ORDER: LoadingStep[] = ["input", "features", "model", "mitre", "report", "done"];

// ─── Helpers ──────────────────────────────────────────────────────────────────

function severityColor(s: string) {
    switch (s) {
        case "Critical":
            return { text: "text-red-400", bg: "bg-red-500/10", border: "border-red-500/20" };
        case "High":
            return { text: "text-orange-400", bg: "bg-orange-500/10", border: "border-orange-500/20" };
        case "Medium":
            return { text: "text-yellow-400", bg: "bg-yellow-500/10", border: "border-yellow-500/20" };
        case "Low":
            return { text: "text-emerald-400", bg: "bg-emerald-500/10", border: "border-emerald-500/20" };
        case "Informational":
            return { text: "text-blue-400", bg: "bg-blue-500/10", border: "border-blue-500/20" };
        default:
            return { text: "text-zinc-400", bg: "bg-zinc-500/10", border: "border-zinc-500/20" };
    }
}

function formatTimestamp(ts: string) {
    try {
        return new Date(ts).toLocaleString("en-US", {
            month: "short",
            day: "numeric",
            year: "numeric",
            hour: "2-digit",
            minute: "2-digit",
            second: "2-digit",
        });
    } catch {
        return ts;
    }
}

function formatBytes(bytes: number) {
    if (bytes < 1024) return `${bytes} B`;
    if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
    return `${(bytes / 1024 / 1024).toFixed(1)} MB`;
}

// ─── Sub-components (inline) ──────────────────────────────────────────────────

function StatusDot({ online }: { online: boolean }) {
    return (
        <span className="relative flex h-2 w-2">
            {online && (
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75" />
            )}
            <span
                className={`relative inline-flex rounded-full h-2 w-2 ${online ? "bg-emerald-400" : "bg-zinc-600"}`}
            />
        </span>
    );
}

function Card({ children, className = "" }: { children: React.ReactNode; className?: string }) {
    return <div className={`bg-[#111111] border border-[#1f1f1f] rounded-2xl ${className}`}>{children}</div>;
}

function SectionLabel({ children }: { children: React.ReactNode }) {
    return <p className="text-[11px] uppercase tracking-widest text-zinc-500 font-medium mb-3">{children}</p>;
}

// ─── Main Component ───────────────────────────────────────────────────────────

export default function Page() {
    // ── Existing state ──
    const [appInfo, setAppInfo] = useState<AppInfo | null>(null);
    const [health, setHealth] = useState<HealthInfo | null>(null);
    const [backendError, setBackendError] = useState(false);
    const [result, setResult] = useState<PredictResponse | null>(null);
    const [loadingStep, setLoadingStep] = useState<LoadingStep>("idle");
    const [predError, setPredError] = useState<string | null>(null);
    const [confidenceDisplay, setConfidenceDisplay] = useState(0);

    // ── New UX state ──
    const [inputSource, setInputSource] = useState<InputSource>("sample");
    const [selectedSampleId, setSelectedSampleId] = useState<string | null>(null);
    const [uploadedFile, setUploadedFile] = useState<{ name: string; size: number; features: Record<string, number> } | null>(null);
    const [isDragOver, setIsDragOver] = useState(false);
    const [uploadError, setUploadError] = useState<string | null>(null);
    const fileInputRef = useRef<HTMLInputElement>(null);

    const isLoading = loadingStep !== "idle" && loadingStep !== "done";

    // ── Derived ──
    const selectedSample = SAMPLE_LIBRARY.find((s) => s.id === selectedSampleId) ?? null;
    const isReady =
        (inputSource === "sample" && selectedSample !== null) ||
        (inputSource === "upload" && uploadedFile !== null);

    // Bootstrap: fetch app info + health
    useEffect(() => {
        (async () => {
            try {
                const [infoRes, healthRes] = await Promise.all([api.get("/"), api.get("/health")]);
                setAppInfo(infoRes.data);
                setHealth(healthRes.data);
            } catch {
                setBackendError(true);
            }
        })();
    }, []);

    // Animate confidence bar when result arrives
    useEffect(() => {
        if (!result) return;
        setConfidenceDisplay(0);
        const target = Math.round(result.prediction.confidence * 100);
        let current = 0;
        const step = target / 60;
        const interval = setInterval(() => {
            current = Math.min(current + step, target);
            setConfidenceDisplay(Math.round(current));
            if (current >= target) clearInterval(interval);
        }, 16);
        return () => clearInterval(interval);
    }, [result]);

    // ── File upload handler ──
    const handleFileData = useCallback((file: File) => {
        setUploadError(null);
        if (!file.name.endsWith(".json")) {
            setUploadError("Only .json files are accepted.");
            return;
        }
        const reader = new FileReader();
        reader.onload = (e) => {
            try {
                const parsed = JSON.parse(e.target?.result as string);
                const features = parsed.features ?? parsed;
                if (typeof features !== "object" || features === null) {
                    setUploadError("Invalid PredictionRequest JSON.");
                    return;
                }
                setUploadedFile({ name: file.name, size: file.size, features });
                setUploadError(null);
            } catch {
                setUploadError("Could not parse JSON file.");
            }
        };
        reader.readAsText(file);
    }, []);

    const handleDrop = useCallback(
        (e: React.DragEvent<HTMLDivElement>) => {
            e.preventDefault();
            setIsDragOver(false);
            const file = e.dataTransfer.files[0];
            if (file) handleFileData(file);
        },
        [handleFileData],
    );

    const handleFileInput = useCallback(
        (e: React.ChangeEvent<HTMLInputElement>) => {
            const file = e.target.files?.[0];
            if (file) handleFileData(file);
        },
        [handleFileData],
    );

    const handleDownloadDemoJson = () => {
        const demoData = {
            features: ddosFeatures
        };
        const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(demoData, null, 4));
        const downloadAnchor = document.createElement("a");
        downloadAnchor.setAttribute("href", dataStr);
        downloadAnchor.setAttribute("download", "ddos_attack_demo.json");
        document.body.appendChild(downloadAnchor);
        downloadAnchor.click();
        downloadAnchor.remove();
    };

    // ── Analyze ──
    async function handleAnalyze() {
        if (!isReady) return;
        setPredError(null);
        setResult(null);

        const features =
            inputSource === "sample" && selectedSample
                ? selectedSample.features
                : uploadedFile!.features;

        for (const stage of LOADING_STAGES) {
            setLoadingStep(stage.key);
            await new Promise((r) => setTimeout(r, stage.duration));
        }

        try {
            const res = await api.post<PredictResponse>("/predict", { features });
            setResult(res.data);
        } catch (e: unknown) {
            const msg = e instanceof Error ? e.message : "Failed to reach the backend. Please try again.";
            setPredError(msg);
        } finally {
            setLoadingStep("done");
        }
    }

    async function handleRetry() {
        setPredError(null);
        setBackendError(false);
        setResult(null);
        setLoadingStep("idle");
        try {
            const [infoRes, healthRes] = await Promise.all([api.get("/"), api.get("/health")]);
            setAppInfo(infoRes.data);
            setHealth(healthRes.data);
        } catch {
            setBackendError(true);
        }
    }

    const severity = result?.prediction.severity ?? "";
    const sc = severityColor(severity);
    const currentStageIndex = STAGE_ORDER.indexOf(loadingStep);

    return (
        <main className="min-h-screen bg-[#0a0a0a] text-white font-sans selection:bg-white/10">

            <div className="max-w-6xl mx-auto px-4 sm:px-6 py-14 space-y-14">
                {/* ── Hero ── */}
                <motion.section
                    className="text-center space-y-6 max-w-2xl mx-auto"
                    initial={{ opacity: 0, y: 18 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.55 }}
                >
                    <div className="inline-flex items-center gap-2 border border-[#1f1f1f] rounded-full px-3.5 py-1.5 text-xs text-zinc-400 bg-[#111111]">
                        <Sparkles size={12} />
                        AI-Powered Intrusion Detection
                    </div>
                    <h1 className="text-4xl sm:text-5xl font-bold tracking-tight text-white leading-[1.1]">
                        Detect threats before
                        <br />
                        they become breaches.
                    </h1>
                    <p className="text-zinc-400 text-base leading-relaxed max-w-xl mx-auto">
                        SecureGen combines PyTorch deep learning with retrieval-augmented generation to classify
                        network intrusions and deliver actionable security intelligence in real time.
                    </p>
                </motion.section>

                {/* ── Backend Status Cards ── */}
                <motion.section
                    initial={{ opacity: 0, y: 12 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.5, delay: 0.1 }}
                >
                    {backendError ? (
                        <Card className="p-6 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-red-500/15">
                            <div className="flex items-center gap-3">
                                <div className="w-9 h-9 rounded-xl bg-red-500/10 border border-red-500/20 flex items-center justify-center shrink-0">
                                    <AlertTriangle size={16} className="text-red-400" />
                                </div>
                                <div>
                                    <p className="text-sm font-medium text-white">Backend Unreachable</p>
                                    <p className="text-xs text-zinc-500 mt-0.5">
                                        Could not connect to the SecureGen API.
                                    </p>
                                </div>
                            </div>
                            <button
                                onClick={handleRetry}
                                className="text-xs font-medium border border-[#2a2a2a] hover:border-white/30 text-zinc-300 hover:text-white px-4 py-2 rounded-xl transition-colors"
                            >
                                Retry Connection
                            </button>
                        </Card>
                    ) : (
                        <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                            {[
                                {
                                    icon: <Server size={15} className="text-zinc-400" />,
                                    label: "Backend",
                                    value: appInfo ? appInfo.application : "—",
                                    sub: appInfo ? `v${appInfo.version}` : "Loading…",
                                    online: !!appInfo,
                                },
                                {
                                    icon: <Activity size={15} className="text-zinc-400" />,
                                    label: "Health",
                                    value: health ? health.status : "—",
                                    sub: health ? "All systems operational" : "Loading…",
                                    online: health?.status === "healthy",
                                },
                                {
                                    icon: <Brain size={15} className="text-zinc-400" />,
                                    label: "Model Version",
                                    value: result ? result.model_version : appInfo ? "v1" : "—",
                                    sub: "PyTorch IDS Classifier",
                                    online: !!appInfo,
                                },
                            ].map((item) => (
                                <Card key={item.label} className="p-5">
                                    <div className="flex items-center gap-2 mb-4">
                                        {item.icon}
                                        <span className="text-xs text-zinc-500 uppercase tracking-widest">
                                            {item.label}
                                        </span>
                                    </div>
                                    <div className="flex items-end justify-between gap-2">
                                        <div>
                                            <p className="text-lg font-semibold text-white leading-none">
                                                {item.value}
                                            </p>
                                            <p className="text-xs text-zinc-500 mt-1">{item.sub}</p>
                                        </div>
                                        <StatusDot online={item.online} />
                                    </div>
                                </Card>
                            ))}
                        </div>
                    )}
                </motion.section>

                {/* ── Analyze Network Traffic ── */}
                <motion.section
                    className="space-y-5"
                    initial={{ opacity: 0, y: 12 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.5, delay: 0.2 }}
                >
                    <div>
                        <h2 className="text-xl font-semibold text-white mb-1.5">Analyze Network Traffic</h2>
                        <p className="text-sm text-zinc-400 leading-relaxed max-w-2xl">
                            Select a built-in attack scenario or upload a PredictionRequest JSON file. SecureGen
                            will classify the traffic, estimate confidence, map the attack to MITRE ATT&CK, and
                            generate an AI-powered threat report.
                        </p>
                    </div>

                    {/* ── Choose Input Source Card ── */}
                    <Card className="overflow-hidden">
                        {/* Card header with segmented control */}
                        <div className="px-6 pt-5 pb-4 border-b border-[#1a1a1a] flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                            <div className="flex items-center gap-2.5">
                                <div className="w-7 h-7 rounded-lg bg-[#1a1a1a] border border-[#2a2a2a] flex items-center justify-center">
                                    <Layers size={13} className="text-zinc-400" />
                                </div>
                                <span className="text-sm font-medium text-white">Choose Input Source</span>
                            </div>
                            <div className="flex items-center gap-1 bg-[#0d0d0d] border border-[#1f1f1f] rounded-xl p-1 self-start sm:self-auto">
                                {(["sample", "upload"] as InputSource[]).map((src) => (
                                    <button
                                        key={src}
                                        onClick={() => setInputSource(src)}
                                        className={`relative flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all duration-200 ${
                                            inputSource === src
                                                ? "bg-white text-black shadow-sm"
                                                : "text-zinc-500 hover:text-zinc-300"
                                        }`}
                                    >
                                        {src === "sample" ? <Wifi size={11} /> : <Upload size={11} />}
                                        {src === "sample" ? "Sample Library" : "Upload JSON"}
                                    </button>
                                ))}
                            </div>
                        </div>

                        {/* Panel content */}
                        <div className="p-6">
                            <AnimatePresence mode="wait">
                                {/* ── Sample Library ── */}
                                {inputSource === "sample" && (
                                    <motion.div
                                        key="sample"
                                        initial={{ opacity: 0, y: 6 }}
                                        animate={{ opacity: 1, y: 0 }}
                                        exit={{ opacity: 0, y: -6 }}
                                        transition={{ duration: 0.2 }}
                                    >
                                        <p className="text-xs text-zinc-500 mb-4">
                                            Choose a built-in traffic scenario to run through the detection pipeline.
                                        </p>
                                        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
                                            {SAMPLE_LIBRARY.map((sample) => {
                                                const isSelected = selectedSampleId === sample.id;
                                                return (
                                                    <motion.button
                                                        key={sample.id}
                                                        onClick={() => setSelectedSampleId(sample.id)}
                                                        whileHover={{ scale: 1.015 }}
                                                        whileTap={{ scale: 0.985 }}
                                                        className={`text-left p-4 rounded-xl border transition-all duration-200 ${
                                                            isSelected
                                                                ? `${sample.borderColor} ${sample.bgColor}`
                                                                : "border-[#1f1f1f] bg-[#0d0d0d] hover:border-[#2a2a2a] hover:bg-[#111111]"
                                                        }`}
                                                    >
                                                        <div className="flex items-start justify-between mb-2.5">
                                                            <span className="text-xl leading-none">{sample.emoji}</span>
                                                            {isSelected && (
                                                                <motion.span
                                                                    initial={{ scale: 0 }}
                                                                    animate={{ scale: 1 }}
                                                                    className={sample.accentColor}
                                                                >
                                                                    <CheckCircle2 size={15} />
                                                                </motion.span>
                                                            )}
                                                        </div>
                                                        <p className={`text-sm font-semibold mb-0.5 ${isSelected ? sample.accentColor : "text-zinc-200"}`}>
                                                            {sample.title}
                                                        </p>
                                                        <p className="text-xs text-zinc-500 leading-snug">
                                                            {sample.description}
                                                        </p>
                                                    </motion.button>
                                                );
                                            })}
                                        </div>
                                    </motion.div>
                                )}

                                {/* ── Upload JSON ── */}
                                {inputSource === "upload" && (
                                    <motion.div
                                        key="upload"
                                        initial={{ opacity: 0, y: 6 }}
                                        animate={{ opacity: 1, y: 0 }}
                                        exit={{ opacity: 0, y: -6 }}
                                        transition={{ duration: 0.2 }}
                                        className="space-y-4"
                                    >
                                        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 bg-[#0d0d0d] border border-[#1f1f1f] rounded-xl p-4">
                                            <p className="text-xs text-zinc-400 max-w-md leading-relaxed">
                                                Upload a <span className="text-zinc-200 font-mono">.json</span> file
                                                containing a{" "}
                                                <span className="text-zinc-200 font-mono">PredictionRequest</span> object
                                                with a <span className="text-zinc-200 font-mono">features</span> key.
                                            </p>
                                            <button
                                                onClick={handleDownloadDemoJson}
                                                type="button"
                                                className="flex items-center justify-center gap-1.5 px-3.5 py-1.5 rounded-lg text-xs font-semibold bg-white/5 border border-white/10 hover:bg-white hover:text-black hover:border-white transition-all duration-200 self-start sm:self-auto shadow-md"
                                            >
                                                <Download size={12} />
                                                <span>Download Demo JSON</span>
                                            </button>
                                        </div>

                                        <div
                                            onDragOver={(e) => { e.preventDefault(); setIsDragOver(true); }}
                                            onDragLeave={() => setIsDragOver(false)}
                                            onDrop={handleDrop}
                                            onClick={() => fileInputRef.current?.click()}
                                            className={`relative group cursor-pointer rounded-xl border-2 border-dashed p-10 flex flex-col items-center justify-center gap-4 transition-all duration-200 ${
                                                isDragOver
                                                    ? "border-blue-500/50 bg-blue-500/5"
                                                    : uploadedFile
                                                      ? "border-emerald-500/30 bg-emerald-500/5"
                                                      : "border-[#2a2a2a] hover:border-[#3a3a3a] hover:bg-[#111111]"
                                            }`}
                                        >
                                            <input
                                                ref={fileInputRef}
                                                type="file"
                                                accept=".json"
                                                className="hidden"
                                                onChange={handleFileInput}
                                            />

                                            {uploadedFile ? (
                                                <motion.div
                                                    initial={{ opacity: 0, scale: 0.9 }}
                                                    animate={{ opacity: 1, scale: 1 }}
                                                    className="flex flex-col items-center gap-3 text-center"
                                                >
                                                    <div className="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center">
                                                        <CheckCircle2 size={22} className="text-emerald-400" />
                                                    </div>
                                                    <div>
                                                        <p className="text-sm font-medium text-emerald-400 mb-0.5">
                                                            ✓ {uploadedFile.name}
                                                        </p>
                                                        <p className="text-xs text-zinc-500">
                                                            {formatBytes(uploadedFile.size)} · Ready to analyze
                                                        </p>
                                                    </div>
                                                    <button
                                                        onClick={(e) => {
                                                            e.stopPropagation();
                                                            setUploadedFile(null);
                                                            setUploadError(null);
                                                        }}
                                                        className="flex items-center gap-1.5 text-xs text-zinc-500 hover:text-zinc-300 transition-colors mt-1"
                                                    >
                                                        <X size={12} />
                                                        Remove
                                                    </button>
                                                </motion.div>
                                            ) : (
                                                <div className="flex flex-col items-center gap-3 text-center">
                                                    <div
                                                        className={`w-12 h-12 rounded-xl border flex items-center justify-center transition-colors ${
                                                            isDragOver
                                                                ? "bg-blue-500/10 border-blue-500/30"
                                                                : "bg-[#1a1a1a] border-[#2a2a2a] group-hover:border-[#3a3a3a]"
                                                        }`}
                                                    >
                                                        <Upload
                                                            size={20}
                                                            className={isDragOver ? "text-blue-400" : "text-zinc-500"}
                                                        />
                                                    </div>
                                                    <div>
                                                        <p className="text-sm font-medium text-zinc-300 mb-1">
                                                            Upload PredictionRequest JSON
                                                        </p>
                                                        <p className="text-xs text-zinc-600">
                                                            or drag &amp; drop · .json only
                                                        </p>
                                                    </div>
                                                </div>
                                            )}
                                        </div>

                                        <AnimatePresence>
                                            {uploadError && (
                                                <motion.p
                                                    initial={{ opacity: 0, y: -4 }}
                                                    animate={{ opacity: 1, y: 0 }}
                                                    exit={{ opacity: 0 }}
                                                    className="text-xs text-red-400 flex items-center gap-1.5"
                                                >
                                                    <AlertTriangle size={12} />
                                                    {uploadError}
                                                </motion.p>
                                            )}
                                        </AnimatePresence>
                                    </motion.div>
                                )}
                            </AnimatePresence>
                        </div>
                    </Card>

                    {/* ── Input Summary ── */}
                    <AnimatePresence>
                        {isReady && (
                            <motion.div
                                initial={{ opacity: 0, y: 6 }}
                                animate={{ opacity: 1, y: 0 }}
                                exit={{ opacity: 0, y: -6 }}
                                transition={{ duration: 0.25 }}
                            >
                                <Card className="px-5 py-4 border-[#252525]">
                                    <div className="flex flex-col sm:flex-row sm:items-center gap-4 sm:gap-8">
                                        <div className="flex items-center gap-2.5 shrink-0">
                                            <div className="w-7 h-7 rounded-lg bg-[#1a1a1a] border border-[#2a2a2a] flex items-center justify-center">
                                                <FileText size={13} className="text-zinc-400" />
                                            </div>
                                            <span className="text-xs font-medium text-zinc-400 uppercase tracking-widest">
                                                Selected Input
                                            </span>
                                        </div>
                                        <div className="flex flex-wrap gap-6">
                                            <div>
                                                <p className="text-[10px] text-zinc-600 uppercase tracking-wider mb-0.5">Source</p>
                                                <p className="text-xs text-zinc-200 font-medium">
                                                    {inputSource === "sample" ? "Sample Library" : "Uploaded JSON"}
                                                </p>
                                            </div>
                                            <div>
                                                <p className="text-[10px] text-zinc-600 uppercase tracking-wider mb-0.5">
                                                    {inputSource === "sample" ? "Sample" : "Filename"}
                                                </p>
                                                <p className="text-xs text-zinc-200 font-medium">
                                                    {inputSource === "sample"
                                                        ? selectedSample?.title
                                                        : uploadedFile?.name}
                                                </p>
                                            </div>
                                            <div>
                                                <p className="text-[10px] text-zinc-600 uppercase tracking-wider mb-0.5">Status</p>
                                                <span className="inline-flex items-center gap-1 text-xs text-emerald-400 font-medium">
                                                    <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
                                                    Ready
                                                </span>
                                            </div>
                                        </div>
                                    </div>
                                </Card>
                            </motion.div>
                        )}
                    </AnimatePresence>

                    {/* ── Analyze Button ── */}
                    <motion.button
                        id="analyze-btn"
                        onClick={handleAnalyze}
                        disabled={isLoading || backendError || !isReady}
                        className={`w-full flex items-center justify-center gap-2.5 px-5 py-4 rounded-xl text-sm font-semibold transition-all duration-200 ${
                            isLoading || backendError || !isReady
                                ? "bg-white/5 text-zinc-600 cursor-not-allowed border border-[#1f1f1f]"
                                : "bg-white text-black hover:bg-zinc-100 active:scale-[0.98] shadow-lg shadow-white/5"
                        }`}
                        whileTap={!isLoading && !backendError && isReady ? { scale: 0.98 } : {}}
                    >
                        {isLoading ? (
                            <>
                                <motion.span
                                    animate={{ rotate: 360 }}
                                    transition={{ duration: 1.2, repeat: Infinity, ease: "linear" }}
                                    className="inline-flex"
                                >
                                    <Activity size={15} />
                                </motion.span>
                                Analyzing…
                            </>
                        ) : (
                            <>
                                <Shield size={15} />
                                Analyze Network Traffic
                                <ArrowRight size={14} className="ml-auto" />
                            </>
                        )}
                    </motion.button>

                    {/* ── Animated Loading Pipeline ── */}
                    <AnimatePresence>
                        {isLoading && (
                            <motion.div
                                initial={{ opacity: 0, height: 0 }}
                                animate={{ opacity: 1, height: "auto" }}
                                exit={{ opacity: 0, height: 0 }}
                                className="overflow-hidden"
                            >
                                <Card className="p-5">
                                    <SectionLabel>Analysis Pipeline</SectionLabel>
                                    <div className="space-y-1.5">
                                        {LOADING_STAGES.map((stage, i) => {
                                            const stageIndex = STAGE_ORDER.indexOf(stage.key);
                                            const isDone = stageIndex < currentStageIndex;
                                            const isActive = stage.key === loadingStep;
                                            const Icon = stage.icon;

                                            return (
                                                <div key={stage.key}>
                                                    <motion.div
                                                        initial={{ opacity: 0, x: -8 }}
                                                        animate={{ opacity: 1, x: 0 }}
                                                        transition={{ delay: i * 0.06 }}
                                                        className={`flex items-center gap-3 px-4 py-3 rounded-xl border text-sm transition-all duration-300 ${
                                                            isActive
                                                                ? "border-blue-500/25 bg-blue-500/5 text-white"
                                                                : isDone
                                                                  ? "border-emerald-500/20 bg-emerald-500/5 text-zinc-400"
                                                                  : "border-[#1a1a1a] text-zinc-700"
                                                        }`}
                                                    >
                                                        <div className="shrink-0 w-5 h-5 flex items-center justify-center">
                                                            {isDone ? (
                                                                <CheckCircle2 size={15} className="text-emerald-400" />
                                                            ) : isActive ? (
                                                                <motion.span
                                                                    animate={{ opacity: [1, 0.3, 1] }}
                                                                    transition={{ duration: 1, repeat: Infinity }}
                                                                    className="text-blue-400"
                                                                >
                                                                    <Icon size={15} />
                                                                </motion.span>
                                                            ) : (
                                                                <Icon size={15} className="text-zinc-700" />
                                                            )}
                                                        </div>
                                                        <span
                                                            className={`text-sm font-medium ${
                                                                isActive
                                                                    ? "text-white"
                                                                    : isDone
                                                                      ? "text-zinc-400"
                                                                      : "text-zinc-700"
                                                            }`}
                                                        >
                                                            {stage.label}
                                                        </span>
                                                        {isActive && (
                                                            <motion.div
                                                                className="ml-auto flex gap-0.5"
                                                                initial={{ opacity: 0 }}
                                                                animate={{ opacity: 1 }}
                                                            >
                                                                {[0, 1, 2].map((dot) => (
                                                                    <motion.span
                                                                        key={dot}
                                                                        className="w-1 h-1 rounded-full bg-blue-400"
                                                                        animate={{ opacity: [0.3, 1, 0.3] }}
                                                                        transition={{
                                                                            duration: 1,
                                                                            repeat: Infinity,
                                                                            delay: dot * 0.2,
                                                                        }}
                                                                    />
                                                                ))}
                                                            </motion.div>
                                                        )}
                                                        {isDone && (
                                                            <ChevronRight
                                                                size={12}
                                                                className="ml-auto text-emerald-500/50"
                                                            />
                                                        )}
                                                    </motion.div>
                                                    {i < LOADING_STAGES.length - 1 && (
                                                        <div className="ml-[22px] border-l border-dashed border-[#1f1f1f] h-3" />
                                                    )}
                                                </div>
                                            );
                                        })}
                                    </div>
                                </Card>
                            </motion.div>
                        )}
                    </AnimatePresence>
                </motion.section>

                {/* ── Prediction Error ── */}
                <AnimatePresence>
                    {predError && (
                        <motion.div initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0 }}>
                            <Card className="p-6 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-red-500/15">
                                <div className="flex items-center gap-3">
                                    <div className="w-9 h-9 rounded-xl bg-red-500/10 border border-red-500/20 flex items-center justify-center shrink-0">
                                        <AlertTriangle size={16} className="text-red-400" />
                                    </div>
                                    <div>
                                        <p className="text-sm font-medium text-white">Analysis Failed</p>
                                        <p className="text-xs text-zinc-500 mt-0.5">{predError}</p>
                                    </div>
                                </div>
                                <button
                                    onClick={handleAnalyze}
                                    className="text-xs font-medium border border-[#2a2a2a] hover:border-white/30 text-zinc-300 hover:text-white px-4 py-2 rounded-xl transition-colors"
                                >
                                    Retry
                                </button>
                            </Card>
                        </motion.div>
                    )}
                </AnimatePresence>

                {/* ── Empty State ── */}
                <AnimatePresence>
                    {!result && !isLoading && !predError && (
                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            exit={{ opacity: 0 }}
                            className="flex flex-col items-center justify-center py-24 text-center"
                        >
                            <motion.div
                                animate={{ y: [0, -4, 0] }}
                                transition={{ duration: 3.5, repeat: Infinity, ease: "easeInOut" }}
                                className="mb-6"
                            >
                                <div className="relative w-20 h-20 mx-auto">
                                    <div className="absolute inset-0 rounded-2xl bg-gradient-to-br from-[#1a1a2e] to-[#111111] border border-[#1f1f1f]" />
                                    <div className="absolute inset-0 flex items-center justify-center">
                                        <Shield size={30} className="text-zinc-600" />
                                    </div>
                                    <div className="absolute -inset-3 rounded-3xl border border-[#1a1a1a] opacity-60" />
                                    <div className="absolute -inset-6 rounded-[28px] border border-[#161616] opacity-40" />
                                </div>
                            </motion.div>
                            <p className="text-base font-semibold text-zinc-300 mb-2">No analysis performed</p>
                            <p className="text-sm text-zinc-600 max-w-sm leading-relaxed">
                                Choose a sample attack or upload a PredictionRequest JSON file to begin threat
                                analysis.
                            </p>
                        </motion.div>
                    )}
                </AnimatePresence>

                {/* ── Report ── */}
                <AnimatePresence>
                    {result && (
                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            exit={{ opacity: 0 }}
                            className="space-y-5"
                        >
                            {/* Section header */}
                            <div className="flex items-center gap-2.5 pb-3 border-b border-[#1f1f1f]">
                                <div className="w-7 h-7 rounded-lg bg-[#1a1a1a] border border-[#2a2a2a] flex items-center justify-center">
                                    <ShieldCheck size={13} className="text-zinc-400" />
                                </div>
                                <h2 className="text-sm font-semibold text-white">Security Report</h2>
                                <span className="ml-auto text-xs text-zinc-600 font-mono">{result.request_id}</span>
                            </div>

                            {/* ── Threat Overview ── */}
                            <motion.div
                                initial={{ opacity: 0, y: 10 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: 0.05 }}
                                className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3"
                            >
                                <Card className="p-4 col-span-2 sm:col-span-1">
                                    <SectionLabel>Attack</SectionLabel>
                                    <p className="text-base font-bold text-white leading-tight">
                                        {result.prediction.attack_name}
                                    </p>
                                </Card>

                                <Card className="p-4">
                                    <SectionLabel>Severity</SectionLabel>
                                    <span
                                        className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg text-xs font-semibold border ${sc.text} ${sc.bg} ${sc.border}`}
                                    >
                                        <AlertTriangle size={11} />
                                        {severity}
                                    </span>
                                </Card>

                                <Card className="p-4">
                                    <SectionLabel>Latency</SectionLabel>
                                    <p className="text-base font-bold text-white">
                                        {result.latency_ms}
                                        <span className="text-xs font-normal text-zinc-500 ml-1">ms</span>
                                    </p>
                                </Card>

                                <Card className="p-4">
                                    <SectionLabel>Model</SectionLabel>
                                    <p className="text-base font-bold text-white">{result.model_version}</p>
                                </Card>

                                <Card className="p-4 col-span-2">
                                    <SectionLabel>Timestamp</SectionLabel>
                                    <div className="flex items-center gap-2 text-sm text-zinc-300">
                                        <Clock size={13} className="text-zinc-500 shrink-0" />
                                        {formatTimestamp(result.timestamp)}
                                    </div>
                                </Card>

                                <Card className="p-4 col-span-2">
                                    <SectionLabel>Request ID</SectionLabel>
                                    <p className="text-xs text-zinc-400 font-mono truncate">{result.request_id}</p>
                                </Card>
                            </motion.div>

                            {/* ── Confidence ── */}
                            <motion.div
                                initial={{ opacity: 0, y: 10 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: 0.1 }}
                            >
                                <Card className="p-5">
                                    <div className="flex items-center justify-between mb-3">
                                        <SectionLabel>Confidence Score</SectionLabel>
                                        <span className="text-2xl font-bold text-white tabular-nums">
                                            {confidenceDisplay}
                                            <span className="text-sm font-normal text-zinc-500">%</span>
                                        </span>
                                    </div>
                                    <div className="h-1.5 bg-[#1f1f1f] rounded-full overflow-hidden">
                                        <motion.div
                                            className="h-full bg-white rounded-full"
                                            initial={{ width: 0 }}
                                            animate={{ width: `${Math.round(result.prediction.confidence * 100)}%` }}
                                            transition={{ duration: 1, ease: "easeOut" }}
                                        />
                                    </div>
                                </Card>
                            </motion.div>

                            {/* ── Executive Summary ── */}
                            <motion.div
                                initial={{ opacity: 0, y: 10 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: 0.15 }}
                            >
                                <Card className="p-5">
                                    <div className="flex items-center gap-2 mb-3">
                                        <FileText size={14} className="text-zinc-500" />
                                        <SectionLabel>Executive Summary</SectionLabel>
                                    </div>
                                    <p className="text-sm text-zinc-300 leading-relaxed">
                                        {result.prediction.executive_summary}
                                    </p>
                                </Card>
                            </motion.div>

                            {/* ── Technical Explanation ── */}
                            <motion.div
                                initial={{ opacity: 0, y: 10 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: 0.18 }}
                            >
                                <Card className="p-5">
                                    <div className="flex items-center gap-2 mb-3">
                                        <Bug size={14} className="text-zinc-500" />
                                        <SectionLabel>Technical Explanation</SectionLabel>
                                    </div>
                                    <p className="text-sm text-zinc-300 leading-relaxed">
                                        {result.prediction.technical_explanation}
                                    </p>
                                </Card>
                            </motion.div>

                            {/* ── Prediction Reason ── */}
                            <motion.div
                                initial={{ opacity: 0, y: 10 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: 0.2 }}
                            >
                                <Card className="p-5">
                                    <div className="flex items-center gap-2 mb-3">
                                        <Brain size={14} className="text-zinc-500" />
                                        <SectionLabel>Prediction Reason</SectionLabel>
                                    </div>
                                    <p className="text-sm text-zinc-300 leading-relaxed">
                                        {result.prediction.prediction_reason}
                                    </p>
                                </Card>
                            </motion.div>

                            {/* ── MITRE ATT&CK ── */}
                            {result.prediction.mitre_attack.length > 0 && (
                                <motion.div
                                    initial={{ opacity: 0, y: 10 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    transition={{ delay: 0.22 }}
                                >
                                    <Card className="p-5">
                                        <div className="flex items-center gap-2 mb-3">
                                            <Terminal size={14} className="text-zinc-500" />
                                            <SectionLabel>MITRE ATT&amp;CK</SectionLabel>
                                        </div>
                                        <div className="flex flex-wrap gap-2">
                                            {result.prediction.mitre_attack.map((m) => (
                                                <div
                                                    key={m.technique_id}
                                                    className="inline-flex items-center gap-2 border border-[#2a2a2a] bg-[#161616] rounded-xl px-3 py-2"
                                                >
                                                    <span className="text-xs font-mono text-zinc-400">
                                                        {m.technique_id}
                                                    </span>
                                                    <span className="w-px h-3 bg-[#2a2a2a]" />
                                                    <span className="text-xs text-zinc-300">{m.technique_name}</span>
                                                    <span className="w-px h-3 bg-[#2a2a2a]" />
                                                    <span className="text-xs text-zinc-500">{m.tactic}</span>
                                                </div>
                                            ))}
                                        </div>
                                    </Card>
                                </motion.div>
                            )}

                            {/* ── Indicators of Compromise ── */}
                            {result.prediction.indicators_of_compromise.length > 0 && (
                                <motion.div
                                    initial={{ opacity: 0, y: 10 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    transition={{ delay: 0.24 }}
                                >
                                    <Card className="p-5">
                                        <div className="flex items-center gap-2 mb-3">
                                            <Zap size={14} className="text-zinc-500" />
                                            <SectionLabel>Indicators of Compromise</SectionLabel>
                                        </div>
                                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                            {result.prediction.indicators_of_compromise.map((ioc, i) => (
                                                <div
                                                    key={i}
                                                    className="border border-[#1f1f1f] rounded-xl p-3 bg-[#0d0d0d]"
                                                >
                                                    <div className="flex items-center gap-2 mb-1">
                                                        <span className="text-[10px] uppercase tracking-wider text-zinc-500 font-medium border border-[#2a2a2a] px-1.5 py-0.5 rounded-md">
                                                            {ioc.type}
                                                        </span>
                                                    </div>
                                                    <p className="text-xs font-mono text-zinc-300 break-all">
                                                        {ioc.value}
                                                    </p>
                                                    {ioc.description && (
                                                        <p className="text-xs text-zinc-500 mt-1 leading-snug">
                                                            {ioc.description}
                                                        </p>
                                                    )}
                                                </div>
                                            ))}
                                        </div>
                                    </Card>
                                </motion.div>
                            )}

                            {/* ── Business Impact ── */}
                            {result.prediction.business_impact.length > 0 && (
                                <motion.div
                                    initial={{ opacity: 0, y: 10 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    transition={{ delay: 0.26 }}
                                >
                                    <Card className="p-5">
                                        <div className="flex items-center gap-2 mb-3">
                                            <AlertTriangle size={14} className="text-zinc-500" />
                                            <SectionLabel>Business Impact</SectionLabel>
                                        </div>
                                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                            {result.prediction.business_impact.map((item, i) => (
                                                <div
                                                    key={i}
                                                    className="flex items-start gap-2.5 border border-yellow-500/15 bg-yellow-500/5 rounded-xl p-3"
                                                >
                                                    <AlertTriangle
                                                        size={13}
                                                        className="text-yellow-400 shrink-0 mt-0.5"
                                                    />
                                                    <p className="text-xs text-zinc-300 leading-snug">{item}</p>
                                                </div>
                                            ))}
                                        </div>
                                    </Card>
                                </motion.div>
                            )}

                            {/* ── Mitigations ── */}
                            {result.prediction.mitigations.length > 0 && (
                                <motion.div
                                    initial={{ opacity: 0, y: 10 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    transition={{ delay: 0.28 }}
                                >
                                    <Card className="p-5">
                                        <div className="flex items-center gap-2 mb-3">
                                            <Lock size={14} className="text-zinc-500" />
                                            <SectionLabel>Mitigations</SectionLabel>
                                        </div>
                                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                                            {result.prediction.mitigations.map((item, i) => (
                                                <div
                                                    key={i}
                                                    className="flex items-start gap-2.5 border border-emerald-500/15 bg-emerald-500/5 rounded-xl p-3"
                                                >
                                                    <CheckCircle2
                                                        size={13}
                                                        className="text-emerald-400 shrink-0 mt-1"
                                                    />
                                                    <div>
                                                        {item.title && (
                                                            <p className="text-xs font-semibold text-emerald-300 mb-0.5">{item.title}</p>
                                                        )}
                                                        <p className="text-xs text-zinc-300 leading-snug">{item.description}</p>
                                                    </div>
                                                </div>
                                            ))}
                                        </div>
                                    </Card>
                                </motion.div>
                            )}

                            {/* ── References ── */}
                            {result.prediction.references.length > 0 && (
                                <motion.div
                                    initial={{ opacity: 0, y: 10 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    transition={{ delay: 0.3 }}
                                >
                                    <Card className="p-5">
                                        <div className="flex items-center gap-2 mb-3">
                                            <BookOpen size={14} className="text-zinc-500" />
                                            <SectionLabel>References</SectionLabel>
                                        </div>
                                        <div className="space-y-2">
                                            {result.prediction.references.map((ref, i) => (
                                                <div
                                                    key={i}
                                                    className="flex items-start gap-3 border border-[#1f1f1f] rounded-xl p-3 group hover:border-[#2a2a2a] transition-colors"
                                                >
                                                    <span className="text-xs text-zinc-600 font-mono mt-0.5 shrink-0 w-5 text-right">
                                                        {i + 1}
                                                    </span>
                                                    <div className="min-w-0">
                                                        {ref.title && (
                                                            <p className="text-xs font-medium text-zinc-300 mb-0.5">{ref.title}</p>
                                                        )}
                                                        {ref.url && (
                                                            <a
                                                                href={ref.url}
                                                                target="_blank"
                                                                rel="noopener noreferrer"
                                                                className="text-xs text-blue-400 hover:text-blue-300 leading-relaxed break-all transition-colors"
                                                            >
                                                                {ref.url}
                                                            </a>
                                                        )}
                                                    </div>
                                                </div>
                                            ))}
                                        </div>
                                    </Card>
                                </motion.div>
                            )}
                        </motion.div>
                    )}
                </AnimatePresence>
            </div>
        </main>
    );
}
