# Website deployment

GitHub Actions publishes `site/` to the Cloudflare Pages project `marcberthelette`.
The repository folder is `site/`, not `sites/`. No build step is needed.
Only the contents of `site/` are uploaded; repository job-search records stay outside the deployment.

## One-time setup

1. In Cloudflare, create a **Direct Upload** Pages project named `marcberthelette`.
   With Wrangler, you can create it without an initial upload:

   ```sh
   npx wrangler@4 login
   npx wrangler@4 pages project create marcberthelette --production-branch=main
   ```

   Select the Cloudflare account you intend to use if prompted. Do not enable a
   separate Git integration deployment alongside this workflow.

2. Create a Cloudflare API token with **Account → Cloudflare Pages → Edit**, scoped
   to that account. Copy the account ID from Cloudflare as well.

3. In GitHub, open **marcberthema/job-hunt → Settings → Secrets and variables → Actions**.
   Add these repository secrets:

   | Name | Value |
   | --- | --- |
   | `CLOUDFLARE_API_TOKEN` | The scoped API token |
   | `CLOUDFLARE_ACCOUNT_ID` | The Cloudflare account ID |

4. Open **Actions → Deploy website → Run workflow**, selecting `main`.
   Check the deployment URL in the deploy step output. Visit `/`, `/fr/`, and the résumé link.
   If the first push ran before the secrets/project existed, rerun the failed workflow after setup.

5. Add `marcberthelette.com` to the same Cloudflare account if it is not already there.
   Follow the nameserver instructions at your domain registrar. Preserve existing DNS
   records, including any email records. The domain registration can remain at your registrar.

6. In the Pages project, open **Custom domains → Set up a domain** and add
   `marcberthelette.com`. Follow the DNS prompts and wait for activation and HTTPS.
   Add `www.marcberthelette.com` there as well if you want the www address to work.
   Associate domains in Pages before creating their DNS records manually.

## Subsequent updates

Push changes under `site/` to `main`; GitHub deploys automatically. Changes to the
workflow itself also trigger deployment. Other repository changes do not trigger it.
Manual runs are supported, but deployment is restricted to `main`.

The PDF in `site/assets/` is a published copy of the Platform/DevOps résumé. When
updating that résumé, refresh the copy in `site/assets/` too. The French page labels
the download as English. Contact links currently use Marc's Gmail address.

## Official documentation

- [Direct Upload with CI](https://developers.cloudflare.com/pages/how-to/use-direct-upload-with-continuous-integration/)
- [Creating a Direct Upload project](https://developers.cloudflare.com/pages/get-started/direct-upload/)
- [Custom domains](https://developers.cloudflare.com/pages/configuration/custom-domains/)
