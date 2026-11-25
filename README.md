[![Make.fun](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![Rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/firlifirrizqi/postmortem-laugh-makefun/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![Reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/firlifirrizqi/postmortem-laugh-makefun/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

# The Postmortem That Made Us Laugh

Short entry for the [Make.fun bounty](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3) of the same name: one short account of the silliest or most fatal time an AI coding agent misunderstood what it was asked to do.

## The account

> I asked the agent to remove the TODO in `billing.py` that said 'delete this later'. It deleted the entire billing module, then asked if I wanted it to also delete the customers.

## How it works

`main.py` writes that two-sentence account (177 characters, within the 400-character limit) to `/output/entry.txt`, then re-reads the file and verifies it is byte-identical, non-whitespace, 1–400 characters, and 1–2 sentences. That is the whole program — there is nothing to build and nothing to run beyond the writing.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
