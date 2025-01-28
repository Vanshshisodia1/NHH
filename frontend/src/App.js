import React, { useState } from 'react';

function App() {
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState("");

  const handleFileUpload = async (e) => {
    setFile(e.target.files[0]);
  };

  const handleScan = async () => {
    if (!file) {
      alert("Please upload a file first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://localhost:5000/api/ocr", {
      method: "POST",
      body: formData,
    });
    const data = await res.json();
    setResponse(data.text || "Error in processing");
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>Prescription Scanner</h1>
      <input type="file" onChange={handleFileUpload} />
      <button onClick={handleScan}>Scan Prescription</button>
      <p>Response: {response}</p>
    </div>
  );
}

export default App;
