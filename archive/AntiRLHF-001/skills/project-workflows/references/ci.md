# CI workflow

Read the repository's manifest, package manager, lockfiles, local test/build commands, and current CI. Derive jobs from required behaviors and valid platform targets. Reuse existing scripts; do not add a universal lint/test/build matrix as ceremony.

Match event triggers and path filters to the files and generated outputs that affect each check. Match permissions and secret exposure to the exact event trust boundary, especially untrusted external contributions. Separate build artifacts from deployment when permissions or life cycles differ.

Test the underlying commands and working directory, validate the workflow with the platform's supported tooling, and inspect an actual run when authorization and environment permit. A configuration-only task ends with the updated workflow and meaningful verification of its paths.
