---
layout: single
title: "Learn to fix bug"
permalink: /teaching/learn-to-fix-bug/
author_profile: false
show_teaching_meta: false
---

<div class="bug-lab">
  <div class="bug-lab__toolbar">
    <span id="bug-lab-step">Etape 0 / 8</span>
    <button id="bug-lab-undo" class="is-hidden" type="button" title="Arriere">↶</button>
    <button id="bug-lab-redo" class="is-hidden" type="button" title="Avant">↷</button>
    <button id="bug-lab-reset" type="button">Reinitialiser</button>
    <button id="bug-lab-validate" type="button" disabled>Valider cette étape</button>
  </div>

  <div class="bug-lab__message" id="bug-lab-message"></div>
  <div class="bug-lab__final is-hidden" id="bug-lab-final">Exercice validé. Bravo, tous les bugs ont été corrigés.</div>

  <div class="bug-lab__instructions" id="bug-lab-instructions">
    <p>
      Reprenons le premier exercice sur les nombres complexes du TP1.<br>
      Vos encadrants vous donnent le corrigé mais un certain nombre de bugs se sont glissés dans le code... c'est à vous de les corriger !<br>
      A chaque étape, un nouveau bug apparaît avec le traceback ("suivi d'erreur") detaillé qui retrace l'erreur.<br>
      Corrige l'erreur et appuie sur "Valider cette étape" pour passer a l'étape suivante. Si l'erreur persiste, il suffit de réessayer...<br>
      Une fois les consignes lues, clique sur "Valider cette étape" et commence le débogage...
    </p>
    <p><strong>Exemple de lecture d'une traceback</strong></p>
    <pre class="bug-lab__example">1 def carre(x):
2     return x ** y
3 print(carre(4))</pre>
    <pre class="bug-lab__example-trace">Traceback (most recent call last):
  File "TP1.py", line 3, in &lt;module&gt;
    print(carre(4))
  File "TP1.py", line 2, in carre
    return x ** y
NameError: name 'y' is not defined</pre>
    <p>
      Le programme essaie d'exécuter la ligne 3, qui appelle la fonction <code>carre</code>.
      Ensuite en ligne 2, dans la fonction <code>carre</code>, il trouve une erreur (la variable <code>y</code> n'existe pas).<br>
      La traceback s'affiche du plus ancien appel vers le plus recent, mais pour trouver la vraie cause du problème il faut généralement commencer par la fin. La toute dernière ligne du traceback donne le type d'erreur et son message.
    </p>
  </div>

  <div class="bug-lab__editor-wrap">
    <textarea id="bug-lab-editor" spellcheck="false"></textarea>
  </div>

  <pre class="bug-lab__output" id="bug-lab-output"></pre>
  <pre class="bug-lab__trace" id="bug-lab-trace"></pre>
</div>

<style>
.bug-lab {
  border: 1px solid #d5dce3;
  border-radius: 12px;
  padding: 1rem;
  background: linear-gradient(165deg, #fbfcfe 0%, #f1f5fb 100%);
}

.bug-lab__status {
  margin-bottom: 0.8rem;
  padding: 0.6rem 0.8rem;
  border-left: 4px solid #2f6da8;
  background: #edf4fc;
}

.bug-lab__toolbar {
  display: flex;
  gap: 0.8rem;
  flex-wrap: wrap;
  align-items: center;
  margin-bottom: 0.8rem;
}

.bug-lab__toolbar button {
  border: none;
  border-radius: 8px;
  padding: 0.5rem 0.9rem;
  color: #ffffff;
  cursor: pointer;
}

#bug-lab-validate {
  background: #1f7a4a;
  margin-left: auto;
}

#bug-lab-validate:disabled {
  background: #7da894;
  cursor: not-allowed;
}

#bug-lab-reset {
  background: #3a4d69;
}

#bug-lab-undo {
  background: #4f5f75;
}

#bug-lab-redo {
  background: #4f5f75;
}

.bug-lab__editor-wrap {
  min-height: 260px;
  max-height: 420px;
  border: 1px solid #bcc8d6;
  border-radius: 10px;
  background: #fdfefe;
  overflow: auto;
}

#bug-lab-editor {
  width: 100%;
  height: auto;
  min-height: 0;
  border: none;
  outline: none;
  padding: 0.9rem;
  font-family: "Fira Code", "Consolas", monospace;
  font-size: 0.93rem;
  line-height: 1.45;
  background: transparent;
  resize: none;
}

.CodeMirror {
  height: auto;
  font-family: "Fira Code", "Consolas", monospace;
  font-size: 0.93rem;
  line-height: 1.45;
}

.CodeMirror-scroll {
  min-height: 260px;
  max-height: 420px;
}

.CodeMirror-gutters {
  border-right: 1px solid #d8e0ea;
  background: #f2f6fb;
}

.CodeMirror-linenumber {
  color: #73859d;
}

.bug-lab__message {
  margin-top: 0.8rem;
  padding: 0.7rem 0.85rem;
  border-radius: 8px;
  min-height: 2.2rem;
  background: #e7eef7;
}

.bug-lab__instructions {
  margin-bottom: 0.8rem;
  padding: 0.75rem 0.9rem;
  border-radius: 8px;
  border: 1px solid #cfd9e8;
  background: #f5f9ff;
}

.bug-lab__instructions ul {
  margin: 0.5rem 0;
}

.bug-lab__final {
  margin-top: 0.8rem;
  padding: 0.9rem 1rem;
  border-radius: 10px;
  border: 2px solid #1f7a4a;
  background: linear-gradient(180deg, #ebfff2 0%, #dff7e8 100%);
  color: #0f5130;
  font-weight: 700;
  text-align: center;
}

.bug-lab__example,
.bug-lab__example-trace {
  margin: 0.45rem 0 0.7rem;
  padding: 0.6rem 0.7rem;
  border-radius: 8px;
  font-family: "Fira Code", "Consolas", monospace;
  font-size: 0.83rem;
  white-space: pre-wrap;
}

.bug-lab__example {
  border: 1px solid #d6e1ef;
  background: #f8fbff;
}

.bug-lab__example-trace {
  border: 1px solid #e5d5d5;
  background: #fff8f8;
}

.bug-lab__trace {
  margin-top: 0.7rem;
  padding: 0.75rem;
  border-radius: 8px;
  border: 1px solid #e3e8ef;
  background: #fbfcff;
  font-family: "Fira Code", "Consolas", monospace;
  font-size: 0.85rem;
  white-space: pre-wrap;
  display: none;
}

.bug-lab__output {
  margin-top: 0.7rem;
  padding: 0.75rem;
  border-radius: 8px;
  border: 1px solid #dbe4d0;
  background: #f8fcf3;
  font-family: "Fira Code", "Consolas", monospace;
  font-size: 0.85rem;
  white-space: pre-wrap;
  display: none;
}

.is-hidden {
  display: none !important;
}
</style>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.18/codemirror.min.css" />
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.18/theme/eclipse.min.css" />
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.18/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.18/mode/python/python.min.js"></script>
<script src="https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js"></script>
<script>
(function () {
  const storageKeyCode = "bugLabCodeV1";
  const storageKeyStep = "bugLabStepV1";
  const scriptPath = "/files/teaching/learn-to-fix-bug.py";

  let baseCode = "";

  const bugStages = [
    {
      label: "Erreur de syntaxe",
      match: (r) => r.type === "SyntaxError" && r.traceback.includes("conjugue")
    },
    {
      label: "Erreur d'indentation",
      match: (r) => r.type === "IndentationError"
    },
    {
      label: "Nom de variable invalide",
      match: (r) => r.type === "SyntaxError" && r.traceback.includes("z resultat")
    },
    {
      label: "Mauvaise utilisation du constructeur",
      match: (r) => r.type === "TypeError" && r.message.includes("missing 1 required positional argument")
    },
    {
      label: "Attribut introuvable",
      match: (r) => r.type === "AttributeError" && r.message.includes("modul")
    },
    {
      label: "Attribut introuvable",
      match: (r) => r.type === "AttributeError" && r.message.includes("'Complexe' object has no attribute 'i'")
    },
    {
      label: "Attribut introuvable",
      match: (r) => r.type === "AttributeError" && r.message.includes("conjuge")
    },
    {
      label: "Type invalide",
      match: (r) => r.type === "TypeError" && r.message.includes("unsupported operand")
    }
  ];
  const totalSteps = bugStages.length;

  const instructions = document.getElementById("bug-lab-instructions");
  const editorWrap = document.querySelector(".bug-lab__editor-wrap");
  const editor = document.getElementById("bug-lab-editor");
  const undoButton = document.getElementById("bug-lab-undo");
  const redoButton = document.getElementById("bug-lab-redo");
  const resetButton = document.getElementById("bug-lab-reset");
  const validateButton = document.getElementById("bug-lab-validate");
  const status = document.getElementById("bug-lab-status");
  const message = document.getElementById("bug-lab-message");
  const finalBanner = document.getElementById("bug-lab-final");
  const output = document.getElementById("bug-lab-output");
  const trace = document.getElementById("bug-lab-trace");
  const stepText = document.getElementById("bug-lab-step");

  let codeEditor = null;
  let pyodide = null;
  let step = 0;

  function setMessage(text, kind) {
    message.textContent = text;
    if (kind === "success") {
      message.style.background = "#e5f6ea";
      message.style.borderLeft = "4px solid #1f7a4a";
    } else if (kind === "warning") {
      message.style.background = "#fff6dd";
      message.style.borderLeft = "4px solid #b58a1d";
    } else {
      message.style.background = "#fbe9e9";
      message.style.borderLeft = "4px solid #a62e2e";
    }
  }

  function setTraceback(text) {
    if (!text) {
      trace.style.display = "none";
      trace.textContent = "";
      return;
    }
    trace.style.display = "block";
    trace.textContent = text;
  }

  function setOutput(text) {
    if (!text) {
      output.style.display = "none";
      output.textContent = "";
      return;
    }
    output.style.display = "block";
    output.textContent = text;
  }

  function normalizeTraceback(text) {
    return String(text || "")
      .replace(/File "<string>"/g, 'File "TP1.py"')
      .replace(/File "<exec>"/g, 'File "TP1.py"');
  }

  function setFinalBannerVisible(isVisible) {
    finalBanner.classList.toggle("is-hidden", !isVisible);
  }

  function refreshUi() {
    const showHistoryButtons = step >= 1 && step < bugStages.length + 1;
    undoButton.classList.toggle("is-hidden", !showHistoryButtons);
    redoButton.classList.toggle("is-hidden", !showHistoryButtons);
    setFinalBannerVisible(false);
    message.classList.remove("is-hidden");

    if (step === 0) {
      stepText.textContent = "Etape 0 / " + totalSteps;
      instructions.style.display = "block";
      editorWrap.classList.add("is-hidden");
      output.classList.add("is-hidden");
      trace.classList.add("is-hidden");
      return;
    }

    instructions.style.display = "none";
    editorWrap.classList.remove("is-hidden");

    if (step >= bugStages.length + 1) {
      stepText.textContent = "Toutes les étapes sont validées";
      editorWrap.classList.add("is-hidden");
      output.classList.add("is-hidden");
      trace.classList.add("is-hidden");
      message.classList.add("is-hidden");
      setFinalBannerVisible(true);
      setMessage("", "success");
      validateButton.disabled = false;
      return;
    }

    stepText.textContent = "Etape " + step + " / " + totalSteps;
  }

  function detectBugStage(result) {
    if (result.ok) {
      return -1;
    }
    for (let i = 0; i < bugStages.length; i += 1) {
      if (bugStages[i].match(result)) {
        return i;
      }
    }
    return -2;
  }

  async function loadBaseCode() {
    const response = await fetch(scriptPath, { cache: "no-store" });
    if (!response.ok) {
      throw new Error("Impossible de charger le script Python source.");
    }
    baseCode = await response.text();
  }

  async function checkCurrentStep() {
    if (!pyodide) {
      setMessage("L'environnement Python n'est pas pret. Patiente quelques secondes.", "warning");
      return;
    }

    if (step === 0) {
      step = 1;
      localStorage.setItem(storageKeyStep, String(step));
      refreshUi();
      setOutput("");
      setTraceback("");
      setMessage("Debogage lance (étape 1/" + totalSteps + ").", "warning");
    }

    const code = codeEditor.getValue();
    localStorage.setItem(storageKeyCode, code);

    const python = [
      "import json",
      "import io",
      "import traceback",
      "from contextlib import redirect_stdout, redirect_stderr",
      "filename = 'TP1.py'",
      "student_code = " + JSON.stringify(code),
      "result = {'ok': True, 'type': '', 'message': '', 'traceback': '', 'stdout': '', 'stderr': ''}",
      "stdout_buffer = io.StringIO()",
      "stderr_buffer = io.StringIO()",
      "try:",
      "    with redirect_stdout(stdout_buffer), redirect_stderr(stderr_buffer): exec(compile(student_code, filename, 'exec'), {'__name__': '__main__'})",
      "except BaseException as e:",
      "    formatted_tb = traceback.format_exc()",
      "    result = {'ok': False, 'type': e.__class__.__name__, 'message': str(e), 'traceback': formatted_tb, 'stdout': stdout_buffer.getvalue(), 'stderr': stderr_buffer.getvalue()}",
      "else:",
      "    result = {'ok': True, 'type': '', 'message': '', 'traceback': '', 'stdout': stdout_buffer.getvalue(), 'stderr': stderr_buffer.getvalue()}",
      "json.dumps(result)"
    ].join("\n");

    try {
      const raw = await pyodide.runPythonAsync(python);
      const result = JSON.parse(raw);
      const bugIndex = detectBugStage(result);
      const bugStep = bugIndex + 1;
      const combinedOutput = [result.stdout, result.stderr].filter(Boolean).join(result.stdout && result.stderr ? "\n" : "");

      output.classList.remove("is-hidden");
      setOutput(combinedOutput);

      if (result.ok) {
        step = bugStages.length + 1;
        localStorage.setItem(storageKeyStep, String(step));
        refreshUi();
        setTraceback("");
        trace.classList.add("is-hidden");
        setMessage("Tu as reussi, bien joue. Tous les bugs sont corriges.", "success");
        return;
      }

      trace.classList.remove("is-hidden");
      setTraceback(normalizeTraceback(result.traceback));

      if (bugIndex === -2) {
        setMessage("Erreur inattendue. Lis la traceback ci-dessous et corrige ce point.", "error");
        return;
      }

      if (bugStep === step) {
        setMessage("Reessaye encore: corrige ce bug, puis valide.", "warning");
        return;
      }

      if (bugStep > step) {
        step = bugStep;
        localStorage.setItem(storageKeyStep, String(step));
        refreshUi();
        setMessage("Tu as reussi, bien joue. Tu es passe au bug suivant.", "success");
        return;
      }

      step = bugStep;
      localStorage.setItem(storageKeyStep, String(step));
      refreshUi();
      setMessage("Presque... un bug precedent est revenu. Corrige-le d'abord.", "warning");
    } catch (err) {
      trace.classList.remove("is-hidden");
      setTraceback(String((err && (err.stack || err.message)) || err || ""));
      setOutput("");
      setMessage("Erreur d'execution cote navigateur: " + String((err && err.message) || err || "inconnue"), "error");
    }
  }

  async function resetAll() {
    localStorage.removeItem(storageKeyCode);
    localStorage.removeItem(storageKeyStep);
    step = 0;
    codeEditor.setValue(baseCode);
    setOutput("");
    setTraceback("");
    refreshUi();
    setMessage("Progression réinitialisée.", "warning");
  }

  undoButton.addEventListener("click", function () {
    if (!codeEditor) {
      return;
    }
    codeEditor.undo();
    localStorage.setItem(storageKeyCode, codeEditor.getValue());
  });

  redoButton.addEventListener("click", function () {
    if (!codeEditor) {
      return;
    }
    codeEditor.redo();
    localStorage.setItem(storageKeyCode, codeEditor.getValue());
  });

  resetButton.addEventListener("click", resetAll);
  validateButton.addEventListener("click", checkCurrentStep);

  async function boot() {
    try {
      await loadBaseCode();
      codeEditor = CodeMirror.fromTextArea(editor, {
        mode: "python",
        theme: "eclipse",
        lineNumbers: true,
        indentUnit: 4,
        tabSize: 4,
        lineWrapping: false
      });
      codeEditor.setValue(localStorage.getItem(storageKeyCode) || baseCode);
      codeEditor.on("change", function (instance) {
        localStorage.setItem(storageKeyCode, instance.getValue());
      });

      refreshUi();
      setOutput("");
      setTraceback("");

      pyodide = await loadPyodide();
      if (status) {
        status.textContent = "Environnement Python pret.";
      }
      validateButton.disabled = false;
      if (step === 0) {
        setMessage("Lis les consignes puis valide l'etape 0.", "warning");
      } else if (step < bugStages.length + 1) {
        setMessage("Corrige le bug courant puis clique sur Valider.", "warning");
      } else {
        setMessage("Tout est deja valide. Tu peux reinitialiser pour recommencer.", "success");
      }
    } catch (err) {
      if (status) {
        status.textContent = "Impossible de charger Python dans le navigateur.";
      }
      setMessage("Erreur de chargement Pyodide: " + String(err), "error");
    }
  }

  boot();
})();
</script>
