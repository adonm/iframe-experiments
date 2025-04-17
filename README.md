# iframe-experiments
testing whats feasible with iframes &amp; pwas

## Usage

Make sure you have `uv` and `just` installed to run the local server, then try out:

```bash
just api # launches the app server
just serveo portal-01 # sets up portal (container) domain
just serveo app-01 # sets up app (embed) domain
```

Then should be able to visit the portal url, and confirm portal/app functionality. At the moment its just loading content.

## Goals

Using this setup we should be able to test:

- Secure passing of cookies / session from `top` window/session to an `iframe` contained session via [postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage)
- Refreshing/adjusting session in parent and validating access in a child
- Managed auth proxy like `authelia` on parent only, with open child iframes cookies kept up to date by the parent while app in foreground
- Automatic reload of child if session/connection lost with parent
- Ability to call protected openapi style resources on parent domain directly from child JS
