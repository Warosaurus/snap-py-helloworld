# snap-py-helloworld
Test project to learn how to make snaps. Read more about snap development [here](https://snapcraft.io/docs/getting-started).

This project creates a simple snap that when executed outputs `Hello World!`
in the terminal.

To create the snap:
  * Ensure the dependencies are met
  * Clone this repo
  * Run `snapcraft` in the project root directory to build the snap
  * Run `sudo snap install --devmode --dangerous *.snap` to install the snap locally
  * Run `test-helloworld` to run the snap once installed

## Dependencies
  * Snapd
  * Snapcraft
  * Multipass for building
