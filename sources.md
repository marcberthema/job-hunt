# Job Sources

Defines where `/findjobs` looks for postings. Single source of truth for the command.

---

## Primary Source — Gmail

- **Mechanism:** Gmail API (OAuth, headless)
- **Label:** `job-alerts`
- **Credentials:** `credentials.json` (gitignored, place in repo root)
- **Token:** `token.json` (gitignored, generated on first OAuth run)
- **Behavior:** fetch all unread emails in `job-alerts`, parse each one, mark as read after processing

See `todo.md` section 4 for one-time Gmail API setup steps.

---

## Platforms Sending to This Inbox

| Platform | Type | Alert configured |
|----------|------|-----------------|
| Toptal | Contract / vetted network | ☐ |
| Gun.io | Contract / tech | ☐ |
| Expert360 | Fractional / advisory | ☐ |
| Contra | Independent / fractional | ☐ |
| Upwork | Contract (high volume) | ☐ |
| LinkedIn | Mixed — filter "Contract" only | ☐ |
| We Work Remotely | Remote contract | ☐ |
| Wellfound | Contract / startup | ☐ |

Check the box once the platform is configured to send alerts to the job email address.
