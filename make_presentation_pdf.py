from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import mm

output_path = "c:/Users/user/OneDrive/Desktop/SKILLHATCH/SkillHatch_Presentation.pdf"

# Combined content: the two assistant responses (project explanation + key snippets/tests/demo)
content = '''
Quick preface
Below is a presentation-ready explanation of your project, organized so you can copy/paste slides or use it as talking points during a demo. It describes what each file does, why things were implemented the way they were, key interactive behaviors, test steps, and suggested next work. After the explanation you'll find a short demo script and recommended screenshots.

Elevator pitch (one-liner)
SkillHatch — a small, static course marketplace/learning portal built with static HTML, Tailwind CSS utilities and a bit of vanilla JS for UI behaviors (sidebar/menu, course cards, banner, back navigation, sign-up form validation). It’s optimized for fast prototyping: no build step, cross-file shared layout patterns, and a simple UX for learners.

Tech stack & conventions
- Plain HTML files (static, no server-side code in repository).
- Tailwind CSS via CDN for styling (utility-first classes).
- Vanilla JavaScript included inline at the bottom of pages for small behaviors.
- File layout: each page is a separate HTML file (index.html, explore courses.html, course detail.html, my courses.html, continue.html, signup.html, login.html, dashboard student.html, profile.html, assessment.html).
- Design tokens used directly in classes (brand color #00418B, blue variants, white/opacity/backdrop-blur).
- Layout pattern recurring across pages: a left sidebar (hidden on small screens) + main content area using a wrapper: <div class="flex ..."> with <aside id="sidebar"> and <main class="flex-1 ...">.

High-level UI patterns (what to point out in a demo)
- Sidebar + Main layout: Responsive sidebar hidden on mobile, visible on larger screens. Uses Tailwind utility classes for width, background color, and sticky behavior.
- Course cards: Grid layout (3 columns at md+) with card components using a flex-column pattern to align CTAs (call-to-action buttons) across different cards.
- Banner (course detail): Large responsive hero image using object-cover; full width to edge-to-edge on main.
- Back button: Small, accessible control in `course detail.html` using `onclick="window.history.back()"` as fallback navigation.
- Sign-up flow: `signup.html` -> `continue.html` collects details; `continue.html` has client-side features:
  - Password show/hide.
  - A Terms checkbox that must be checked (client-side) before Sign Up can proceed (in prior edits we enforced it).
- Mobile menu: small JS toggles to show/hide the sidebar on small screens.

File-by-file walkthrough (what to present & why)
index.html — Landing / marketing
Purpose: Public homepage with hero, features, featured courses, and footer.
Key points:
- Uses responsive grid for feature blocks and featured course cards.
- Cards here are "marketing" variants — smaller, centered, and intended for conversion.
- Contains a mobile menu area toggled by JS (simple, lightweight).

Presentation tip: Show the hero and featured courses; highlight how the same card concept is reused in course listing pages.

explore courses.html — Course marketplace / catalog
Purpose: Main catalog of courses a learner can browse.
Key code & patterns:
- Grid layout: `grid grid-cols-1 md:grid-cols-3 lg:grid-cols-3 gap-8`.
- Each card uses `w-full leading-relaxed flex flex-col h-full min-h-[420px]` with:
  - Image (fixed height): `img class="w-full h-48 object-cover rounded"`.
  - `div.flex-1` for title/description to push CTA to bottom.
  - CTA block at bottom (`div.mt-4`) for consistent alignment across cards.
- Interaction: clicking View Details or Click to Continue navigates to `course detail.html`.

Why this matters:
- The flex-column + `flex-1` pattern ensures the CTAs align horizontally across rows even when descriptions vary. This is a small but important UX polish that improves perceived polish in listing pages.

Demo tip: Show two cards with different description lengths to demonstrate aligned CTAs.

my courses.html — Learner’s enrolled courses (you asked me to update this)
Purpose: Display courses the user is enrolled in with progress info and CTAs.
What I changed (and why):
- Converted all course cards to the same `flex flex-col h-full min-h-[420px]` pattern as in `explore courses.html`.
- Wrapped main text in `flex-1` and moved the CTA to a bottom block (`<a ...>` styled as a button). This aligns CTAs across cards for a neater look.

Talk point: This demonstrates consistency across the site and how reuse of a simple layout pattern yields much neater UIs.

course detail.html — Course landing / lesson list
Purpose: Show hero/banner, course title, instructor, overview, and lesson list.
Key code & UX:
- Sidebar is `sticky top-0 h-screen` so it extends the full viewport height and the main content scrolls independently.
- Banner image: `class="w-full h-56 sm:h-72 md:h-96 object-cover opacity-80"` — responsive heights and opacity to blend with page.
- Back button: placed absolutely in the top-left of the main container:
  - `onclick="window.history.back()"`, a compact monochrome arrow SVG + "Back" label.
  - Uses a semi-transparent background (`bg-black/30`) + `backdrop-blur-sm` to blend with the banner while staying readable and clickable.
- Lesson cards list: standardized markup using Tailwind utilities (spacing, icons, titles, metadata).

Accessibility notes:
- Back button has aria-label; ensure further ARIA on dynamic controls as needed.

Demo tip: Click the back button to show it uses browser history (works even if you navigated directly; fallback is the same page).

signup.html -> continue.html -> login.html (Auth & Sign-up flow)
Purpose: Basic onboarding and auth pages; mostly static front-end forms.
Key code/behaviors:
- `signup.html` collects minimal info and leads to `continue.html` for full sign-up.
- `continue.html` has:
  - Password show/hide: JS toggles input type between password/text and toggles icons.
  - Terms checkbox: controlling whether the Sign Up button is enabled (client-side enforcement).
  - Sign Up button currently navigates to `dashboard student.html` in the static flow; in a real app this would be a server request.
- `login.html` contains a simple form with CTA leading to the dashboard (placeholder). Also supports "Sign in with Google" visual button.

Presentation point:
- Clarify that this is a static prototype; the forms are wired for client-side UI only and need backend endpoints for real authentication and server-side validation.

dashboard student.html, profile.html, assessment.html
Purpose: Internal user area (dashboard, profile, results).
Highlights:
- Consistent sidebar and header UI pattern.
- Dashboard uses card summaries (counts, progress, hours).
- Profile page uses user card and statistics; these pages are mostly layout and visuals for a full product mock.

Key JS behaviors and where they live
- Sidebar toggle (small-screen): toggles `hidden` class on `#sidebar`. Found in multiple pages (`explore`, `my courses`, `dashboard`).
- Course toggle (Explore / My courses): a small switch to visually mark which tab is active; in `my courses.html` clicking Explore navigates to `explore courses.html`.
- Password visibility (continue.html): toggles `input.type` and icon visibility.
- Terms enforcement (continue.html): JS enables/disables Sign Up; we added an ID for checkbox and `signupBtn` and wired enable/disable logic.
- Back button (course detail.html): `onclick="window.history.back()"`.

Why highlight these in a presentation:
- They demonstrate how small, targeted JavaScript makes the prototypes feel interactive without a full SPA or backend.
- Each is easy to replace with server-driven behavior later.

Important design/implementation choices (talking points)
- Utility-first styling (Tailwind) speeds iteration — show the class-based HTML snippets to explain.
- Reuse of sidebar/CTA/button styling across pages improves visual coherence.
- Flex-column cards + `flex-1` solves CTA alignment across cards with variable content (a common product detail).
- Using relative/absolute positioning for the back button keeps it visually placed over the banner while remaining accessible.

Contract & acceptance criteria (2–3 bullets you can use on a slide)
- Inputs: user navigates pages, submits forms (signup/login), toggles menu and password visibility, checks Terms.
- Outputs: navigation to index/explore/course-detail/dashboard pages; CTA buttons trigger navigation; client-side validation for form control states.
- Error modes: No server-side validation — missing fields or invalid formats will not be verified beyond simple HTML input types. Terms check is only client-side.

Edge cases & how the code handles them
- Small screens: sidebar is hidden and toggled with a menu button.
- Long descriptions: card `flex-1` ensures CTA stays at the bottom; still, extremely long text may grow cards past intended heights — consider truncation for very long descriptions.
- Back button: uses browser history; if a user opens `course detail.html` directly (no history), back will generally go back in the browser (could leave the site). For robust UX, consider a fallback: if history length is small, redirect to a sensible page (e.g., `explore courses.html`).
- Terms enforcement: currently client-side only — must add server-side enforcement before real signup.

How to run and verify locally
No build system is required — pages are static. To view:
- Option A — double-click:
  - In File Explorer, double-click any .html file (e.g., `explore courses.html`) to open it in your default browser.
- Option B — run a simple local server (recommended for some image paths and relative navigation):
  - In PowerShell (project root), run:
    python -m http.server 8000
    then open http://localhost:8000/explore%20courses.html
- Option C — use VS Code Live Server extension (right-click > Open with Live Server).

Manual verification checklist:
- Sidebar toggle: shrink window <640px and click menu button; open/close sidebar.
- Course cards: on `explore courses.html` and `my courses.html`, ensure CTA buttons align horizontally across rows.
- Course detail:
  - Back button visible and clickable.
  - Banner stretches edge to edge and scales at different breakpoints.
- Signup flow:
  - On `continue.html`, try toggling password visibility.
  - Try clicking Sign Up with Terms unchecked — it should be disabled or show an error (if enforcement was added).
- Links: check navigation: Explore -> Course detail -> Back; Sign up flow -> Dashboard.

Edge-case tests (optional)
- Open `course detail.html` in a new tab (no prior history): the back button will either go back to a previous cross-site page or remain (explain fallback).
- Very long description in card: verify how cards expand and whether min-height is adequate.

Presentation notes & demo script (speaker-ready)
Short demo script (3–5 minutes live demo)
1. Start with one-liner: "SkillHatch — static Tailwind prototype for a small course marketplace with accessible patterns and consistent UI components."
2. Show the homepage / `explore courses.html`:
   - Point out sidebar and its responsive hide/show behavior.
   - Emphasize card uniformity (open inspector or show two cards with different length text).
3. Click a course -> `course detail.html`:
   - Show the banner, explain use of `object-cover` and responsive heights.
   - Click the "Back" button to show browser history navigation.
4. Show `my courses.html`:
   - Explain that cards use the same pattern and now all CTAs are aligned.
5. Demo `continue.html`:
   - Toggle password visibility, show Terms checkbox and Sign Up being disabled until checked.
6. Close with next steps slide (server-side auth, accessibility, componentization).

Speaker bullets (one-liners to use while demoing)
- "No build step — pages are static and fast to iterate using Tailwind CDN."
- "Consistent sidebar pattern across pages simplifies navigation & reduces cognitive load."
- "Card layout uses flex + flex-1 to align action buttons — a subtle UX improvement."
- "Form interactions use small JS hooks to improve UX; backend integration remains for production."

Suggested screenshots (which slides to include)
- Homepage (hero + featured courses).
- `explore courses.html` grid with CTAs aligned.
- `course detail.html` banner + back button overlay.
- `continue.html` password toggle + terms checkbox (two images showing disabled/enabled Sign Up).
- `my courses.html` showing alignment consistency.

Next steps & prioritized improvements (what to do after the demo)
1. Server integration (High)
   - Implement backend for signup/login (Node/Express, Flask, or Firebase Auth) and server-side Terms verification.
   - Replace anchor-navigations on form submit with proper POST requests.
2. Accessibility (High)
   - Add ARIA attributes where appropriate; ensure error messages use aria-describedby.
   - Ensure keyboard-only flow properly focuses modals/menu.
3. Pixel-perfect card alignment (Medium)
   - Convert card layout to CSS Grid with explicit rows (image / content / CTA). This guarantees exact CTA alignment regardless of content wrapping.
4. Componentize (Medium)
   - Move repeated markup into templates or build partials (e.g., if moving to a simple static site generator or small frontend framework).
5. Tests & CI (Low)
   - Add a small HTML linter / CI step; optionally add visual regression tests if you plan to iterate frequently.
6. UX polish (Low)
   - Add fallback for Back button when history length is insufficient (redirect to `explore courses.html`).
   - Consider making `min-h` responsive (smaller on mobile).

Final notes & quick checklist before presenting
- Open the pages locally and take screenshots at desktop widths.
- Validate the main flows once: catalog → course → back; signup form (terms) behavior.
- If you want I can:
  - Convert the card layout to a CSS grid variant for strict pixel-perfect alignment.
  - Add a fallback for Back (redirect to explore) in `course detail.html`.
  - Replace anchors-with-buttons inside nested anchors (I already removed a nested anchor in `my courses.html`) and double-check semantic correctness.


Key code snippets — explanation & talking points

1) Sidebar + Main layout (shared across pages)
- Typical markup pattern:
  - <div class="flex h-screen">
    <aside id="sidebar" class="hidden sm:flex w-64 bg-[#00418B] text-white flex flex-col justify-between">...</aside>
    <main class="flex-1 overflow-y-auto p-6">...</main>
    </div>
- Why this works:
  - The outer `flex` makes two columns: fixed-width sidebar and flexible main.
  - `w-64` fixes sidebar width; `flex-1` on main ensures it takes remaining horizontal space.
  - `hidden sm:flex` hides sidebar on small screens and shows on sm+ screens.
  - `overflow-y-auto` on main provides independent scrolling of content while keeping sidebar fixed.
- Demo talking points:
  - Explain responsive behavior (sidebar toggled with a menu button); show small-screen behavior.

2) Sticky, full-height sidebar
- Key classes: `sticky top-0 h-screen` used in `course detail.html` for sidebar.
- Purpose:
  - `sticky top-0` pins the sidebar at the top while the main scrolls.
  - `h-screen` ensures the sidebar visually spans the full viewport height.
- Talking point:
  - Useful for course navigation/quick access — improves UX for long content pages.

3) Course card pattern (flex-column + CTA alignment)
- Before/after pattern used in `explore courses.html` and `my courses.html`:
  - Card wrapper: `class="w-full leading-relaxed flex flex-col h-full min-h-[420px]"`
  - Image: `class="w-full h-48 object-cover rounded"`
  - Content area: `div class="flex-1"` — grows to fill vertical space
  - CTA: `div class="mt-4"><a class="block w-full text-center py-2 bg-[#00418B] text-white rounded-lg">View Details</a></div>`
- Why this is important:
  - `flex-1` ensures the middle portion expands so the CTA sits at the bottom for every card.
  - `min-h-[420px]` gives a baseline card height so cards look consistent.
- Edge case:
  - Extremely long text can still make cards uneven; for strict pixel-perfect alignment across many breakpoints, consider CSS grid rows instead of `min-height`.

4) Banner (course detail) and back button
- Banner markup:
  - `<img src="..." class="w-full h-56 sm:h-72 md:h-96 object-cover opacity-80">`
  - Uses responsive heights so the banner scales across breakpoints.
  - `object-cover` ensures the image fills the area without distortion.
- Back button:
  - Placed inside main with absolute positioning:
    - `<div class="absolute top-4 left-4 z-50"> <button onclick="window.history.back()" ...>...</button></div>`
  - Styling choices:
    - `bg-black/30 backdrop-blur-sm` — semi-transparent background with blur so it blends with the banner.
    - `z-50` ensures it stays above other content.
    - `pointer-events-auto` and the SVG using `pointer-events-none` avoids capturing pointer events on the icon.
- Demo talking point:
  - Explain history-based back navigation with a fallback recommendation (we can add a redirect to `explore courses.html` when history is empty).

5) Terms checkbox and Sign Up enable/disable (continue.html)
- Key idea (previous edits introduced IDs):
  - Checkbox: `<input id="terms" type="checkbox">`
  - Button: `<button id="signupBtn" disabled>Sign Up</button>`
- Sample JS pattern (conceptual):
  - document.addEventListener('DOMContentLoaded', () => {
      const terms = document.getElementById('terms');
      const signupBtn = document.getElementById('signupBtn');
      terms.addEventListener('change', () => signupBtn.disabled = !terms.checked);
    });
- Why it matters:
  - Basic client-side enforcement prevents accidental signups without agreement but must be backed server-side.
- Presentation note:
  - Clarify that client-side validation improves UX but is not a security control.

6) Password show/hide toggle (continue.html)
- Pattern:
  - Password input: `<input id="password" type="password">`
  - Toggle button: `<button id="togglePassword">` which toggles `passwordInput.type` between 'password' and 'text', and swaps icons.
- Talking point:
  - Small but familiar UX pattern; show the code toggling the icon classes and the input type.

7) Mobile menu / sidebar toggle (multiple pages)
- Pattern:
  - Menu button: `button id="menu-toggle"` (visible on small screens with `sm:hidden`).
  - JS toggles the `hidden` class on `#sidebar`.
- Example code:
  - menuBtn.addEventListener('click', () => sidebar.classList.toggle('hidden'));
- Demo talking point:
  - Explain progressive disclosure for navigation — sidebar visible on desktop, hidden on mobile to save space.

Tests & verification steps (manual checklist + quick local server)

How to serve locally (PowerShell)
- Run a simple static server from the project root (recommended):
```powershell
# from C:\Users\user\OneDrive\Desktop\SKILLHATCH
python -m http.server 8000
# then open in browser:
# http://localhost:8000/explore%20courses.html
```
(If you prefer Live Server in VS Code, open the folder and use Live Server extension.)

Manual verification checklist (quick pass — ~5–10 minutes)
1. Layout & navigation
   - Open `explore courses.html`:
     - Expect a 3-column grid at desktop widths.
     - Cards should have CTAs aligned across the row.
   - Shrink width to <640px:
     - Sidebar should hide; menu button should toggle sidebar visibility.
2. Course detail / banner / back
   - Open `course detail.html`:
     - Banner should be full-width and responsive.
     - Back button should be visible over the banner; clicking it should go back (or close enough in demo).
3. Sign-up flow
   - Open `signup.html` → click Continue → `continue.html`:
     - Toggle the password visibility icon — password field should switch between text and password.
     - If Terms checkbox is present and enforced, ensure Sign Up button is disabled until checked.
     - Clicking Sign Up should (in current static flow) navigate to `dashboard student.html`.
4. Card consistency
   - Compare `explore courses.html` and `my courses.html`:
     - Buttons should sit on the same horizontal line across cards despite differing description lengths.
5. Accessibility & keyboard
   - Tab through the page:
     - Menu button, sidebar links, search, CTAs, and forms should be reachable via keyboard.
   - Focus states: visually visible for interactive elements (Tailwind focus styles used).
6. Broken link check
   - Click a few CTAs to ensure relative links point to the correct files (e.g., course detail, dashboard).

Edge-case tests (optional)
- Open `course detail.html` in a new tab (no prior history): the back button will either go back to a previous cross-site page or remain (explain fallback).
- Very long description in card: verify how cards expand and whether min-height is adequate.

Presentation notes & demo script (speaker-ready)

Short demo script (3–5 minutes live demo)
1. Start with one-liner: "SkillHatch — static Tailwind prototype for a small course marketplace with accessible patterns and consistent UI components."
2. Show the homepage / `explore courses.html`:
   - Point out sidebar and its responsive hide/show behavior.
   - Emphasize card uniformity (open inspector or show two cards with different length text).
3. Click a course -> `course detail.html`:
   - Show the banner, explain use of `object-cover` and responsive heights.
   - Click the "Back" button to show browser history navigation.
4. Show `my courses.html`:
   - Explain that cards use the same pattern and now all CTAs are aligned.
5. Demo `continue.html`:
   - Toggle password visibility, show Terms checkbox and Sign Up being disabled until checked.
6. Close with next steps slide (server-side auth, accessibility, componentization).

Speaker bullets (one-liners to use while demoing)
- "No build step — pages are static and fast to iterate using Tailwind CDN."
- "Consistent sidebar pattern across pages simplifies navigation & reduces cognitive load."
- "Card layout uses flex + flex-1 to align action buttons — a subtle UX improvement."
- "Form interactions use small JS hooks to improve UX; backend integration remains for production."

Next steps & prioritized improvements (what to do after the demo)
(Repeated above) ...

End of content.
'''

# Build PDF using ReportLab
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=4))

doc = SimpleDocTemplate(output_path, pagesize=A4,
                        rightMargin=20*mm, leftMargin=20*mm,
                        topMargin=20*mm, bottomMargin=20*mm)

flowables = []

for para in content.split('\n\n'):
    text = para.strip()
    if not text:
        continue
    # Use bold for headings heuristically: lines ending with '—' or short lines
    if len(text) < 80 and text.endswith(':') or text.isupper() or text.startswith('Quick preface'):
        flowables.append(Paragraph('<b>%s</b>' % text.replace('&', '&amp;'), styles['Heading2']))
    else:
        # Replace repeated hyphens or markers and escape &
        safe = text.replace('&', '&amp;').replace('<', '&lt;')
        flowables.append(Paragraph(safe.replace('\n', '<br/>'), styles['BodyText']))
    flowables.append(Spacer(1, 6))

print('Generating PDF to', output_path)
doc.build(flowables)
print('Done')
