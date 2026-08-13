# Google Chrome Root Programs

Google Chrome relies on Certification Authority systems ("CAs") to issue certificates to websites. Chrome uses these certificates to help ensure the connections it makes on behalf of its users are properly secured. Chrome accomplishes this by verifying that a website's certificate was issued by a recognized CA, while also performing additional evaluations of the HTTPS connection's security properties. Certificates not issued by a CA recognized by Chrome or a user's local settings can cause users to see warnings and error pages.

To secure the web today and prepare for the post-quantum future, Chrome operates two distinct root programs:

* **[The Chrome Root Program](content/crp/policy.md)**: [Launched in 2022](https://blog.chromium.org/2022/09/announcing-launch-of-chrome-root-program.html), this program establishes the minimum requirements for self-signed root CA certificates to be included in the [Chrome Root Store](https://g.co/chrome/root-store) by default, providing consistent and reliable security for HTTPS connections across platforms. The authoritative policy is available at [https://g.co/chrome/root-policy](https://g.co/chrome/root-policy).
* **[The Chrome Quantum-resistant Root Program](content/cqrp/draft-policy.md)**: Designed for the post-quantum era, this program uses Merkle Tree Certificates (MTCs) to deliver quantum-safe security without slowing down page connections. Learn more about Google's planned adoption of MTCs on the [Google Security Blog](https://blog.google/security/cultivating-a-robust-and-efficient-quantum-safe-https/).

Any questions regarding the Chrome Root Program can be directed to `chrome-root-program [at] google [dot] com`.

Any questions regarding the Chrome Quantum-Resistant Root Program can be directed to `chrome-quantum-resistant-root-program [at] google [dot] com`.

## Updating the CRP Policy

The site is deployed automatically on commits to `main`. To add a new Chrome Root Program policy revision:

- Archive the current version in `content/policy-archive/` (create the directory and copy the current policy to the proper version file).
- Update `config.yaml`:
    - Update `context.versions` array so that the path for the now archived version is no longer marked as `current`.
    - Add a new entry at the bottom of the array for the next version, with an archive path, `path: content/policy-archive/policy-version-NEW-VERSION`.
    - Bump `context.current_version` to the next version value. It should match the version number at the end of the versions array. Be sure all version numbers are in quotes so they are interpreted as strings, not floats.
- Update `content/crp/policy.md` with the new policy content.

This can all be done in a single pull request. The diff in the PR will show the diff between the two policy versions.

### A note on links

Links in Markdown to other documents in this repository should end in `.md`, e.g. `[Policy](content/crp/policy.md)`. Links in raw HTML, e.g. `<a href="{{ '/crp/moving-forward-together' | absolute_url }}">` should not. This makes the links in the GitHub UI work for Markdown while also resulting in a correctly compiled static site. Hardcoded HTML links will not resolve correctly in previews.
