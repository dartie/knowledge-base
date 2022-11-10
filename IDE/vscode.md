# VSCODE

## Keymapping

### Locations

* Windows: `%UserProfile%\AppData\Roaming\Code\User\keybindings.json`
* Linux: `~/.config/Code/User/keybindings.json`
* OSX: ``

### Add swap lines shortcut

```json
// Place your key bindings in this file to overwrite the defaults
 [
   {
     "key": "ctrl+shift+up",
     "command": "editor.action.moveLinesUpAction",
     "when": "editorTextFocus"
   },
   {
     "key": "ctrl+shift+down",
     "command": "editor.action.moveLinesDownAction",
     "when": "editorTextFocus"
   }
 ]
```

### My settings

- `editor.action.duplicateSelection` : `CTRL+D`
- `editor.action.deleteLines` : `CTRL+Y`
- `editor.action.joinLines` : `CTRL+SHIFT+J`
- `editor.action.blockComment` : `CTRL+/`

```json
// Place your key bindings in this file to override the defaultsauto[]
[
    {
        "key": "ctrl+d",
        "command": "-editor.action.addSelectionToNextFindMatch",
        "when": "editorFocus"
    },
    {
        "key": "ctrl+d",
        "command": "editor.action.duplicateSelection"
    },
    {
        "key": "ctrl+y",
        "command": "-redo"
    },
    {
        "key": "ctrl+y",
        "command": "editor.action.deleteLines",
        "when": "textInputFocus && !editorReadonly"
    },
    {
        "key": "ctrl+shift+k",
        "command": "-editor.action.deleteLines",
        "when": "textInputFocus && !editorReadonly"
    },
    {
        "key": "ctrl+shift+j",
        "command": "-workbench.action.search.toggleQueryDetails",
        "when": "inSearchEditor || searchViewletFocus"
    },
    {
        "key": "ctrl+shift+j",
        "command": "editor.action.joinLines"
    },
    {
        "key": "ctrl+/",
        "command": "editor.action.blockComment",
        "when": "editorTextFocus && !editorReadonly"
    },
    {
        "key": "ctrl+shift+a",
        "command": "-editor.action.blockComment",
        "when": "editorTextFocus && !editorReadonly"
    },
    {
        "key": "ctrl+shift+up",
        "command": "editor.action.moveLinesUpAction",
        "when": "editorTextFocus"
    },
    {
        "key": "ctrl+shift+down",
        "command": "editor.action.moveLinesDownAction",
        "when": "editorTextFocus"
    }
]
```