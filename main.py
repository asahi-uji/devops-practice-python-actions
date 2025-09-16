import sys
import logging
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox

# ---------- ログ設定 ----------
def get_app_dir() -> Path:
    # PyInstaller後は exe のフォルダ、通常はこのファイルのフォルダ
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path(__file__).parent

def setup_logging() -> Path:
    app_dir = get_app_dir()
    log_dir = app_dir / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "app.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),  # デバッグ用
        ],
    )
    logging.info("=== app start ===")
    return log_file

# ---------- 業務ロジック（テスト対象） ----------
def compute_sum(a: int, b: int) -> int:
    return int(a) + int(b)

# ---------- GUI本体 ----------
def start_app() -> int:
    log_file = setup_logging()
    logging.info(f"log file: {log_file}")

    root = tk.Tk()
    root.title("DevOps GUI Practice")

    frm = ttk.Frame(root, padding=12)
    frm.grid(sticky="nsew")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    ttk.Label(frm, text="A:").grid(row=0, column=0, sticky="e", padx=4, pady=4)
    ent_a = ttk.Entry(frm, width=12)
    ent_a.insert(0, "2")
    ent_a.grid(row=0, column=1, sticky="w", padx=4, pady=4)

    ttk.Label(frm, text="B:").grid(row=1, column=0, sticky="e", padx=4, pady=4)
    ent_b = ttk.Entry(frm, width=12)
    ent_b.insert(0, "3")
    ent_b.grid(row=1, column=1, sticky="w", padx=4, pady=4)

    result_var = tk.StringVar(value="sum = (未計算)")
    lbl_result = ttk.Label(frm, textvariable=result_var)
    lbl_result.grid(row=2, column=0, columnspan=2, sticky="w", padx=4, pady=8)

    def on_calc():
        try:
            a = int(ent_a.get())
            b = int(ent_b.get())
            s = compute_sum(a, b)
            result_var.set(f"sum = {s}")
            logging.info(f"calc: a={a}, b={b}, sum={s}")
        except Exception as e:
            logging.exception(f"calc error: {e}")
            messagebox.showerror("Error", f"入力が不正です: {e}")

    btn = ttk.Button(frm, text="計算", command=on_calc)
    btn.grid(row=3, column=0, columnspan=2, sticky="ew", padx=4, pady=8)

    # 初回起動メッセージ（GUI確認用）
    root.after(100, lambda: messagebox.showinfo("起動", "アプリを起動しました"))
    try:
        root.mainloop()
        logging.info("=== app exit ===")
        return 0
    except Exception as e:
        logging.exception(f"unhandled: {e}")
        messagebox.showerror("Error", f"異常終了: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(start_app())
