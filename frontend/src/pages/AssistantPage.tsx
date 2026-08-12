import { useState, type FormEvent } from "react";
import { practiceApi } from "../api/practice";
import { ApiError } from "../api/client";

interface Message {
  role: "user" | "assistant";
  text: string;
}

const SUGGESTED_QUESTIONS = [
  "Which chapters should I study before my exam?",
  "How am I doing overall?",
  "How many chapters have I mastered?",
  "Am I improving?",
  "How many questions have I answered?",
  "How is mastery calculated?",
  "What's my streak?",
];

/**
 * Student Insights: a fixed set of question patterns answered from the
 * student's real practice data, not a generic chatbot. Suggested-question
 * chips make the finite-intent nature visible rather than implying
 * open-ended natural language understanding.
 */
export default function AssistantPage() {
  const [messages, setMessages] = useState<Message[]>([
    { role: "assistant", text: "Ask me about your chapters, overall performance, or study streak." },
  ]);
  const [input, setInput] = useState("");
  const [sending, setSending] = useState(false);

  async function ask(question: string) {
    if (!question.trim() || sending) return;
    setMessages((m) => [...m, { role: "user", text: question }]);
    setInput("");
    setSending(true);
    try {
      const res = await practiceApi.askAssistant(question);
      setMessages((m) => [...m, { role: "assistant", text: res.answer }]);
    } catch (err) {
      setMessages((m) => [
        ...m,
        { role: "assistant", text: err instanceof ApiError ? err.message : "Something went wrong answering that." },
      ]);
    } finally {
      setSending(false);
    }
  }

  function handleSubmit(e: FormEvent) {
    e.preventDefault();
    ask(input);
  }

  return (
    <div className="assistant-page">
      <h1>Student Insights</h1>
      <p className="dashboard-subtitle">
        Data-aware answers grounded in your own practice history - not a generic chatbot.
      </p>

      <div className="assistant-chips">
        {SUGGESTED_QUESTIONS.map((q) => (
          <button key={q} type="button" className="assistant-chip" onClick={() => ask(q)} disabled={sending}>
            {q}
          </button>
        ))}
      </div>

      <div className="assistant-transcript">
        {messages.map((m, i) => (
          <div key={i} className={`assistant-message assistant-message-${m.role}`}>
            {m.text.split("\n").map((line, j) => (
              <p key={j}>{line}</p>
            ))}
          </div>
        ))}
        {sending && <div className="assistant-message assistant-message-assistant">…</div>}
      </div>

      <form className="assistant-input-row" onSubmit={handleSubmit}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask about your chapters, performance, or streak…"
          disabled={sending}
        />
        <button type="submit" disabled={sending || !input.trim()}>
          Ask
        </button>
      </form>
    </div>
  );
}
