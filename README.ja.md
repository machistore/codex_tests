# Codex Tests

[English version](./README.md)

このリポジトリには Codex をテストするためのサンプルスクリプトが含まれています。

## 含まれているスクリプト

- `export_classes_csv.py` - Vectorworks のクラス設定を `class_settings.csv` という CSV ファイルにエクスポートします。スクリプトは線色や塗り色、不透明度、テキストスタイルの使用、マーカー情報、ベクターフィルのパターンなど多くの属性を収集します。最近の更新では `use_text_style`, `beginning_marker`, `end_marker`, `by_style`, `opacity_n`, `vector_fill`, `drop_shadow_enabled` のほか、`class_options`, `drop_shadow_data`, `line_style_n`, `text_style_ref` の各フィールドが追加されました。
  - `drop_shadow_data`: `(x, y, blur, opacity, ...)` を文字列化して出力します。
  - `drop_shadow_enabled` フィールドは `GetCLDropShadowEnabled` API を使用します。

## テスト

`tests` ディレクトリには pytest スイートが含まれています。`tests/test_export_classes_csv.py` は `export_classes_csv.py` が期待通りの CSV を作成することを確認し、Vectorworks API をテスト用にスタブ化する方法を示しています。
