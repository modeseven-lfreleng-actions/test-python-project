<!--
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 The Linux Foundation
-->

# Sample Mypy Pre-Commit Configuration File

Some linting tools are not able to run under [pre-commit.ci][pre-commit.ci]
because of resource limitations. When this occurs, remove those linting tools
from the main pre-commit configuration and run them under a standalone
action/workflow that invokes pre-commit on GitHub pull requests.

The action/workflow links below are suitable for this purpose:

- [lfreleng-actions/standalone-linting-action][action]
- [lfit/releng-reusable-workflows: reuse-standalone-linting.yaml][workflow]

This directory contains a template .pre-commit-config.yaml to run mypy, one
of the linting tools that can experience this limitation.

<!-- markdownlint-disable MD013 -->

[pre-commit.ci]: https://pre-commit.ci/
[action]: https://github.com/lfreleng-actions/standalone-linting-action/
[workflow]: https://github.com/lfit/releng-reusable-workflows/blob/main/.github/workflows/reuse-standalone-linting.yaml
