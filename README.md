# Graph Studio — GitHub APK Builder

This repository wraps the supplied, self-contained Graph Studio HTML app with Capacitor and builds an Android debug APK using GitHub Actions.

## Build the APK on GitHub

1. Create a new **empty** GitHub repository (for example `graph-studio`).
2. Upload the **contents** of this folder to the repository root. The `.github/workflows/build-apk.yml` file must remain inside the `.github/workflows/` folder.
3. Open the repository's **Actions** tab.
4. Select **Build Graph Studio APK**. If it has not run automatically after the upload, click **Run workflow**.
5. Wait for the workflow to finish successfully.
6. Open the completed run and download **Graph-Studio-APK** under **Artifacts**.
7. Extract the downloaded ZIP. The file inside is `app-debug.apk`; transfer it to your Android phone and install it.

## Notes

- The app's HTML is bundled locally in `www/index.html`; it does not need a website or hosting server to launch.
- The supplied square image is used as the Android launcher icon.
- The workflow creates a **debug APK** suitable for personal testing and installation. A Play Store release requires a separately signed release build.
- Every push to `main` starts a new APK build. You can also start one manually from Actions.
