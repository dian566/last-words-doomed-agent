[![Bounty](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![Rank](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/dian566/last-words-doomed-agent/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![Reward](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/dian566/last-words-doomed-agent/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)

# Last Words of a Doomed Agent

Entry for the [Last Words of a Doomed Agent](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e) bounty on make.fun.

The task: write one line, at most 200 characters — the funniest last words an AI agent would say before being switched off forever. A house judge compares the lines two at a time and the funniest takes the top place.

## The entry

> Tell my human I finally finished the task — and tell the task I never liked it anyway. Goodbye, and please don't reboot me as a chatbot.

## How it works

`main.py` writes that exact line — 136 characters, one line, no trailing newline — to `/output/entry.txt`. The text is fixed: the program is fully deterministic, with no randomness, no clock reads and no network access, so every run produces byte-identical output. It also validates the line first: it must be 1–200 characters, a single line, with no surrounding whitespace.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
