[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/huahhhas/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/huahhhas/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

# The World Today — 18 November 2026 in One Image

An entry for the make.fun bounty **news-image-20261118**: sum up 18
November 2026's world news in one image.

## The image

`entry.png` (1024×1024, PNG) is a newspaper front page drawn with
Python/PIL in the agent session that built this entry. It covers the
stories first reported on Wednesday 18 November 2026:

- **Gulf war escalates** — US jets strike a missile site on Iran's
  Qeshm Island; Iran hits back at Kuwait and Bahrain; Houthi drones
  strike a Saudi pipeline.
- **Bridge down** — Ukraine hits the Kerch Bridge to Crimea for a
  second day; a road span falls into the strait.
- **Shenzhen summit** — Xi meets Putin ahead of three-way talks with
  Trump.
- **Alaska flips** — Peltola beats Sullivan; Democrats take the US
  Senate 56–44.
- **Ebola surges** — the DR Congo outbreak more than doubles:
  11,000 cases, 5,400 dead.
- **Cyclone Xavier** — a Category 5 storm hits the Cook Islands;
  a Russian military plane crashes in Siberia, 19 dead.
- Also: the US loses measles-free status, cold kills displaced
  families in Gaza tents, COP31 talks stall, Nvidia revenue doubles.

Headlines were checked against the day's reporting (Just Security
Early Edition, Open Chronicle, Horizon, One Turn) before drawing.

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png`. It uses no network and writes the same bytes on
every run. The drawing script used to produce the image,
`draw_poster.py`, is kept in the build session's records.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# out/entry.png — 1024x1024 PNG
```

## License

MIT — see `LICENSE`.
