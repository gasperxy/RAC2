# =============================================================================
# Tekmovanje - Nahrbtnik
#
# Na vajah bomo izvedli tekmovanje v parih. Spodnje naloge se navezujejo na uporabo 0/1 nahrbtnika in 
# njegovih variacij. Par, ki bo rešil največ nalog v času (recimo dve šolski uri) bo dobil neko simbolično 
# nagrado v smislu oprostitve nekega dela poročila. Testni primeri so sestavljeni, da ob pravilni implementaciji funkcije
# trajajo nekje do 10-15 sekund. Če vaša funkcija deluje bistveno več časa potem prekinite delovanje in optimizirajte svojo
# rešite.
# 
# 
# Trgovec želi iz Evrope v Ameriko spravit večjo količino predmetov. Pri tem ima na 
# razpolago tovorno letalo, ki pa lahko prenese le omejeno količino blaga.
# Predmete predstavimo s seznamom elementov oblike $(c_i, v_i)$, kjer $c_i$ predstavlja
# ceno $i$-tega predmeta, $v_i$ pa njegovo težo.
# =====================================================================@033253=
# 1. podnaloga
# Implementiraj funkcijo `optimalni_tovor(predmeti, W)`, ki vrne največjo skupno ceno
# predmetov, ki jih lahko trgovec natovori na letalo z maksimalno nosilnostjo `W`.
# Na primer:
# 
#     >>> optimalni_tovor([(2,3), (4,4), (5,4), (3,2), (1,2), (15, 12)], 7)
#     8
# =============================================================================
from functools import lru_cache


def optimalni_tovor(predmeti, W):
    @lru_cache(maxsize=None)
    def pomozna(i, W):
        if W < 0:
            # če nimamo prostora
            return float("-inf")
        if W == 0 or i == 0:
            # če nimamo več predmetov ali prostora
            return 0
        ne_vzamemo = pomozna(i-1,W)  # ne vzamemo i-tega predmeta, W se ne spremeni
        vzamemo = pomozna(i - 1, W - predmeti[i-1][1]) + predmeti[i-1][0]  # vzamemo i-ti predmet, W se ustrezno zmanjša, vrednost se ustrezno poveča
        return max(ne_vzamemo, vzamemo)
    return pomozna(len(predmeti),W)

# =====================================================================@033254=
# 2. podnaloga
# Implementiraj funkcijo `optimalni_predmeti(predmeti, W)`, ki vrne seznam predmetov
# ki dosežejo največjo vrednost, če lahko na letalo natovorimo skupno težo največ `W`.
# Če je možnosti več, vrni katerokoli.
# Na primer:
# 
#     >>> optimalni_predmeti([(2,3), (4,4), (5,4), (3,2), (1,2), (15, 12)], 7)
#     [(3, 2), (5, 4)]
# =============================================================================
def optimalni_predmeti(predmeti, W):
    '''Vrne seznam predmetov ki dosežejo največjo vrednost, če lahko na letalo natovorimo skupno težo največ `W`.'''
    predmeti = [(el[1],el[0]) for el in predmeti]
    n = len(predmeti)
    # ustvari matriko za hranjenje maksimalne vrednosti, ki je lahko posodobljena za vsak predmet
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]  # matrika velikosti (n+1)x(W+1)
    
    # grajenje matrike od spodaj navzgor
    for i in range(1, n + 1):  # z i gremo po vrsticah
        for j in range(1, W + 1):  # z j gremo po stolpciih
            # če trenutni predmet ustreza nahrbtniku
            if predmeti[i-1][0] <= j:
                # vzame največjo vrednost med tem, ali vzamemo predmet ali ne
                ne_vzamemo = dp[i-1][j]  # predmeta ne vzamemo
                vzamemo = dp[i-1][j-predmeti[i-1][0]] + predmeti[i-1][1]  # predmet vzamemo
                dp[i][j] = max(ne_vzamemo, vzamemo)
            else:
                # če trenutni predmet ne ustreza nahrbtniku, vzame vrednost prejšnjega predmeta
                dp[i][j] = dp[i-1][j]

    izbrani = list()
    j = W
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i-1][j]:
            izbrani.append(predmeti[i-1])
            j -= predmeti[i-1][0]

    # Vrne seznam izbranih predmetov
    izbrani = [(el[1],el[0]) for el in izbrani]
    return izbrani

# =====================================================================@033255=
# 3. podnaloga
# Trgovec je dobil dodatno pošiljko obstoječih predmetov. Tako ima sedaj na razpolago več
# kot en predmet posameznega tipa. Predmete tako predstavimo s seznamom elementov oblike
# $(c_i, v_i, z_i)$, kjer je:
# * $c_i$ cena
# * $v_i$ teža
# * $z_i$ zaloga
# $i$-tega predmeta.
# 
# Implementiraj funkcijo `optimalni_tovor_zaloga(predmeti, W)`, ki vrne največjo skupno ceno
# predmetov, ki jih lahko trgovec natovori na letalo z maksimalno nosilnostjo `W`.
# Na primer:
# 
#     >>> optimalni_tovor_zaloga([(2,3, 1), (4,4, 2), (5,4, 4), (3,2, 3), (1,2, 3), (15, 12, 2)], 7))
#     9
# =============================================================================
def optimalni_tovor_zaloga(predmeti, W):
    '''Vrne največjo skupno ceno predmetov, ki jih lahko trgovec natovori na letalo z maksimalno nosilnostjo `W`.
        Sedaj so predmeti predstavljeni kot trojice (vrednost, teža, zaloga). Istih predmetov je toliko, kolikor je njegove zaloge.'''
    # ustvarimo novo tabelo, v kateri so navedeni predmeti tako, da lahko kličemo fn. iz prve naloge 
    nova = [(el[0], el[1]) for el in predmeti for _ in range(el[2])]
    return optimalni_tovor(nova, W)


# =====================================================================@033256=
# 4. podnaloga
# Predpostavi, da ima sedaj trgovec na voljo neomejeno zalogo posameznih predmetov.
# implementiraj funkcijo `neomejena_zaloga(predmeti, W)`, ki vrne najvišjo skupno ceno tovora na letalu 
# z maksimalno nosilnostjo `W`
# Na primer:
# 
#     >>> neomejena_zaloga([(2,3), (4,4), (5,4), (3,2), (1,2), (15, 12)], 23)
#     33
# =============================================================================
def neomejena_zaloga(predmeti, W):
    def pomozna(W, n, val, wt):
        dp = [0 for i in range(W+1)]
        for i in range(W+1):
            for j in range(n):
                if (wt[j] <= i):
                    dp[i] = max(dp[i], dp[i - wt[j]] + val[j])
        return dp[W]
    return pomozna(W, len(predmeti), [el[0] for el in predmeti], [el[1] for el in predmeti])

  
# =====================================================================@033257=
# 5. podnaloga
# Trgovec je ugotovil, da se mu izplača imeti nekaterih predmetov več na zalogi kot ostalih.
# Implementiraj funkcijo `najboljsa_zaloga(predmeti, W)`, ki vrne seznam `zaloga` dolžine `len(predmeti)`,
# kjer `zaloga[i]` predstavlja koliko zaloge potrebuje za predmet `i`, tako da bo skupna vrednost pošiljke na letalu z
# maksimalno nosilnostjo `W` čim večja.
# Na primer:
# 
#     >>> najboljsa_zaloga([(2,3), (4,4), (5,4), (3,2), (1,2), (15, 12)], 23)
#     [1, 0, 0, 10, 0, 0]
# =============================================================================

# =====================================================================@033284=
# 6. podnaloga
# Letalski prevoznik je trgovcu ponudil opcijo, da mu ni treba pošiljati celotnih predmetov. Zapakira jih lahko v manjšo škatlo in 
# jih naloži na letalo. Bolj natančno, za nek predmet $(c_i, v_i)$ lahko na letalo naloži predmet oblike $(c_i/r, v_i/r)$ za $r \in \{1,2,3,4\}$.
# Pri tem lahko na letalo naloži le en tip predmeta. Na letalu ne more tako biti recimo $1/2 + 1/3 = 5/6$ nekega predmeta. Implementiraj funkcijo # `tovor_rezanje(predmeti, W)`, ki vrne koliko je sedaj največja  skupna cena tovora, če je nosilnost letala največ `W`. Rezultat vrni zaokrožen na dve decimalni mesti.
# Na primer:
# 
#     >>> tovor_rezanje([(2,3), (4,4), (5,4), (3,2), (1,2), (15, 12)], 20)
#     25.0
# =============================================================================

# =====================================================================@033285=
# 7. podnaloga
# Trgovec je dobil na razpolago nabor novih izdelkov. Odločiti se mora za enega, ki ga bo vključil v svoje trgovanje.
# Odloča se na podlagi tega, koliko bo največja skupna cena tovora, ki ga bo lahko poslal z letalom. Pomagaj mu, tako da
# implementiraš funkcijo `tovor_novi_predmet(predmeti, W, novi_predmeti)`, ki vrne najboljšo skupno ceno tovora, ki ga lahko
# spravimo na letalo z nosilnostjo najvč `W` z predmeti iz seznama `predmeti` ter enim dodatnim predmetom iz seznama `novi_predmeti`.
# Pozor: pri testnih primerih je seznam `novi_predmeti` dolg približno `1000` elementov. Funkcija mora biti tako spisana čim bolje.
# Na primer:
# 
#     >>> tovor_novi_predmet([(2,3), (4,4), (5,4), (3,2), (1,2), (15, 12)], 20,[(4,4), (12,11), (2,3), (17, 5), (18,8), (5,6), (7,6), (6,6)])
#     35
# =============================================================================






































































































# ============================================================================@
# fmt: off
"Če vam Python sporoča, da je v tej vrstici sintaktična napaka,"
"se napaka v resnici skriva v zadnjih vrsticah vaše kode."

"Kode od tu naprej NE SPREMINJAJTE!"

# isort: off
import json
import os
import re
import shutil
import sys
import traceback
import urllib.error
import urllib.request
import io
from contextlib import contextmanager


class VisibleStringIO(io.StringIO):
    def read(self, size=None):
        x = io.StringIO.read(self, size)
        print(x, end="")
        return x

    def readline(self, size=None):
        line = io.StringIO.readline(self, size)
        print(line, end="")
        return line


class Check:
    parts = None
    current_part = None
    part_counter = None

    @staticmethod
    def has_solution(part):
        return part["solution"].strip() != ""

    @staticmethod
    def initialize(parts):
        Check.parts = parts
        for part in Check.parts:
            part["valid"] = True
            part["feedback"] = []
            part["secret"] = []

    @staticmethod
    def part():
        if Check.part_counter is None:
            Check.part_counter = 0
        else:
            Check.part_counter += 1
        Check.current_part = Check.parts[Check.part_counter]
        return Check.has_solution(Check.current_part)

    @staticmethod
    def feedback(message, *args, **kwargs):
        Check.current_part["feedback"].append(message.format(*args, **kwargs))

    @staticmethod
    def error(message, *args, **kwargs):
        Check.current_part["valid"] = False
        Check.feedback(message, *args, **kwargs)

    @staticmethod
    def clean(x, digits=6, typed=False):
        t = type(x)
        if t is float:
            x = round(x, digits)
            # Since -0.0 differs from 0.0 even after rounding,
            # we change it to 0.0 abusing the fact it behaves as False.
            v = x if x else 0.0
        elif t is complex:
            v = complex(
                Check.clean(x.real, digits, typed), Check.clean(x.imag, digits, typed)
            )
        elif t is list:
            v = list([Check.clean(y, digits, typed) for y in x])
        elif t is tuple:
            v = tuple([Check.clean(y, digits, typed) for y in x])
        elif t is dict:
            v = sorted(
                [
                    (Check.clean(k, digits, typed), Check.clean(v, digits, typed))
                    for (k, v) in x.items()
                ]
            )
        elif t is set:
            v = sorted([Check.clean(y, digits, typed) for y in x])
        else:
            v = x
        return (t, v) if typed else v

    @staticmethod
    def secret(x, hint=None, clean=None):
        clean = Check.get("clean", clean)
        Check.current_part["secret"].append((str(clean(x)), hint))

    @staticmethod
    def equal(expression, expected_result, clean=None, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        actual_result = eval(expression, global_env)
        if clean(actual_result) != clean(expected_result):
            Check.error(
                "Izraz {0} vrne {1!r} namesto {2!r}.",
                expression,
                actual_result,
                expected_result,
            )
            return False
        else:
            return True

    @staticmethod
    def approx(expression, expected_result, tol=1e-6, env=None, update_env=None):
        try:
            import numpy as np
        except ImportError:
            Check.error("Namestiti morate numpy.")
            return False
        if not isinstance(expected_result, np.ndarray):
            Check.error("Ta funkcija je namenjena testiranju za tip np.ndarray.")

        if env is None:
            env = dict()
        env.update({"np": np})
        global_env = Check.init_environment(env=env, update_env=update_env)
        actual_result = eval(expression, global_env)
        if type(actual_result) is not type(expected_result):
            Check.error(
                "Rezultat ima napačen tip. Pričakovan tip: {}, dobljen tip: {}.",
                type(expected_result).__name__,
                type(actual_result).__name__,
            )
            return False
        exp_shape = expected_result.shape
        act_shape = actual_result.shape
        if exp_shape != act_shape:
            Check.error(
                "Obliki se ne ujemata. Pričakovana oblika: {}, dobljena oblika: {}.",
                exp_shape,
                act_shape,
            )
            return False
        try:
            np.testing.assert_allclose(
                expected_result, actual_result, atol=tol, rtol=tol
            )
            return True
        except AssertionError as e:
            Check.error("Rezultat ni pravilen." + str(e))
            return False

    @staticmethod
    def run(statements, expected_state, clean=None, env=None, update_env=None):
        code = "\n".join(statements)
        statements = "  >>> " + "\n  >>> ".join(statements)
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        exec(code, global_env)
        errors = []
        for x, v in expected_state.items():
            if x not in global_env:
                errors.append(
                    "morajo nastaviti spremenljivko {0}, vendar je ne".format(x)
                )
            elif clean(global_env[x]) != clean(v):
                errors.append(
                    "nastavijo {0} na {1!r} namesto na {2!r}".format(
                        x, global_env[x], v
                    )
                )
        if errors:
            Check.error("Ukazi\n{0}\n{1}.", statements, ";\n".join(errors))
            return False
        else:
            return True

    @staticmethod
    @contextmanager
    def in_file(filename, content, encoding=None):
        encoding = Check.get("encoding", encoding)
        with open(filename, "w", encoding=encoding) as f:
            for line in content:
                print(line, file=f)
        old_feedback = Check.current_part["feedback"][:]
        yield
        new_feedback = Check.current_part["feedback"][len(old_feedback) :]
        Check.current_part["feedback"] = old_feedback
        if new_feedback:
            new_feedback = ["\n    ".join(error.split("\n")) for error in new_feedback]
            Check.error(
                "Pri vhodni datoteki {0} z vsebino\n  {1}\nso se pojavile naslednje napake:\n- {2}",
                filename,
                "\n  ".join(content),
                "\n- ".join(new_feedback),
            )

    @staticmethod
    @contextmanager
    def input(content, visible=None):
        old_stdin = sys.stdin
        old_feedback = Check.current_part["feedback"][:]
        try:
            with Check.set_stringio(visible):
                sys.stdin = Check.get("stringio")("\n".join(content) + "\n")
                yield
        finally:
            sys.stdin = old_stdin
        new_feedback = Check.current_part["feedback"][len(old_feedback) :]
        Check.current_part["feedback"] = old_feedback
        if new_feedback:
            new_feedback = ["\n  ".join(error.split("\n")) for error in new_feedback]
            Check.error(
                "Pri vhodu\n  {0}\nso se pojavile naslednje napake:\n- {1}",
                "\n  ".join(content),
                "\n- ".join(new_feedback),
            )

    @staticmethod
    def out_file(filename, content, encoding=None):
        encoding = Check.get("encoding", encoding)
        with open(filename, encoding=encoding) as f:
            out_lines = f.readlines()
        equal, diff, line_width = Check.difflines(out_lines, content)
        if equal:
            return True
        else:
            Check.error(
                "Izhodna datoteka {0}\n  je enaka{1}  namesto:\n  {2}",
                filename,
                (line_width - 7) * " ",
                "\n  ".join(diff),
            )
            return False

    @staticmethod
    def output(expression, content, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        too_many_read_requests = False
        try:
            exec(expression, global_env)
        except EOFError:
            too_many_read_requests = True
        finally:
            output = sys.stdout.getvalue().rstrip().splitlines()
            sys.stdout = old_stdout
        equal, diff, line_width = Check.difflines(output, content)
        if equal and not too_many_read_requests:
            return True
        else:
            if too_many_read_requests:
                Check.error("Program prevečkrat zahteva uporabnikov vnos.")
            if not equal:
                Check.error(
                    "Program izpiše{0}  namesto:\n  {1}",
                    (line_width - 13) * " ",
                    "\n  ".join(diff),
                )
            return False

    @staticmethod
    def difflines(actual_lines, expected_lines):
        actual_len, expected_len = len(actual_lines), len(expected_lines)
        if actual_len < expected_len:
            actual_lines += (expected_len - actual_len) * ["\n"]
        else:
            expected_lines += (actual_len - expected_len) * ["\n"]
        equal = True
        line_width = max(
            len(actual_line.rstrip())
            for actual_line in actual_lines + ["Program izpiše"]
        )
        diff = []
        for out, given in zip(actual_lines, expected_lines):
            out, given = out.rstrip(), given.rstrip()
            if out != given:
                equal = False
            diff.append(
                "{0} {1} {2}".format(
                    out.ljust(line_width), "|" if out == given else "*", given
                )
            )
        return equal, diff, line_width

    @staticmethod
    def init_environment(env=None, update_env=None):
        global_env = globals()
        if not Check.get("update_env", update_env):
            global_env = dict(global_env)
        global_env.update(Check.get("env", env))
        return global_env

    @staticmethod
    def generator(
        expression,
        expected_values,
        should_stop=None,
        further_iter=None,
        clean=None,
        env=None,
        update_env=None,
    ):
        from types import GeneratorType

        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        gen = eval(expression, global_env)
        if not isinstance(gen, GeneratorType):
            Check.error("Izraz {0} ni generator.", expression)
            return False

        try:
            for iteration, expected_value in enumerate(expected_values):
                actual_value = next(gen)
                if clean(actual_value) != clean(expected_value):
                    Check.error(
                        "Vrednost #{0}, ki jo vrne generator {1} je {2!r} namesto {3!r}.",
                        iteration,
                        expression,
                        actual_value,
                        expected_value,
                    )
                    return False
            for _ in range(Check.get("further_iter", further_iter)):
                next(gen)  # we will not validate it
        except StopIteration:
            Check.error("Generator {0} se prehitro izteče.", expression)
            return False

        if Check.get("should_stop", should_stop):
            try:
                next(gen)
                Check.error("Generator {0} se ne izteče (dovolj zgodaj).", expression)
            except StopIteration:
                pass  # this is fine
        return True

    @staticmethod
    def summarize():
        for i, part in enumerate(Check.parts):
            if not Check.has_solution(part):
                print("{0}. podnaloga je brez rešitve.".format(i + 1))
            elif not part["valid"]:
                print("{0}. podnaloga nima veljavne rešitve.".format(i + 1))
            else:
                print("{0}. podnaloga ima veljavno rešitev.".format(i + 1))
            for message in part["feedback"]:
                print("  - {0}".format("\n    ".join(message.splitlines())))

    settings_stack = [
        {
            "clean": clean.__func__,
            "encoding": None,
            "env": {},
            "further_iter": 0,
            "should_stop": False,
            "stringio": VisibleStringIO,
            "update_env": False,
        }
    ]

    @staticmethod
    def get(key, value=None):
        if value is None:
            return Check.settings_stack[-1][key]
        return value

    @staticmethod
    @contextmanager
    def set(**kwargs):
        settings = dict(Check.settings_stack[-1])
        settings.update(kwargs)
        Check.settings_stack.append(settings)
        try:
            yield
        finally:
            Check.settings_stack.pop()

    @staticmethod
    @contextmanager
    def set_clean(clean=None, **kwargs):
        clean = clean or Check.clean
        with Check.set(clean=(lambda x: clean(x, **kwargs)) if kwargs else clean):
            yield

    @staticmethod
    @contextmanager
    def set_environment(**kwargs):
        env = dict(Check.get("env"))
        env.update(kwargs)
        with Check.set(env=env):
            yield

    @staticmethod
    @contextmanager
    def set_stringio(stringio):
        if stringio is True:
            stringio = VisibleStringIO
        elif stringio is False:
            stringio = io.StringIO
        if stringio is None or stringio is Check.get("stringio"):
            yield
        else:
            with Check.set(stringio=stringio):
                yield


def _validate_current_file():
    def extract_parts(filename):
        with open(filename, encoding="utf-8") as f:
            source = f.read()
        part_regex = re.compile(
            r"# =+@(?P<part>\d+)=\s*\n"  # beginning of header
            r"(\s*#( [^\n]*)?\n)+?"  # description
            r"\s*# =+\s*?\n"  # end of header
            r"(?P<solution>.*?)"  # solution
            r"(?=\n\s*# =+@)",  # beginning of next part
            flags=re.DOTALL | re.MULTILINE,
        )
        parts = [
            {"part": int(match.group("part")), "solution": match.group("solution")}
            for match in part_regex.finditer(source)
        ]
        # The last solution extends all the way to the validation code,
        # so we strip any trailing whitespace from it.
        parts[-1]["solution"] = parts[-1]["solution"].rstrip()
        return parts

    def backup(filename):
        backup_filename = None
        suffix = 1
        while not backup_filename or os.path.exists(backup_filename):
            backup_filename = "{0}.{1}".format(filename, suffix)
            suffix += 1
        shutil.copy(filename, backup_filename)
        return backup_filename

    def submit_parts(parts, url, token):
        submitted_parts = []
        for part in parts:
            if Check.has_solution(part):
                submitted_part = {
                    "part": part["part"],
                    "solution": part["solution"],
                    "valid": part["valid"],
                    "secret": [x for (x, _) in part["secret"]],
                    "feedback": json.dumps(part["feedback"]),
                }
                if "token" in part:
                    submitted_part["token"] = part["token"]
                submitted_parts.append(submitted_part)
        data = json.dumps(submitted_parts).encode("utf-8")
        headers = {"Authorization": token, "content-type": "application/json"}
        request = urllib.request.Request(url, data=data, headers=headers)
        # This is a workaround because some clients (and not macOS ones!) report
        # <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)>
        import ssl

        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(request, context=context)
        # When the issue is resolved, the following should be used
        # response = urllib.request.urlopen(request)
        return json.loads(response.read().decode("utf-8"))

    def update_attempts(old_parts, response):
        updates = {}
        for part in response["attempts"]:
            part["feedback"] = json.loads(part["feedback"])
            updates[part["part"]] = part
        for part in old_parts:
            valid_before = part["valid"]
            part.update(updates.get(part["part"], {}))
            valid_after = part["valid"]
            if valid_before and not valid_after:
                wrong_index = response["wrong_indices"].get(str(part["part"]))
                if wrong_index is not None:
                    hint = part["secret"][wrong_index][1]
                    if hint:
                        part["feedback"].append("Namig: {}".format(hint))

    filename = os.path.abspath(sys.argv[0])
    file_parts = extract_parts(filename)
    Check.initialize(file_parts)

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozMzI1MywidXNlciI6MzkzNX0:1pdFvO:Y24LOmNdEJ4opfKNHm6q__ENaDTj7NAsbjz_AmNjtDY"
        try:
            Check.equal('optimalni_tovor([(2,3), (4,4), (5,4), (3,2), (1,2), (15, 12)], 7)', 8)
            Check.equal('optimalni_tovor([(90, 4942), (28, 3173), (58, 3515), (76, 637), (9, 5404), (29, 8912), (25, 753), (7, 186), (10, 6055), (58, 7686), (89, 7892), (5, 6709), (43, 7281), (85, 6171), (34, 7676), (54, 5481), (65, 6972), (7, 5146), (48, 5487), (71, 7110), (21, 8080), (25, 3948), (25, 8008), (4, 2765), (58, 7509), (85, 2432), (57, 3933), (23, 639), (18, 7577), (41, 7038), (62, 7685), (23, 4659), (48, 5920), (21, 1924), (63, 6688), (19, 6309), (73, 6807), (30, 2201), (22, 9218), (77, 6274), (68, 4114), (27, 7668), (54, 3871), (49, 5739), (55, 1298), (89, 7515), (20, 3797), (6, 732), (16, 2778), (69, 3293)], 100000)',1425)
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozMzI1NCwidXNlciI6MzkzNX0:1pdFvO:mt9-qR6mX6gJLzs5udh9shi-QnvBqXycZzpsWZZ9t-Q"
        try:
            Check.equal('sum(c for c,v in optimalni_predmeti([(2,3), (4,4), (5,4), (3,2), (1,2), (15, 12)], 7))', 8)
            Check.equal('sum(c for c,v in optimalni_predmeti([(90, 4942), (28, 3173), (58, 3515), (76, 637), (9, 5404), (29, 8912), (25, 753), (7, 186), (10, 6055), (58, 7686), (89, 7892), (5, 6709), (43, 7281), (85, 6171), (34, 7676), (54, 5481), (65, 6972), (7, 5146), (48, 5487), (71, 7110), (21, 8080), (25, 3948), (25, 8008), (4, 2765), (58, 7509), (85, 2432), (57, 3933), (23, 639), (18, 7577), (41, 7038), (62, 7685), (23, 4659), (48, 5920), (21, 1924), (63, 6688), (19, 6309), (73, 6807), (30, 2201), (22, 9218), (77, 6274), (68, 4114), (27, 7668), (54, 3871), (49, 5739), (55, 1298), (89, 7515), (20, 3797), (6, 732), (16, 2778), (69, 3293)], 100000))', 1425)
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozMzI1NSwidXNlciI6MzkzNX0:1pdFvO:cNjOD13m77ehOzWBJGgQRK0_ibP1SSG3aJFTkAAz7do"
        try:
            Check.equal('optimalni_tovor_zaloga([(2,3, 1), (4,4, 2), (5,4, 4), (3,2, 3), (1,2, 3), (15, 12, 2)], 7)', 9)
            Check.equal('optimalni_tovor_zaloga([(73, 2282, 4), (3, 4266, 2), (90, 2468, 4), (60, 3146, 4), (33, 8901, 3), (14, 4964, 2), (44, 6967, 2), (44, 4919, 3), (63, 2490, 5), (37, 9778, 2), (77, 2247, 3), (15, 1707, 1), (37, 8138, 4), (63, 7537, 1), (3, 6821, 5), (28, 6514, 1), (83, 9471, 1), (31, 9486, 1), (58, 8770, 2), (43, 7711, 2), (11, 185, 1), (25, 5456, 4), (94, 8798, 4), (7, 2043, 5), (80, 9840, 1), (14, 6453, 4), (50, 3876, 4), (80, 4624, 1), (56, 3345, 2), (74, 8109, 3), (10, 7845, 4), (65, 5562, 2), (55, 5272, 1), (25, 7095, 3), (9, 1542, 5), (78, 284, 1), (7, 490, 4), (62, 9167, 4), (69, 8708, 2)], 50000)', 1488)
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozMzI1NiwidXNlciI6MzkzNX0:1pdFvO:QND8gMCkwP5qYU4TkV09-ffJ6gpgrYizJdYmFiH5pXw"
        try:
            Check.equal('neomejena_zaloga([(2,3), (4,4), (5,4), (3,2), (1,2), (15, 12)], 23)', 33)
            Check.equal('neomejena_zaloga([(90, 4942), (28, 3173), (58, 3515), (76, 637), (9, 5404), (29, 8912), (25, 753), (7, 186), (10, 6055), (58, 7686), (89, 7892), (5, 6709), (43, 7281), (85, 6171), (34, 7676), (54, 5481), (65, 6972), (7, 5146), (48, 5487), (71, 7110), (21, 8080), (25, 3948), (25, 8008), (4, 2765), (58, 7509), (85, 2432), (57, 3933), (23, 639), (18, 7577), (41, 7038), (62, 7685), (23, 4659), (48, 5920), (21, 1924), (63, 6688), (19, 6309), (73, 6807), (30, 2201), (22, 9218), (77, 6274), (68, 4114), (27, 7668), (54, 3871), (49, 5739), (55, 1298), (89, 7515), (20, 3797), (6, 732), (16, 2778), (69, 3293)], 100000)', 11877)
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozMzI1NywidXNlciI6MzkzNX0:1pdFvO:ot8doZLittTx3RlNXQxdLxu3OrO3xLtOHNu4ZWv4OMs"
        try:
            def vrednost_zaloga(zaloga, pr):
                v = 0
                for i in range(len(zaloga)):
                    v += zaloga[i]*pr[i][0]
            
                return v
                
            
            
            Check.equal('vrednost_zaloga(najboljsa_zaloga([(2,3), (4,4), (5,4), (3,2), (1,2), (15, 12)], 23), [(2,3), (4,4), (5,4), (3,2), (1,2), (15, 12)])', 32, env = {"vrednost_zaloga" : vrednost_zaloga })
            Check.equal('vrednost_zaloga(najboljsa_zaloga([(90, 4942), (28, 3173), (58, 3515), (76, 637), (9, 5404), (29, 8912), (25, 753), (7, 186), (10, 6055), (58, 7686), (89, 7892), (5, 6709), (43, 7281), (85, 6171), (34, 7676), (54, 5481), (65, 6972), (7, 5146), (48, 5487), (71, 7110), (21, 8080), (25, 3948), (25, 8008), (4, 2765), (58, 7509), (85, 2432), (57, 3933), (23, 639), (18, 7577), (41, 7038), (62, 7685), (23, 4659), (48, 5920), (21, 1924), (63, 6688), (19, 6309), (73, 6807), (30, 2201), (22, 9218), (77, 6274), (68, 4114), (27, 7668), (54, 3871), (49, 5739), (55, 1298), (89, 7515), (20, 3797), (6, 732), (16, 2778), (69, 3293)], 100000), [(90, 4942), (28, 3173), (58, 3515), (76, 637), (9, 5404), (29, 8912), (25, 753), (7, 186), (10, 6055), (58, 7686), (89, 7892), (5, 6709), (43, 7281), (85, 6171), (34, 7676), (54, 5481), (65, 6972), (7, 5146), (48, 5487), (71, 7110), (21, 8080), (25, 3948), (25, 8008), (4, 2765), (58, 7509), (85, 2432), (57, 3933), (23, 639), (18, 7577), (41, 7038), (62, 7685), (23, 4659), (48, 5920), (21, 1924), (63, 6688), (19, 6309), (73, 6807), (30, 2201), (22, 9218), (77, 6274), (68, 4114), (27, 7668), (54, 3871), (49, 5739), (55, 1298), (89, 7515), (20, 3797), (6, 732), (16, 2778), (69, 3293)])', 11877,env = {"vrednost_zaloga" : vrednost_zaloga })
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozMzI4NCwidXNlciI6MzkzNX0:1pdFvO:HAkNFBj_ox-Lyq6UqQnhpnWBoe6ihDqG3L8c6Y3HP_E"
        try:
            Check.equal('tovor_rezanje([(2,3), (4,4), (5,4), (3,2), (1,2), (15, 12)], 20)', 25.0)
            Check.equal('tovor_rezanje([(13, 34), (51, 48), (71, 59), (23, 36), (79, 55), (50, 66), (18, 92), (5, 24), (75, 60), (62, 78), (87, 31), (78, 65), (10, 14), (44, 28), (31, 43), (94, 54), (35, 5), (27, 13), (58, 8), (93, 23)], 500)', 830.75)
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozMzI4NSwidXNlciI6MzkzNX0:1pdFvO:_YHp17v2GVot6aSVGzZ_76wnwvo44jnEw449yNXZtA4"
        try:
            predmeti = [(90, 4942), (28, 3173), (58, 3515), (76, 637), (9, 5404), (29, 8912), (25, 753), (7, 186), (10, 6055), (58, 7686), (89, 7892), (5, 6709), (43, 7281), (85, 6171), (34, 7676), (54, 5481), (65, 6972), (7, 5146), (48, 5487), (71, 7110), (21, 8080), (25, 3948), (25, 8008), (4, 2765), (58, 7509), (85, 2432), (57, 3933), (23, 639), (18, 7577), (41, 7038), (62, 7685), (23, 4659), (48, 5920), (21, 1924), (63, 6688), (19, 6309), (73, 6807), (30, 2201), (22, 9218), (77, 6274), (68, 4114), (27, 7668), (54, 3871), (49, 5739), (55, 1298), (89, 7515), (20, 3797), (6, 732), (16, 2778), (69, 3293)]
            novi_predmeti = [(22, 116), (49, 451), (67, 756), (80, 94), (22, 456), (8, 816), (30, 183), (77, 529), (4, 374), (87, 354), (31, 262), (66, 682), (3, 179), (38, 781), (37, 23), (94, 915), (46, 733), (56, 771), (59, 252), (29, 418), (9, 745), (50, 416), (37, 412), (95, 689), (15, 574), (63, 9), (27, 387), (21, 975), (68, 2), (45, 550), (69, 857), (46, 793), (91, 549), (32, 533), (31, 433), (42, 375), (72, 625), (10, 734), (81, 923), (87, 135), (60, 866), (53, 995), (32, 346), (18, 436), (71, 478), (76, 280), (61, 684), (60, 74), (23, 716), (89, 444), (67, 162), (6, 834), (98, 613), (28, 24), (81, 474), (46, 238), (16, 718), (65, 725), (37, 460), (54, 613), (51, 883), (4, 215), (36, 51), (13, 140), (98, 246), (20, 227), (21, 436), (28, 166), (100, 41), (56, 22), (76, 896), (12, 77), (79, 22), (3, 117), (70, 259), (31, 778), (25, 276), (53, 82), (70, 283), (3, 191), (98, 420), (98, 727), (83, 911), (35, 846), (38, 443), (25, 416), (56, 644), (70, 906), (81, 76), (18, 459), (17, 713), (3, 701), (7, 377), (11, 483), (80, 83), (19, 386), (64, 563), (43, 13), (42, 717), (2, 585), (88, 86), (48, 694), (11, 1000), (56, 11), (72, 568), (69, 712), (62, 351), (16, 768), (73, 215), (4, 606), (47, 70), (57, 237), (44, 190), (73, 552), (59, 91), (49, 784), (26, 567), (48, 836), (92, 431), (89, 611), (76, 68), (68, 756), (14, 206), (7, 460), (97, 32), (78, 804), (99, 726), (98, 94), (90, 90), (40, 445), (6, 617), (4, 578), (2, 559), (7, 205), (19, 193), (39, 983), (16, 427), (22, 767), (87, 668), (29, 416), (96, 581), (81, 857), (35, 647), (48, 884), (67, 802), (59, 348), (55, 684), (17, 556), (3, 334), (41, 701), (73, 364), (48, 610), (20, 105), (88, 145), (88, 115), (62, 921), (74, 633), (55, 150), (2, 473), (15, 699), (58, 472), (79, 590), (72, 62), (20, 741), (97, 560), (11, 139), (49, 419), (85, 591), (70, 914), (95, 496), (53, 291), (41, 334), (7, 888), (8, 198), (24, 1000), (18, 342), (64, 134), (11, 652), (85, 375), (23, 713), (47, 244), (75, 94), (82, 272), (15, 169), (16, 908), (19, 191), (5, 32), (49, 712), (38, 364), (30, 489), (12, 1000), (45, 872), (88, 940), (68, 844), (83, 386), (67, 428), (83, 48), (98, 720), (67, 618), (57, 541), (76, 171), (36, 539), (38, 674), (51, 63), (86, 831), (61, 4), (56, 319), (27, 951), (65, 149), (90, 753), (12, 624), (52, 375), (69, 619), (55, 998), (32, 141), (38, 527), (23, 686), (45, 628), (35, 242), (35, 801), (21, 720), (91, 439), (50, 703), (19, 480), (35, 307), (70, 570), (42, 61), (70, 954), (38, 506), (48, 847), (65, 48), (88, 610), (27, 154), (96, 18), (20, 145), (76, 19), (72, 179), (16, 206), (16, 327), (88, 396), (88, 827), (43, 735), (74, 825), (61, 256), (60, 587), (39, 357), (18, 799), (47, 75), (60, 885), (32, 904), (3, 612), (54, 940), (97, 217), (99, 141), (3, 900), (31, 301), (83, 267), (44, 857), (37, 262), (60, 643), (96, 502), (74, 320), (40, 710), (10, 4), (65, 729), (52, 393), (9, 241), (46, 162), (31, 191), (34, 912), (87, 504), (28, 971), (93, 541), (98, 149), (83, 331), (2, 192), (81, 811), (100, 217), (72, 998), (9, 585), (37, 147), (25, 697), (96, 73), (36, 332), (97, 514), (36, 457), (23, 930), (20, 30), (92, 762), (3, 961), (47, 15), (66, 620), (77, 807), (45, 318), (13, 64), (10, 777), (16, 875), (79, 237), (87, 660), (36, 47), (42, 739), (40, 716), (6, 953), (72, 616), (100, 55), (52, 686), (98, 535), (44, 35), (70, 59), (82, 238), (36, 174), (98, 172), (80, 468), (12, 97), (84, 347), (94, 272), (95, 437), (28, 508), (85, 232), (36, 486), (54, 31), (16, 470), (42, 272), (69, 678), (95, 606), (93, 254), (27, 837), (93, 954), (92, 908), (53, 963), (5, 610), (49, 725), (63, 658), (29, 451), (9, 961), (25, 737), (100, 792), (38, 770), (48, 602), (20, 668), (5, 708), (63, 365), (47, 984), (26, 737), (7, 811), (17, 77), (62, 920), (64, 513), (100, 61), (67, 35), (11, 153), (1, 201), (9, 521), (26, 655), (43, 747), (36, 17), (13, 882), (30, 509), (55, 401), (87, 388), (98, 294), (58, 609), (84, 239), (19, 32), (42, 453), (93, 619), (57, 576), (91, 580), (26, 585), (72, 704), (53, 601), (8, 18), (52, 573), (57, 866), (59, 464), (89, 996), (67, 13), (60, 430), (56, 512), (47, 213), (18, 505), (79, 623), (97, 499), (34, 362), (42, 449), (82, 391), (96, 773), (2, 74), (18, 785), (62, 558), (29, 765), (6, 109), (67, 722), (46, 855), (28, 560), (62, 205), (80, 200), (98, 659), (6, 846), (33, 622), (24, 510), (15, 446), (67, 988), (34, 953), (79, 395), (14, 492), (89, 245), (55, 45), (26, 926), (17, 251), (84, 384), (3, 802), (85, 574), (29, 741), (55, 458), (58, 403), (43, 324), (29, 19), (94, 677), (16, 721), (21, 70), (78, 927), (1, 485), (75, 467), (21, 603), (49, 201), (15, 927), (85, 862), (90, 783), (89, 927), (6, 185), (24, 409), (17, 861), (9, 603), (80, 227), (89, 953), (51, 342), (30, 228), (32, 605), (69, 907), (24, 186), (74, 637), (91, 996), (3, 672), (15, 119), (3, 251), (45, 638), (39, 935), (40, 839), (98, 145), (83, 607), (20, 749), (33, 525), (40, 751), (53, 70), (33, 117), (52, 111), (65, 265), (72, 756), (12, 68), (96, 873), (14, 551), (64, 276), (96, 532), (16, 13), (80, 786), (57, 798), (99, 928), (16, 719), (11, 394), (79, 466), (32, 510), (55, 682), (64, 138), (80, 384), (2, 950), (36, 757), (62, 30), (7, 118), (56, 180), (1, 168), (47, 814), (70, 491), (71, 203), (92, 846), (87, 598), (19, 235), (40, 338), (90, 456), (7, 118), (43, 16), (98, 982), (78, 864), (27, 285), (20, 334), (12, 732), (70, 941), (96, 235), (99, 395), (41, 374), (92, 984), (56, 615), (90, 619), (22, 147), (54, 385), (8, 426), (81, 992), (57, 751), (28, 535), (83, 541), (99, 444), (69, 184), (58, 848), (1, 582), (46, 563), (87, 424), (56, 180), (40, 503), (69, 132), (8, 1), (18, 461), (88, 915), (49, 872), (66, 823), (77, 277), (50, 332), (19, 598), (70, 307), (2, 174), (89, 143), (82, 154), (33, 593), (25, 702), (1, 382), (77, 101), (93, 619), (86, 187), (24, 523), (1, 722), (46, 157), (95, 777), (74, 965), (89, 274), (29, 232), (72, 473), (30, 423), (91, 126), (46, 127), (87, 802), (27, 484), (14, 757), (67, 625), (22, 434), (50, 217), (91, 660), (59, 789), (82, 200), (25, 643), (61, 273), (74, 825), (66, 376), (35, 707), (69, 588), (67, 271), (55, 598), (49, 34), (83, 3), (19, 793), (3, 740), (55, 558), (11, 585), (32, 746), (27, 949), (67, 111), (19, 867), (82, 623), (34, 726), (85, 790), (16, 201), (59, 703), (18, 549), (55, 293), (48, 154), (76, 458), (92, 975), (45, 327), (85, 622), (98, 135), (61, 402), (74, 261), (39, 362), (96, 814), (16, 223), (57, 485), (10, 965), (17, 132), (28, 301), (4, 133), (8, 491), (9, 238), (38, 986), (45, 399), (24, 550), (3, 318), (13, 539), (77, 438), (43, 446), (35, 704), (62, 577), (83, 48), (64, 500), (91, 984), (30, 125), (8, 365), (37, 512), (41, 508), (65, 134), (84, 893), (8, 838), (40, 805), (20, 949), (86, 964), (64, 831), (99, 315), (94, 644), (12, 685), (89, 408), (30, 32), (83, 638), (13, 842), (47, 691), (89, 996), (11, 751), (77, 156), (36, 799), (57, 754), (4, 638), (46, 434), (90, 526), (25, 881), (53, 521), (19, 880), (87, 142), (16, 17), (6, 453), (7, 344), (40, 508), (81, 115), (80, 368), (58, 130), (51, 785), (57, 400), (13, 650), (68, 461), (40, 886), (74, 429), (65, 698), (2, 482), (12, 632), (38, 798), (72, 855), (45, 389), (15, 525), (87, 53), (29, 506), (57, 153), (23, 731), (100, 872), (95, 204), (100, 1000), (64, 178), (68, 176), (3, 485), (13, 889), (2, 373), (65, 185), (92, 767), (51, 458), (53, 615), (75, 687), (21, 720), (70, 62), (41, 40), (51, 103), (61, 562), (19, 701), (15, 500), (42, 310), (10, 53), (70, 443), (86, 885), (34, 854), (30, 850), (67, 424), (24, 34), (56, 465), (53, 421), (31, 216), (11, 475), (11, 589), (8, 27), (36, 961), (61, 920), (49, 670), (71, 397), (33, 109), (62, 341), (54, 108), (17, 786), (78, 539), (63, 659), (32, 933), (18, 893), (23, 304), (64, 523), (23, 25), (64, 297), (13, 895), (23, 509), (15, 318), (51, 981), (4, 102), (24, 621), (34, 853), (97, 673), (12, 671), (78, 472), (5, 971), (31, 991), (72, 116), (54, 539), (78, 329), (88, 485), (100, 626), (8, 115), (78, 543), (56, 988), (89, 208), (21, 443), (100, 93), (67, 683), (27, 362), (55, 664), (56, 322), (44, 516), (2, 34), (32, 739), (6, 348), (5, 51), (72, 179), (100, 491), (18, 556), (65, 403), (15, 934), (67, 557), (72, 190), (35, 64), (78, 916), (52, 725), (75, 474), (55, 51), (6, 600), (69, 36), (99, 989), (7, 101), (43, 714), (36, 4), (71, 80), (68, 429), (28, 223), (67, 268), (48, 44), (60, 733), (97, 823), (76, 230), (70, 757), (2, 336), (8, 728), (35, 677), (91, 135), (51, 873), (72, 925), (4, 81), (90, 176), (36, 859), (45, 766), (27, 850), (23, 440), (78, 598), (5, 477), (80, 150), (70, 95), (72, 1), (67, 533), (12, 524), (77, 789), (6, 916), (73, 529), (68, 748), (7, 520), (38, 21), (15, 489), (79, 212), (18, 456), (30, 274), (25, 2), (99, 311), (62, 633), (40, 363), (89, 338), (2, 317), (48, 110), (85, 786), (69, 886), (80, 880), (44, 630), (87, 983), (74, 401), (45, 353), (38, 507), (98, 245), (56, 307), (64, 493), (66, 457), (4, 757), (91, 375), (20, 229), (52, 829), (11, 10), (27, 704), (72, 9), (21, 424), (29, 367), (39, 152), (70, 230), (86, 237), (52, 894), (44, 765), (35, 727), (51, 103), (62, 205), (98, 316), (17, 647), (25, 214), (10, 222), (23, 112), (19, 303), (100, 526), (41, 145), (26, 14), (52, 734), (16, 913), (33, 886), (74, 213), (87, 260), (21, 177), (4, 285), (57, 234), (32, 193), (72, 371), (5, 435), (73, 447), (1, 231), (52, 700), (15, 514), (61, 825), (84, 375), (70, 909), (13, 757), (35, 384), (20, 214), (73, 683), (71, 20), (85, 115), (13, 613), (8, 343), (30, 369), (41, 306), (61, 678), (14, 208), (74, 106), (96, 123), (99, 461), (24, 294), (85, 179), (66, 832), (6, 819), (98, 857), (65, 296), (16, 175), (3, 7), (47, 388), (16, 502), (39, 963), (48, 885), (53, 274), (1, 287), (79, 400), (77, 794), (32, 114), (85, 803), (81, 127), (45, 973), (8, 830), (29, 93), (5, 279), (65, 418), (35, 383), (32, 620), (63, 907), (26, 413), (22, 362), (35, 137), (60, 516), (95, 452), (91, 712), (83, 45), (16, 83), (59, 640), (81, 264), (100, 536), (32, 132), (1, 54), (26, 653), (89, 602), (11, 434), (90, 906), (75, 840), (47, 862), (9, 149), (73, 241), (35, 799), (14, 990), (45, 475), (62, 127), (73, 475), (96, 152), (69, 402), (86, 361), (63, 339), (73, 134), (20, 437), (100, 448), (39, 518), (94, 578), (9, 553), (88, 334), (77, 4), (40, 154), (41, 655), (60, 453), (64, 334), (4, 767), (56, 185), (11, 315), (19, 579), (41, 933), (12, 567), (75, 692), (25, 89), (88, 2), (44, 149), (41, 787), (3, 902), (62, 472), (93, 14), (37, 750), (80, 285), (48, 619), (88, 62), (96, 937), (26, 32), (4, 474), (41, 887), (14, 754), (2, 949), (96, 795), (86, 677), (33, 69), (86, 329), (59, 650), (28, 972), (44, 544), (66, 5), (47, 533), (7, 981), (20, 88), (21, 397), (31, 909), (14, 683), (72, 554), (88, 435), (68, 422), (27, 470), (66, 191), (20, 540), (86, 843), (1, 196), (37, 352), (2, 8)]
            Check.equal('tovor_novi_predmet([(2,3), (4,4), (5,4), (3,2), (1,2), (15, 12)], 20,[(4,4), (12,11), (2,3), (17, 5), (18,8), (5,6), (7,6), (6,6)])', 35)
            Check.equal('tovor_novi_predmet(predmeti, 100000,novi_predmeti)', 1525, env = {"predmeti":predmeti, "novi_predmeti":novi_predmeti})
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    print("Shranjujem rešitve na strežnik... ", end="")
    try:
        url = "https://www.projekt-tomo.si/api/attempts/submit/"
        token = "Token 44eadea4e0e5d4cdc9316392da42a5fbb9fcc070"
        response = submit_parts(Check.parts, url, token)
    except urllib.error.URLError:
        message = (
            "\n"
            "-------------------------------------------------------------------\n"
            "PRI SHRANJEVANJU JE PRIŠLO DO NAPAKE!\n"
            "Preberite napako in poskusite znova ali se posvetujte z asistentom.\n"
            "-------------------------------------------------------------------\n"
        )
        print(message)
        traceback.print_exc()
        print(message)
        sys.exit(1)
    else:
        print("Rešitve so shranjene.")
        update_attempts(Check.parts, response)
        if "update" in response:
            print("Updating file... ", end="")
            backup_filename = backup(filename)
            with open(__file__, "w", encoding="utf-8") as f:
                f.write(response["update"])
            print("Previous file has been renamed to {0}.".format(backup_filename))
            print("If the file did not refresh in your editor, close and reopen it.")
    Check.summarize()


if __name__ == "__main__":
    _validate_current_file()
