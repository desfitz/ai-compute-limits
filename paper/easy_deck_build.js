const pptxgen = require("pptxgenjs");
const { applyTheme } = require("/root/.claude/skills/synced/c8a5a490-4a2d-440d-bca5-a78c054bf17b_67bd6897-f4e8-4ad4-9fce-d5bbf4ec4bc3/pptx/scripts/apply_theme.js");
const fs = require("fs");

const THEME = {
  name: "Classic Navy",
  headFontFace: "Cambria",
  bodyFontFace: "Calibri",
  colors: { dk1: "1F1F1F", lt1: "FFFFFF", dk2: "1E2761", lt2: "F3F5F9", accent1: "1E2761", accent2: "4A6FA5", accent3: "8C8C8C", accent4: "B85042", accent5: "6B7B8C", accent6: "C9D3E3", hlink: "1E2761", folHlink: "4A6FA5" },
};

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.author = "Desmond Fitzpatrick"; pres.title = "Will the AI build-out pay for itself?";
const C = pres.SchemeColor;
const FOOT = "Will the AI build-out pay for itself?  |  from The Macroeconomic Limits of AI Compute, v27, October 2026";

pres.defineSlideMaster({
  title: "CONTENT", background: { color: "FFFFFF" },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.35, w: 12.1, h: 0.8, fontSize: 30, bold: true, color: C.text2, margin: 0, valign: "middle", align: "left" }, text: "" } },
  ],
  slideNumber: { x: 12.3, y: 7.0, w: 0.5, h: 0.3, fontSize: 9, color: "8C8C8C" },
});
pres.defineSlideMaster({ title: "TITLE", background: { color: "FFFFFF" }, objects: [] });

const T = (s, txt, sub) => {
  s.addText(txt, { placeholder: "title" });
  if (sub) s.addText(sub, { x: 0.6, y: 1.1, w: 12.1, h: 0.4, fontSize: 16, italic: true, color: C.accent3, margin: 0, isTextBox: true });
};
const P = (s, txt, x, y, w, h, opts = {}) => s.addText(txt, Object.assign({ x, y, w, h, fontSize: 16, color: C.text1, margin: 0, valign: "top", isTextBox: true, paraSpaceAfter: 6 }, opts));
const BIG = (s, num, lab, x, y, w) => {
  s.addText(num, { x, y, w, h: 0.9, fontSize: 40, bold: true, color: C.accent1, align: "center", margin: 0, isTextBox: true });
  s.addText(lab, { x, y: y + 0.9, w, h: 0.6, fontSize: 13, color: C.accent3, align: "center", margin: 0, isTextBox: true });
};
const IMG = (s, f, x, y, w, h) => s.addImage({ path: `figc/${f}.png`, x, y, w, h, sizing: { type: "contain", w, h } });
const SRC = (s, txt) => s.addText(txt, { x: 0.6, y: 6.55, w: 12.1, h: 0.4, fontSize: 10, color: C.accent3, margin: 0, isTextBox: true });
const BUL = (items) => items.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i < items.length - 1, paraSpaceAfter: 8 } }));

let s;
// 1 Title
s = pres.addSlide({ masterName: "TITLE" });
s.addText("Will the AI build-out pay for itself?", { x: 0.8, y: 1.6, w: 11.7, h: 1.2, fontSize: 44, bold: true, color: C.text2, margin: 0, isTextBox: true });
s.addText("A Fermi estimate, in thirteen slides", { x: 0.8, y: 2.8, w: 11.7, h: 0.6, fontSize: 24, color: C.accent2, margin: 0, isTextBox: true });
s.addText([
  { text: "Desmond Fitzpatrick", options: { bold: true, breakLine: true } },
  { text: "Retired, IBM Systems   |   Founder, Nvara.ai", options: { breakLine: true } },
  { text: "desmond.fitzpatrick@nvara.ai   |   ORCID 0009-0001-0534-2793", options: {} },
], { x: 0.8, y: 4.0, w: 11.7, h: 1.2, fontSize: 16, color: C.text1, margin: 0, isTextBox: true });
s.addText("This is a probability assessment, not a forecast: the most likely outcome at the inputs we could source, and what would move it. It is the short version of a 106-page paper whose every number sits in a public register anyone can challenge. If a slide here and the paper disagree, the paper is right. Paper, model and data: doi.org/10.5281/zenodo.23406476", { x: 0.8, y: 5.6, w: 11.7, h: 1.0, fontSize: 12, color: C.accent3, margin: 0, isTextBox: true });

// 2 The question
s = pres.addSlide({ masterName: "CONTENT" }); T(s, "1. The question", "Will the revenue arrive to pay for the build-out?");
P(s, "Five companies — Microsoft, Alphabet, Amazon, Meta and Oracle — are spending about $780 billion this year on AI data centers, after $448 billion last year. The question is not whether AI is useful. It is whether the revenue will arrive, fast enough, to pay for the buildings and the chips.", 0.6, 1.7, 5.4, 4.5, { fontSize: 18 });
IMG(s, "f1_capex", 6.4, 1.7, 6.3, 4.6);
SRC(s, "Capex from company filings via Epoch AI; 2026 from the companies' own July guidance. Street consensus for 2027 is higher still, about $1.05 trillion.");


// 2 Fermi
s = pres.addSlide({ masterName: "CONTENT" }); T(s, "2. How we estimate: the Fermi way", "A long way on bounded factors; only the big uncertainties left as a tail");
P(s, "Fermi asked how many piano tuners Chicago had and got within a factor of two by chaining things he could bound: people, households, pianos per household, tunings a year, tunings a tuner can do. No single factor was known well. The product was, because the errors cancel rather than compound.\n\nThis paper does the same. The carry is a chain of factors each known to tens of percent (capex, silicon share, lives, power, cost of capital). Demand is fifteen such chains. Where an input carried too much of the uncertainty, we split it into sourced pieces — nineteen times — until the spread fell from 286 to 104 and only two big uncertainties were left: how fast firms actually adopt, and how big the office-assistant market gets. Those two are the tail, and the probability map is drawn over them.", 0.6, 1.7, 6.2, 4.8, { fontSize: 15 });
IMG(s, "f7_tornado", 7.0, 1.6, 5.7, 4.9);
SRC(s, "Paper Sections 2 and 9. The chart ranks every input by how much it moves the 2030 result; the long bars are the tail.");

// 3 Carry
s = pres.addSlide({ masterName: "CONTENT" }); T(s, "3. What it costs every year", "The carry: wear, running costs, and the return on the money");
P(s, "A data center is not paid for when it is bought. Each year it costs its owner three things: the chips wearing out (about four years), running the building (power, people, maintenance), and the return the money could have earned elsewhere. We call that yearly cost the carry.", 0.6, 1.7, 5.4, 2.2);
BIG(s, "$390B → $725B", "carry per year, 2027 to 2030, if spending merely stays flat", 0.6, 4.0, 5.4);
P(s, "It keeps rising even if spending stops rising: this year's chips are still on the books when next year's arrive.", 0.6, 5.6, 5.4, 0.9, { fontSize: 14, color: C.accent3 });
IMG(s, "f2_carry", 6.4, 1.7, 6.3, 4.6);
SRC(s, "Paper Section 4. About 28 cents of revenue per dollar of capital per year; Goldman Sachs's September 2026 framework says 27.");

// 4 Today
s = pres.addSlide({ masterName: "CONTENT" }); T(s, "4. What comes in today");
P(s, "All AI revenue in calendar 2026 — the frontier labs (OpenAI, Anthropic and others), the clouds' AI services, the AI lift in advertising, consumer subscriptions — adds up to roughly $180 billion. That is real money and it is growing very fast. It is also less than a quarter of what the installed base will cost to carry in 2030.", 0.6, 1.5, 12.1, 1.6, { fontSize: 18 });
BIG(s, "~$180B", "AI revenue, 2026, all channels (range $165–190B)", 1.0, 3.4, 5.4);
BIG(s, "~$725B", "carry of the installed base, 2030, if spending plateaus", 6.9, 3.4, 5.4);
P(s, "So the whole argument is about one number: how fast revenue has to grow to catch the carry — and whether anything in the real economy can grow that fast for that long.", 0.6, 5.3, 12.1, 1.0, { fontSize: 18, bold: false });
SRC(s, "Paper Section 7: the 2026 base, decomposed into seven sourced pieces; lab run-rates are discounted to booked revenue.");

// 5 Scissors
s = pres.addSlide({ masterName: "CONTENT" }); T(s, "5. How fast revenue must grow", "The scissors");
P(s, "Grow today's $180 billion at a steady rate and see where it crosses the carry. It takes about 49% a year, every year to 2030, just to break even on a flat spending path — and nothing clears 2027–28, which is already a sunk loss of $100–250 billion a year.", 0.6, 1.7, 5.0, 4.0, { fontSize: 18 });
IMG(s, "f3_scissors", 5.9, 1.6, 6.8, 4.9);
SRC(s, "Paper Section 10. Under the street's own spending path (an arms race) break-even needs 62% a year; under a 35% cut, 33%.");

// 6 Sectors
s = pres.addSlide({ masterName: "CONTENT" }); T(s, "6. Where the revenue would come from", "Fifteen sectors, counted one by one");
IMG(s, "f9_sectors", 0.6, 1.6, 7.0, 4.9);
P(s, "Instead of assuming a growth rate, the paper builds demand up from fifteen sectors — office assistants and agents, advertising, consumer apps, coding tools, healthcare, robotics and so on — each with a 2026 base, a ceiling set by payrolls, IT budgets or users, and a realistic ramp.", 7.9, 1.6, 4.8, 2.2, { fontSize: 15 });
BIG(s, "~$625B", "what end customers spend on AI in 2030 (range $525–745B)", 7.9, 3.9, 4.8);
P(s, "About 33% a year, not 49%. Growth starts near 57% in 2027 and decays toward 14% by 2030.", 7.9, 5.5, 4.8, 0.9, { fontSize: 14, color: C.accent3 });
SRC(s, "Paper Section 8. No single sector closes the gap; the four largest are office assistants, advertising, consumer and coding.");

// 7 Leak
s = pres.addSlide({ masterName: "CONTENT" }); T(s, "7. Not all of it reaches the builders", "Where a customer's dollar goes");
P(s, "A customer's dollar passes through the labs and the application builders before any of it reaches the cloud owner. Routine work moves onto cheap or local chips; outcome-priced integrators keep most of the savings they create. In contact centers, roughly $50 of payroll disappears for every $1 of cloud tokens.", 0.6, 1.7, 4.6, 4.5, { fontSize: 16 });
IMG(s, "f18_flow", 5.4, 1.6, 7.3, 4.9);
SRC(s, "Paper Sections 8 and 13. Of the $625B customers spend in 2030, about $480–490B reaches the infrastructure owners.");

// 8 Gap
s = pres.addSlide({ masterName: "CONTENT" }); T(s, "8. The gap", "The most likely outcome at the register's current inputs");
BIG(s, "~$255B a year", "short in 2030 if spending plateaus", 0.6, 1.7, 5.4);
BIG(s, "$190–540B", "short in 2030 under the street's arms-race path", 0.6, 3.5, 5.4);
P(s, "This is the most likely outcome, 3.5 standard deviations from break-even with every range propagated. Change the inputs and it moves; the last slide says how.", 0.6, 5.2, 5.4, 1.2, { fontSize: 15, color: C.accent3 });
IMG(s, "f10_reconcile", 6.4, 1.6, 6.3, 4.9);
SRC(s, "Paper Section 10, Table 12. 2027–28 is a loss on every path; the argument is about whether 2029–30 recovers it.");

// 9 Why growth slows
s = pres.addSlide({ masterName: "CONTENT" }); T(s, "9. Why growth slows", "Five things already visible");
s.addText(BUL([
  "Slack. Saving an analyst thirty minutes a day across six tasks does not let you fire anyone. Nominal time savings convert to cash at roughly 28 cents on the dollar.",
  "Verification. The person who used to write the memo now checks it. Liability keeps a human in the loop.",
  "Leakage. Savings go to the buyer and the integrator who fixed the process, not the cloud. Routine inference moves to 1.45 billion on-device chips a year.",
  "Sovereignty. Europe, India and others carve 15–35% of demand out of the US clouds while forcing them to duplicate capital.",
  "Grid and consent. $130 billion of US projects were blocked or delayed in the first quarter of 2026 alone. Chips bought before they can be powered earn nothing.",
]), { x: 0.6, y: 1.8, w: 12.1, h: 4.6, fontSize: 19, color: C.text1, margin: 0, valign: "top", isTextBox: true, paraSpaceAfter: 14 });
SRC(s, "Paper Sections 11–13. Each has a precedent: electricity took forty years to show up in factory productivity; computers took twenty.");

// 10 Chips worth less
s = pres.addSlide({ masterName: "CONTENT" }); T(s, "10. The chips are worth less than the books say");
P(s, "Accountants depreciate a chip over five or six years. Economically it is worth what it can earn against the newest chip, whose cost per token falls 50–90% a year. On that schedule the silicon bought through 2026 is already worth $100–250 billion less than the balance sheets show.", 0.6, 1.5, 12.1, 1.5, { fontSize: 17 });
IMG(s, "f23_econdep_floor", 0.6, 3.1, 12.1, 3.4);
SRC(s, "Paper Section 14. If token prices fall to the cash cost of running the chips (a tenth of today's), the capital is never recovered.");

// 11 Bulls
s = pres.addSlide({ masterName: "CONTENT" }); T(s, "11. Where we agree and disagree with the bulls", "a16z and Goldman Sachs, September 2026");
P(s, "The paper takes a16z's State of Markets and Goldman Sachs's ROIC note point by point. We agree with both on almost every observable: capex consensus, backlogs near $1.7 trillion, rising GPU rents, the ROIC on existing businesses. The yearly cost per dollar of capital is not in dispute — Goldman's 27 cents, our 28.", 0.6, 1.7, 12.1, 1.6, { fontSize: 17 });
P(s, "The disagreements are three, and they are judgments, not arithmetic:", 0.6, 3.3, 12.1, 0.4, { fontSize: 16, bold: true });
s.addText(BUL([
  "Whether AI gets paid from labor budgets (the $30 trillion payroll) as well as IT budgets — the bulls say yes; we show why only a fraction converts.",
  "Whether today's scarce, expensive compute is the permanent state or the top of a cycle.",
  "Whether you count one cohort of spending (Goldman's $1.73 trillion for 2026–27) or every cohort stacked on the balance sheet. A balance sheet does not get to choose.",
]), { x: 0.6, y: 3.9, w: 12.1, h: 2.6, fontSize: 17, color: C.text1, margin: 0, valign: "top", isTextBox: true, paraSpaceAfter: 12 });
SRC(s, "Paper Sections 15 and 16.");

// 12 Prove wrong
s = pres.addSlide({ masterName: "CONTENT" }); T(s, "12. What would change the most likely outcome, and when");
BIG(s, "$400B", "AI revenue in calendar 2028 above this overturns the most likely outcome", 0.6, 1.7, 5.4);
P(s, "Interim marker: calendar 2027 near $330B is our path; above $350B favours the build-out.\n\nThe next data: the Q3 earnings calls of 28–30 October, Nvidia on 19 November, the Anthropic listing. The register is rebuilt after each and the paper re-issued if anything moves materially.", 0.6, 3.5, 5.4, 2.9, { fontSize: 15 });
IMG(s, "f17_probmap", 6.4, 1.8, 6.3, 2.6);
P(s, "Probability of profit in 2030 over the two things we cannot pin down: how fast firms actually adopt, and how big the office-assistant market gets.", 6.4, 4.6, 6.3, 1.2, { fontSize: 12, color: C.accent3 });
SRC(s, "Paper Section 17 and the update protocol.");

// 13 Way out
s = pres.addSlide({ masterName: "CONTENT" }); T(s, "13. The way out is not dramatic");
P(s, "Stop building ahead of revenue. An operator that cuts spending by about a third — or simply lets spending track the revenue it actually books — turns profitable around 2031 and recovers the hole by 2034–35. A plateau never recovers within the horizon; an arms race widens the gap every year.", 0.6, 1.5, 12.1, 1.4, { fontSize: 17 });
IMG(s, "f20_adaptive", 2.4, 3.0, 8.5, 3.5);
SRC(s, "Paper appendix on the 2035 horizon. The forecast is impairments and a capex retreat in 2027–29, then a cheaper, more distributed equilibrium — not the end of AI.");

// 14 Whole argument
s = pres.addSlide({ masterName: "CONTENT" }); T(s, "The whole argument", "and how to take part");
P(s, "In six lines", 0.6, 1.7, 6.6, 0.4, { bold: true });
s.addText([
  "Fermi, not forecast: every number is a chain of bounded factors; nineteen were decomposed until only two big uncertainties remain.",
  "The installed base costs about 28 cents per dollar per year to carry; that is $725B a year by 2030 on a flat path.",
  "Revenue is $180B today and must grow 49% a year to catch it.",
  "Counted sector by sector, it grows 33%, and only $480–490B of it reaches the owners.",
  "The gap is $255B a year in 2030, more under the street's path, and 2027–28 is already lost.",
  "Watch 2027 and 2028 revenue: above $400B in 2028, the most likely outcome was wrong.",
].map((t, i, a) => ({ text: t, options: { bullet: { type: "number" }, breakLine: i < a.length - 1, paraSpaceAfter: 6 } })), { x: 0.6, y: 2.2, w: 6.6, h: 4.2, fontSize: 15, color: C.text1, margin: 0, valign: "top", isTextBox: true });
P(s, "Every number is yours to challenge", 7.6, 1.7, 5.1, 0.4, { bold: true });
P(s, "The paper, the model, the data and the register of inputs — each with its evidence, its range and what would improve it — are public. Change an input, run one script, and the paper's numbers and charts regenerate; the script says whether the change is minor or forces a re-issue.\n\nPaper and bundle: doi.org/10.5281/zenodo.23406476\nModel and register: the GitHub repository named in the paper\nComments: desmond.fitzpatrick@nvara.ai", 7.6, 2.2, 5.1, 4.2, { fontSize: 13 });
SRC(s, "Figures are the paper's own; no number here is newer than the paper's register.");

(async () => {
  const out = "ai_compute_easy_deck_v28-2_2026-10-15.pptx";
  await pres.writeFile({ fileName: out });
  await applyTheme(out, THEME);
  console.log("wrote", out);
})();
