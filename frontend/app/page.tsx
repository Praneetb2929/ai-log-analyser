"use client";

import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const uploadLog = async () => {
    if (!file) return alert("Upload a file first");

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const res = await axios.post(
        "http://127.0.0.1:8000/upload-log",
        formData
      );

      setData(res.data);
    } catch (err) {
      alert("Upload failed. Check backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="p-10 min-h-screen bg-black text-white">
      
      {/* Title */}
      <h1 className="text-4xl font-bold mb-8">
        AI Log Analyzer 🚀
      </h1>

      {/* Upload Section */}
      <div className="bg-gray-900 p-6 rounded-xl shadow-md mb-8">
        <input
          type="file"
          onChange={(e) => setFile(e.target.files?.[0] || null)}
          className="mb-4"
        />

        <button
          onClick={uploadLog}
          className="bg-blue-600 hover:bg-blue-700 px-6 py-2 rounded"
        >
          {loading ? "Analyzing..." : "Upload & Analyze"}
        </button>
      </div>

      {/* Results */}
      {data && (
        <div className="grid md:grid-cols-2 gap-6">

          {/* Errors Card */}
          <div className="bg-gray-900 p-6 rounded-xl shadow-md">
            <h2 className="text-xl font-semibold mb-4 text-red-400">
              Errors ❌
            </h2>

            {data.issues.errors.length === 0 ? (
              <p>No errors</p>
            ) : (
              data.issues.errors.map((e: string, i: number) => (
                <p key={i} className="text-red-400 mb-2">
                  {e}
                </p>
              ))
            )}
          </div>

          {/* Warnings Card */}
          <div className="bg-gray-900 p-6 rounded-xl shadow-md">
            <h2 className="text-xl font-semibold mb-4 text-yellow-400">
              Warnings ⚠️
            </h2>

            {data.issues.warnings.length === 0 ? (
              <p>No warnings</p>
            ) : (
              data.issues.warnings.map((w: string, i: number) => (
                <p key={i} className="text-yellow-400 mb-2">
                  {w}
                </p>
              ))
            )}
          </div>

          {/* AI Analysis Card */}
          <div className="md:col-span-2 bg-gray-900 p-6 rounded-xl shadow-md">
            <h2 className="text-xl font-semibold mb-4 text-green-400">
              AI Analysis 🧠
            </h2>

            <pre className="whitespace-pre-wrap text-sm leading-6">
              {data.analysis}
            </pre>
          </div>

        </div>
      )}
    </main>
  );
}