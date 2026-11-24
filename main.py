"""One Line, One Chill — a single sentence of horror (166 chars, under 200).

The scare lands on the twist: the voice on the monitor is the narrator's
own childhood voice, and the intruder already knows the child is listening.
"""

import os

ENTRY = "The baby monitor crackled, and in my own voice — sleepy, small, six years old — something whispered, 'Mummy, the man in your bed isn't Daddy, and he knows I'm awake.'"


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
