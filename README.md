# Chrome Root Program

Google Chrome relies on Certification Authority systems ("CAs") to issue certificates to websites. Chrome uses these certificates to help ensure the connections it makes on behalf of its users are properly secured. Chrome accomplishes this by verifying that a website's certificate was issued by a recognized CA, while also performing additional evaluations of the HTTPS connection's security properties. Certificates not issued by a CA recognized by Chrome or a user's local settings can cause users to see warnings and error pages.

When making HTTPS connections, Chrome refers to a list of root certificates from CAs that have demonstrated why continued trust in them is justified. This list is known as a "Root Store." CA certificates included in the [Chrome Root Store](https://g.co/chrome/root-store) are selected on the basis of publicly available and verified information, such as that within the Common CA Database ([CCADB](https://ccadb.org/)), and ongoing reviews by the Chrome Root Program.

In Chrome 105, Chrome began a platform-by-platform transition from relying on the host operating system's Root Store to its own on Windows, macOS, ChromeOS, Linux, and Android. This change makes Chrome more secure and promotes consistent user and developer experiences across platforms. Apple policies prevent the Chrome Root Store and corresponding Chrome Certificate Verifier from being used on Chrome for iOS. Learn more about the Chrome Root Store and Chrome Certificate Verifier [here](https://chromium.googlesource.com/chromium/src/+/main/net/data/ssl/chrome_root_store/faq.md).

The Chrome Root Program Policy establishes the minimum requirements for self-signed root CA certificates to be included as trusted in a default installation of Chrome. This GitHub repository contains a Markdown-formatted version of the authoritative version available [here](https://g.co/chrome/root-policy).

Any questions regarding the Chrome Root Program Policy can be directed to chrome-root-program [at] google [dot] com.

## Updating the Policy

The site is deployed on commits to `main`. To add a new policy revision:

- Archive the current version in `content/policy-archive/` (create the directory
  and copy it to the proper index.md file).
- Update `config.yaml`:
    - Update `context.versions` array so that the path for the now archived
      version is no longer marked as `current`
    - Add a new entry at the bottom of the array for the next version, with an
      archive path, `path: content/policy-archive/policy-version-NEW-VERSION`.
      The file and folder do not need to exist.
    - Bump `context.current_version` to the next version value. It should match
      the version number in at the end of the versions array. Be sure all version
      numbers are in quotes so they are interpreted as strings, not floats.
- Update `content/index.md` with the new content. This way the PR will show a
  diff of the new policies in index.md.

This can all be done in a single pull request. The diff in the PR will show the diff between the two policy versions.

### A note on links

Links in Markdown to other documents in this repository should end in `md`, e.g.
`[Policy](index.md)`. Links in raw HTML, e.g. `<a
href=/moving-forward-together>` should not. This make the links in the Github UI
work for Markdown, and results in a correctly-compiled site. Hardcoded HTML
links will not resolve correctly in previews.
