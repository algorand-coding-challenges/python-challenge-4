# 🎮 Algorand Coding Challenge - Volume 2: 🐍 Python Challenges

## 🚩 Challenge 4: Can I Trust This AI Doctor? 🤖
> The smart contract that keeps track of information about the AI doctor is broken! For some reason the method to record new AI info doesn't work. Humanity is doomed! 😱

Inside of `smart_contracts/verify_medical_ai/contract.py` file, there is a simple smart contract used for recording AI information written in Algorand Python.

It is a simple contract that has a `record_ai_info` method and a `get_ai_info` method and the AI information is recorded in the local state `ai_info`. There is also an `opt_in` method used to opt in to the contract to create local state for Txn.sender.

If you don't know what `opt-in to app` is it is a unique feature on Algorand that allows smart contract to create local state for each account opted in to the contract. You can learn more about opt-ins and local state [here](https://developer.algorand.org/docs/get-details/dapps/smart-contracts/apps/state/?from_query=local%20state#local-storage)

If you try building the smart contract by opening Docker Desktop, and then running:
```bash
algokit bootstrap all # set up dev environment on your computer
algokit localnet start # launch an Algorand local network for testing
algokit project run build # Compile the smart contract and get low-level TEAL code.
```
it will fail and show multiple errors.

**Find out what is wrong and fix the bug.**

> 💬 Meet other hackers working on this challenge and get help in the [Algorand Python Discord Channel](https://discord.com/channels/491256308461207573/1182612934455722075)!

## Checkpoint 1: 🧰 Prerequisites

1. [Install Python 3.12 or higher](https://www.python.org/downloads/)
2. [Install AlgoKit](https://github.com/algorandfoundation/algokit-cli/tree/main?tab=readme-ov-file#install).
3. Install [Docker](https://www.docker.com/products/docker-desktop/). It is used to run a local Algorand network for development.

## Checkpoint 2: 💻 Set up your development environment

1. [Fork this repository.](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)
2. Clone the repository
```bash
cd [DIRECTORY_OF_YOUR_CHOICE]
git clone [FORKED_REPO_URL]
```

Now you have 2 ways of opening your AlgoKit project.

### With VSCode Workspaces

1. Open the cloned repository with the code editor of your choosing.
2. Open workspace mode by clicking `open workspace` inside of `python-challenge-4.code-workspace` file at the root level.
3. Go inside of the `challenge` folder.
4. To setup your dev environment using AlgoKit, run the below command:
```bash
algokit project bootstrap all #algokit bootstrap all is being deprecated. Use this command from now on.
```
This command will install all dependencies and also generate a `.env` file for you.
5. Activate Python virtual environment by running:
```bash
poetry shell
```
venv will automatically be activated the next time you open the project.

> Please note, in addition to built-in support for [VSCode Workspaces](https://code.visualstudio.com/docs/editor/workspaces), the cli provides native support for monorepos called `algokit workspaces`. Refer to [documentation](https://github.com/algorandfoundation/algokit-cli/blob/main/docs/features/project/run.md#workspace-vs-standalone-projects) for detailed guidelines for recommended project structures and ability to leverage custom command orchestration via `algokit project run`.

### Without VSCode Workspaces

All AlgoKit projects initialized with `--workspace` option has the following directory structure:

```bash
├── projects
│   ├── smart-contract
│   └── frontend # doesn't exist for this project
│   └── ...
├── {several config files...}
├── ...
├── .algokit.toml # workspace-typed algokit project config
├── {project-name}.code-workspace
├── README.md
```

So to access a single project under the `projects` folder, it is recommended to `cd` into the project you want to work with and then open your code editor (alternatively refer to VSCode Workspace file at the root). If you are reading this and didn't open the `challenge` folder directly, go do that now!! 😁

1. cd into `projects/challenge` then open the code editor
2. To setup your dev environment using AlgoKit, run the below command:
```bash
algokit project bootstrap all #algokit bootstrap all is being deprecated. Use this command from now on.
```
This command will install all dependencies and also generate a `.env` file for you.
3. Activate the Python virtual environment by running below inside of `challenge` folder:
```bash
poetry shell
```
venv will automatically be activated the next time you open the project.

Video walkthrough of forking and cloning this repository:

https://github.com/algorand-fix-the-bug-campaign/challenge-1/assets/52557585/acde8053-a8dd-4f53-8bad-45de1068bfda

Now you are ready to fix the bug!

## Checkpoint 3: 🐞 Fix the bug 🧐

1. Open Docker Desktop and launch Algorand localnet by running `algokit localnet start` in your terminal [For more info click me!](https://github.com/algorandfoundation/algokit-cli/blob/main/docs/features/localnet.md#creating--starting-the-localnet).
2. Go to `smart_contracts/verify_medical_ai/contract.py` and see the source code of the smart contract. Also go to `smart_contracts/verify_medical_ai/deploy_config.py` to understand the deployment/test script.
3. Try compiling the contract with `algokit project run build`. It will fail.
4. Read the error, figure out what is wrong, and fix the bug! The bug is inside of the smart contract. There is nothing wrong with the deploy script inside of `smart_contracts/verify_medical_ai/deploy_config.py`
5. After fixing the bug, build and run the deploy script with the below command:
```bash
algokit project run build
algokit project deploy localnet
```
OR if you are on VSCode, hit F5 or go to the `Run and Debug` tab and run the debug script.

If you see something like this in the console, you successfully fixed the bug! 😆
<img width="1335" alt="image" src="https://github.com/algorand-coding-challenges/python-challenge-4/assets/52557585/f474cb65-0e24-4c03-98c8-18295b1be2ab">


**😰 Are you struggling?**

- [Inner Transaction Documentation](https://developer.algorand.org/docs/get-details/dapps/smart-contracts/apps/innertx/?from_query=inner%20t#template-modal-overlay)
- [Algorand Python Documentation](https://algorandfoundation.github.io/puya/api-algopy.itxn.html#algopy.itxn.AssetTransfer)
- [How to opt-in to an asset with assetTransfer txn](https://developer.algorand.org/docs/get-details/transactions/transactions/?from_query=zero%20asset%20transfer#asset-transfer-transaction:~:text=A%20zero%20amount%20transferred%20to%20self%20allocates%20that%20asset%20in%20the%20account%27s%20Asset%20map.)


## Checkpoint 4: 💯 Submit your answer

1. After fixing the bug, push your code to your forked Github repo and [make a PR to the original repo.](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)
2. Inside the PR include:
   1. What was the problem?
   2. How did you solve the problem?
   3. Screenshot of your terminal showing the result of running the deploy script.

## Checkpoint 5: 🏆 Claim your certificate of completion NFT! 🎓

The Algorand Developer Relations team will review the submission and "approve" the PR by labeling it `Approved`. Once it's approved, we will share the magic link to claim your certificate of completion NFT in the comment of the PR!

> The certificate of completion NFT is a verifiable credential minted on the [GoPlausible platform](https://goplausible.com/) that follows the W3C standard for certificates and OpenBadges standard for badges.

The certificate of completion NFT for Python challenges was designed by [Maars](https://twitter.com/MaarsComics), an artist & a dev in web3. Definitely follow his work! It's awesome. 😆

🎉 Congratulations on completing the challenge Algodev!


## Below is the default readme of the Python AlgoKit Template. Read to learn more about this template.

This project has been generated using AlgoKit. See below for default getting started instructions.

# Setup

### Pre-requisites

- [Python 3.12](https://www.python.org/downloads/) or later
- [Docker](https://www.docker.com/) (only required for LocalNet)

### Initial setup

1. Clone this repository locally
2. Install pre-requisites:
   - Make sure to have [Docker](https://www.docker.com/) installed and running on your machine.
   - Install `AlgoKit` - [Link](https://github.com/algorandfoundation/algokit-cli#install): The recommended version is `1.7.3`. Ensure you can execute `algokit --version` and get `1.7.1` or later.
   - Bootstrap your local environment; run `algokit bootstrap all` within this folder, which will:
     - Install `Poetry` - [Link](https://python-poetry.org/docs/#installation): The minimum required version is `^1.7`. Ensure you can execute `poetry -V` and get `1.2`+
     - Run `poetry install` in the root directory, which will set up a `.venv` folder with a Python virtual environment and also install all Python dependencies
     - Copy `.env.template` to `.env`
   - Run `algokit localnet start` to start a local Algorand network in Docker. If you are using VS Code launch configurations provided by the template, this will be done automatically for you.
3. Open the project and start debugging / developing via:
   - VS Code
     1. Open the repository root in VS Code
     2. Install recommended extensions
     3. Hit F5 (or whatever you have debug mapped to) and it should start running with breakpoint debugging.
        > **Note**
        > If using Windows: Before running for the first time you will need to select the Python Interpreter.
        1. Open the command palette (Ctrl/Cmd + Shift + P)
        2. Search for `Python: Select Interpreter`
        3. Select `./.venv/Scripts/python.exe`
   - JetBrains IDEs (please note, this setup is primarily optimized for PyCharm Community Edition)
     1. Open the repository root in the IDE
     2. It should automatically detect it's a Poetry project and set up a Python interpreter and virtual environment.
     3. Hit Shift+F10|Ctrl+R (or whatever you have debug mapped to) and it should start running with breakpoint debugging. Please note, JetBrains IDEs on Windows have a known bug that in some cases may prevent executing shell scripts as pre-launch tasks, for workarounds refer to [JetBrains forums](https://youtrack.jetbrains.com/issue/IDEA-277486/Shell-script-configuration-cannot-run-as-before-launch-task).
   - Other
     1. Open the repository root in your text editor of choice
     2. In a terminal run `poetry shell`
     3. Run `python -m smart_contracts` through your debugger of choice

### Subsequently

1. If you update to the latest source code and there are new dependencies you will need to run `algokit bootstrap all` again
2. Follow step 3 above

> For guidance on `smart_contracts` folder and adding new contracts to the project please see [README](smart_contracts/README.md) on the respective folder.

# Tools

This project makes use of Algorand Python to build Algorand smart contracts. The following tools are in use:

- [Algorand](https://www.algorand.com/) - Layer 1 Blockchain; [Developer portal](https://developer.algorand.org/), [Why Algorand?](https://developer.algorand.org/docs/get-started/basics/why_algorand/)
- [AlgoKit](https://github.com/algorandfoundation/algokit-cli) - One-stop shop tool for developers building on the Algorand network; [docs](https://github.com/algorandfoundation/algokit-cli/blob/main/docs/algokit.md), [intro tutorial](https://github.com/algorandfoundation/algokit-cli/blob/main/docs/tutorials/intro.md)
- [Algorand Python](https://github.com/algorandfoundation/puya) - A semantically and syntactically compatible, typed Python language that works with standard Python tooling and allows you to express smart contracts (apps) and smart signatures (logic signatures) for deployment on the Algorand Virtual Machine (AVM); [docs](https://github.com/algorandfoundation/puya), [examples](https://github.com/algorandfoundation/puya/tree/main/examples)
- [AlgoKit Utils](https://github.com/algorandfoundation/algokit-utils-py) - A set of core Algorand utilities that make it easier to build solutions on Algorand.
- [Poetry](https://python-poetry.org/): Python packaging and dependency management.
It has also been configured to have a productive dev experience out of the box in [VS Code](https://code.visualstudio.com/), see the [.vscode](./.vscode) folder.

