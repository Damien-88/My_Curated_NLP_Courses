# Day 1: Character Encodings, Bytes, and UTF-8

### Learning Objective
Understand how raw binary data (bytes) maps to human-readable text characters, how the UTF-8 encoding scheme variable-length maps code points, and how processing mismatches create data corruption (mojibake).


## Core Concepts

### 1. The Distinction Between Characters, Code Points, and Bytes
To process text deterministically, computers separate a semantic symbol from its underlying memory representation:
* **Character**: An abstract unit of text (e.g., the letter `A` or the emoji `🐍`).
* **Code Point**: A unique integer assigned to a character by the Unicode standard. Written in hexadecimal notation prefixed by `U+` (e.g., `A` is `U+0041`).
* **Bytes**: The actual binary data stored on a disk or transmitted over a network. How a code point maps to bytes depends entirely on the **Encoding Scheme** used.

### 2. Fixed-Length vs. Variable-Length Encoding
* **ASCII**: A 7-bit fixed-length encoding mapping 128 characters. It cannot represent non-English text.
* **UTF-32**: A 32-bit (4-byte) fixed-length encoding. Every character takes exactly 4 bytes. While easy to index in memory, it is highly inefficient for storage since most English text is padded with leading zeros.
* **UTF-8**: A variable-length encoding that uses between 1 and 4 bytes per code point. It is backward-compatible with ASCII.

### 3. The UTF-8 Binary Architecture
UTF-8 determines how many bytes a character uses by reading marker bits at the start of the first byte:

```text
|   Number of Bytes  |  Code Point Range (Hex) | Byte 1 Structure | Byte 2 Structure | Byte 3 Structure | Byte 4 Structure |
| :----------------- | :---------------------- | :--------------- | :--------------- | :--------------- | :--------------- |
| **1 Byte** (ASCII) |  `U+0000` to `U+007F`   |    `0xxxxxxx`    |        N/A       |        N/A       |        N/A       |
|    **2 Bytes**     |  `U+0080` to `U+07FF`   |    `110xxxxx`    |    `10xxxxxx`    |        N/A       |        N/A       |
|    **3 Bytes**     |  `U+0800` to `U+FFFF`   |    `1110xxxx`    |    `10xxxxxx`    |    `10xxxxxx`    |        N/A       |
|    **4 Bytes**     | `U+10000` to `U+10FFFF` |    `11110xxx`    |    `10xxxxxx`    |    `10xxxxxx`    |    `10xxxxxx`    |
```

> **Rule**: For multi-byte characters, the number of leading `1` bits in Byte 1 tells the system how many total bytes long the character is. Every subsequent continuation byte must begin with the bits `10`.


## Why This Matters in NLP Pipelines
If a file is written using one encoding (e.g., `Windows-1252`) and read using another (e.g., `UTF-8`), bytes are misaligned. This produces **Mojibake** (corrupted symbols like `æ¾³é—¨`) or throws a terminal `UnicodeDecodeError`, crashing down-stream text preprocessing models.