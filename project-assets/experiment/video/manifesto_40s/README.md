# Blunt Manifesto 40s

Self-contained HTML/CSS/JS motion artifact for a 40-second Blunt manifesto film.

## Preview

Open:

```sh
open experiment/video/manifesto_40s/index.html
```

Scrub to a timestamp:

```sh
open "experiment/video/manifesto_40s/index.html?t=22"
```

## Render MP4

From the workspace root:

```sh
node experiment/video/manifesto_40s/render.js
```

The render uses local `canvas` from `experiment/video/node_modules` and encodes with `ffmpeg`.
Temporary frames are removed after encoding. Set `KEEP_FRAMES=1` to keep them.

Output:

```text
experiment/video/manifesto_40s/blunt_manifesto_40s.mp4
```
