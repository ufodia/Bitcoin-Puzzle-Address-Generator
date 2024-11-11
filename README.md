# Bitcoin Puzzle Address Generator

## Introduction

This repository hosts a Python script capable of generating Bitcoin (BTC) address puzzles similar to the intriguing ones created in 2015, enhanced in 2017, and again in 2023. These puzzles involved BTC addresses with balances that increased significantly over the years – a compelling challenge for crypto-enthusiasts and puzzle solvers.

Unlike the original puzzles, which were designed for solving, this script is tailored for creating new puzzles. It generates BTC addresses and their corresponding private keys following a specific pattern, enabling users to craft their own complex and intriguing BTC puzzles.

## Background

The original BTC puzzles featured partially known private keys and required solvers to uncover the missing parts. Typically, a BTC Private Key is a 256-bit integer or a 64-character hexadecimal string. The script uses this principle to create new puzzles with a known pattern in the private keys.

## Puzzle Generation Mechanism

The script generates a series of BTC addresses where each private key is constructed following a pattern:
- The n-th Private Key is composed of (256-n) zeros, a '1', and (n-1) random bits.
- For example:
  - \#1: 000...<255>...0001
  - \#2: 000...<254>...001x
  - \#3: 000...<253>...01xx
  - ...
  - \#n: 000...<256-n>...1xx<n-1>xx

This pattern allows for the creation of a puzzle with a scalable difficulty, where the complexity of finding each subsequent key doubles.

## Script Features

- **Private Key Generation**: Randomly generates Private Keys within a specific range for each address in the puzzle sequence.
- **Percentage Calculation**: Calculates the position of each Private Key within its range, adding another layer to the puzzle.
- **BTC Address Generation**: Derives the corresponding BTC address from each Private Key.

## Usage

To generate a new set of puzzle addresses:
1. Run the `puzzle.py` script.
2. This will produce a file named `bitcoin_puzzle_addresses.txt`, containing a list of BTC addresses, their respective private keys in hexadecimal format, and the key's position percentage in its range.

    ```bash
    python puzzle.py

## Creating Your Puzzle

You can modify the script parameters to create a puzzle of desired difficulty and length. Each generated address can be funded with BTC, creating a real-world puzzle for participants to solve.

## Donate BTC

If you appreciate this project and would like to support it, consider donating Bitcoin to the following address:


**BTC**: `1GZdNtQYa2DN4b3hLekrYErv9c8WLqbBTm`
Your support is greatly appreciated!

## Disclaimer

This tool is provided for educational and entertainment purposes only. It should not be used for storing real funds. The creator of this tool bears no responsibility for any misuse or loss incurred.
