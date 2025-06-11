# Codex Tests

[English version](./README.md)

このリポジトリには Codex をテストするためのサンプルスクリプトが含まれています。

## 含まれているスクリプト

- export_classes_csv.py - Vectorworks のクラス設定を `class_settings.csv` という CSV ファイルにエクスポートします。スクリプトは線色や塗り色、不透明度、テキストスタイルの使用、マーカー情報、ベクターフィルのパターンなど多くの属性を収集します。最近の更新では `use_text_style`, `beginning_marker`, `end_marker`, `by_style`, `opacity_n`, `vector_fill`, `drop_shadow_enabled` のほか、`class_options`, `drop_shadow_data`, `line_style_n`, `text_style_ref` の各フィールドが追加されました。
  - drop_shadow_data: `(1, 2, 3, 4, 5, 6, 7, 8)` のような形式で文字列としてCSVに出力されます。
    - 値が None の場合は ""（空文字列）になります。
  - drop_shadow_enabled フィールドは `GetCLDropShadowEnabled` API を使用します。

## スクリプトの実行方法

Vectorworks を起動し、**ツール → プラグイン → Python スクリプトを実行...** を選んで `export_classes_csv.py` を実行するとクラス設定をエクスポートできます。スクリプトは `class_settings.csv` をデスクトップに保存します。

README 内の項目一覧を再生成するには次のコマンドを実行します。

```bash
python scripts/generate_fields_md.py
```

### 取得できるクラス設定項目

スクリプトが各クラスについて出力するフィールドは次のとおりです。

<!--FIELDS-->
- `beginning_marker`
- `by_style`
- `class_options`
- `drop_shadow_data`
- `drop_shadow_enabled`
- `end_marker`
- `fill_color`
- `fill_color_back`
- `fill_color_fore`
- `fill_opacity`
- `fill_style`
- `line_color`
- `line_color_back`
- `line_color_fore`
- `line_marker`
- `line_opacity`
- `line_style`
- `line_style_n`
- `line_thickness`
- `line_weight`
- `name`
- `opacity_n`
- `shadow_angle`
- `shadow_blur`
- `shadow_color`
- `shadow_offset_x`
- `shadow_offset_y`
- `shadow_opacity`
- `sync_line_opacity`
- `text_style`
- `text_style_ref`
- `use_drop_shadow`
- `use_graphic`
- `use_text_attrs`
- `use_text_style`
- `vector_fill`
- `visibility`
<!--/FIELDS-->

## テスト

`tests` ディレクトリには pytest スイートが含まれています。`tests/test_export_classes_csv.py` は `export_classes_csv.py` が期待通りの CSV を作成することを確認し、Vectorworks API をテスト用にスタブ化する方法を示しています。
