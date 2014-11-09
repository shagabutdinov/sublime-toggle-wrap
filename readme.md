# Sublime ToggleWrap plugin

Toggles wrap type between (), {}, [] and quotes "", ''. Also provides way to
remove wrap.


### Demo

![Demo](https://github.com/shagabutdinov/sublime-enhanced-demos/raw/master/toggle_wrap.gif "Demo")


### Installation

This plugin is part of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
plugin set. You can install sublime-enhanced and this plugin will be installed
automatically.

If you would like to install this package separately check "Installing packages
separately" section of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
package.


### Features

- Change between brackets type (), {}, [] or between quotes "", ''.

- Remove brackets or quotes.


### Usage


##### By selection:

1. Select a brackets or quotes

2. Hit bracket or quote shortcut to change wrap type

3. Hit delete forward to remove wrap


##### Delete wrap

1. Set cursor before opening or after closing bracket or quote

2. Hit delete subword forward or subword backward accordingly to remove wrap


### Commands

| Description              | Keyboard shortcut | Command palette                      |
|------------------------- |-------------------|------------------------------------- |
| Remove wrap              | alt+/             | ToggleWrap: Remove wrap              |
| Clean brackets forward   | ctrl+/            | ToggleWrap: Clean brackets forward   |
| Clean quotes forward     | ctrl+/            | ToggleWrap: Clean quotes forward     |
| Clean brackets backward  | ctrl+backspace    | ToggleWrap: Clean brackets backward  |
| Clean quotes backward    | ctrl+backspace    | ToggleWrap: Clean quotes backward    |
| Change to ''             | '                 | ToggleWrap: Change to ''             |
| Change to ""             | "                 | ToggleWrap: Change to ""             |
| Change to ``             | `                 | ToggleWrap: Change to ``             |
| Change to preceding :    | :                 | ToggleWrap: Change to preceding :    |
| Change to following :    | ;                 | ToggleWrap: Change to following :    |
| Change to ()             | (                 | ToggleWrap: Change to ()             |
| Change to {}             | {                 | ToggleWrap: Change to {}             |
| Change to []             | [                 | ToggleWrap: Change to []             |


### Dependencies

None