def ActiveClass():
    '''https://developer.vectorworks.net/index.php?title=VS:ActiveClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:ActiveClass/ja
    \nアクティブなクラスの名前を返します。'''
    return STRING

def GetClLW(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClLW
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClLW/ja
    \nクラスに設定されている線の太さを返します。'''
    return INTEGER

def LSByClass():
    '''https://developer.vectorworks.net/index.php?title=VS:LSByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:LSByClass/ja
    \nデフォルトの線の種類として、アクティブなクラスの線の種類を使います。'''
    return None

def SetClLW(className, LW):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClLW
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClLW/ja
    \nクラスの線の太さを設定します。'''
    return None

def CLDropShadowEnabled(className):
    '''https://developer.vectorworks.net/index.php?title=VS:CLDropShadowEnabled
    \nhttps://developer.vectorworks.net/index.php?title=VS:CLDropShadowEnabled/ja'''
    return BOOLEAN

def GetClOpacity(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClOpacity
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClOpacity/ja
    \n指定したクラスの不透明度を返します。'''
    return INTEGER

def LWByClass():
    '''https://developer.vectorworks.net/index.php?title=VS:LWByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:LWByClass/ja
    \nデフォルトの線の太さとして、アクティブなクラスの線の太さを使います。'''
    return None

def SetClOpacity(className, opacity):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClOpacity
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClOpacity/ja
    \n指定したクラスの不透明度を設定します。'''
    return None

def ClassList(index):
    '''https://developer.vectorworks.net/index.php?title=VS:ClassList
    \nhttps://developer.vectorworks.net/index.php?title=VS:ClassList/ja
    \n指定した索引番号をもつクラスの名前を返します。例えば、索引番号を4とすると4番目のクラスの名前を返します。'''
    return STRING

def GetClOpacityN(strClassName):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClOpacityN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClOpacityN/ja'''
    return (outFillOpacity, outPenOpacity)

def MarkerByClass():
    '''https://developer.vectorworks.net/index.php?title=VS:MarkerByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:MarkerByClass/ja
    \nデフォルトのマーカの種類として、アクティブなクラスのマーカの種類を使います。'''
    return None

def SetClPenBack(className, r,g,b):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClPenBack
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClPenBack/ja
    \nクラスの線の地色を設定します。色は赤、緑、青の成分で指定します。値の範囲は0から65535までです。'''
    return None

def ClassNum():
    '''https://developer.vectorworks.net/index.php?title=VS:ClassNum
    \nhttps://developer.vectorworks.net/index.php?title=VS:ClassNum/ja
    \nアクティブなドキュメント内のクラスの数を返します。'''
    return LONGINT

def GetClPenBack(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClPenBack
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClPenBack/ja
    \nクラスに設定されている線の地色の成分を返します。色は赤、緑、青の成分として返されます。値の範囲は0から65535までです。'''
    return (colorRV, colorGV, colorBV)

def NameClass(className):
    '''https://developer.vectorworks.net/index.php?title=VS:NameClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:NameClass/ja
    \n新しいクラスを指定した名前で作成し、アクティブにします。'''
    return None

def SetClPenFore(className, r,g,b):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClPenFore
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClPenFore/ja
    \nクラスの線の色を設定します。色は赤、緑、青の成分で指定します。値の範囲は0から65535までです。'''
    return None

def DelClass(className):
    '''https://developer.vectorworks.net/index.php?title=VS:DelClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:DelClass/ja
    \nアクティブなドキュメントから指定した名前のクラスを削除します。削除するクラスにある図形は「一般」クラスに割り当てられます。'''
    return None

def GetClPenFore(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClPenFore
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClPenFore/ja
    \nクラスに設定されている線の色成分を返します。色は赤、緑、青の成分として返されます。値の範囲は0から65535までです。'''
    return (colorRV, colorGV, colorBV)

def OpacityByClass():
    '''https://developer.vectorworks.net/index.php?title=VS:OpacityByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:OpacityByClass/ja
    \nアクティブクラスの不透明度にファイルのデフォルト設定を使用します。'''
    return None

def SetClTextStyleRef(className, textStyleRef):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClTextStyleRef
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClTextStyleRef/ja
    \n指定したクラスの文字スタイルを設定します。  textStyleRefに文字スタイルのインデックスを指定します。'''
    return None

def EnableCLDropShadow(className, enable):
    '''https://developer.vectorworks.net/index.php?title=VS:EnableCLDropShadow
    \nhttps://developer.vectorworks.net/index.php?title=VS:EnableCLDropShadow/ja'''
    return None

def GetClTextStyleRef(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClTextStyleRef
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClTextStyleRef/ja
    \n指定したクラスの文字スタイルのインデックスを返します。'''
    return LONGINT

def OpacityByClassN(fillOpacityByClass, penOpacityByClass):
    '''https://developer.vectorworks.net/index.php?title=VS:OpacityByClassN
    \nhttps://developer.vectorworks.net/index.php?title=VS:OpacityByClassN/ja'''
    return None

def SetClUseGraphic(className, use):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClUseGraphic
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClUseGraphic/ja
    \nクラスのグラフィック属性を設定します。'''
    return None

def FPatByClass():
    '''https://developer.vectorworks.net/index.php?title=VS:FPatByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:FPatByClass/ja
    \nデフォルトの面の模様として、アクティブなクラスの面の模様を使います。'''
    return None

def GetClUseGraphic(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClUseGraphic
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClUseGraphic/ja
    \nクラスに設定されているグラフィック属性が有効か無効かを返します。'''
    return BOOLEAN

def PenColorByClass():
    '''https://developer.vectorworks.net/index.php?title=VS:PenColorByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:PenColorByClass/ja
    \nデフォルトの線の色として、アクティブなクラスの線の色を使います。'''
    return None

def SetClUseTextStyle(className, use):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClUseTextStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClUseTextStyle/ja
    \n指定したクラスの文字スタイルの使用の有無を設定します。'''
    return None

def FillColorByClass():
    '''https://developer.vectorworks.net/index.php?title=VS:FillColorByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:FillColorByClass/ja
    \nデフォルトの面の色として、アクティブなクラスの面の色を使います。'''
    return None

def GetClUseTextStyle(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClUseTextStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClUseTextStyle/ja
    \n指定したクラスの文字スタイルの使用の有無を返します。'''
    return BOOLEAN

def RenameClass(className, newName):
    '''https://developer.vectorworks.net/index.php?title=VS:RenameClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:RenameClass/ja
    \nクラスの名前を変更します。'''
    return None

def SetClUseTexture(className, use):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClUseTexture
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClUseTexture/ja
    \nクラスのテクスチャ使用の有無を設定します。'''
    return None

def GetCLDrpShadowData(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCLDrpShadowData
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCLDrpShadowData/ja'''
    return (nUnits, dOffset, dBlurRadius, dAngle, nOpacity, colorRV, colorGV, colorBV)

def GetClVectorFill(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClVectorFill
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClVectorFill/ja
    \nクラスに設定されているハッチングの名前を返します。'''
    return (BOOLEAN, hatchName)

def SetCLDrpShadowData(className, nUnits, dOffset, dBlurRadius, dAngle, nOpacity, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCLDrpShadowData
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCLDrpShadowData/ja'''
    return None

def SetClVectorFill(className, hatchName):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClVectorFill
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClVectorFill/ja
    \nクラスのハッチングを設定します。'''
    return BOOLEAN

def GetCVis(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCVis
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCVis/ja
    \nクラスの表示状態を返します。'''
    return INTEGER

def GetClassArrow(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClassArrow
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClassArrow/ja
    \nクラスに設定されているマーカスタイル、長さ（インチ）、角度（度数）を返します。'''
    return (style, size, angle)

def SetCLOpacityN(className, penOpacity, fillOpacity):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCLOpacityN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCLOpacityN/ja'''
    return None

def SetClassArrow(className, style, size, angle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClassArrow
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClassArrow/ja
    \nクラスのマーカを設定します。'''
    return None

def GetClFPat(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClFPat
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClFPat/ja
    \nクラスに設定されている面の模様を返します。'''
    return LONGINT

def GetClassBeginningMarker(name):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClassBeginningMarker
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClassBeginningMarker/ja
    \n指定したクラスの始点マーカのすべての設定値を返します。正常終了するとTRUEが返されます。'''
    return (BOOLEAN, style, angle, size, width, thicknessBasis, thickness)

def SetClFPat(className, fillpattern):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClFPat
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClFPat/ja
    \nクラスの面の模様を設定します。'''
    return None

def SetClassBeginningMarker(name, style, angle, size, width, thicknessBasis, thickness):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClassBeginningMarker
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClassBeginningMarker/ja
    \n指定したクラスの始点マーカのすべての設定値を設定します。正常終了するとTRUEが返されます。'''
    return BOOLEAN

def GetClFillBack(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClFillBack
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClFillBack/ja
    \nクラスに設定されている面の地色の成分を返します。色は赤、緑、青の成分として返されます。値の範囲は0から65535までです。'''
    return (colorRV, colorGV, colorBV)

def GetClassEndMarker(name):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClassEndMarker
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClassEndMarker/ja
    \n指定したクラスの終点マーカのすべての設定値を返します。正常終了するとTRUEが返されます。'''
    return (BOOLEAN, style, angle, size, width, thicknessBasis, thickness)

def SetClFillBack(className, r,g,b):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClFillBack
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClFillBack/ja
    \nクラスの面の地色を設定します。色は赤、緑、青の成分で指定します。値の範囲は0から65535までです。'''
    return None

def SetClassEndMarker(name, style, angle, size, width, thicknessBasis, thickness):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClassEndMarker
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClassEndMarker/ja
    \n指定したクラスの終点マーカのすべての設定値を設定します。正常終了するとTRUEが返されます。'''
    return BOOLEAN

def GetClFillFore(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClFillFore
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClFillFore/ja
    \nクラスに設定されている面の色成分を返します。色は赤、緑、青の成分として返されます。値の範囲は0から65535までです。'''
    return (colorRV, colorGV, colorBV)

def GetClassOptions():
    '''https://developer.vectorworks.net/index.php?title=VS:GetClassOptions
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClassOptions/ja
    \nアクティブなドキュメントの、他のクラスの表示方法を値で返します。'''
    return INTEGER

def SetClFillFore(className, r,g,b):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClFillFore
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClFillFore/ja
    \nクラスの面の色を設定します。色は赤、緑、青の成分で指定します。値の範囲は0から65535までです。'''
    return None

def SetClassOptions(classOpts):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClassOptions
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClassOptions/ja
    \n他のクラスの表示状態を設定します。'''
    return None

def GetClLS(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClLS
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClLS/ja
    \nクラスに設定されている線の種類を返します。'''
    return INTEGER

def GrayClass(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GrayClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:GrayClass/ja
    \n指定したクラスをグレイ表示にします。'''
    return None

def SetClLS(className, LS):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClLS
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClLS/ja
    \nクラスの線の種類を設定します。'''
    return None

def ShowClass(className):
    '''https://developer.vectorworks.net/index.php?title=VS:ShowClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:ShowClass/ja
    \n指定したクラスを表示します。'''
    return None

def GetClLSN(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClLSN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClLSN/ja
    \nクラスに設定されている線の種類を返します。'''
    return LONGINT

def HideClass(className):
    '''https://developer.vectorworks.net/index.php?title=VS:HideClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:HideClass/ja
    \n指定したクラスを隠します。'''
    return None

def SetClLSN(className, lineStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClLSN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClLSN/ja
    \nクラスの線の種類を設定します。'''
    return None

def RunColorPaletteMgr():
    '''https://developer.vectorworks.net/index.php?title=VS:RunColorPaletteMgr
    \nhttps://developer.vectorworks.net/index.php?title=VS:RunColorPaletteMgr/ja
    \nカラーパレットマネージャーを表示します'''
    return BOOLEAN

def RunNewColorPalette():
    '''https://developer.vectorworks.net/index.php?title=VS:RunNewColorPalette
    \nhttps://developer.vectorworks.net/index.php?title=VS:RunNewColorPalette/ja
    \n新規のカラーパレットダイアログを表示します。'''
    return STRING

def RunPickClrFromPal():
    '''https://developer.vectorworks.net/index.php?title=VS:RunPickClrFromPal
    \nhttps://developer.vectorworks.net/index.php?title=VS:RunPickClrFromPal/ja
    \nカラーパレットから色を取得します。'''
    return (BOOLEAN, filename, index)

def Absolute():
    '''https://developer.vectorworks.net/index.php?title=VS:Absolute
    \nhttps://developer.vectorworks.net/index.php?title=VS:Absolute/ja
    \n座標指定を絶対指定にします。'''
    return None

def DoMenuTextByName(subMenu, index):
    '''https://developer.vectorworks.net/index.php?title=VS:DoMenuTextByName
    \nhttps://developer.vectorworks.net/index.php?title=VS:DoMenuTextByName/ja
    \nVectorWorksのメニューコマンドを実行します。'''
    return None

def OpenPDFDocument(inFilenameStr):
    '''https://developer.vectorworks.net/index.php?title=VS:OpenPDFDocument
    \nhttps://developer.vectorworks.net/index.php?title=VS:OpenPDFDocument/ja
    \nPDFドキュメントへの取り出しを開始します。この関数を使用する前にAcquireExportPDFSettingsAndLocationを使用する必要があります。これは、PDFの一括取り出しに対応するための操作です。'''
    return BOOLEAN

def PushAttrs():
    '''https://developer.vectorworks.net/index.php?title=VS:PushAttrs
    \nhttps://developer.vectorworks.net/index.php?title=VS:PushAttrs/ja
    \n現在の属性の設定を記憶します。'''
    return None

def AcquireExportPDFSettingsAndLocation(inbSeparateDocuments):
    '''https://developer.vectorworks.net/index.php?title=VS:AcquireExportPDFSettingsAndLocation
    \nhttps://developer.vectorworks.net/index.php?title=VS:AcquireExportPDFSettingsAndLocation/ja
    \n「PDF取り出し」の設定ダイアログとPDFファイル名（パラメータをTRUEにした場合は保存先のフォルダ名）を設定するダイアログを表示します。PDFの一括取り出しに対応します。'''
    return BOOLEAN

def ExportPDFPages(savedViewNameStr):
    '''https://developer.vectorworks.net/index.php?title=VS:ExportPDFPages
    \nhttps://developer.vectorworks.net/index.php?title=VS:ExportPDFPages/ja
    \n現在のドキュメントがPDFとして取り出されます。この関数を使用する前にOpenPDFDocumentを使用する必要があります。これは、PDFの一括取り出しに対応するための操作です。'''
    return INTEGER

def PenLoc():
    '''https://developer.vectorworks.net/index.php?title=VS:PenLoc
    \nhttps://developer.vectorworks.net/index.php?title=VS:PenLoc/ja
    \n現在のペンの座標位置を返します。'''
    return p

def Relative():
    '''https://developer.vectorworks.net/index.php?title=VS:Relative
    \nhttps://developer.vectorworks.net/index.php?title=VS:Relative/ja
    \n座標指定を相対指定にします。'''
    return None

def AngleVar():
    '''https://developer.vectorworks.net/index.php?title=VS:AngleVar
    \nhttps://developer.vectorworks.net/index.php?title=VS:AngleVar/ja
    \n変数を極座標として角度指定に使用することを宣言します。'''
    return None

def Move(move):
    '''https://developer.vectorworks.net/index.php?title=VS:Move
    \nhttps://developer.vectorworks.net/index.php?title=VS:Move/ja
    \n現在のペン位置を相対的に移動します。'''
    return None

def PopAttrs():
    '''https://developer.vectorworks.net/index.php?title=VS:PopAttrs
    \nhttps://developer.vectorworks.net/index.php?title=VS:PopAttrs/ja
    \n記憶されている属性を現在の設定にします。'''
    return None

def Run(p):
    '''https://developer.vectorworks.net/index.php?title=VS:Run
    \nhttps://developer.vectorworks.net/index.php?title=VS:Run/ja
    \nVectorScript プログラムを実行します。'''
    return None

def ClosePDFDocument():
    '''https://developer.vectorworks.net/index.php?title=VS:ClosePDFDocument
    \nhttps://developer.vectorworks.net/index.php?title=VS:ClosePDFDocument/ja
    \nOpenPDFDocumentで開始されたPDFドキュメントの作成プロセスが完了します。これは、PDFの一括取り出しに対応するための操作です。'''
    return None

def MoveTo(p):
    '''https://developer.vectorworks.net/index.php?title=VS:MoveTo
    \nhttps://developer.vectorworks.net/index.php?title=VS:MoveTo/ja
    \nペン位置を絶対座標の位置に移動します。'''
    return None

def PrintUsingPrintDialog():
    '''https://developer.vectorworks.net/index.php?title=VS:PrintUsingPrintDialog
    \nhttps://developer.vectorworks.net/index.php?title=VS:PrintUsingPrintDialog/ja
    \nアクティブなドキュメントをプリントします。プリントダイアログが表示されます。用紙設定が正しくない場合は、プリントダイアログの前に用紙設定ダイアログが表示されます。'''
    return INTEGER

def SetTool(theTool):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTool
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTool/ja
    \nツールパレットからツールを選択します。ツールが使われた後も、そのツールを選択したままにします。'''
    return None

def DoMenuText(menuItem):
    '''https://developer.vectorworks.net/index.php?title=VS:DoMenuText
    \nhttps://developer.vectorworks.net/index.php?title=VS:DoMenuText/ja
    \n指定した名前のメニューを実行します。ワークシートのメニューを実行する場合は、頭に「WS」を付けます（「WS」は半角英字）。'''
    return None

def NoAngleVar():
    '''https://developer.vectorworks.net/index.php?title=VS:NoAngleVar
    \nhttps://developer.vectorworks.net/index.php?title=VS:NoAngleVar/ja
    \nAngleVarの宣言を解除します。'''
    return None

def PrintWithoutUsingPrintDialog():
    '''https://developer.vectorworks.net/index.php?title=VS:PrintWithoutUsingPrintDialog
    \nhttps://developer.vectorworks.net/index.php?title=VS:PrintWithoutUsingPrintDialog/ja
    \nアクティブなドキュメントをプリントします。プリントダイアログ、用紙設定ダイアログのどちらも表示しません。'''
    return INTEGER

def CC_CircuitFromShape(hObj):
    '''https://developer.vectorworks.net/index.php?title=VS:CC_CircuitFromShape'''
    return None

def CC_GetCircuitSource(hCircuit):
    '''https://developer.vectorworks.net/index.php?title=VS:CC_GetCircuitSource'''
    return (hDevice, hDevSkt, hAdapter, hSocket)

def CC_ReloadData():
    '''https://developer.vectorworks.net/index.php?title=VS:CC_ReloadData'''
    return None

def CC_DeviceFromShape(hObj):
    '''https://developer.vectorworks.net/index.php?title=VS:CC_DeviceFromShape'''
    return None

def CC_GetDevice(hSocket, skip adapters):
    '''https://developer.vectorworks.net/index.php?title=VS:CC_GetDevice'''
    return HANDLE

def CC_RoomFromShape(hObj):
    '''https://developer.vectorworks.net/index.php?title=VS:CC_RoomFromShape'''
    return HANDLE

def CC_GetCircuitDest(hCircuit):
    '''https://developer.vectorworks.net/index.php?title=VS:CC_GetCircuitDest'''
    return (hDevice, hDevSkt, hAdapter, hSocket)

def CC_GetEquipmentItem(hDevice):
    '''https://developer.vectorworks.net/index.php?title=VS:CC_GetEquipmentItem'''
    return HANDLE

def CC_RouteFromShape(hObj):
    '''https://developer.vectorworks.net/index.php?title=VS:CC_RouteFromShape'''
    return None

def Angle(c):
    '''https://developer.vectorworks.net/index.php?title=VS:Angle
    \nhttps://developer.vectorworks.net/index.php?title=VS:Angle/ja
    \n線分や円弧の角度を返します。検索条件に合致した図形が複数ある場合は合計を返します。'''
    return REAL

def EvalStr(h, c):
    '''https://developer.vectorworks.net/index.php?title=VS:EvalStr
    \nhttps://developer.vectorworks.net/index.php?title=VS:EvalStr/ja
    \nハンドルで指定した図形の検索条件に合致したデータを文字列で返します。'''
    return STRING

def RoofArea_Heated(c):
    '''https://developer.vectorworks.net/index.php?title=VS:RoofArea_Heated
    \nhttps://developer.vectorworks.net/index.php?title=VS:RoofArea_Heated/ja
    \n検索条件に合致した屋根、屋根面の勾配に沿った暖房領域の面積を返します。暖房領域は軒の出を含まない領域です。'''
    return REAL

def WallAverageHeight(c):
    '''https://developer.vectorworks.net/index.php?title=VS:WallAverageHeight
    \nhttps://developer.vectorworks.net/index.php?title=VS:WallAverageHeight/ja
    \n検索条件に合致した壁の頂点、開始位置、終了位置の高さを含めて計算した平均の高さを返します。'''
    return REAL

def Area(c):
    '''https://developer.vectorworks.net/index.php?title=VS:Area
    \nhttps://developer.vectorworks.net/index.php?title=VS:Area/ja
    \n検索条件に合致した図形の面積を返します。検索条件に合致した図形が複数ある場合は合計を返します。'''
    return REAL

def ForEachObject(callback, c):
    '''https://developer.vectorworks.net/index.php?title=VS:ForEachObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:ForEachObject/ja
    \n検索条件に合致した図形を、指定した手続き型サブルーチンで処理します。手続き型サブルーチンには、検索条件に合致した図形のハンドルを渡すための、ハンドル型のパラメータがなければなりません。'''
    return None

def RoofArea_HeatedProj(c):
    '''https://developer.vectorworks.net/index.php?title=VS:RoofArea_HeatedProj
    \nhttps://developer.vectorworks.net/index.php?title=VS:RoofArea_HeatedProj/ja
    \n検索条件に合致した屋根、屋根面の暖房領域の水平投影面積を返します。暖房領域は軒の出を含まない領域です。'''
    return REAL

def WallThickness(c):
    '''https://developer.vectorworks.net/index.php?title=VS:WallThickness
    \nhttps://developer.vectorworks.net/index.php?title=VS:WallThickness/ja
    \n検索条件に合致した壁の厚さを返します。'''
    return REAL

def AreaN(c):
    '''https://developer.vectorworks.net/index.php?title=VS:AreaN
    \nhttps://developer.vectorworks.net/index.php?title=VS:AreaN/ja
    \n検索条件に合致した図形の面積を返します。検索条件に合致した図形が複数ある場合は合計を返します。'''
    return REAL

def Height(c):
    '''https://developer.vectorworks.net/index.php?title=VS:Height
    \nhttps://developer.vectorworks.net/index.php?title=VS:Height/ja
    \n検索条件に合致した図形の高さを返します。検索条件に合致した図形が複数ある場合は合計を返します。'''
    return REAL

def RoofArea_Total(c):
    '''https://developer.vectorworks.net/index.php?title=VS:RoofArea_Total
    \nhttps://developer.vectorworks.net/index.php?title=VS:RoofArea_Total/ja
    \n検索条件に合致した屋根、屋根面の勾配に沿った総面積を返します。'''
    return REAL

def Width(c):
    '''https://developer.vectorworks.net/index.php?title=VS:Width
    \nhttps://developer.vectorworks.net/index.php?title=VS:Width/ja
    \n検索条件に合致した図形の幅を返します。検索条件に合致した図形が複数ある場合は合計を返します。'''
    return REAL

def BotBound(c):
    '''https://developer.vectorworks.net/index.php?title=VS:BotBound
    \nhttps://developer.vectorworks.net/index.php?title=VS:BotBound/ja
    \n検索条件に合致した図形の下辺のY座標を返します。検索条件に合致した図形が複数ある場合は、最後に合致した図形の値を返します。'''
    return REAL

def Hide(c):
    '''https://developer.vectorworks.net/index.php?title=VS:Hide
    \nhttps://developer.vectorworks.net/index.php?title=VS:Hide/ja
    \n検索条件に合致した図形を隠します。'''
    return None

def RoofArea_TotalProj(c):
    '''https://developer.vectorworks.net/index.php?title=VS:RoofArea_TotalProj
    \nhttps://developer.vectorworks.net/index.php?title=VS:RoofArea_TotalProj/ja
    \n検索条件に合致した屋根、屋根面の水平投影面積を返します。'''
    return REAL

def XCenter(c):
    '''https://developer.vectorworks.net/index.php?title=VS:XCenter
    \nhttps://developer.vectorworks.net/index.php?title=VS:XCenter/ja
    \n検索条件に合致した図形の中心のX座標を返します。検索条件に合致した図形が複数ある場合は合計を返します。'''
    return REAL

def BotBoundN(c):
    '''https://developer.vectorworks.net/index.php?title=VS:BotBoundN
    \nhttps://developer.vectorworks.net/index.php?title=VS:BotBoundN/ja
    \n検索条件に合致した図形の下辺のY座標を返します。検索条件に合致した図形が複数ある場合は、一番下の図形の値を返します。'''
    return REAL

def IsFlipped(c):
    '''https://developer.vectorworks.net/index.php?title=VS:IsFlipped
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsFlipped/ja
    \n反転されている図形（壁の中のシンボルなど）で検索条件に合致したものの数を返します。'''
    return REAL

def SelectObj(c):
    '''https://developer.vectorworks.net/index.php?title=VS:SelectObj
    \nhttps://developer.vectorworks.net/index.php?title=VS:SelectObj/ja
    \n検索条件に合致したすべての図形を選択します。'''
    return None

def XCenterN(c):
    '''https://developer.vectorworks.net/index.php?title=VS:XCenterN
    \nhttps://developer.vectorworks.net/index.php?title=VS:XCenterN/ja
    \n検索条件に合致した図形の中心のX座標を返します。複数の図形が検索条件に一致する場合、この関数は、一致するすべての図形の平均的な中心点のx座標を返します。'''
    return REAL

def CheckoutObj(c):
    '''https://developer.vectorworks.net/index.php?title=VS:CheckoutObj
    \nhttps://developer.vectorworks.net/index.php?title=VS:CheckoutObj/ja
    \n検索条件に合致するすべてのオブジェクトをチェックアウトします。'''
    return None

def LeftBound(c):
    '''https://developer.vectorworks.net/index.php?title=VS:LeftBound
    \nhttps://developer.vectorworks.net/index.php?title=VS:LeftBound/ja
    \n検索条件に合致した図形の左辺のX座標を返します。検索条件に合致した図形が複数ある場合は、最後に合致した図形の値を返します。'''
    return REAL

def Show(c):
    '''https://developer.vectorworks.net/index.php?title=VS:Show
    \nhttps://developer.vectorworks.net/index.php?title=VS:Show/ja
    \n隠されているまたは、グレイ表示されている図形で検索条件に合致したものを表示します。'''
    return None

def XCoordinate(c):
    '''https://developer.vectorworks.net/index.php?title=VS:XCoordinate
    \nhttps://developer.vectorworks.net/index.php?title=VS:XCoordinate/ja
    \nユーザ原点に基づく図形の X 座標を返します。'''
    return REAL

def ComponentArea(c, index):
    '''https://developer.vectorworks.net/index.php?title=VS:ComponentArea
    \nhttps://developer.vectorworks.net/index.php?title=VS:ComponentArea/ja
    \n指定した構成要素の片面の面積を返します。3D 図形の開口を考慮 (差し引き) します。'''
    return REAL

def LeftBoundN(c):
    '''https://developer.vectorworks.net/index.php?title=VS:LeftBoundN
    \nhttps://developer.vectorworks.net/index.php?title=VS:LeftBoundN/ja
    \n検索条件に合致した図形の左辺のX座標を返します。検索条件に合致した図形が複数ある場合は、一番左の図形の値を返します。'''
    return REAL

def SlabThickness(c):
    '''https://developer.vectorworks.net/index.php?title=VS:SlabThickness
    \nhttps://developer.vectorworks.net/index.php?title=VS:SlabThickness/ja
    \n検索条件に合致したスラブの厚さを返します。'''
    return REAL

def YCenter(c):
    '''https://developer.vectorworks.net/index.php?title=VS:YCenter
    \nhttps://developer.vectorworks.net/index.php?title=VS:YCenter/ja
    \n検索条件に合致した図形の中心のY座標を返します。検索条件に合致した図形が複数ある場合は合計を返します。'''
    return REAL

def ComponentVolume(c, index):
    '''https://developer.vectorworks.net/index.php?title=VS:ComponentVolume
    \nhttps://developer.vectorworks.net/index.php?title=VS:ComponentVolume/ja
    \n指定した構成要素の3D 容積を返します。3D 図形の開口を考慮 (差し引き) します。'''
    return REAL

def Length(c):
    '''https://developer.vectorworks.net/index.php?title=VS:Length
    \nhttps://developer.vectorworks.net/index.php?title=VS:Length/ja
    \n検索条件に合致した図形の長さを返します。検索条件に合致した図形が複数ある場合は合計を返します。'''
    return REAL

def SurfaceArea(c):
    '''https://developer.vectorworks.net/index.php?title=VS:SurfaceArea
    \nhttps://developer.vectorworks.net/index.php?title=VS:SurfaceArea/ja
    \n検索条件に合致したソリッドの表面積を返します。検索条件に合致した図形が複数ある場合は合計を返します。'''
    return REAL

def YCenterN(c):
    '''https://developer.vectorworks.net/index.php?title=VS:YCenterN
    \nhttps://developer.vectorworks.net/index.php?title=VS:YCenterN/ja
    \n検索条件に合致した図形の中心のY座標を返します。複数の図形が検索条件に一致する場合、この関数は、一致するすべての図形の平均的な中心点のy座標を返します。'''
    return REAL

def Count(c):
    '''https://developer.vectorworks.net/index.php?title=VS:Count
    \nhttps://developer.vectorworks.net/index.php?title=VS:Count/ja
    \n検索条件に合致した図形の数を返します。'''
    return LONGINT

def LengthN(c):
    '''https://developer.vectorworks.net/index.php?title=VS:LengthN
    \nhttps://developer.vectorworks.net/index.php?title=VS:LengthN/ja
    \n検索条件に合致した図形の長さを返します。検索条件に合致した図形が複数ある場合は合計を返します。'''
    return REAL

def SurfaceAreaN(c):
    '''https://developer.vectorworks.net/index.php?title=VS:SurfaceAreaN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SurfaceAreaN/ja
    \n検索条件に合致したソリッドの表面積を返します。検索条件に合致した図形が複数ある場合は合計を返します。'''
    return REAL

def YCoordinate(c):
    '''https://developer.vectorworks.net/index.php?title=VS:YCoordinate
    \nhttps://developer.vectorworks.net/index.php?title=VS:YCoordinate/ja
    \nユーザ原点に基づく図形の Y 座標を返します。'''
    return REAL

def CriteriaArea(c):
    '''https://developer.vectorworks.net/index.php?title=VS:CriteriaArea
    \nhttps://developer.vectorworks.net/index.php?title=VS:CriteriaArea/ja
    \n検索条件に合致した図形の面積を返します。値は「単位の設定」ダイアログで設定されている「面積」の単位になります。'''
    return REAL

def ObjectType(c):
    '''https://developer.vectorworks.net/index.php?title=VS:ObjectType
    \nhttps://developer.vectorworks.net/index.php?title=VS:ObjectType/ja
    \n検索条件に合致した図形の種類を返します。検索条件に合致した図形が複数ある場合は、最後に合致した図形の値を返します。'''
    return INTEGER

def TopBound(c):
    '''https://developer.vectorworks.net/index.php?title=VS:TopBound
    \nhttps://developer.vectorworks.net/index.php?title=VS:TopBound/ja
    \n検索条件に合致した図形の上辺のY座標を返します。検索条件に合致した図形が複数ある場合は合計を返します。'''
    return REAL

def ZCenter(c):
    '''https://developer.vectorworks.net/index.php?title=VS:ZCenter
    \nhttps://developer.vectorworks.net/index.php?title=VS:ZCenter/ja
    \n検索条件に合致した図形の中心のZ座標を返します。検索条件に合致した図形が複数ある場合は合計を返します。'''
    return REAL

def CriteriaSurfaceArea(c):
    '''https://developer.vectorworks.net/index.php?title=VS:CriteriaSurfaceArea
    \nhttps://developer.vectorworks.net/index.php?title=VS:CriteriaSurfaceArea/ja
    \n検索条件に合致したソリッドの表面積を返します。値は「単位の設定」ダイアログで設定されている「面積」の単位になります。'''
    return REAL

def Perim(c):
    '''https://developer.vectorworks.net/index.php?title=VS:Perim
    \nhttps://developer.vectorworks.net/index.php?title=VS:Perim/ja
    \n検索条件に合致した図形の周長を返します。検索条件に合致した図形が複数ある場合は合計を返します。'''
    return REAL

def TopBoundN(c):
    '''https://developer.vectorworks.net/index.php?title=VS:TopBoundN
    \nhttps://developer.vectorworks.net/index.php?title=VS:TopBoundN/ja
    \n検索条件に合致した図形の上辺のY座標を返します。検索条件に合致した図形が複数ある場合は最上位の座標の値が返されます。'''
    return REAL

def ZCenterN(c):
    '''https://developer.vectorworks.net/index.php?title=VS:ZCenterN
    \nhttps://developer.vectorworks.net/index.php?title=VS:ZCenterN/ja
    \n検索条件に合致した図形の中心のZ座標を返します。複数の図形が検索条件に一致する場合、この関数は、一致するすべての図形の平均的な中心点のZ座標を返します。'''
    return REAL

def CriteriaVolume(c):
    '''https://developer.vectorworks.net/index.php?title=VS:CriteriaVolume
    \nhttps://developer.vectorworks.net/index.php?title=VS:CriteriaVolume/ja
    \n検索条件に合致した図形の体積を返します。値は「単位の設定」ダイアログで設定されている「体積」の単位になります。'''
    return REAL

def PerimN(c):
    '''https://developer.vectorworks.net/index.php?title=VS:PerimN
    \nhttps://developer.vectorworks.net/index.php?title=VS:PerimN/ja
    \n検索条件に合致した図形の周長を返します。検索条件に合致した図形が複数ある場合は合計を返します。'''
    return REAL

def Volume(c):
    '''https://developer.vectorworks.net/index.php?title=VS:Volume
    \nhttps://developer.vectorworks.net/index.php?title=VS:Volume/ja
    \n検索条件に合致したソリッドの体積を返します。検索条件に合致した図形が複数ある場合は合計を返します。'''
    return REAL

def ZCoordinate(c):
    '''https://developer.vectorworks.net/index.php?title=VS:ZCoordinate
    \nhttps://developer.vectorworks.net/index.php?title=VS:ZCoordinate/ja
    \nユーザ原点に基づく図形の Z 座標を返します。'''
    return REAL

def DSelectObj(c):
    '''https://developer.vectorworks.net/index.php?title=VS:DSelectObj
    \nhttps://developer.vectorworks.net/index.php?title=VS:DSelectObj/ja
    \n検索条件に合致したすべての図形の選択を解除します。'''
    return None

def ReleaseObj(c):
    '''https://developer.vectorworks.net/index.php?title=VS:ReleaseObj
    \nhttps://developer.vectorworks.net/index.php?title=VS:ReleaseObj/ja
    \n検索条件に合致したオブジェクトをリリースします。'''
    return None

def VolumeN(c):
    '''https://developer.vectorworks.net/index.php?title=VS:VolumeN
    \nhttps://developer.vectorworks.net/index.php?title=VS:VolumeN/ja
    \n検索条件に合致したソリッドの体積を返します。検索条件に合致した図形が複数ある場合は合計を返します。'''
    return REAL

def EditProperties(c):
    '''https://developer.vectorworks.net/index.php?title=VS:EditProperties
    \nhttps://developer.vectorworks.net/index.php?title=VS:EditProperties/ja
    \n指定した検索条件に一致するすべての図形の「プロパティ」ダイアログを表示します。'''
    return None

def RightBound(c):
    '''https://developer.vectorworks.net/index.php?title=VS:RightBound
    \nhttps://developer.vectorworks.net/index.php?title=VS:RightBound/ja
    \n検索条件に合致した図形の右辺のX座標を返します。検索条件に合致した図形が複数ある場合は、最後に合致した図形の値を返します。'''
    return REAL

def WallArea_Gross(c):
    '''https://developer.vectorworks.net/index.php?title=VS:WallArea_Gross
    \nhttps://developer.vectorworks.net/index.php?title=VS:WallArea_Gross/ja
    \n検索条件に合致した壁の内側と外側の表面積 (グロス) の平均値を返します。表面積 (グロス) は壁の中のドアや窓を含めた全体の面積です。'''
    return REAL

def Eval(h, c):
    '''https://developer.vectorworks.net/index.php?title=VS:Eval
    \nhttps://developer.vectorworks.net/index.php?title=VS:Eval/ja
    \nハンドルで指定した図形の検索条件に合致したデータを実数で返します。'''
    return REAL

def RightBoundN(c):
    '''https://developer.vectorworks.net/index.php?title=VS:RightBoundN
    \nhttps://developer.vectorworks.net/index.php?title=VS:RightBoundN/ja
    \n検索条件に合致した図形の右辺のX座標を返します。検索条件に合致した図形が複数ある場合は、右端の図形の値を返します。'''
    return REAL

def WallArea_Net(c):
    '''https://developer.vectorworks.net/index.php?title=VS:WallArea_Net
    \nhttps://developer.vectorworks.net/index.php?title=VS:WallArea_Net/ja
    \n検索条件に合致した壁の内側と外側の表面積 (ネット) の平均値を返します。表面積 (ネット) は壁全体の面積からドアと窓の面積を除いた値です。'''
    return REAL

def DSH_GetDSCount(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:DSH_GetDSCount'''
    return (BOOLEAN, outCount)

def DSH_GetDSFieldValue(hObject, dsName, fieldLabel):
    '''https://developer.vectorworks.net/index.php?title=VS:DSH_GetDSFieldValue'''
    return (BOOLEAN, outValue, outStatus, outType)

def DSH_GetDSNameAt(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:DSH_GetDSNameAt'''
    return (BOOLEAN, dsIndex, outDataSheetName)

def DSH_GetDSFieldInfoAt(hObject, dsName):
    '''https://developer.vectorworks.net/index.php?title=VS:DSH_GetDSFieldInfoAt'''
    return (BOOLEAN, fieldIndex, outUniSrc, outLocSrc, outLabel)

def DSH_GetDSFieldsCount(hObject, dsName):
    '''https://developer.vectorworks.net/index.php?title=VS:DSH_GetDSFieldsCount'''
    return (BOOLEAN, outCount)

def DSH_SetDSFieldValue(hObject, dsName, fieldLabel, value):
    '''https://developer.vectorworks.net/index.php?title=VS:DSH_SetDSFieldValue'''
    return (BOOLEAN, outStatus)

def DT_AssociateWithObj(hDataTag, hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:DT_AssociateWithObj'''
    return BOOLEAN

def DT_EndMultipleMove():
    '''https://developer.vectorworks.net/index.php?title=VS:DT_EndMultipleMove'''
    return BOOLEAN

def DT_UpdateTaggedTags(h):
    '''https://developer.vectorworks.net/index.php?title=VS:DT_UpdateTaggedTags'''
    return BOOLEAN

def DT_BeginMultipleMove():
    '''https://developer.vectorworks.net/index.php?title=VS:DT_BeginMultipleMove'''
    return BOOLEAN

def DT_ResetAllDataTags():
    '''https://developer.vectorworks.net/index.php?title=VS:DT_ResetAllDataTags'''
    return None

def DT_AssociateWithObj(hDataTag, hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:DT_AssociateWithObj'''
    return BOOLEAN

def DelRecord(h, name):
    '''https://developer.vectorworks.net/index.php?title=VS:DelRecord
    \nhttps://developer.vectorworks.net/index.php?title=VS:DelRecord/ja
    \nハンドルで指定した図形に連結されているレコードを削除します。'''
    return None

def GetParametricRecord(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetParametricRecord
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetParametricRecord/ja
    \n参照された図形に添付されているパラメトリックレコードのハンドルを返します。'''
    return HANDLE

def NewField(recName, fieldName, fieldValue, fType, fFlag):
    '''https://developer.vectorworks.net/index.php?title=VS:NewField
    \nhttps://developer.vectorworks.net/index.php?title=VS:NewField/ja
    \nレコードに新しいレコードフィールドを追加します。指定した名前のレコードが存在しなければ、新しいレコードを作成します。'''
    return None

def Record(h, s):
    '''https://developer.vectorworks.net/index.php?title=VS:Record
    \nhttps://developer.vectorworks.net/index.php?title=VS:Record/ja
    \nハンドルで指定した図形にレコードを連結し直します。'''
    return None

def Field(h, s1, s2, s3):
    '''https://developer.vectorworks.net/index.php?title=VS:Field
    \nhttps://developer.vectorworks.net/index.php?title=VS:Field/ja
    \n使用できなくなった関数／手続きです。'''
    return None

def GetRField(h, record, field):
    '''https://developer.vectorworks.net/index.php?title=VS:GetRField
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetRField/ja
    \nハンドルで指定した図形に連結されたレコードフィールドの値を文字列で返します。'''
    return DYNARRAY[] of CHAR

def NumFields(h):
    '''https://developer.vectorworks.net/index.php?title=VS:NumFields
    \nhttps://developer.vectorworks.net/index.php?title=VS:NumFields/ja
    \nレコードフィールドの数を返します。'''
    return INTEGER

def SetRField(h, record, field, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetRField
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetRField/ja
    \nハンドルで指定した図形に連結しているレコードフィールドに値を設定します。'''
    return None

def GetFldFlag(h, t):
    '''https://developer.vectorworks.net/index.php?title=VS:GetFldFlag
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetFldFlag/ja
    \n指定したレコードの精度フラグを返します。'''
    return INTEGER

def GetRFieldOpt(h, record, field):
    '''https://developer.vectorworks.net/index.php?title=VS:GetRFieldOpt'''
    return (outIsEmpty, outIsDataLinked)

def NumRecords(h):
    '''https://developer.vectorworks.net/index.php?title=VS:NumRecords
    \nhttps://developer.vectorworks.net/index.php?title=VS:NumRecords/ja
    \nハンドルで指定した図形に連結されているレコードの数を返します。'''
    return INTEGER

def SetRFieldOpt(h, record, field, isEmpty, isDataLinked):
    '''https://developer.vectorworks.net/index.php?title=VS:SetRFieldOpt'''
    return None

def GetFldName(h, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetFldName
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetFldName/ja
    \nレコードフィールドの名前を返します。'''
    return STRING

def GetRecord(h, cnt):
    '''https://developer.vectorworks.net/index.php?title=VS:GetRecord
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetRecord/ja
    \nハンドルで指定した図形に連結されているレコードのハンドルを返します。'''
    return HANDLE

def PopupGetChoices(recName, fieldName):
    '''https://developer.vectorworks.net/index.php?title=VS:PopupGetChoices'''
    return (outNumValues, outPopUpValues)

def SetRecord(h, record):
    '''https://developer.vectorworks.net/index.php?title=VS:SetRecord
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetRecord/ja
    \nハンドルで指定した図形にレコードを連結します。'''
    return None

def GetFldType(h, t):
    '''https://developer.vectorworks.net/index.php?title=VS:GetFldType
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetFldType/ja
    \nレコードフィールドの形式を返します。'''
    return INTEGER

def LinkText(h, rec, fld):
    '''https://developer.vectorworks.net/index.php?title=VS:LinkText
    \nhttps://developer.vectorworks.net/index.php?title=VS:LinkText/ja
    \nハンドルで指定した文字図形にレコードとレコードフィールドを連結させます。この機能は「文字をレコードに連結」メニューに相当し、シンボル内の文字の制御に使います。'''
    return None

def PopupSetChoices(recName, fieldName, popUpValues):
    '''https://developer.vectorworks.net/index.php?title=VS:PopupSetChoices'''
    return None

def AddButtonMode(imageSpecifier):
    '''https://developer.vectorworks.net/index.php?title=VS:AddButtonMode
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddButtonMode/ja
    \nツールのモードバーにボタンイメージを追加します。vstAddButtonModeの代わりに使用してください。'''
    return None

def CreateSwapPane(dialogID, swapControlID, newGroupID):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateSwapPane
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateSwapPane/ja
    \nスワップペインコントロールの中にスワップペインを作成します。'''
    return None

def GetNumImagePopupItems(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetNumImagePopupItems
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNumImagePopupItems/ja
    \nイメージポップアップメニュー内のメニュー項目数を返します。'''
    return INTEGER

def SetEdgeBinding(dialogID, itemID, boundToLeft, boundToRight, boundToTop, boundToBottom):
    '''https://developer.vectorworks.net/index.php?title=VS:SetEdgeBinding
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetEdgeBinding/ja
    \nレイアウトダイアログに対してコントロールの縁を固定（TRUE）します。'''
    return None

def AddChoice(dialogID, componentID, choiceText, itemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:AddChoice
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddChoice/ja
    \nプルダウンメニューやリストアイテムに項目を追加します。'''
    return None

def CreateSymDispCtrlN(dialogID, itemID, symbolName, width, height, margin, view, renderMode, component, scaleByZoom):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateSymDispCtrlN'''
    return None

def GetNumLineTypeItems(dialogID, itemID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetNumLineTypeItems
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNumLineTypeItems/ja
    \n線種ポップアップコントロール内のラインタイプの数を返します'''
    return INTEGER

def SetEditColorTextStyl(dialogID, itemID, strStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetEditColorTextStyl'''
    return (BOOLEAN, outValue, outParam2)

def AddListBoxTabStop(dialogID, itemID, tabStop):
    '''https://developer.vectorworks.net/index.php?title=VS:AddListBoxTabStop
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddListBoxTabStop/ja
    \nリストボックスにタブストップを設定します。'''
    return None

def CreateSymbolDisplayControl(dialogID, itemID, symbolName, height, width, margin, renderMode, view):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateSymbolDisplayControl
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateSymbolDisplayControl/ja
    \nシンボルを表示するコントロールを作成します。 コントロールには指定されたレンダリングモードと視点で指定されたシンボルを表示します。 空白のコントロールを表示するには、シンボル名を空にしてください。'''
    return None

def GetPatternData(dialogID, itemID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPatternData
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPatternData/ja
    \n選択されている模様ポップアップコントロールの情報を返します。'''
    return (patternIndex, foreColor, backColor)

def SetEditInteger(dialogID, itemID, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetEditInteger
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetEditInteger/ja
    \n整数型の編集フィールドに整数値を設定します。'''
    return None

def AddRadioMode(initialSetting, buttonCount, imageSpecifier1, imageSpecifier2, imageSpecifier3, imageSpecifier4, imageSpecifier5, imageSpecifier):
    '''https://developer.vectorworks.net/index.php?title=VS:AddRadioMode
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddRadioMode/ja
    \nツールのモードバーにボタンイメージのグループを追加します。vstAddRadioModeの代わりに使用してください。'''
    return None

def CreateTabControl(dialogID, itemID):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateTabControl
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateTabControl/ja
    \nタブペインコントロールを作成します。タブペインコントロールは、情報を複数のタブペインに表示し、タブボタンでタブペイン間の切り替えができるようにします。'''
    return None

def GetPopUpChoiceIndex(dialogID, componentID, itemText):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPopUpChoiceIndex
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPopUpChoiceIndex/ja
    \nポップアップの中から文字列を検索し一致するインデックス（0基準）を取得します。存在しない場合、-1を返します。'''
    return itemIndex

def SetEditReal(dialogID, itemID, editRealType, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetEditReal
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetEditReal/ja
    \n実数型の編集フィールドに実数値を設定します。'''
    return None

def AdjustComponentPixelPos(nDialogID, nComponentID, nHorizontalPixels, nVerticalPixels):
    '''https://developer.vectorworks.net/index.php?title=VS:AdjustComponentPixelPos
    \nhttps://developer.vectorworks.net/index.php?title=VS:AdjustComponentPixelPos/ja
    \n指定したレイアウトダイアログのコンポーネントのピクセル幅とピクセル高さを調整します。'''
    return BOOLEAN

def CreateTabPane(dialogID, itemID, groupID):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateTabPane
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateTabPane/ja
    \nタブペインコントロールの中にタブペインを作成します。'''
    return None

def GetSelectedChoiceIndex(dialogID, componentID, startIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetSelectedChoiceIndex
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSelectedChoiceIndex/ja
    \n選択されている項目の番号を返します。'''
    return outSelectedIndex

def SetFirstGroupItem(dialogID, groupID, firstItemID):
    '''https://developer.vectorworks.net/index.php?title=VS:SetFirstGroupItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetFirstGroupItem/ja
    \nグループボックス内の最初のアイテムを設定します。'''
    return None

def AlignItemEdge(dialogID, itemID, whichEdge, alignID, alignMode):
    '''https://developer.vectorworks.net/index.php?title=VS:AlignItemEdge
    \nhttps://developer.vectorworks.net/index.php?title=VS:AlignItemEdge/ja
    \nダイアログ上の指定したアイテムの位置を揃えます。'''
    return None

def CreateThreeStateCheckBox(dialogID, componentID, strName):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateThreeStateCheckBox
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateThreeStateCheckBox/ja
    \n３状態チェックボックスを作成します。'''
    return None

def GetSelectedChoiceInfo(dialogID, componentID, startIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetSelectedChoiceInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSelectedChoiceInfo/ja
    \n選択されている項目の番号と文字列を返します。'''
    return (outSelectedIndex, outSelectedChoiceText)

def SetFirstLayoutItem(dialogID, firstItemID):
    '''https://developer.vectorworks.net/index.php?title=VS:SetFirstLayoutItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetFirstLayoutItem/ja
    \nレイアウト内の最初のアイテムを設定します。'''
    return None

def ClearGradientSliderSegments(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:ClearGradientSliderSegments
    \nhttps://developer.vectorworks.net/index.php?title=VS:ClearGradientSliderSegments/ja
    \nグラデーションスライダーからすべての変化位置を消去します。'''
    return None

def CreateThumbnailPopup(dialogID, controlID):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateThumbnailPopup
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateThumbnailPopup/ja
    \nVectorworksの図形のプレビューが表示される、ポップアップを作成します。'''
    return None

def GetSelectionRange(dialogID, controlID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetSelectionRange
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSelectionRange/ja
    \n指定したコントロール内の選択範囲の始点と終点を返します。'''
    return (startPos, endPos)

def SetFocusOnItem(liDialogID, liComponentID):
    '''https://developer.vectorworks.net/index.php?title=VS:SetFocusOnItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetFocusOnItem/ja
    \n指定したアイテムにキーボードからの入力フォーカスを設定します。'''
    return None

def CreateCenteredStaticText(dialogID, controlID, text, widthInCharacters):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateCenteredStaticText
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateCenteredStaticText/ja
    \nCreateStaticTextのように、編集不可能なフィールドを作成します。文字列はダイアログのフィールドの中心に作成されます。'''
    return None

def CreateTreeControl(nDialogID, nComponentID, nWidthInChars, nHeightInChars):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateTreeControl
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateTreeControl/ja
    \nツリーアイテムを作成します。'''
    return None

def GetStoryBoundChoiceStrings(story, topBound):
    '''https://developer.vectorworks.net/index.php?title=VS:GetStoryBoundChoiceStrings
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetStoryBoundChoiceStrings/ja
    \nストーリの高さ基準コントロールの選択ストリングを返します。'''
    return strings

def SetGradientSlider(dialogID, componentID, segmentIndex, spotPosition, midpointPosition, red, green, blue, opacity):
    '''https://developer.vectorworks.net/index.php?title=VS:SetGradientSlider
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetGradientSlider/ja
    \nグラデーションスライダーの変化位置の変化点の位置、変化の中心点の位置や色、不透明度を設定します。注：変化位置の番号には初期化した変数を使わなければなりません。変化点の位置が変更されデータが設定された後は、変数に変化位置の番号を返します。'''
    return segmentIndex

def CreateCheckBox(dialogID, itemID, text):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateCheckBox
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateCheckBox/ja
    \nチェックボックスを作成します。'''
    return None

def DeleteAllItems(dialogID, itemID):
    '''https://developer.vectorworks.net/index.php?title=VS:DeleteAllItems
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeleteAllItems/ja
    \nリストボックスからすべての行を削除します。'''
    return None

def GetStoryBoundDataFromChoiceString(choiceString):
    '''https://developer.vectorworks.net/index.php?title=VS:GetStoryBoundDataFromChoiceString
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetStoryBoundDataFromChoiceString/ja
    \nストーリの高さ基準選択ストリングから、ストーリの高さ基準データを返します。'''
    return (boundType, boundStory, layerLevelType)

def SetGradientSliderData(dialogID, componentID, segmentIndex, spotPosition, midpointPosition, red, green, blue):
    '''https://developer.vectorworks.net/index.php?title=VS:SetGradientSliderData
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetGradientSliderData/ja
    \nグラデーションスライダーの変化位置の変化点の位置、変化の中心点の位置や色を設定します。'''
    return segmentIndex

def CreateCheckBox2(dialogID, itemID, text, iconResPath):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateCheckBox2'''
    return None

def DeregisterDialogFromTimerEvents(dialogID):
    '''https://developer.vectorworks.net/index.php?title=VS:DeregisterDialogFromTimerEvents
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeregisterDialogFromTimerEvents/ja
    \nタイマーイベントレジストリからダイアログを削除します。'''
    return None

def GetStoryChoiceStrsN(story, boundSelection):
    '''https://developer.vectorworks.net/index.php?title=VS:GetStoryChoiceStrsN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetStoryChoiceStrsN/ja
    \nストーリの高さ基準コントロールの選択ストリングを返します。上、下、両方についてのストリングを取得できます。'''
    return strings

def SetGradientSliderSelectedMarker(dialogID, componentID, segmentIndex, markerType):
    '''https://developer.vectorworks.net/index.php?title=VS:SetGradientSliderSelectedMarker
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetGradientSliderSelectedMarker/ja
    \nグラデーションスライダーの点を選択します。'''
    return None

def CreateCheckBoxGroupBox(dialogID, itemID, name, hasFrame):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateCheckBoxGroupBox
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateCheckBoxGroupBox/ja
    \nチェックボックスのグループボックスを作成します。チェックボックスのグループボックスにはラベルをつけることができます。hasFrameがTRUEならば、枠線が表示されます。'''
    return None

def DeselectEditText(dialogID, controlID):
    '''https://developer.vectorworks.net/index.php?title=VS:DeselectEditText
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeselectEditText/ja
    \nすべての文字列型の編集フィールドの選択状態を解除します。'''
    return None

def GetThreeStateCheckBoxState(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetThreeStateCheckBoxState
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetThreeStateCheckBoxState/ja
    \n３状態チェックボックスの状態を返します。'''
    return iState

def SetHelpText(dialogID, componentID, helpText):
    '''https://developer.vectorworks.net/index.php?title=VS:SetHelpText
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetHelpText/ja
    \nヘルプフィールドに表示する文字列を設定します。'''
    return None

def CreateClassPullDownMenu(nDialogID, nComponentID, nWidthInChars):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateClassPullDownMenu
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateClassPullDownMenu/ja
    \nクラスのプルダウンメニューを作成します。'''
    return None

def DialogTimerEventMessageC():
    '''https://developer.vectorworks.net/index.php?title=VS:DialogTimerEventMessageC'''
    return INTEGER

def GetTreeControlItemData(nDialogID, nComponentID, nItemID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTreeControlItemData
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTreeControlItemData/ja
    \n指定したツリーアイテムのユーザデータを返します。'''
    return nUserData

def SetIconPushButtonState(nDialogID, nComponentID, bPressed):
    '''https://developer.vectorworks.net/index.php?title=VS:SetIconPushButtonState
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetIconPushButtonState/ja
    \n指定したアイコンプッシュボタンの状態（押された、押されていないなど）を設定します。'''
    return BOOLEAN

def CreateColorPopup(dialogID, itemID, widthInCharacters):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateColorPopup
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateColorPopup/ja
    \nアクティブドキュメントのカラーパレットを表示するカラーポップアップコントロールを作成します。'''
    return None

def DisplayDialogHelpC():
    '''https://developer.vectorworks.net/index.php?title=VS:DisplayDialogHelpC'''
    return INTEGER

def GetTreeControlItemText(nDialogID, nComponentID, nItemID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTreeControlItemText
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTreeControlItemText/ja
    \nツリーコントロールから指定した項目のテキストを返します。'''
    return (BOOLEAN, itemText)

def SetImageControlHandle(dialogID, componentID, hImage):
    '''https://developer.vectorworks.net/index.php?title=VS:SetImageControlHandle
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetImageControlHandle/ja
    \n指定したイメージのイメージ定義ノードハンドルを設定します。'''
    return None

def CreateControl(dialogID, itemID, controlKind, name, data):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateControl
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateControl/ja
    \nイメージ、カラーパレット、スライダーなどのアイテムを作成します。'''
    return None

def DisplaySwapPane(dialogID, swapControlID, groupNumber):
    '''https://developer.vectorworks.net/index.php?title=VS:DisplaySwapPane
    \nhttps://developer.vectorworks.net/index.php?title=VS:DisplaySwapPane/ja
    \nスワップコントロール内に指定したスワップペインを表示します。'''
    return None

def GetTreeControlSelectedItem(nDialogID, nComponentID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTreeControlSelectedItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTreeControlSelectedItem/ja
    \n選択されているツリーアイテムの項目番号を返します。'''
    return (BOOLEAN, nItemID)

def SetImageControlPath(nDialogID, nComponentID, strPath):
    '''https://developer.vectorworks.net/index.php?title=VS:SetImageControlPath
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetImageControlPath/ja
    \n指定したイメージのイメージパスを設定します。CreateImageControlと共に使用します。'''
    return BOOLEAN

def CreateCustThumbPopup(dialogID, controlID, sizeType):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateCustThumbPopup
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateCustThumbPopup/ja
    \nVectorworksの図形のプレビューが表示される、カスタムのサムネイルポップアップを作成します。'''
    return None

def DisplayTabPane(dialogID, tabControlID, groupNumber):
    '''https://developer.vectorworks.net/index.php?title=VS:DisplayTabPane
    \nhttps://developer.vectorworks.net/index.php?title=VS:DisplayTabPane/ja
    \nスワップコントロール内に指定したスワップペインを表示します。'''
    return None

def GetTreeControlTextSelectedItem(nDialogID, nComponentID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTreeControlTextSelectedItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTreeControlTextSelectedItem/ja
    \nツリーコントロールから選択した項目のテキストを返します。'''
    return (BOOLEAN, itemText)

def SetImagePopupSelectedItem(dialogID, componentID, itemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:SetImagePopupSelectedItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetImagePopupSelectedItem/ja
    \nイメージポップアップメニューを設定します。'''
    return None

def CreateCustomControl(dialogID, componentID, iWidth, iHeight):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateCustomControl
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateCustomControl/ja
    \nレイアウトコントロールをVectorScriptに作成し、外部ダイアログハンドラのGS_OverrideControlと組み合わせて使用します。'''
    return None

def EnableItem(dialogID, componentID, enableState):
    '''https://developer.vectorworks.net/index.php?title=VS:EnableItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:EnableItem/ja
    \nアイテムの有効／無効を設定します。'''
    return None

def InsertEnhanPullDownMenuItem(dialogID, controlID, strName, imageSpecifier):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertEnhanPullDownMenuItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:InsertEnhanPullDownMenuItem/ja
    \nInsertEnhancedPulldownMenuItem の代わりに、イメージを挿入します。'''
    return INTEGER

def SetItemClickable(dialogID, componentID, clickable):
    '''https://developer.vectorworks.net/index.php?title=VS:SetItemClickable
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetItemClickable/ja
    \n指定されたコントロールがクリックイベントを受け取れるようにします。現在は静的文字列と画像が対応している。'''
    return None

def CreateDesignLayerPullDownMenu(nDialogID, nComponentID, nWidthInChars):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateDesignLayerPullDownMenu
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateDesignLayerPullDownMenu/ja
    \nデザインレイヤのプルダウンメニューを作成します。'''
    return None

def EnableLBDropOnIndices(dialogID, componentID, iStartIndex, iEndIndex, bEnable):
    '''https://developer.vectorworks.net/index.php?title=VS:EnableLBDropOnIndices
    \nhttps://developer.vectorworks.net/index.php?title=VS:EnableLBDropOnIndices/ja
    \n指定した番号内でのドラッグ＆ドロップ操作を有効／無効にします。'''
    return BOOLEAN

def InsertEnhancedPullDownMenuItem(dialogID, componentID, strName, iIconID):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertEnhancedPullDownMenuItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:InsertEnhancedPullDownMenuItem/ja
    \n指定した拡張プルダウンメニューに項目を挿入します。廃止予定の関数です。代わりに InsertEnhanPullDownMenuItem を使用してください。'''
    return INTEGER

def SetItemText(dialogID, componentID, text):
    '''https://developer.vectorworks.net/index.php?title=VS:SetItemText
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetItemText/ja
    \nテキストフィールドに表示する文字列を設定します。'''
    return None

def CreateEditColorText(dialogID, itemID, widthInStdChar, heightInLines):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateEditColorText'''
    return None

def EnableTextEdit(dialogID, componentID, editableState):
    '''https://developer.vectorworks.net/index.php?title=VS:EnableTextEdit
    \nhttps://developer.vectorworks.net/index.php?title=VS:EnableTextEdit/ja
    \nテキストフィールドの編集可／不可を設定します。'''
    return None

def InsertGradientSliSeg(dialogID, componentID, spotPosition, red, green, blue, opacity):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertGradientSliSeg
    \nhttps://developer.vectorworks.net/index.php?title=VS:InsertGradientSliSeg/ja'''
    return INTEGER

def SetItemToolTipText(nDialogID, nComponentID, strToolTip, strSubToolTip, nIndex, nSubIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:SetItemToolTipText
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetItemToolTipText/ja
    \nリストブラウザ、編集フィールド、プルダウンメニューの、ツールチップとして表示される文字列を設定します。nIndexとnSubIndexはリストブラウザのみで使用されます。'''
    return None

def CreateEditInteger(dialogID, itemID, defaultValue, widthInCharacters):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateEditInteger
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateEditInteger/ja
    \n整数型の編集フィールドを作成します。'''
    return None

def ExpandTreeControlItem(nDialogID, nComponentID, nItemID, bExpand):
    '''https://developer.vectorworks.net/index.php?title=VS:ExpandTreeControlItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:ExpandTreeControlItem/ja
    \n指定したツリーアイテムを開くまたは折りたたみます。'''
    return None

def InsertGradientSliderSegment(dialogID, componentID, spotPosition, red, green, blue):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertGradientSliderSegment
    \nhttps://developer.vectorworks.net/index.php?title=VS:InsertGradientSliderSegment/ja
    \nグラデーションスライダーに新しい変化位置を挿入し、指定した値でそのデータを初期化します。'''
    return INTEGER

def SetLBImageIndexes(dialogID, controlID, itemIndex, subItemIndex, imageSpecifier0, imageSpecifier1, imageSpecifier2):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBImageIndexes
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBImageIndexes/ja
    \nリストブラウザの行にイメージを設定します。SetLBMultImageIndexesの代わりに使用してください。'''
    return BOOLEAN

def CreateEditPassword(dialogID, itemID, widthInStdChar):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateEditPassword'''
    return None

def GetActiveEditItem(dialogID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetActiveEditItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetActiveEditItem/ja
    \nアクティブな編集フィールドの値を返します。アクティブな編集フィールドがなければ、-1を返します。'''
    return LONGINT

def InsertImagePopupObjectItem(dialogID, componentID, objectName):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertImagePopupObjectItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:InsertImagePopupObjectItem/ja
    \n図形をイメージポップアップメニューに挿入します。'''
    return INTEGER

def SetLayoutDialogPosition(dialogID, left, top):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLayoutDialogPosition
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLayoutDialogPosition/ja
    \n指定した位置にダイアログウインドウを移動します。'''
    return BOOLEAN

def CreateEditReal(dialogID, itemID, editRealType, defaultValue, widthInCharacters):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateEditReal
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateEditReal/ja
    \n実数型の編集フィールドを作成します。'''
    return None

def GetActivePane(dialogID, tabControlID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetActivePane
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetActivePane/ja
    \n現在表示されているタブかスワップパネルを返します。'''
    return LONGINT

def InsertImagePopupResource(dialogID, componentID, listID, index):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertImagePopupResource
    \nhttps://developer.vectorworks.net/index.php?title=VS:InsertImagePopupResource/ja
    \nリソースファイルから指定された項目を、イメージポップアップメニューに挿入します。挿入された項目のイメージポップアップのインデックスを返します。'''
    return LONGINT

def SetLayoutDialogSize(dialogID, width, height):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLayoutDialogSize
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLayoutDialogSize/ja
    \nレイアウトダイアログをピクセル単位で設定します。'''
    return None

def CreateEditText(dialogID, itemID, defaultText, widthInCharacters):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateEditText
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateEditText/ja
    \n文字列型の編集フィールドを作成します。'''
    return None

def GetBooleanItem(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetBooleanItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetBooleanItem/ja
    \nチェックボックスまたはラジオボタンの選択状態を返します。'''
    return outState

def InsertImagePopupSeparator(liDialogID, liComponentID, strLabel):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertImagePopupSeparator
    \nhttps://developer.vectorworks.net/index.php?title=VS:InsertImagePopupSeparator/ja
    \nイメージポップアップメニューリストの末尾に指定したラベルがある状態で、セパレータを挿入します。'''
    return INTEGER

def SetLayoutOption(dialogID, option, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLayoutOption
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLayoutOption/ja
    \nレイアウトダイアログのオプションを設定します。'''
    return BOOLEAN

def CreateEditTextBox(dialogID, itemID, defaultText, widthInCharacters, heightInLines):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateEditTextBox
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateEditTextBox/ja
    \nスクロールすることで複数行を編集可能なフィールドを作成します。'''
    return None

def GetChoiceCount(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetChoiceCount
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetChoiceCount/ja
    \nプルダウンメニューやリストアイテムの項目数を返します。'''
    return outCount

def InsertPropClassOrLayerItem(dialogID, controlID, strLabel, imageSpecifier):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertPropClassOrLayerItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:InsertPropClassOrLayerItem/ja
    \nInsertProposedClassOrLayerItem の代わりに、イメージを挿入します。'''
    return BOOLEAN

def SetLineAttributeData(dialogID, itemID, lineStyle, lineWeight):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLineAttributeData
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLineAttributeData/ja
    \n線種と線の太さポップアップを設定します。線種と線の太さの両方を指定できます。'''
    return None

def CreateEnhancedPullDownMenu(dialogID, componentID, iWidthInCharacters, bShowIconInMainWindow):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateEnhancedPullDownMenu
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateEnhancedPullDownMenu/ja
    \nグループボックスのプルダウンメニューを作成します。'''
    return None

def GetChoiceIndex(dialogID, componentID, itemText):
    '''https://developer.vectorworks.net/index.php?title=VS:GetChoiceIndex
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetChoiceIndex/ja
    \nリストボックスやプルダウンメニューで、特定のストリングを検索します。インデックスは0から始まり、見つからなかったときは、-1を返します。'''
    return itemIndex

def InsertProposedClassOrLayerItem(nDialogID, nComponentID, strLabel, nIconIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertProposedClassOrLayerItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:InsertProposedClassOrLayerItem/ja
    \nクラス項目またはレイヤ項目を、クラス、デザインレイヤ、またはシートレイヤのプルダウンメニューの任意の場所に挿入します。廃止予定の関数です。代わりに InsertPropClassOrLayerItem を使用してください。'''
    return BOOLEAN

def SetLineStyleChoice(dialogID, itemID, lineStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLineStyleChoice
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLineStyleChoice/ja
    \n線種ポップアップを設定します。'''
    return None

def CreateGradient(name):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateGradient
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateGradient/ja
    \nグラデーションを新規に作成します。'''
    return HANDLE

def GetChoiceStringFromStoryBoundData(boundType, boundStory, layerLevelType):
    '''https://developer.vectorworks.net/index.php?title=VS:GetChoiceStringFromStoryBoundData
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetChoiceStringFromStoryBoundData/ja
    \nストーリの高さ基準データから、ストーリの高さ基準の選択ストリングを返します。'''
    return choiceString

def InsertTreeControlItem(nDialogID, nComponentID, strItemLabel, nParentID, nAfterID):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertTreeControlItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:InsertTreeControlItem/ja
    \nツリーアイテムに項目を挿入します。'''
    return INTEGER

def SetLineTypeAttriData(dialogID, itemID, lineType, lineWeight):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLineTypeAttriData
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLineTypeAttriData/ja
    \n線種と線の太さポップアップを設定します。ラインタイプと線の太さの両方を指定できます。'''
    return None

def CreateGroupBox(dialogID, itemID, text, hasFrame):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateGroupBox
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateGroupBox/ja
    \nグループボックスを作成します。'''
    return None

def GetChoiceText(dialogID, componentID, itemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetChoiceText
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetChoiceText/ja
    \nインデックスを使用して、プルダウンメニューやリストアイテムのテキストを返します。'''
    return itemText

def IsClassChoiceSelected(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:IsClassChoiceSelected
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsClassChoiceSelected/ja
    \nマーカー、線種、色のポップアップで「クラス属性」が選択されているかを返します。'''
    return BOOLEAN

def SetLineTypeChoice(dialogID, itemID, lineType):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLineTypeChoice
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLineTypeChoice/ja
    \n線種ポップアップで選択中の項目に指定したラインタイプを設定します'''
    return None

def CreateIconPushButton(nDialogID, nComponentID, nIconID, nWidthInChars):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateIconPushButton
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateIconPushButton/ja
    \nアイコンプッシュボタンを作成し、アイコンの番号と幅（文字数）を指定します。廃止予定の関数です。代わりに CreateImagePushButton を使用してください。'''
    return None

def GetColorButton(dialogID, itemID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetColorButton
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetColorButton/ja
    \nカラーボタンの色を返します。'''
    return (red, green, blue)

def IsItemEnabled(nDialogID, nComponentID):
    '''https://developer.vectorworks.net/index.php?title=VS:IsItemEnabled
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsItemEnabled/ja
    \n指定したアイテムの有効／無効を返します。'''
    return BOOLEAN

def SetLineWeightChoice(dialogID, itemID, lineWeight):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLineWeightChoice
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLineWeightChoice/ja
    \n線の太さポップアップを設定します。'''
    return None

def CreateImageControl(dialogID, componentID, iWidthPixels, iHeightPixels, hImage):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateImageControl
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateImageControl/ja
    \nイメージコントロールを作成します。'''
    return None

def GetColorChoice(dialogID, itemID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetColorChoice
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetColorChoice/ja
    \n選択されているカラーポップアップコントロールを返します。'''
    return colorIndex

def IsItemVisible(nDialogID, nComponentID):
    '''https://developer.vectorworks.net/index.php?title=VS:IsItemVisible
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsItemVisible/ja
    \n指定したアイテムの表示／非表示を返します。'''
    return BOOLEAN

def SetListBoxTabStops(dialogID, componentID, tabStops):
    '''https://developer.vectorworks.net/index.php?title=VS:SetListBoxTabStops
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetListBoxTabStops/ja
    \nリストコントロールにタブストップを設定します。'''
    return None

def CreateImageControl2(dialogID, controlID, widthInPixels, heightInPixels, imageSpecifier):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateImageControl2
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateImageControl2/ja'''
    return None

def GetComponentRect(nDialogID, nComponentID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponentRect
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetComponentRect/ja
    \n指定したレイアウトダイアログのコンポーネントの四角形の領域の座標を返します。'''
    return (BOOLEAN, nLeft, nTop, nRight, nBottom)

def LeftButtonC():
    '''https://developer.vectorworks.net/index.php?title=VS:LeftButtonC'''
    return INTEGER

def SetMarkerChoice(dialogID, itemID, index, style, angle, size):
    '''https://developer.vectorworks.net/index.php?title=VS:SetMarkerChoice
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetMarkerChoice/ja
    \nマーカポップアップを設定します。角度パラメータは、0から90度の範囲でなければなりません。'''
    return None

def CreateImagePushButton(dialogID, controlID, widthInCharacters, imageSpecifier):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateImagePushButton
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateImagePushButton/ja
    \nイメージプッシュボタンを作成します。CreateIconPushButton の代わりに使用してください。'''
    return None

def GetComponentTextWidth(nDialogID, nComponentID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponentTextWidth
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetComponentTextWidth/ja
    \n指定したレイアウトダイアログの単位でテキストフィールドの幅を返します。'''
    return (BOOLEAN, nWidthInLMUnits)

def NotifyPullDownClicked(nDialogID, nComponentID):
    '''https://developer.vectorworks.net/index.php?title=VS:NotifyPullDownClicked
    \nhttps://developer.vectorworks.net/index.php?title=VS:NotifyPullDownClicked/ja
    \nプルダウンメニューがクリックされたことを返します。動的メニューを生成することができます。'''
    return None

def SetMarkerValue(dialogID, itemID, style, angle, length, width, basis, thickness):
    '''https://developer.vectorworks.net/index.php?title=VS:SetMarkerValue
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetMarkerValue/ja
    \nマーカポップアップの値を設定します。（VW2008より前のバージョンのマーカポップアップ手続きの代わりになります。）'''
    return None

def CreateLayerPDMenu(nDialogID, nComponentID, widthInStandardChar):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateLayerPDMenu'''
    return None

def GetControlData(dialogID, itemID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetControlData
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetControlData/ja
    \n指定したアイテムのデータを返します。'''
    return data

def RefreshItem(liDialogID, liComponentID):
    '''https://developer.vectorworks.net/index.php?title=VS:RefreshItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:RefreshItem/ja
    \n指定したアイテムを更新します。'''
    return None

def SetPatternData(dialogID, itemID, patternIndex, foreColor, backColor):
    '''https://developer.vectorworks.net/index.php?title=VS:SetPatternData
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetPatternData/ja
    \n模様ポップアップを設定します。'''
    return None

def CreateLayout(dialogTitle, hasHelp, defaultButtonName, cancelButtonName):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateLayout
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateLayout/ja
    \nダイアログのレイアウトを作成し、ダイアログ番号を返します。'''
    return LONGINT

def GetDlgCtrlWidthStdCh(str):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDlgCtrlWidthStdCh'''
    return INTEGER

def RegisterDialogForTimerEvents(dialogID, timerDelayInMilliseconds):
    '''https://developer.vectorworks.net/index.php?title=VS:RegisterDialogForTimerEvents
    \nhttps://developer.vectorworks.net/index.php?title=VS:RegisterDialogForTimerEvents/ja
    \nダイアログを登録して一定時間ごとにイベントを受け取れるようにします。'''
    return None

def SetProportionalBinding(dialogID, itemID, leftProportional, rightProportional, topProportional, bottomProportional):
    '''https://developer.vectorworks.net/index.php?title=VS:SetProportionalBinding
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetProportionalBinding/ja
    \nレイアウトダイアログに対してコントロールの位置が比例距離を保つ設定をします。'''
    return None

def CreateLineAttributePopup(dialogID, itemID):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateLineAttributePopup
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateLineAttributePopup/ja
    \nドキュメントで利用可能か線種と線の太さの選択肢を表示するポップアップコントロールを作成します。'''
    return None

def GetEditInteger(dialogID, itemID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetEditInteger
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetEditInteger/ja
    \n整数型の編集フィールドに入力されている整数値を返します。'''
    return (BOOLEAN, value)

def RemoveAllImagePopupItems(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:RemoveAllImagePopupItems
    \nhttps://developer.vectorworks.net/index.php?title=VS:RemoveAllImagePopupItems/ja
    \nイメージポップアップメニューからすべてのメニュー項目を削除します。'''
    return None

def SetRightItem(dialogID, srcItemID, rightItemID, indent, lineSpacing):
    '''https://developer.vectorworks.net/index.php?title=VS:SetRightItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetRightItem/ja
    \n基準とするアイテムの右に、アイテムを配置します。挿入点からX軸、Y軸方向のオフセットを設定できます。'''
    return None

def CreateLineStylePopup(dialogID, itemID):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateLineStylePopup
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateLineStylePopup/ja
    \nアクティブなドキュメントで利用可能な線種の選択肢を表示するポップアップを作成します。'''
    return None

def GetEditReal(dialogID, itemID, editRealType):
    '''https://developer.vectorworks.net/index.php?title=VS:GetEditReal
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetEditReal/ja
    \n実数型の編集フィールドに入力されている実数値を返します。'''
    return (BOOLEAN, value)

def RemoveChoice(dialogID, componentID, itemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:RemoveChoice
    \nhttps://developer.vectorworks.net/index.php?title=VS:RemoveChoice/ja
    \nプルダウンメニューやリストアイテムにある項目を削除します。'''
    return None

def SetSelectionRange(dialogID, controlID, startPos, endPos):
    '''https://developer.vectorworks.net/index.php?title=VS:SetSelectionRange
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetSelectionRange/ja
    \n指定したコントロール内の選択範囲の始点と終点を設定します。'''
    return None

def CreateLineWeightPopup(dialogID, itemID):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateLineWeightPopup
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateLineWeightPopup/ja
    \nアクティブなドキュメントで利用可能な線の太さの選択肢を表示するポップアップを作成します。'''
    return None

def GetGradientSlider(dialogID, componentID, segmentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetGradientSlider
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetGradientSlider/ja'''
    return (spotPosition, midpointPosition, red, green, blue, opacity)

def RemoveEnhancedPullDownMenuItemRange(dialogID, componentID, iStartItemIndexToRemove, iEndItemIndexToRemove):
    '''https://developer.vectorworks.net/index.php?title=VS:RemoveEnhancedPullDownMenuItemRange
    \nhttps://developer.vectorworks.net/index.php?title=VS:RemoveEnhancedPullDownMenuItemRange/ja
    \nグループボックスのプルダウンメニューにある指定した範囲の項目を削除します。'''
    return None

def SetSliderLiveUpdate(dialogID, componentID, liveUpdate):
    '''https://developer.vectorworks.net/index.php?title=VS:SetSliderLiveUpdate
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetSliderLiveUpdate/ja
    \nスライダーアイテムのイベントをライブアップデートにするかを設定します。'''
    return None

def CreateListBox(dialogID, itemID, widthInCharacters, heightInCharacters):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateListBox
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateListBox/ja
    \nリストボックスを作成します。'''
    return None

def GetGradientSliderData(dialogID, componentID, segmentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetGradientSliderData
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetGradientSliderData/ja
    \nグラデーションスライダーにある変化位置の変化点、変化の中心点の位置と色を返します。'''
    return (spotPosition, midpointPosition, red, green, blue)

def RemoveGradientSliderSegment(dialogID, componentID, segmentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:RemoveGradientSliderSegment
    \nhttps://developer.vectorworks.net/index.php?title=VS:RemoveGradientSliderSegment/ja
    \nグラデーションスライダーから変化位置を削除します。'''
    return None

def SetStaticTextColor(dialogID, componentID, red, green, blue):
    '''https://developer.vectorworks.net/index.php?title=VS:SetStaticTextColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetStaticTextColor/ja
    \n編集不可能なフィールドに色を指定します。'''
    return None

def CreateListBoxN(dialogID, itemID, widthInCharacters, heightInCharacters, isMultipleSelect):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateListBoxN
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateListBoxN/ja
    \nリストボックスを作成します。isMultipleSelectパラメータをTRUEにすると、リストボックス内の項目を複数選択することができます。'''
    return None

def GetGradientSliderSelectedMarker(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetGradientSliderSelectedMarker
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetGradientSliderSelectedMarker/ja
    \nグラデーションスライダーの選択されている点を返します。'''
    return (segmentIndex, markerType)

def RemoveImagePopupItem(dialogID, componentID, itemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:RemoveImagePopupItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:RemoveImagePopupItem/ja
    \nイメージポップアップメニューからメニュー項目を削除します。'''
    return None

def SetStaticTextColorN(dialogID, componentID, tint):
    '''https://developer.vectorworks.net/index.php?title=VS:SetStaticTextColorN'''
    return None

def CreateMarkerPopup(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateMarkerPopup
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateMarkerPopup/ja
    \nマーカポップアップを作成します。'''
    return None

def GetIconPushButtonState(nDialogID, nComponentID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetIconPushButtonState
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetIconPushButtonState/ja
    \n指定したアイコンプッシュボタンの状態（押された、または押されていないなど）を返します。'''
    return (BOOLEAN, bPressed)

def RemoveListBoxTabStop(dialogID, itemID):
    '''https://developer.vectorworks.net/index.php?title=VS:RemoveListBoxTabStop
    \nhttps://developer.vectorworks.net/index.php?title=VS:RemoveListBoxTabStop/ja
    \nリストボックスから最後のタブストップを削除します。'''
    return None

def SetStaticTextStyle(dialogID, componentID, style):
    '''https://developer.vectorworks.net/index.php?title=VS:SetStaticTextStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetStaticTextStyle/ja
    \n編集不可能なフィールドに文字スタイルを指定します。'''
    return None

def CreatePatternPopup(dialogID, itemID):
    '''https://developer.vectorworks.net/index.php?title=VS:CreatePatternPopup
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreatePatternPopup/ja
    \nアクティブなドキュメントで利用可能な模様の選択肢を表示するポップアップを作成します。'''
    return None

def GetImagePopupObject(dialogID, componentID, itemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetImagePopupObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetImagePopupObject/ja
    \nイメージポップアップメニューのメニュー項目番号から図形の名前を返します。'''
    return STRING

def RemoveTreeControlItem(nDialogID, nComponentID, nItemID):
    '''https://developer.vectorworks.net/index.php?title=VS:RemoveTreeControlItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:RemoveTreeControlItem/ja
    \nツリーアイテムから項目を削除します。'''
    return BOOLEAN

def SetThreeStateCheckBoxState(dialogID, componentID, iState):
    '''https://developer.vectorworks.net/index.php?title=VS:SetThreeStateCheckBoxState
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetThreeStateCheckBoxState/ja
    \n３状態チェックボックスの状態を設定します。'''
    return None

def CreatePullDownMenu(dialogID, itemID, widthInCharacters):
    '''https://developer.vectorworks.net/index.php?title=VS:CreatePullDownMenu
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreatePullDownMenu/ja
    \nプルダウンメニューを作成します。'''
    return None

def GetImagePopupObjectItemIndex(dialogID: int, componentID: int, objectName: str):
    '''https://developer.vectorworks.net/index.php?title=VS:GetImagePopupObjectItemIndex
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetImagePopupObjectItemIndex/ja
    \nイメージポップアップメニュー内の図形の名前からメニュー項目番号を返します。'''
    return int

def ResizeDialogC():
    '''https://developer.vectorworks.net/index.php?title=VS:ResizeDialogC'''
    return INTEGER

def SetTreeControlItemData(nDialogID, nComponentID, nItemID, nUserData):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTreeControlItemData
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTreeControlItemData/ja
    \n指定したツリーアイテムのユーザデータを設定します。'''
    return None

def CreatePullDownMenuGroupBox(liDialogID, liComponentID, iPullDownWidth, strLabel, bHasFrame):
    '''https://developer.vectorworks.net/index.php?title=VS:CreatePullDownMenuGroupBox
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreatePullDownMenuGroupBox/ja
    \nプルダウンメニューのグループボックスを作成します。'''
    return None

def GetImagePopupSelectedItem(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetImagePopupSelectedItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetImagePopupSelectedItem/ja
    \nイメージポップアップメニューの選択されているメニュー項目番号を返します。'''
    return INTEGER

def RunLayoutDialog(dialogID, callback):
    '''https://developer.vectorworks.net/index.php?title=VS:RunLayoutDialog
    \nhttps://developer.vectorworks.net/index.php?title=VS:RunLayoutDialog/ja
    \n指定したダイアログ番号とサブルーチンの名前で、ダイアログイベントループを実行します。'''
    return LONGINT

def SetVSResourceFile(fileName):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVSResourceFile
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetVSResourceFile/ja
    \nリソースファイルを開きます。ファイルの名前は、拡張子を含まない名前で指定します。'''
    return BOOLEAN

def CreatePullDownSearch(nDialogID, nComponentID, nWidthInChars):
    '''https://developer.vectorworks.net/index.php?title=VS:CreatePullDownSearch'''
    return None

def GetItemText(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetItemText
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetItemText/ja
    \nテキストフィールドに入力された文字列を返します。（255文字以下）'''
    return text

def RunLayoutDialogN(dialogID, callback, enableContextualHelp):
    '''https://developer.vectorworks.net/index.php?title=VS:RunLayoutDialogN'''
    return LONGINT

def SetdownDialogC():
    '''https://developer.vectorworks.net/index.php?title=VS:SetdownDialogC'''
    return INTEGER

def CreatePushButton(dialogID, itemID, text):
    '''https://developer.vectorworks.net/index.php?title=VS:CreatePushButton
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreatePushButton/ja
    \nプッシュボタンを作成します。'''
    return None

def GetLBHeaderTextWidth(className, allowForSortIcon):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBHeaderTextWidth
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBHeaderTextWidth/ja
    \nリストブラウザの列ヘッダで文字列が短縮されずに表示される幅をピクセルで返します。InsertLBColumnで幅を適切に設定する際に利用します。'''
    return INTEGER

def RunNamedDialog(dialogID, callback, univName):
    '''https://developer.vectorworks.net/index.php?title=VS:RunNamedDialog
    \nhttps://developer.vectorworks.net/index.php?title=VS:RunNamedDialog/ja
    \n指定したダイアログをユニバーサルな名前で表示し、ダイアログイベントループを実行します。ダイアログイベントループはこの関数に渡すパラメーターのサブルーチン関数で指定します。'''
    return LONGINT

def SetupDialogC():
    '''https://developer.vectorworks.net/index.php?title=VS:SetupDialogC'''
    return INTEGER

def CreateRadioButton(dialogID, itemID, text):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateRadioButton
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateRadioButton/ja
    \nラジオボタンを作成します。'''
    return None

def GetLayoutDialogPosition(dialogID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLayoutDialogPosition
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLayoutDialogPosition/ja
    \nダイアログウインドウの位置を検索し、ピクセルで返します。'''
    return (BOOLEAN, left, top, right, bottom)

def RunNamedDialogN(dialogID, callback, univName, enableContextualHelp):
    '''https://developer.vectorworks.net/index.php?title=VS:RunNamedDialogN'''
    return LONGINT

def ShowByClassChoice(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:ShowByClassChoice
    \nhttps://developer.vectorworks.net/index.php?title=VS:ShowByClassChoice/ja
    \nマーカー、線種、色のポップアップに「クラス属性」選択を追加します。'''
    return None

def CreateRadioButton2(dialogID, itemID, text, iconResPath):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateRadioButton2'''
    return None

def GetLayoutDialogSize(dialogID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLayoutDialogSize
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLayoutDialogSize/ja
    \nレイアウトダイアログのサイズを返します。'''
    return (width, height)

def SelectChoice(dialogID, componentID, itemIndex, selectState):
    '''https://developer.vectorworks.net/index.php?title=VS:SelectChoice
    \nhttps://developer.vectorworks.net/index.php?title=VS:SelectChoice/ja
    \nプルダウンメニューやリストアイテムにある項目の選択状態を設定します。'''
    return None

def ShowEditTileDialog(tileHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:ShowEditTileDialog
    \nhttps://developer.vectorworks.net/index.php?title=VS:ShowEditTileDialog/ja
    \nタイル編集ダイアログを表示します。タイルの形状と設定のどちらを編集するか選択することができます。'''
    return None

def CreateRadioButtonGroupBox(dialogID, itemID, name, hasFrame):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateRadioButtonGroupBox
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateRadioButtonGroupBox/ja
    \nラジオボタンのグループボックスを作成します。ラジオボタンのグループボックスにはラベルをつけることができます。hasFrameがTRUEならば、枠線が表示されます。'''
    return None

def GetLineAttributeData(dialogID, itemID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLineAttributeData
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLineAttributeData/ja
    \n選択されている線種と線の太さを返します。線種はインデックス（2、-1〜-32）、線の太さはミル。'''
    return (lineStyle, lineWeight)

def SelectClassChoice(dialogID, componentID, select):
    '''https://developer.vectorworks.net/index.php?title=VS:SelectClassChoice
    \nhttps://developer.vectorworks.net/index.php?title=VS:SelectClassChoice/ja
    \nShowByClassChoice を呼び出している際の、ポップアップのクラスオプションの選択状態を設定します。'''
    return None

def ShowEditTileSettingsDialog(tileHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:ShowEditTileSettingsDialog
    \nhttps://developer.vectorworks.net/index.php?title=VS:ShowEditTileSettingsDialog/ja
    \nタイル設定編集ダイアログを表示します。'''
    return tileHandle

def CreateResizableLayout(dialogTitle, hasHelp, defaultButtonName, cancelButtonName, widthResizable, heightResizable):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateResizableLayout
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateResizableLayout/ja
    \nリサイズ可能なダイアログのレイアウトを作成します。'''
    return LONGINT

def GetLineStyleChoice(dialogID, itemID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLineStyleChoice
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLineStyleChoice/ja
    \n選択されている線種を返します。線種はインデックス（2、-1〜-32）。'''
    return lineStyle

def SelectEditText(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:SelectEditText
    \nhttps://developer.vectorworks.net/index.php?title=VS:SelectEditText/ja
    \nテキストフィールドを選択状態にします。'''
    return None

def ShowEnhancedPullDownMenuGroupIcon(liDialogID, liComponentID, bShowGroupIcon):
    '''https://developer.vectorworks.net/index.php?title=VS:ShowEnhancedPullDownMenuGroupIcon
    \nhttps://developer.vectorworks.net/index.php?title=VS:ShowEnhancedPullDownMenuGroupIcon/ja
    \n指定したグループボックスのプルダウンメニューにグループアイコンを表示する／しないを設定します。'''
    return None

def CreateResourcePopup(nDialogID, nComponentID, nWidthInChars):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateResourcePopup'''
    return None

def GetLineTypeAtIndex(dialogID, itemID, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLineTypeAtIndex
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLineTypeAtIndex/ja
    \n線種ポップアップコントロールで指定した項目のラインタイプのインデックスを返します。'''
    return lineType

def SelectTreeControlItem(nDialogID, nComponentID, nItemID):
    '''https://developer.vectorworks.net/index.php?title=VS:SelectTreeControlItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:SelectTreeControlItem/ja
    \n指定したツリーアイテムの項目を選択します。'''
    return None

def ShowItem(dialogID, item, show):
    '''https://developer.vectorworks.net/index.php?title=VS:ShowItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:ShowItem/ja
    \nダイアログアイテムの表示／非表示を設定します。'''
    return None

def CreateRightStaticText(dialogID, itemID, text, widthInCharacters):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateRightStaticText
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateRightStaticText/ja
    \nCreateStaticTextのように、編集不可能なフィールドを作成します。文字列はダイアログのフィールドの右に作成されます。'''
    return None

def GetLineTypeAttriData(dialogID, itemID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLineTypeAttriData
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLineTypeAttriData/ja
    \n線種と線の太さポップアップコントロール選択されているラインタイプのインデックスと線の太さ(ミル)を返します。'''
    return (lineType, lineWeight)

def SetBelowItem(dialogID, srcItemID, belowtItemID, indent, lineSpacing):
    '''https://developer.vectorworks.net/index.php?title=VS:SetBelowItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetBelowItem/ja
    \n基準とするアイテムの下に、アイテムを配置します。挿入点からX軸、Y軸方向のオフセットを設定できます。'''
    return None

def ShowNewTileDialog():
    '''https://developer.vectorworks.net/index.php?title=VS:ShowNewTileDialog
    \nhttps://developer.vectorworks.net/index.php?title=VS:ShowNewTileDialog/ja
    \n新しいタイルダイアログを表示します。'''
    return HANDLE

def CreateSearchEditBox(dialogID, itemID, promptText, widthInStdChar):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateSearchEditBox'''
    return None

def GetLineTypeChoice(dialogID, itemID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLineTypeChoice
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLineTypeChoice/ja
    \n線種ポップアップコントロールで選択されている項目のラインタイプのインデックスを返します。'''
    return lineType

def SetBooleanItem(dialogID, componentID, setState):
    '''https://developer.vectorworks.net/index.php?title=VS:SetBooleanItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetBooleanItem/ja
    \nチェックボックスまたはラジオボタンの選択状態を設定します。'''
    return None

def UpdateImageControl2(dialogID, controlID, imageSpecifier):
    '''https://developer.vectorworks.net/index.php?title=VS:UpdateImageControl2
    \nhttps://developer.vectorworks.net/index.php?title=VS:UpdateImageControl2/ja
    \nCreateImageControl2 で作成されたイメージコントロールを更新します。'''
    return None

def CreateSeparator(dialogID, componentID, iLength):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateSeparator
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateSeparator/ja
    \nセパレータを作成します。'''
    return None

def GetLineWeightChoice(dialogID, itemID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLineWeightChoice
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLineWeightChoice/ja
    \n選択されている線の太さを返します。線の太さはミル。'''
    return lineWeight

def SetColorButton(dialogID, itemID, red, green, blue):
    '''https://developer.vectorworks.net/index.php?title=VS:SetColorButton
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetColorButton/ja
    \nカラーボタンの色を設定します。黒ならばすべての色の成分を0、白ならばすべての色の成分を65535にします。'''
    return None

def UpdateImageControl3(dialogID, controlID, imageFullPath):
    '''https://developer.vectorworks.net/index.php?title=VS:UpdateImageControl3'''
    return BOOLEAN

def CreateSheetLayerPullDownMenu(nDialogID, nComponentID, nWidthInChars):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateSheetLayerPullDownMenu
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateSheetLayerPullDownMenu/ja
    \nシートレイヤのプルダウンメニューを作成します。'''
    return None

def GetMarkerChoice(dialogID, itemID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetMarkerChoice
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetMarkerChoice/ja
    \n選択されているマーカスタイルを返します。'''
    return (index, style, angle, size)

def SetColorChoice(dialogID, itemID, colorIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:SetColorChoice
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetColorChoice/ja
    \n色ポップアップの色を設定します。'''
    return None

def UpdateImagePushButton(dialogID, controlID, imageSpecifier):
    '''https://developer.vectorworks.net/index.php?title=VS:UpdateImagePushButton
    \nhttps://developer.vectorworks.net/index.php?title=VS:UpdateImagePushButton/ja
    \nCreateImagePushButton で作成したイメージボタンを更新します。'''
    return None

def CreateStandardIconControl(dialogID, iconControlID, iconNumber):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateStandardIconControl
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateStandardIconControl/ja
    \nアプリケーションアイコンや警告アイコンで表示される標準アイコンアイテム作成します。'''
    return None

def GetMarkerPopupSelectedItem(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetMarkerPopupSelectedItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetMarkerPopupSelectedItem/ja
    \n選択されているマーカスタイルを番号（1から始まる）で返します。カスタムが選択されている場合は8を返します。'''
    return (INTEGER, style, angle, size)

def SetComponentIndeterminate(nDialogID, nComponentID, bIndeterminateState):
    '''https://developer.vectorworks.net/index.php?title=VS:SetComponentIndeterminate
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetComponentIndeterminate/ja
    \n指定された属性（線種、太さ、色など）を、3番目の未定の状態に設定します。'''
    return BOOLEAN

def UpdateSymDispCtrlN(dialogID, itemID, symbolName, view, renderMode, component, scaleByZoom):
    '''https://developer.vectorworks.net/index.php?title=VS:UpdateSymDispCtrlN'''
    return None

def CreateStaticText(dialogID, itemID, text, widthInCharacters):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateStaticText
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateStaticText/ja
    \n編集不可能なフィールドを作成します。'''
    return None

def GetMarkerValue(dialogID, itemID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetMarkerValue
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetMarkerValue/ja
    \n選択されているマーカポップアップの値を返します。（VW2008より前のバージョンのマーカポップアップ手続きの代わりになります。）'''
    return (style, angle, length, width, basis, thickness)

def SetComponentSize(nDialogID, nComponentID, nWidthPixels, nHeightPixels):
    '''https://developer.vectorworks.net/index.php?title=VS:SetComponentSize
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetComponentSize/ja
    \n指定したレイアウトダイアログのコンポーネントの幅と高さを設定します。'''
    return BOOLEAN

def UpdateSymbolDisplayControl(dialogID, itemID, symbolName, renderMode, view):
    '''https://developer.vectorworks.net/index.php?title=VS:UpdateSymbolDisplayControl
    \nhttps://developer.vectorworks.net/index.php?title=VS:UpdateSymbolDisplayControl/ja
    \nシンボルを表示するコントロールを更新します。 空白のコントロールを表示するには、シンボル名を空にしてください。'''
    return None

def CreateStyledStatic(dialogID, componentID, text, widthInCharacters, style):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateStyledStatic
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateStyledStatic/ja
    \n定義済みの文字スタイルセットで、編集不可能なフィールドを作成します。'''
    return BOOLEAN

def GetMultilineText(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetMultilineText
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetMultilineText/ja
    \nテキストフィールドに入力された文字列を返します。'''
    return text

def SetControlData(dialogID, itemID, data):
    '''https://developer.vectorworks.net/index.php?title=VS:SetControlData
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetControlData/ja
    \n指定したアイテムのデータを設定します。'''
    return None

def VerifyLayout(dialogID):
    '''https://developer.vectorworks.net/index.php?title=VS:VerifyLayout
    \nhttps://developer.vectorworks.net/index.php?title=VS:VerifyLayout/ja
    \n作成したレイアウトの整合性をチェックします。'''
    return BOOLEAN

def CreateSwapControl(dialogID, swapControlID):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateSwapControl
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateSwapControl/ja
    \nスワップペインコントロールを作成します。'''
    return None

def GetNumGradientSliderSegments(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetNumGradientSliderSegments
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNumGradientSliderSegments/ja
    \nグラデーションスライダーの変化位置の数を返します。'''
    return INTEGER

def SetControlText(DlogID, ItemID, newtext):
    '''https://developer.vectorworks.net/index.php?title=VS:SetControlText
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetControlText/ja
    \nラジオボタン、チェックボックス、ボタンに表示する文字列を設定します。'''
    return None

def AddLBImage(dialogID, componentID, resourceType, resourceID):
    '''https://developer.vectorworks.net/index.php?title=VS:AddLBImage
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddLBImage/ja
    \nイメージリソースをイメージリストに追加します。廃止予定の関数です。代わりに AddListBrowserImage を使用してください。'''
    return INTEGER

def GetLBColumnWidth(dialogID, componentID, columnIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBColumnWidth
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBColumnWidth/ja
    \n指定したリストブラウザにある指定した列の幅を返します。'''
    return (BOOLEAN, width)

def HierLBItemClosed(dialogID, componentID, itemIndex, recursive):
    '''https://developer.vectorworks.net/index.php?title=VS:HierLBItemClosed
    \nhttps://developer.vectorworks.net/index.php?title=VS:HierLBItemClosed/ja
    \nユーザがコンテナアイテムを閉じるためにクリックすると呼び出されます。閉じるコンテナ内にあるアイテムを削除します。'''
    return None

def SetLBItemFillBackColor(dialogID, componentID, itemIndex, subItemIndex, redIndex, greenIndex, blueIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBItemFillBackColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBItemFillBackColor/ja
    \nリストブラウザアイテムの面の地色を設定します。'''
    return BOOLEAN

def AddLBOriginalName(dialogID, componentID, originalName):
    '''https://developer.vectorworks.net/index.php?title=VS:AddLBOriginalName
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddLBOriginalName/ja
    \n階層表示がONで、新規アイテムをリストブラウザに追加する時に呼び出されます。'''
    return None

def GetLBControlType(dialogID, componentID, columnIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBControlType
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBControlType/ja
    \n列の制御タイプを返します。'''
    return INTEGER

def HierLBItemIsClosed(dialogID, componentID, itemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:HierLBItemIsClosed
    \nhttps://developer.vectorworks.net/index.php?title=VS:HierLBItemIsClosed/ja
    \n指定したコンテナアイテムが閉じているかを返します。'''
    return BOOLEAN

def SetLBItemFillForeColor(dialogID, componentID, itemIndex, subItemIndex, redIndex, greenIndex, blueIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBItemFillForeColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBItemFillForeColor/ja
    \nリストブラウザアイテムの面の色を設定します。'''
    return BOOLEAN

def AddListBrowserImage(dialogID, controlID, imageSpecifier):
    '''https://developer.vectorworks.net/index.php?title=VS:AddListBrowserImage
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddListBrowserImage/ja
    \nリストブラウザにイメージを追加します。AddLBImage の代わりに使用してください。'''
    return INTEGER

def GetLBEditDisplayType(dialogID, componentID, columnIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBEditDisplayType
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBEditDisplayType/ja
    \n指定した列にあるリストアイテムの表示形式を返します。'''
    return INTEGER

def HierLBItemIsContain(dialogID, componentID, itemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:HierLBItemIsContain
    \nhttps://developer.vectorworks.net/index.php?title=VS:HierLBItemIsContain/ja
    \n指定したアイテムがコンテナアイテムかを返します。'''
    return BOOLEAN

def SetLBItemGradientOrImageRefNumber(dialogID, componentID, itemIndex, subItemIndex, refNumber):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBItemGradientOrImageRefNumber
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBItemGradientOrImageRefNumber/ja
    \nリストブラウザアイテムのグラデーションまたはイメージを設定します。'''
    return BOOLEAN

def AreLBColumnLinesEnabled(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:AreLBColumnLinesEnabled
    \nhttps://developer.vectorworks.net/index.php?title=VS:AreLBColumnLinesEnabled/ja
    \n列の枠線が描かれている／いないを返します。'''
    return BOOLEAN

def GetLBEventInfo(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBEventInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBEventInfo/ja
    \nリストブラウザで最後に実行されたイベントの情報を返します。'''
    return (BOOLEAN, eventType, rowIndex, columIndex)

def HierLBItemOpened(dialogID, componentID, itemIndex, recursive):
    '''https://developer.vectorworks.net/index.php?title=VS:HierLBItemOpened
    \nhttps://developer.vectorworks.net/index.php?title=VS:HierLBItemOpened/ja
    \nユーザがコンテナアイテムを開くためにクリックすると呼び出されます。閉じている下位レベルコンテナ内にない限り、非表示だったコンテナ内のアイテムを再表示します。'''
    return numbRedisplItems

def SetLBItemHatchRefNum(dialogID, componentID, itemIndex, subItemIndex, refNumber):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBItemHatchRefNum'''
    return BOOLEAN

def AreLBRadioColumnLinesEnabled(dialogID, componentID, columnIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:AreLBRadioColumnLinesEnabled
    \nhttps://developer.vectorworks.net/index.php?title=VS:AreLBRadioColumnLinesEnabled/ja
    \n列の枠線がラジオボタンの間に描かれている／いないを返します。'''
    return BOOLEAN

def GetLBItemDashStyle(dialogID, componentID, itemIndex, subItemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBItemDashStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBItemDashStyle/ja
    \nリストブラウザアイテムの破線の種類を返します。'''
    return (BOOLEAN, styleIndex, lineWeight)

def InsertLBColumn(dialogID, componentID, columnIndex, headerString, width):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertLBColumn
    \nhttps://developer.vectorworks.net/index.php?title=VS:InsertLBColumn/ja
    \n指定したリストブラウザに列を挿入します。作成された列の番号を返します。'''
    return INTEGER

def SetLBItemInfo(dialogID, componentID, itemIndex, subItemIndex, itemString, imageIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBItemInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBItemInfo/ja
    \nアイテムにデータを設定します。'''
    return BOOLEAN

def CollapseAllLBItems(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:CollapseAllLBItems
    \nhttps://developer.vectorworks.net/index.php?title=VS:CollapseAllLBItems/ja
    \nリストブラウザが階層表示モードの時に呼び出され、トップレベルにないすべてのアイテムを削除し、すべてのコンテナアイテムを閉じます。'''
    return None

def GetLBItemData(nDialogID, nComponentID, nItemIndex, nSubItemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBItemData
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBItemData/ja
    \nリストブラウザアイテムのユーザデータを返します。'''
    return nUserData

def InsertLBColumnDataItem(dialogID, componentID, columnIndex, itemString, imageOn, imageOff, itemData):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertLBColumnDataItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:InsertLBColumnDataItem/ja
    \n指定したデータを列に挿入します。作成されたアイテムの番号を返します。'''
    return INTEGER

def SetLBItemInteracType(dialogID, componentID, itemIndex, subItemIndex, interactionType):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBItemInteracType'''
    return BOOLEAN

def CreateLB(dialogID, componentID, widthInCharacters, heightInCharacters):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateLB
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateLB/ja
    \nリストブラウザを作成します。'''
    return None

def GetLBItemDisplayType(dialogID, componentID, columnIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBItemDisplayType
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBItemDisplayType/ja
    \n指定した列にあるリストアイテムの表示形式を返します。'''
    return INTEGER

def InsertLBItem(dialogID, componentID, itemIndex, itemString):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertLBItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:InsertLBItem/ja
    \n指定したリストブラウザにアイテムを挿入します。作成されたアイテムの番号を返します。'''
    return INTEGER

def SetLBItemLineType(dialogID, componentID, itemIndex, subItemIndex, lineType, lineWeight):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBItemLineType
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBItemLineType/ja
    \n指定したリストブラウザアイテムのラインタイプを設定します。'''
    return BOOLEAN

def DeleteAllLBItems(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:DeleteAllLBItems
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeleteAllLBItems/ja
    \nリストブラウザからすべての項目を削除します。'''
    return BOOLEAN

def GetLBItemFillBackColor(dialogID, componentID, itemIndex, subItemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBItemFillBackColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBItemFillBackColor/ja
    \nリストブラウザアイテムの面の地色を返します。'''
    return (BOOLEAN, redIndex, greenIndex, blueIndex)

def IsLBColumnTrackingEnabled(dialogID, componentID, columnIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:IsLBColumnTrackingEnabled
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsLBColumnTrackingEnabled/ja
    \n指定した列で編成の有効／無効を返します。'''
    return BOOLEAN

def SetLBItemMkrByClass(dialogID, componentID, itemIndex, subItemIndex, isByClass):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBItemMkrByClass'''
    return BOOLEAN

def DeleteLBColumn(dialogID, componentID, columnIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:DeleteLBColumn
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeleteLBColumn/ja
    \n指定したリストブラウザから列を削除します。'''
    return BOOLEAN

def GetLBItemFillForeColor(dialogID, componentID, itemIndex, subItemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBItemFillForeColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBItemFillForeColor/ja
    \nリストブラウザアイテムの面の色を返します。'''
    return (BOOLEAN, redIndex, greenIndex, blueIndex)

def IsLBDisplayHier(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:IsLBDisplayHier
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsLBDisplayHier/ja
    \n指定したリストブラウザがアイテムを階層表示するよう設定されているかを返します。'''
    return BOOLEAN

def SetLBItemMkrChoice(dialogID, componentID, itemIndex, subItemIndex, style, angle, size, width, thicknessBasis, thickness):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBItemMkrChoice'''
    return BOOLEAN

def DeleteLBItem(dialogID, componentID, itemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:DeleteLBItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeleteLBItem/ja
    \n指定したリストブラウザからアイテムを削除します。'''
    return BOOLEAN

def GetLBItemGradientOrImageRefNumber(dialogID, componentID, itemIndex, subItemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBItemGradientOrImageRefNumber
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBItemGradientOrImageRefNumber/ja
    \nリストブラウザアイテムのグラデーションまたはイメージを返します。'''
    return (BOOLEAN, refNumber)

def IsLBItemReadOnly(dialogID, componentID, itemIndex, subItemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:IsLBItemReadOnly'''
    return BOOLEAN

def SetLBItemPatternIndex(dialogID, componentID, itemIndex, subItemIndex, patIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBItemPatternIndex
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBItemPatternIndex/ja
    \nリストブラウザアイテムの模様番号を設定します。'''
    return BOOLEAN

def EnableLB(dialogID, componentID, enable):
    '''https://developer.vectorworks.net/index.php?title=VS:EnableLB
    \nhttps://developer.vectorworks.net/index.php?title=VS:EnableLB/ja
    \nリストブラウザを使用する／しないを設定します。'''
    return BOOLEAN

def GetLBItemHatchRefNum(dialogID, componentID, itemIndex, subItemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBItemHatchRefNum'''
    return (BOOLEAN, refNumber)

def IsLBItemSelected(dialogID, componentID, itemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:IsLBItemSelected
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsLBItemSelected/ja
    \n指定したアイテムが現在選択されている／いないを返します。'''
    return BOOLEAN

def SetLBItemPenBackColor(dialogID, componentID, itemIndex, subItemIndex, redIndex, greenIndex, blueIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBItemPenBackColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBItemPenBackColor/ja
    \nリストブラウザアイテムの線の地色を設定します。'''
    return BOOLEAN

def EnableLBClickAllDataChange(dialogID, componentID, enable):
    '''https://developer.vectorworks.net/index.php?title=VS:EnableLBClickAllDataChange
    \nhttps://developer.vectorworks.net/index.php?title=VS:EnableLBClickAllDataChange/ja
    \nクリックする際にoption (Mac) ／alt (Win) キーを押していれば、ラジオボタンや複数選択可能な列にあるすべてのデータ項目を一回のクリックで変更する／しないを設定します。'''
    return BOOLEAN

def GetLBItemInfo(dialogID, componentID, itemIndex, subItemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBItemInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBItemInfo/ja
    \n指定したアイテムのデータを返します。'''
    return (BOOLEAN, itemString, imageIndex)

def IsLBReadOnly(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:IsLBReadOnly'''
    return BOOLEAN

def SetLBItemPenForeColor(dialogID, componentID, itemIndex, subItemIndex, redIndex, greenIndex, blueIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBItemPenForeColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBItemPenForeColor/ja
    \nリストブラウザアイテムの線の色を設定します。'''
    return BOOLEAN

def EnableLBColumnLines(dialogID, componentID, enableColumnLines):
    '''https://developer.vectorworks.net/index.php?title=VS:EnableLBColumnLines
    \nhttps://developer.vectorworks.net/index.php?title=VS:EnableLBColumnLines/ja
    \n列の枠線を作成する／しないを設定します。'''
    return None

def GetLBItemLineType(dialogID, componentID, itemIndex, subItemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBItemLineType
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBItemLineType/ja
    \n指定したリストブラウザアイテムのラインタイプを返します。'''
    return (BOOLEAN, lineType, lineWeight)

def IsLBResOnlyCurDoc(dialogID, componentID, itemIndex, subItemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:IsLBResOnlyCurDoc'''
    return BOOLEAN

def SetLBItemReadOnly(dialogID, componentID, itemIndex, subItemIndex, readOnly):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBItemReadOnly'''
    return None

def EnableLBColumnTracking(dialogID, componentID, columnIndex, enableColumnTracking):
    '''https://developer.vectorworks.net/index.php?title=VS:EnableLBColumnTracking
    \nhttps://developer.vectorworks.net/index.php?title=VS:EnableLBColumnTracking/ja
    \n列を編成する／しないを設定します。'''
    return None

def GetLBItemMkrByClass(dialogID, componentID, itemIndex, subItemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBItemMkrByClass'''
    return (BOOLEAN, isByClass)

def IsLBSortingEnabled(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:IsLBSortingEnabled
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsLBSortingEnabled/ja
    \n並び替え（ソート）の有効／無効を返します。'''
    return BOOLEAN

def SetLBItemTextColor(dialogID, componentID, itemIndex, subItemIndex, redIndex, greenIndex, blueIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBItemTextColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBItemTextColor/ja
    \nリストブラウザアイテムの文字の色を設定します。'''
    return BOOLEAN

def EnableLBDragAndDrop(dialogID, componentID, enable):
    '''https://developer.vectorworks.net/index.php?title=VS:EnableLBDragAndDrop
    \nhttps://developer.vectorworks.net/index.php?title=VS:EnableLBDragAndDrop/ja
    \nドラッグ&amp;ドロップ機能を使用する／しないを設定します。SetLBDragDropColumnを使って、ドラッグ＆ドロップ列を設定します。'''
    return BOOLEAN

def GetLBItemMkrChoice(dialogID, componentID, itemIndex, subItemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBItemMkrChoice'''
    return (BOOLEAN, style, angle, size, width, thicknessBasis, thickness)

def RefreshLB(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:RefreshLB
    \nhttps://developer.vectorworks.net/index.php?title=VS:RefreshLB/ja
    \nリストブラウザの内容を更新します。'''
    return BOOLEAN

def SetLBItemTextColorN(dialogID, componentID, itemIndex, subItemIndex, tint):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBItemTextColorN'''
    return BOOLEAN

def EnableLBExternalSort(dialogID, componentID, enable):
    '''https://developer.vectorworks.net/index.php?title=VS:EnableLBExternalSort'''
    return None

def GetLBItemOrigName(dialogID, compenentID, itemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBItemOrigName
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBItemOrigName/ja
    \n階層表示がONの時に、リストブラウザアイテムの元の名前を返します。アイテムがコンテナアイテムの場合には、空のストリングを返します。'''
    return STRING

def RemoveAllLBColumnDataItems(dialogID, componentID, columnIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:RemoveAllLBColumnDataItems
    \nhttps://developer.vectorworks.net/index.php?title=VS:RemoveAllLBColumnDataItems/ja
    \nすべての列のデータアイテムを削除します。'''
    return None

def SetLBItemTextJust(dialogID, componentID, itemIndex, subItemIndex, justification):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBItemTextJust
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBItemTextJust/ja
    \nリストブラウザアイテムの文字の位置揃えを設定します。'''
    return BOOLEAN

def EnableLBHierDisplay(dialogID, componentID, enableHierDisplay):
    '''https://developer.vectorworks.net/index.php?title=VS:EnableLBHierDisplay
    \nhttps://developer.vectorworks.net/index.php?title=VS:EnableLBHierDisplay/ja
    \nリストブラウザでアイテムを階層表示する／しないを設定します。この関数を呼んだだけでは表示は変わりません。列が階層表示する設定である必要があります。'''
    return None

def GetLBItemPatternIndex(dialogID, componentID, itemIndex, the column index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBItemPatternIndex
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBItemPatternIndex/ja
    \nリストブラウザアイテムの模様番号をを返します。'''
    return (BOOLEAN, outPatIndex)

def RemoveLBColumnDataItem(dialogID, componentID, columnIndex, columnDataItemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:RemoveLBColumnDataItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:RemoveLBColumnDataItem/ja
    \n指定した列のデータアイテムを削除します。'''
    return BOOLEAN

def SetLBItemTextStyle(dialogID, componentID, itemIndex, subItemIndex, textStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBItemTextStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBItemTextStyle/ja
    \nリストブラウザアイテムの文字のスタイルを設定します。'''
    return BOOLEAN

def EnableLBRadioColumnLines(dialogID, componentID, columnIndex, enableRadioColumnLines):
    '''https://developer.vectorworks.net/index.php?title=VS:EnableLBRadioColumnLines
    \nhttps://developer.vectorworks.net/index.php?title=VS:EnableLBRadioColumnLines/ja
    \nラジオボタンを列の線に配置する／しないを設定します。'''
    return None

def GetLBItemPenBackColor(dialogID, componentID, itemIndex, subItemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBItemPenBackColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBItemPenBackColor/ja
    \nリストブラウザアイテムの線の地色を返します。'''
    return (BOOLEAN, redIndex, greenIndex, blueIndex)

def SetFocusOnLB(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:SetFocusOnLB
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetFocusOnLB/ja
    \nリストブラウザにキーボード入力フォーカスを設定します。'''
    return BOOLEAN

def SetLBItemTileRefNum(dialogID, componentID, itemIndex, subItemIndex, refNumber):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBItemTileRefNum'''
    return BOOLEAN

def EnableLBSingleLineSelection(dialogID, componentID, enable):
    '''https://developer.vectorworks.net/index.php?title=VS:EnableLBSingleLineSelection
    \nhttps://developer.vectorworks.net/index.php?title=VS:EnableLBSingleLineSelection/ja
    \n１行のみ選択可能に設定します。'''
    return BOOLEAN

def GetLBItemPenForeColor(dialogID, componentID, itemIndex, subItemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBItemPenForeColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBItemPenForeColor/ja
    \nリストブラウザアイテムの線の色を返します。'''
    return (BOOLEAN, redIndex, greenIndex, blueIndex)

def SetLBColumnHeaderJust(dialogID, componentID, columnIndex, justification):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBColumnHeaderJust
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBColumnHeaderJust/ja
    \n指定した列ヘッダの位置揃えを設定します。'''
    return BOOLEAN

def SetLBItemUsingColumnDataItem(dialogID, componentID, itemIndex, subItemIndex, columnDataItemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBItemUsingColumnDataItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBItemUsingColumnDataItem/ja
    \n指定した列のデータアイテムにリストアイテムデータを設定します。'''
    return BOOLEAN

def EnableLBSorting(dialogID, componentID, enableSorting):
    '''https://developer.vectorworks.net/index.php?title=VS:EnableLBSorting
    \nhttps://developer.vectorworks.net/index.php?title=VS:EnableLBSorting/ja
    \n並び替え（ソート）する／しないを設定します。'''
    return None

def GetLBItemTextColor(dialogID, componentID, itemIndex, subItemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBItemTextColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBItemTextColor/ja
    \nリストブラウザアイテムの文字の色を返します。'''
    return (BOOLEAN, redIndex, greenIndex, blueIndex)

def SetLBColumnHeaderToolTip(dialogID, componentID, columnIndex, toolTipPrimaryText, toolTipSubText):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBColumnHeaderToolTip
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBColumnHeaderToolTip/ja
    \nリストブラウザの列ヘッダでツールチップとして表示される文字列を設定します。サブツールチップはcommand (Mac) ／shift (Win) を押した時に表示されます。'''
    return BOOLEAN

def SetLBMultImageIndexes(dialogID, componentID, itemIndex, subItemIndex, imageIndex0, imageIndex1, imageIndex2):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBMultImageIndexes
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBMultImageIndexes/ja
    \nリストブラウザの複数イメージ表示にあるイメージの番号を設定します。廃止予定の関数です。代わりに SetLBImageIndexes を使用してください。'''
    return BOOLEAN

def EnableLBUpdates(liDialogID, liComponentID, bEnableUpdates):
    '''https://developer.vectorworks.net/index.php?title=VS:EnableLBUpdates
    \nhttps://developer.vectorworks.net/index.php?title=VS:EnableLBUpdates/ja
    \nリストブラウザを更新する／しないを設定します。'''
    return None

def GetLBItemTextJust(dialogID, componentID, itemIndex, subItemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBItemTextJust
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBItemTextJust/ja
    \nリストブラウザアイテムの文字の位置揃えを返します。'''
    return (BOOLEAN, justification)

def SetLBColumnImage(nDialogID, nComponentID, nColumnIndex, nImageIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBColumnImage
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBColumnImage/ja
    \nリストブラウザの列ヘッダで文字の代わりにアイコンを描画します。'''
    return BOOLEAN

def SetLBNumericItemInfo(dialogID, componentID, itemIndex, subItemIndex, itemString, itemNumVal, imageIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBNumericItemInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBNumericItemInfo/ja
    \nアイテムの数値データを設定します。'''
    return BOOLEAN

def EnsureLBItemIsVisible(dialogID, componentID, index):
    '''https://developer.vectorworks.net/index.php?title=VS:EnsureLBItemIsVisible
    \nhttps://developer.vectorworks.net/index.php?title=VS:EnsureLBItemIsVisible/ja
    \nリストブラウザで、指定した行のデータが表示されるようにします。'''
    return BOOLEAN

def GetLBItemTextStyle(dialogID, componentID, itemIndex, subItemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBItemTextStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBItemTextStyle/ja
    \nリストブラウザアイテムの文字のスタイルを返します。'''
    return (BOOLEAN, textStyle)

def SetLBColumnOwnerDrawnType(dialogID, componentID, itemIndex, subItemIndex, ownerDrawnType):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBColumnOwnerDrawnType
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBColumnOwnerDrawnType/ja
    \nリストブラウザの列の描画タイプを設定します。'''
    return BOOLEAN

def SetLBOrigNameClLevel(dialogID, componentID, originalName, level1Closed, level2Closed, level3Closed):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBOrigNameClLevel
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBOrigNameClLevel/ja
    \nリストブラウザでの元のアイテムの閉じレベルを設定します。アイテムは非表示になり、適切なコンテナが閉じます。'''
    return None

def ExpandAllLBItems(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:ExpandAllLBItems
    \nhttps://developer.vectorworks.net/index.php?title=VS:ExpandAllLBItems/ja
    \nリストブラウザが階層表示モードの時に呼び出され、非表示になっていたすべてのアイテムを再表示し、すべてのコンテナを開きます。'''
    return None

def GetLBItemTileRefNum(dialogID, componentID, itemIndex, subItemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBItemTileRefNum'''
    return (BOOLEAN, refNumber)

def SetLBColumnWidth(dialogID, componentID, fromColumn, toColumn, width):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBColumnWidth
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBColumnWidth/ja
    \n指定したリストブラウザの指定した範囲の列の幅を設定します。'''
    return BOOLEAN

def SetLBReadOnly(dialogID, componentID, readOnly):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBReadOnly'''
    return None

def FindLBColumnDataItem(dialogID, componentID, columnIndex, itemString):
    '''https://developer.vectorworks.net/index.php?title=VS:FindLBColumnDataItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:FindLBColumnDataItem/ja
    \n文字列を指定して列に含まれているデータアイテムを検索します。'''
    return (BOOLEAN, columnDataItemIndex)

def GetLBMultImageIndexes(dialogID, componentID, itemIndex, subItemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBMultImageIndexes
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBMultImageIndexes/ja
    \nリストブラウザの複数イメージ表示にあるイメージの番号を返します。'''
    return (BOOLEAN, imageIndex0, imageIndex1, imageIndex2)

def SetLBControlType(dialogID, componentID, columnIndex, controlType):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBControlType
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBControlType/ja
    \n指定した列の種類を設定します。'''
    return BOOLEAN

def SetLBResOnlyCurDoc(dialogID, componentID, itemIndex, subItemIndex, onlyCurrentDoc):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBResOnlyCurDoc'''
    return None

def FindLBColumnItem(dialogID, componentID, columnIndex, itemString):
    '''https://developer.vectorworks.net/index.php?title=VS:FindLBColumnItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:FindLBColumnItem/ja
    \n文字列を指定して列に含まれているアイテムを検索します。'''
    return (BOOLEAN, itemIndex)

def GetLBOrigNameClLevel(dialogID, componentID, originalName):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBOrigNameClLevel
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBOrigNameClLevel/ja
    \nリストブラウザ内の元の名前の閉じレベルを返します。名前が表示されているときは、全てFALSEとなります。'''
    return (level1Closed, level2Closed, level3Closed)

def SetLBDragDropColumn(dialogID, componentID, columnIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBDragDropColumn
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBDragDropColumn/ja
    \nドラッグ＆ドロップ列を設定します。'''
    return BOOLEAN

def SetLBSelection(dialogID, componentID, firstItemIndex, lastItemIndex, select):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBSelection
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBSelection/ja
    \n指定した範囲のアイテムを選択します。'''
    return BOOLEAN

def GetLBColumnDataItemInfo(dialogID, componentID, columnIndex, columnDataItemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBColumnDataItemInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBColumnDataItemInfo/ja
    \n指定した列のデータ（文字列やイメージ、ユーザデータ）を返します。'''
    return (BOOLEAN, itemString, imageOn, imageOff, itemData)

def GetLBSortColumn(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBSortColumn
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBSortColumn/ja
    \nリストブラウザでソートされている列の番号を返します。'''
    return INTEGER

def SetLBEditDisplayType(dialogID, componentID, columnIndex, displayType):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBEditDisplayType
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBEditDisplayType/ja
    \n指定した列のリストアイテムの表示形式を設定します。'''
    return BOOLEAN

def SetLBSortColumn(dialogID, componentID, columnIndex, isAscending):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBSortColumn
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBSortColumn/ja
    \nリストブラウザにある特定の列をソート列として設定します。'''
    return None

def GetLBColumnHeaderJust(dialogID, componentID, columnIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBColumnHeaderJust
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBColumnHeaderJust/ja
    \n指定した列ヘッダの位置揃えを返します。'''
    return (BOOLEAN, justification)

def GetNumLBColumnDataItems(dialogID, componentID, columnIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetNumLBColumnDataItems
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNumLBColumnDataItems/ja
    \n列のデータアイテムの数を返します。'''
    return INTEGER

def SetLBHierDispColumn(dialogID, componentID, columnID):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBHierDispColumn
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBHierDispColumn/ja
    \nリストブラウザで階層表示する列を設定します。'''
    return None

def ShowLBHeader(dialogID, componentID, show):
    '''https://developer.vectorworks.net/index.php?title=VS:ShowLBHeader
    \nhttps://developer.vectorworks.net/index.php?title=VS:ShowLBHeader/ja
    \nダイアログ内のリストブラウザでヘッダ行の表示／非表示を設定します。'''
    return None

def GetLBColumnHeaderToolTip(dialogID, componentID, columnIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBColumnHeaderToolTip
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBColumnHeaderToolTip/ja
    \nリストブラウザの列ヘッダでツールチップとして表示される文字列を返します。サブツールチップはcommand (Mac) ／shift (Win) を押した時に表示されます。'''
    return (BOOLEAN, toolTipPrimaryText, toolTipSubText)

def GetNumLBColumns(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetNumLBColumns
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNumLBColumns/ja
    \n指定したリストブラウザにある列の数を返します。'''
    return INTEGER

def SetLBItemDashStyle(dialogID, componentID, itemIndex, subItemIndex, styleIndex, lineWeight):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBItemDashStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBItemDashStyle/ja
    \nリストブラウザアイテムの破線の種類を設定します。'''
    return BOOLEAN

def ShowLBItemMkrByClass(dialogID, componentID, itemIndex, subItemIndex, showByClass):
    '''https://developer.vectorworks.net/index.php?title=VS:ShowLBItemMkrByClass'''
    return None

def GetLBColumnOwnerDrawnType(dialogID, componentID, itemIndex, subItemIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBColumnOwnerDrawnType
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBColumnOwnerDrawnType/ja
    \nリストブラウザの列の描画タイプを返します。'''
    return (BOOLEAN, ownerDrawnType)

def GetNumLBItems(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetNumLBItems
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNumLBItems/ja
    \n指定したリストブラウザにあるアイテムの数を返します。'''
    return INTEGER

def SetLBItemData(nDialogID, nComponentID, nItemIndex, nSubItemIndex, nUserData):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBItemData
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBItemData/ja
    \nリストブラウザアイテムのユーザデータを設定します。'''
    return None

def ShowLBItemMkrEditLst(dialogID, componentID, itemIndex, subItemIndex, showEditList):
    '''https://developer.vectorworks.net/index.php?title=VS:ShowLBItemMkrEditLst'''
    return None

def GetLBColumnSortState(dialogID, componentID, columnIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLBColumnSortState
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLBColumnSortState/ja
    \n列のソート状態を返します。'''
    return INTEGER

def GetNumSelectedLBItems(dialogID, componentID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetNumSelectedLBItems
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNumSelectedLBItems/ja
    \nリストブラウザで選択されているアイテムの数を返します。'''
    return INTEGER

def SetLBItemDisplayType(dialogID, componentID, columnIndex, displayType):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLBItemDisplayType
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLBItemDisplayType/ja
    \n指定した列のリストアイテムの表示形式を設定します。'''
    return BOOLEAN

def AlertCritical(text, advice):
    '''https://developer.vectorworks.net/index.php?title=VS:AlertCritical
    \nhttps://developer.vectorworks.net/index.php?title=VS:AlertCritical/ja
    \n作業を継続する前に訂正が必要な問題が発生したことをユーザに知らせます。'''
    return None

def AlertQuestion(question, advice, defaultButton, OKOverrideText, CancelOverrideText, customButtonAText, customButtonBText):
    '''https://developer.vectorworks.net/index.php?title=VS:AlertQuestion
    \nhttps://developer.vectorworks.net/index.php?title=VS:AlertQuestion/ja
    \nユーザの決定を入力することができる警告ダイアログを表示します。'''
    return INTEGER

def DetailGraphicOptDlg(Marker, ShoulderLength, TagPosIndex, LeaderType, LeaderThick):
    '''https://developer.vectorworks.net/index.php?title=VS:DetailGraphicOptDlg
    \nhttps://developer.vectorworks.net/index.php?title=VS:DetailGraphicOptDlg/ja
    \n詳細引出線マーカーおよび詳細引出線オブジェクトのグラフィックオプションダイアログを表示します。'''
    return (BOOLEAN, Marker, ShoulderLength, TagPosIndex, LeaderType, LeaderThick)

def NonUndoableActionOK():
    '''https://developer.vectorworks.net/index.php?title=VS:NonUndoableActionOK
    \nhttps://developer.vectorworks.net/index.php?title=VS:NonUndoableActionOK/ja
    \n取り消しができないことをダイアログでユーザに知らせます。ユーザーが「OK」ボタンをクリックした場合はTRUEを、「キャンセル」ボタンをクリックした場合はFALSEを返します。'''
    return BOOLEAN

def AlertCriticalHLink(text, adviceBeforeLink, linkTitle, linkURL, adviceAfterLink):
    '''https://developer.vectorworks.net/index.php?title=VS:AlertCriticalHLink'''
    return None

def AlertQuestionDontShowAgain(question, advice, defaultButton, OKOverrideText, CancelOverrideText, customButtonAText, customButtonBText, arrOptions):
    '''https://developer.vectorworks.net/index.php?title=VS:AlertQuestionDontShowAgain
    \nhttps://developer.vectorworks.net/index.php?title=VS:AlertQuestionDontShowAgain/ja
    \n二度と表示しないオプション付きのユーザの決定を入力することができる警告ダイアログ表示します。'''
    return INTEGER

def DidCancel():
    '''https://developer.vectorworks.net/index.php?title=VS:DidCancel
    \nhttps://developer.vectorworks.net/index.php?title=VS:DidCancel/ja
    \n直前に表示されたダイアログで、「キャンセル」ボタンが押された場合はTRUEを返します。'''
    return BOOLEAN

def PtDialog(request, defaultX, defaultY):
    '''https://developer.vectorworks.net/index.php?title=VS:PtDialog
    \nhttps://developer.vectorworks.net/index.php?title=VS:PtDialog/ja
    \n座標を入力するためのダイアログを表示し、入力された値を返します。'''
    return (x, y)

def AlertInform(text, advice, minorAlert):
    '''https://developer.vectorworks.net/index.php?title=VS:AlertInform
    \nhttps://developer.vectorworks.net/index.php?title=VS:AlertInform/ja
    \nプログラムの実行結果を警告ダイアログに表示します。ユーザに選択肢は提供しません。'''
    return None

def AlertSetAlwaysDoVal(category, item, value):
    '''https://developer.vectorworks.net/index.php?title=VS:AlertSetAlwaysDoVal
    \nhttps://developer.vectorworks.net/index.php?title=VS:AlertSetAlwaysDoVal/ja
    \nAlertQuestionDontShowAgain と AlertInformDontShowAgain の標準ダイアログに、「常に選択した動作を行う」値を設定します。-1の値を設定すると、値はクリアされます。'''
    return None

def DistDialog(request, default):
    '''https://developer.vectorworks.net/index.php?title=VS:DistDialog
    \nhttps://developer.vectorworks.net/index.php?title=VS:DistDialog/ja
    \n距離を入力するためのダイアログを表示し、入力された値を返します。'''
    return REAL

def PtDialog3D(displayStr, xStr, yStr, zStr):
    '''https://developer.vectorworks.net/index.php?title=VS:PtDialog3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:PtDialog3D/ja
    \n3次元の座標を入力するためのダイアログを表示し、入力された値を返します。'''
    return (xPt, yPt, zPt)

def AlertInformDontShowAgain(text, advice, minorAlert, arrOptions):
    '''https://developer.vectorworks.net/index.php?title=VS:AlertInformDontShowAgain
    \nhttps://developer.vectorworks.net/index.php?title=VS:AlertInformDontShowAgain/ja
    \n二度と表示しないオプション付きのアラートダイアログ表示します。'''
    return None

def AlrtDialog(message):
    '''https://developer.vectorworks.net/index.php?title=VS:AlrtDialog
    \nhttps://developer.vectorworks.net/index.php?title=VS:AlrtDialog/ja
    \n警告ダイアログを表示します。'''
    return None

def EditSymMarkersDlg(dialogTitle, contextHelpID, inOutStartMarkerSymName, inOutEndMarkerSymName):
    '''https://developer.vectorworks.net/index.php?title=VS:EditSymMarkersDlg'''
    return (BOOLEAN, inOutStartMarkerSymName, inOutEndMarkerSymName)

def RealDialog(request, default):
    '''https://developer.vectorworks.net/index.php?title=VS:RealDialog
    \nhttps://developer.vectorworks.net/index.php?title=VS:RealDialog/ja
    \n実数を入力するためのダイアログを表示し、入力された値を返します。'''
    return REAL

def AlertInformHLink(text, adviceBeforeLink, linkTitle, linkURL, adviceAfterLink, minorAlert):
    '''https://developer.vectorworks.net/index.php?title=VS:AlertInformHLink'''
    return None

def AngDialog(request, default):
    '''https://developer.vectorworks.net/index.php?title=VS:AngDialog
    \nhttps://developer.vectorworks.net/index.php?title=VS:AngDialog/ja
    \n角度を入力するためのダイアログを表示し、入力された値を返します。'''
    return REAL

def FormatTextDialog(fontName, style, size, spacing, leading, hAlignment, vAlignment, disableMask):
    '''https://developer.vectorworks.net/index.php?title=VS:FormatTextDialog
    \nhttps://developer.vectorworks.net/index.php?title=VS:FormatTextDialog/ja
    \n文字の種類や位置揃え等を設定するためのダイアログを表示し、その内容を返します。'''
    return (fontName, style, size, spacing, leading, hAlignment, vAlignment)

def StrDialog(request, default):
    '''https://developer.vectorworks.net/index.php?title=VS:StrDialog
    \nhttps://developer.vectorworks.net/index.php?title=VS:StrDialog/ja
    \n文字列を入力するためのダイアログを表示し、入力された値を返します。'''
    return STRING

def AlertInformHLinkN(text, adviceBeforeLink, linkTitle, linkURL, adviceAfterLink, minorAlert, arrOptions):
    '''https://developer.vectorworks.net/index.php?title=VS:AlertInformHLinkN'''
    return None

def AngDialog3D(displayStr, xStr, yStr, zStr):
    '''https://developer.vectorworks.net/index.php?title=VS:AngDialog3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:AngDialog3D/ja
    \n3次元の角度を入力するためのダイアログを表示し、入力された値を返します。'''
    return (xAngleResult, yAngleResult, zAngleResult)

def IntDialog(request, default):
    '''https://developer.vectorworks.net/index.php?title=VS:IntDialog
    \nhttps://developer.vectorworks.net/index.php?title=VS:IntDialog/ja
    \n整数を入力するためのダイアログを表示し、入力された値を返します。'''
    return INTEGER

def YNDialog(s):
    '''https://developer.vectorworks.net/index.php?title=VS:YNDialog
    \nhttps://developer.vectorworks.net/index.php?title=VS:YNDialog/ja
    \n「はい」か「いいえ」を選択するダイアログを表示し、どちらのボタンが押されたかを返します。ユーザーが「はい」ボタンをクリックした場合はTRUEを、「いいえ」ボタンをクリックした場合はFALSEを返します。'''
    return BOOLEAN

def AngularDim(startPt, endPt, vert1, textOffsetDistance, arrow, textFlag, posAngle):
    '''https://developer.vectorworks.net/index.php?title=VS:AngularDim
    \nhttps://developer.vectorworks.net/index.php?title=VS:AngularDim/ja
    \n角度の寸法線を作成します。'''
    return None

def DimArcText():
    '''https://developer.vectorworks.net/index.php?title=VS:DimArcText
    \nhttps://developer.vectorworks.net/index.php?title=VS:DimArcText/ja
    \n直前に作成した円弧から寸法を作成します。'''
    return None

def GetDimText(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDimText
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDimText/ja
    \nハンドルで指定した寸法線の値を文字列で返します。'''
    return STRING

def SetDimNote(h, note):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDimNote
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDimNote/ja
    \nハンドルで指定した寸法線の注釈の文字を、指定した文字列に置き換えます。'''
    return None

def AssociateLinearDimension(h, selectedObjectsMode):
    '''https://developer.vectorworks.net/index.php?title=VS:AssociateLinearDimension
    \nhttps://developer.vectorworks.net/index.php?title=VS:AssociateLinearDimension/ja
    \n寸法の終点がオブジェクトと一致した場合、寸法線をオブジェクトと関連づけます。selectedObjectsModeがTRUEならば、選択されているオブジェクトだけがチェックされます。'''
    return None

def DimText():
    '''https://developer.vectorworks.net/index.php?title=VS:DimText
    \nhttps://developer.vectorworks.net/index.php?title=VS:DimText/ja
    \n直前に作成した直線から寸法を作成します。'''
    return None

def HasDim(h):
    '''https://developer.vectorworks.net/index.php?title=VS:HasDim
    \nhttps://developer.vectorworks.net/index.php?title=VS:HasDim/ja
    \nハンドルで指定した図形が寸法文字を含んでいればTRUEを、含んでいなければFALSEを返します。'''
    return BOOLEAN

def SetDimText(h, leaderTrailer):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDimText
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDimText/ja
    \nハンドルで指定した寸法線の値を、指定した文字列に置き換えます。'''
    return None

def CircularDim(startPt, endPt, box1, box2, textOffsetDistance, dimType, arrow, textFlag, shoulder):
    '''https://developer.vectorworks.net/index.php?title=VS:CircularDim
    \nhttps://developer.vectorworks.net/index.php?title=VS:CircularDim/ja
    \n半径、直径の寸法線を作成します。'''
    return None

def DoubleFixedTolerance(showVal, boxText, leader, trailer, topStr, botStr):
    '''https://developer.vectorworks.net/index.php?title=VS:DoubleFixedTolerance
    \nhttps://developer.vectorworks.net/index.php?title=VS:DoubleFixedTolerance/ja
    \n作成直後の寸法線に対して、上下別の公差寸法（文字）を設定します。'''
    return None

def LimitTolerance(showVal, boxText, leader, trailer, lowDistance, hiDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:LimitTolerance
    \nhttps://developer.vectorworks.net/index.php?title=VS:LimitTolerance/ja
    \n作成直後の寸法線に対して、許容限界公差寸法を設定します。'''
    return None

def SingleTolerance(showVal, boxText, leader, trailer, limDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:SingleTolerance
    \nhttps://developer.vectorworks.net/index.php?title=VS:SingleTolerance/ja
    \n作成直後の寸法線に対して、上下等の公差寸法表示を設定します。'''
    return None

def CreateChainDimension(h1, h2):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateChainDimension
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateChainDimension/ja
    \n通過する2つの寸法線または直列寸法線が、単体の直列寸法線オブジェクトになるための要件に合致すれば、新しい直列寸法線オブジェクトを作成して返します。'''
    return HANDLE

def DoubleTolerance(showVal, boxText, leader, trailer, topDistance, botDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:DoubleTolerance
    \nhttps://developer.vectorworks.net/index.php?title=VS:DoubleTolerance/ja
    \n作成直後の寸法線に対して、上下別の公差寸法表示を設定します。'''
    return None

def LinearDim(startPt, endPt, offsetDistance, dimType, arrow, textFlag, textOffset):
    '''https://developer.vectorworks.net/index.php?title=VS:LinearDim
    \nhttps://developer.vectorworks.net/index.php?title=VS:LinearDim/ja
    \n横、縦、斜めの寸法線を作成します。'''
    return None

def AddTileGeometryObject(tileHandle, objectHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:AddTileGeometryObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddTileGeometryObject/ja
    \n指定したタイルリソースに指定した図形を追加します。'''
    return BOOLEAN

def FPenColorByClass():
    '''https://developer.vectorworks.net/index.php?title=VS:FPenColorByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:FPenColorByClass/ja
    \n現在設定されている線の色に、クラス属性を使っている場合はTRUEを返します。'''
    return BOOLEAN

def GetGradientSpotColor(gradient, segmentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetGradientSpotColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetGradientSpotColor/ja
    \n変化位置の変化点の色を返します。'''
    return (red, green, blue)

def SetDashStyle(swt, numPairs, pair1, pair2, pair3, pair4, pair5):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDashStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDashStyle/ja
    \n指定された線の長さと間隔をもとに破線の種類を追加します。'''
    return None

def CreateImageFromPaint(paint, imageName):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateImageFromPaint
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateImageFromPaint/ja
    \nペイントノードからイメージを作成します。'''
    return HANDLE

def FPenFore():
    '''https://developer.vectorworks.net/index.php?title=VS:FPenFore
    \nhttps://developer.vectorworks.net/index.php?title=VS:FPenFore/ja
    \n現在設定されている線の色成分を返します。値の範囲は0から65535までです。'''
    return (red, green, blue)

def GetGradientSpotPosition(gradient, segmentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetGradientSpotPosition
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetGradientSpotPosition/ja
    \n変化位置の変化点の位置を返します。'''
    return position

def SetDashStyleN(name, swt, numPairs, pair1, pair2, pair3, pair4, pair5):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDashStyleN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDashStyleN/ja
    \n指定された名前と線の長さと間隔をもとに破線の種類を追加します。'''
    return None

def CreateImgFromSymbol(symbolName, symbolHeight, symbolWidth, symbolMargin, renderMode, view):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateImgFromSymbol'''
    return HANDLE

def FPenPat():
    '''https://developer.vectorworks.net/index.php?title=VS:FPenPat
    \nhttps://developer.vectorworks.net/index.php?title=VS:FPenPat/ja
    \n現在設定されている線の模様を返します。'''
    return INTEGER

def GetNumDashDataPairs(dashIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetNumDashDataPairs
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNumDashDataPairs/ja
    \n指定した破線の種類で定義されている、破線／間隔のペアの数を返します。 線の太さに連動しているかどうかも返します。 破線／間隔のペアは最大で5組です。'''
    return (INTEGER, swt)

def SetDefOpacityByClsN(inIsPenOpacityByClass, inIsFillOpacityByClass):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDefOpacityByClsN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDefOpacityByClsN/ja'''
    return None

def CreateImgFromSymbolN(symbolName, width, height, margin, renderMode, view, component):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateImgFromSymbolN'''
    return HANDLE

def FPenPatN():
    '''https://developer.vectorworks.net/index.php?title=VS:FPenPatN
    \nhttps://developer.vectorworks.net/index.php?title=VS:FPenPatN/ja
    \n現在設定されている線の模様を返します。'''
    return LONGINT

def GetNumDashDataPairsN(dashIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetNumDashDataPairsN'''
    return (INTEGER, swt)

def SetDefaultBeginningMarker(style, angle, size, width, thicknessBasis, thickness, visibility):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDefaultBeginningMarker
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDefaultBeginningMarker/ja
    \nファイルのデフォルト始点マーカのすべての設定値を設定します。正常終了するとTRUEが返されます。'''
    return BOOLEAN

def CreateTile(tileName):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateTile
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateTile/ja
    \nタイルを新規に作成します。'''
    return HANDLE

def FPenSize():
    '''https://developer.vectorworks.net/index.php?title=VS:FPenSize
    \nhttps://developer.vectorworks.net/index.php?title=VS:FPenSize/ja
    \n現在設定されている線の太さを返します。'''
    return INTEGER

def GetNumGradientSegments(gradient):
    '''https://developer.vectorworks.net/index.php?title=VS:GetNumGradientSegments
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNumGradientSegments/ja
    \nグラデーションの変化位置の数を返します。'''
    return INTEGER

def SetDefaultEndMarker(style, angle, size, width, thicknessBasis, thickness, visibility):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDefaultEndMarker
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDefaultEndMarker/ja
    \nファイルのデフォルト終点マーカのすべての設定値を設定します。正常終了するとTRUEが返されます。'''
    return BOOLEAN

def DS_GetAngle():
    '''https://developer.vectorworks.net/index.php?title=VS:DS_GetAngle
    \nhttps://developer.vectorworks.net/index.php?title=VS:DS_GetAngle/ja
    \n書類の影の角度を返します。'''
    return REAL

def FillBack(color):
    '''https://developer.vectorworks.net/index.php?title=VS:FillBack
    \nhttps://developer.vectorworks.net/index.php?title=VS:FillBack/ja
    \n現在設定されている面の地色を変更します。値の範囲は0から65535までです。'''
    return None

def GetTileBackgroundColor(tileHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTileBackgroundColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTileBackgroundColor/ja
    \n指定したタイルリソースの背景色を取得します。'''
    return (red, green, blue)

def SetDefaultOpacity(opacity):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDefaultOpacity
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDefaultOpacity/ja
    \nデフォルトの不透明度を設定します。'''
    return None

def DS_GetFillStyle():
    '''https://developer.vectorworks.net/index.php?title=VS:DS_GetFillStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:DS_GetFillStyle/ja
    \n書類の、影の面属性、面属性の名前、あるいは色インデックスを返します。'''
    return (shadowFillStyle, shadowFillName, solidColorRef)

def FillFore(color):
    '''https://developer.vectorworks.net/index.php?title=VS:FillFore
    \nhttps://developer.vectorworks.net/index.php?title=VS:FillFore/ja
    \n現在設定されている面の色を変更します。値の範囲は0から65535までです。'''
    return None

def GetTileGeometryGroup(tileHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTileGeometryGroup
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTileGeometryGroup/ja
    \nタイルリソースの形状グループを取得します。'''
    return HANDLE

def SetDefaultOpacityByClass():
    '''https://developer.vectorworks.net/index.php?title=VS:SetDefaultOpacityByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDefaultOpacityByClass/ja
    \n現在のクラスの不透明度を、デフォルトの不透明度に設定します。'''
    return None

def DS_GetOffset():
    '''https://developer.vectorworks.net/index.php?title=VS:DS_GetOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:DS_GetOffset/ja
    \n書類の影のオフセットを返します'''
    return REAL

def FillPat(patNumber):
    '''https://developer.vectorworks.net/index.php?title=VS:FillPat
    \nhttps://developer.vectorworks.net/index.php?title=VS:FillPat/ja
    \nアクティブな面の模様を設定します。この手続きの後に作成された図形は指定した面の模様が使われます。'''
    return None

def GetTileGroupParent(groupHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTileGroupParent
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTileGroupParent/ja
    \n指定したタイルグループを内包するコンテナのハンドルを取得します。'''
    return HANDLE

def SetDefaultOpacityN(inPenOpacity, inFillOpacity):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDefaultOpacityN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDefaultOpacityN/ja'''
    return None

def DS_GetOffsetUnit():
    '''https://developer.vectorworks.net/index.php?title=VS:DS_GetOffsetUnit
    \nhttps://developer.vectorworks.net/index.php?title=VS:DS_GetOffsetUnit/ja
    \n書類の影のオフセットの単位を返します'''
    return INTEGER

def GetDashDataValPairAt(dashStyleIndex, dataIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDashDataValPairAt
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDashDataValPairAt/ja
    \n指定した破線の種類の破線データを返します。 破線データは破線／間隔のペアです。 破線の種類や破線データがない場合はFalseを返します。 破線の種類では破線／間隔のペアを5つまで指定できます。'''
    return (BOOLEAN, dash, gap)

def GetTileOffsetPoint(tileHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTileOffsetPoint
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTileOffsetPoint/ja
    \n指定したタイルリソースのオフセットポイントを取得します。'''
    return offsetPoint

def SetDocDrpShadowData(bUseDropShadow, nUnits, dOffset, dBlurRadius, dAngle, nOpacity, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDocDrpShadowData
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDocDrpShadowData/ja'''
    return None

def DS_GetOpacity():
    '''https://developer.vectorworks.net/index.php?title=VS:DS_GetOpacity
    \nhttps://developer.vectorworks.net/index.php?title=VS:DS_GetOpacity/ja
    \n書類の影の不透明度を返します。'''
    return LONGINT

def GetDashDataValPrAtN(dashStyleIndex, dataIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDashDataValPrAtN'''
    return (BOOLEAN, dash, gap)

def GetTileRepetitionPoint(tileHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTileRepetitionPoint
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTileRepetitionPoint/ja
    \n指定したタイルリソースの繰り返しポイントを取得します。'''
    return repetitionPoint

def SetDocDrpShadwByCls(bEnable):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDocDrpShadwByCls
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDocDrpShadwByCls/ja'''
    return None

def DS_IsOpacityByClass():
    '''https://developer.vectorworks.net/index.php?title=VS:DS_IsOpacityByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:DS_IsOpacityByClass/ja
    \n書類の影の不透明度がクラスによるかどうかを返します。'''
    return BOOLEAN

def GetDashStyle(swt, numPairs, pair1, pair2, pair3, pair4, pair5):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDashStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDashStyle/ja
    \n現在設定されている破線の種類を返します。'''
    return INTEGER

def InsertGradientData(gradient, spotPosition, midpointPosition, red, green, blue, opacity):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertGradientData
    \nhttps://developer.vectorworks.net/index.php?title=VS:InsertGradientData/ja
    \nグラデーションに新しい変化位置を挿入し、そのデータを指定した値で初期化します。'''
    return INTEGER

def SetDocumentDefaultSketchStyle(sketchName):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDocumentDefaultSketchStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDocumentDefaultSketchStyle/ja
    \nドキュメントデフォルトのスケッチスタイルを設定します。'''
    return BOOLEAN

def DS_IsUnderCanopy():
    '''https://developer.vectorworks.net/index.php?title=VS:DS_IsUnderCanopy
    \nhttps://developer.vectorworks.net/index.php?title=VS:DS_IsUnderCanopy/ja
    \nファイル設定で、影が樹冠の下に表示されるかどうかを返します。'''
    return BOOLEAN

def GetDashStyleIndex(swt, numPairs, pair1, pair2, pair3, pair4, pair5):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDashStyleIndex
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDashStyleIndex/ja
    \n現在設定されている破線の名前と種類を返します。'''
    return INTEGER

def InsertGradientSegment(gradient, spotPosition, midpointPosition, red, green, blue):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertGradientSegment
    \nhttps://developer.vectorworks.net/index.php?title=VS:InsertGradientSegment/ja
    \nグラデーションに新しい変化位置を挿入し、そのデータを指定した値で初期化します。'''
    return INTEGER

def SetGradientData(gradient, segmentIndex, spotPosition, midpointPosition, red, green, blue):
    '''https://developer.vectorworks.net/index.php?title=VS:SetGradientData
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetGradientData/ja
    \n変化位置の変化点、変化の中心点の位置や色を設定します。'''
    return segmentIndex

def DefDrpShadowEnabled():
    '''https://developer.vectorworks.net/index.php?title=VS:DefDrpShadowEnabled
    \nhttps://developer.vectorworks.net/index.php?title=VS:DefDrpShadowEnabled/ja'''
    return BOOLEAN

def GetDashStyleIndexN(swt, numPairs, pair1, pair2, pair3, pair4, pair5):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDashStyleIndexN'''
    return LONGINT

def IsTileGroupContainedObject(objectHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:IsTileGroupContainedObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsTileGroupContainedObject/ja
    \n指定した図形がタイルグループに含まれている/いないを返します。'''
    return BOOLEAN

def SetGradientDataN(gradient, segmentIndex, spotPosition, midpointPosition, red, green, blue, opacity):
    '''https://developer.vectorworks.net/index.php?title=VS:SetGradientDataN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetGradientDataN/ja
    \n変化位置の変化点、変化の中心点の位置や色、不透明度を設定します。注：変化位置の番号には初期化した変数を使わなければなりません。変化点の位置が変更されデータが設定された後は、変数に変化位置の番号を返します。'''
    return segmentIndex

def DocDropShadowByCls():
    '''https://developer.vectorworks.net/index.php?title=VS:DocDropShadowByCls
    \nhttps://developer.vectorworks.net/index.php?title=VS:DocDropShadowByCls/ja'''
    return BOOLEAN

def GetDashStyleN(swt, numPairs, pair1, pair2, pair3, pair4, pair5):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDashStyleN'''
    return LONGINT

def IsUserColor(ColorIDX):
    '''https://developer.vectorworks.net/index.php?title=VS:IsUserColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsUserColor/ja
    \n色がユーザ色の場合は、TRUEを返します。'''
    return (BOOLEAN, ColorName)

def SetGradientMidpointPosition(gradient, segmentIndex, position):
    '''https://developer.vectorworks.net/index.php?title=VS:SetGradientMidpointPosition
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetGradientMidpointPosition/ja
    \n変化位置の変化の中心点の位置を設定します。'''
    return None

def EnableDefDropShadow(bEnable):
    '''https://developer.vectorworks.net/index.php?title=VS:EnableDefDropShadow
    \nhttps://developer.vectorworks.net/index.php?title=VS:EnableDefDropShadow/ja'''
    return None

def GetDefOpacityByClsN():
    '''https://developer.vectorworks.net/index.php?title=VS:GetDefOpacityByClsN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDefOpacityByClsN/ja'''
    return (outDefFillOpacityByClass, outDefPenOpacityByClass)

def Marker(style, size, ang):
    '''https://developer.vectorworks.net/index.php?title=VS:Marker
    \nhttps://developer.vectorworks.net/index.php?title=VS:Marker/ja
    \n現在設定されているマーカスタイル、長さ（インチ）、角度（度数）を変更します。'''
    return None

def SetGradientOpacity(gradient, segmentIndex, opacity):
    '''https://developer.vectorworks.net/index.php?title=VS:SetGradientOpacity
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetGradientOpacity/ja'''
    return None

def FFPatByClass():
    '''https://developer.vectorworks.net/index.php?title=VS:FFPatByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:FFPatByClass/ja
    \n現在設定されている面の模様に、クラス属性を使っている場合はTRUEを返します。'''
    return BOOLEAN

def GetDefaultBeginningMarker():
    '''https://developer.vectorworks.net/index.php?title=VS:GetDefaultBeginningMarker
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDefaultBeginningMarker/ja
    \nファイルのデフォルト始点マーカのすべての設定値を返します。正常終了するとTRUEが返されます。'''
    return (BOOLEAN, style, angle, size, width, thicknessBasis, thickness, visibility)

def NumColors():
    '''https://developer.vectorworks.net/index.php?title=VS:NumColors
    \nhttps://developer.vectorworks.net/index.php?title=VS:NumColors/ja
    \n現在のファイルで最後に使用した色番号を返します。'''
    return INTEGER

def SetGradientSpotColor(gradient, segmentIndex, red, green, blue):
    '''https://developer.vectorworks.net/index.php?title=VS:SetGradientSpotColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetGradientSpotColor/ja
    \n変化位置の変化点を設定します。'''
    return None

def FFillBack():
    '''https://developer.vectorworks.net/index.php?title=VS:FFillBack
    \nhttps://developer.vectorworks.net/index.php?title=VS:FFillBack/ja
    \n現在設定されている面の地色の成分を返します。値の範囲は0から65535までです。'''
    return (red, green, blue)

def GetDefaultEndMarker():
    '''https://developer.vectorworks.net/index.php?title=VS:GetDefaultEndMarker
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDefaultEndMarker/ja
    \nファイルのデフォルト終点マーカのすべての設定値を返します。正常終了するとTRUEが返されます。'''
    return (BOOLEAN, style, angle, size, width, thicknessBasis, thickness, visibility)

def NumDashStyles():
    '''https://developer.vectorworks.net/index.php?title=VS:NumDashStyles
    \nhttps://developer.vectorworks.net/index.php?title=VS:NumDashStyles/ja
    \n現在設定されている破線の数を返します。'''
    return INTEGER

def SetGradientSpotPosition(gradient, segmentIndex, position):
    '''https://developer.vectorworks.net/index.php?title=VS:SetGradientSpotPosition
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetGradientSpotPosition/ja
    \n変化位置の変化点の位置を設定します。'''
    return segmentIndex

def FFillColorByClass():
    '''https://developer.vectorworks.net/index.php?title=VS:FFillColorByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:FFillColorByClass/ja
    \n現在設定されている面の色に、クラス属性を使っている場合はTRUEを返します。'''
    return BOOLEAN

def GetDefaultOpacity():
    '''https://developer.vectorworks.net/index.php?title=VS:GetDefaultOpacity
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDefaultOpacity/ja
    \nデフォルトの不透明度に返します。'''
    return opacity

def Opacity(opacity):
    '''https://developer.vectorworks.net/index.php?title=VS:Opacity
    \nhttps://developer.vectorworks.net/index.php?title=VS:Opacity/ja
    \nアクティブな不透明度を設定します。'''
    return None

def SetTileBackgroundColor(tileHandle, backgroundColor):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTileBackgroundColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTileBackgroundColor/ja
    \n指定したタイルリソースの背景色を設定します。'''
    return None

def FFillFore():
    '''https://developer.vectorworks.net/index.php?title=VS:FFillFore
    \nhttps://developer.vectorworks.net/index.php?title=VS:FFillFore/ja
    \n現在設定されている面の色の成分を返します。値の範囲は0から65535までです。'''
    return (red, green, blue)

def GetDefaultOpacityN():
    '''https://developer.vectorworks.net/index.php?title=VS:GetDefaultOpacityN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDefaultOpacityN/ja'''
    return (outPenOpacity, outFillOpacity)

def OpacityN(fillOpacity, penOpacity):
    '''https://developer.vectorworks.net/index.php?title=VS:OpacityN
    \nhttps://developer.vectorworks.net/index.php?title=VS:OpacityN/ja'''
    return None

def SetTileOffsetPoint(tileHandle, offsetPoint):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTileOffsetPoint
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTileOffsetPoint/ja
    \n指定したタイルリソースのオフセットポイントを設定します。'''
    return None

def FFillPat():
    '''https://developer.vectorworks.net/index.php?title=VS:FFillPat
    \nhttps://developer.vectorworks.net/index.php?title=VS:FFillPat/ja
    \n現在設定されている模様番号を返します。'''
    return LONGINT

def GetDocDrpShadowData():
    '''https://developer.vectorworks.net/index.php?title=VS:GetDocDrpShadowData
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDocDrpShadowData/ja'''
    return (bUseDropShadow, nUnits, dOffset, dBlurRadius, dAngle, nOpacity, colorRV, colorGV, colorBV)

def PenBack(color):
    '''https://developer.vectorworks.net/index.php?title=VS:PenBack
    \nhttps://developer.vectorworks.net/index.php?title=VS:PenBack/ja
    \n現在設定されている線の地色を変更します。値の範囲は0から65535までです。'''
    return None

def SetTileRepetitionPoint(tileHandle, repetitionPoint):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTileRepetitionPoint
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTileRepetitionPoint/ja
    \n指定したタイルリソースの繰り返しポイントを設定します。'''
    return None

def FLSByClass():
    '''https://developer.vectorworks.net/index.php?title=VS:FLSByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:FLSByClass/ja
    \n現在設定されている線の種類に、クラス属性を使っている場合はTRUEを返します。'''
    return BOOLEAN

def GetDocumentDefaultSketchStyle():
    '''https://developer.vectorworks.net/index.php?title=VS:GetDocumentDefaultSketchStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDocumentDefaultSketchStyle/ja
    \nドキュメントデフォルトのスケッチスタイルを返します。'''
    return STRING

def PenFore(color):
    '''https://developer.vectorworks.net/index.php?title=VS:PenFore
    \nhttps://developer.vectorworks.net/index.php?title=VS:PenFore/ja
    \n現在設定されている線の色を変更します。値の範囲は0から65535までです。'''
    return None

def SheetList(sheetIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:SheetList
    \nhttps://developer.vectorworks.net/index.php?title=VS:SheetList/ja
    \n番号で指定した登録画面の名前を返します。'''
    return STRING

def FLWByClass():
    '''https://developer.vectorworks.net/index.php?title=VS:FLWByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:FLWByClass/ja
    \n現在設定されている線の太さに、クラス属性を使っている場合はTRUEを返します。'''
    return BOOLEAN

def GetGradientData(gradient, segmentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetGradientData
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetGradientData/ja
    \n変化位置の変化点、変化の中心点の位置と色を返します。'''
    return (spotPosition, midpointPosition, red, green, blue)

def PenPat(patNumber):
    '''https://developer.vectorworks.net/index.php?title=VS:PenPat
    \nhttps://developer.vectorworks.net/index.php?title=VS:PenPat/ja
    \nアクティブな線の模様／種類を設定します。'''
    return None

def SheetNum():
    '''https://developer.vectorworks.net/index.php?title=VS:SheetNum
    \nhttps://developer.vectorworks.net/index.php?title=VS:SheetNum/ja
    \nドキュメントに含まれる登録画面の数を返します。'''
    return INTEGER

def FMarker():
    '''https://developer.vectorworks.net/index.php?title=VS:FMarker
    \nhttps://developer.vectorworks.net/index.php?title=VS:FMarker/ja
    \n現在設定されているマーカスタイル、長さ（インチ）、角度（度数）を返します。'''
    return (style, size, ang)

def GetGradientDataN(gradient, segmentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetGradientDataN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetGradientDataN/ja'''
    return (Boolean, spotPosition, midpointPosition, red, green, blue, opacity)

def PenPatN(patNumber):
    '''https://developer.vectorworks.net/index.php?title=VS:PenPatN
    \nhttps://developer.vectorworks.net/index.php?title=VS:PenPatN/ja
    \nアクティブな線の模様／種類を、0から71または負の値で設定します。'''
    return None

def ShowCreateImageDialog():
    '''https://developer.vectorworks.net/index.php?title=VS:ShowCreateImageDialog
    \nhttps://developer.vectorworks.net/index.php?title=VS:ShowCreateImageDialog/ja
    \nダイアログを表示して、イメージ属性を作成するためのファイルをユーザーに選択させます。'''
    return HANDLE

def FMarkerByClass():
    '''https://developer.vectorworks.net/index.php?title=VS:FMarkerByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:FMarkerByClass/ja
    \n現在設定されているマーカの種類に、クラス属性を使っている場合はTRUEを返します。'''
    return BOOLEAN

def GetGradientMidpointPosition(gradient, segmentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetGradientMidpointPosition
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetGradientMidpointPosition/ja
    \n変化位置の変化の中心点の位置を返します。'''
    return position

def PenSize(lw):
    '''https://developer.vectorworks.net/index.php?title=VS:PenSize
    \nhttps://developer.vectorworks.net/index.php?title=VS:PenSize/ja
    \n現在設定されている線の太さを変更します。'''
    return None

def ShowGradientEditorDialog(gradient):
    '''https://developer.vectorworks.net/index.php?title=VS:ShowGradientEditorDialog
    \nhttps://developer.vectorworks.net/index.php?title=VS:ShowGradientEditorDialog/ja
    \nグラデーションの編集ダイアログを表示します。'''
    return gradient

def FPenBack():
    '''https://developer.vectorworks.net/index.php?title=VS:FPenBack
    \nhttps://developer.vectorworks.net/index.php?title=VS:FPenBack/ja
    \n現在設定されている線の地色の成分を返します。値の範囲は0から65535までです。'''
    return (red, green, blue)

def GetGradientOpacity(gradient, segmentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetGradientOpacity
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetGradientOpacity/ja'''
    return opacity

def RemoveGradientSegment(gradient, segmentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:RemoveGradientSegment
    \nhttps://developer.vectorworks.net/index.php?title=VS:RemoveGradientSegment/ja
    \nグラデーションから変化位置を削除します。'''
    return None

def ShowPlanShadowsTab():
    '''https://developer.vectorworks.net/index.php?title=VS:ShowPlanShadowsTab
    \nhttps://developer.vectorworks.net/index.php?title=VS:ShowPlanShadowsTab/ja
    \n「ファイル設定」ダイアログの「影の表現」タブを開く。'''
    return BOOLEAN

def AddResourceToList(listID, resource):
    '''https://developer.vectorworks.net/index.php?title=VS:AddResourceToList
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddResourceToList/ja
    \n指定したリソースリストにリソースを追加します。リスト内の番号、または0を返します。'''
    return LONGINT

def FInSymDef(sdHd):
    '''https://developer.vectorworks.net/index.php?title=VS:FInSymDef
    \nhttps://developer.vectorworks.net/index.php?title=VS:FInSymDef/ja
    \nハンドルで指定した登録シンボルの中で最上位の図形のハンドルを返します。'''
    return HANDLE

def LSActLayer():
    '''https://developer.vectorworks.net/index.php?title=VS:LSActLayer
    \nhttps://developer.vectorworks.net/index.php?title=VS:LSActLayer/ja
    \nアクティブなレイヤ上で選択されている最下位の図形のハンドルを返します。図形が存在しない場合はNILを返します。'''
    return HANDLE

def ResList_Filter(uniqueID, callback):
    '''https://developer.vectorworks.net/index.php?title=VS:ResList_Filter'''
    return None

def BeginFolder():
    '''https://developer.vectorworks.net/index.php?title=VS:BeginFolder
    \nhttps://developer.vectorworks.net/index.php?title=VS:BeginFolder/ja
    \nこの手続きを実行した後、EndFolderを実行するまでの間に作成されたシンボルをシンボルフォルダに入れます。シンボルフォルダの名前は、この手続きの直前にNameObjectを実行して設定します。'''
    return None

def FObject():
    '''https://developer.vectorworks.net/index.php?title=VS:FObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:FObject/ja
    \nドキュメント内にある最上位の図形のハンドルを返します。図形が存在しない場合はNILを返します。'''
    return HANDLE

def NextDObj(h):
    '''https://developer.vectorworks.net/index.php?title=VS:NextDObj
    \nhttps://developer.vectorworks.net/index.php?title=VS:NextDObj/ja
    \nハンドルで指定した図形の次にある図形のうち、選択されていないもののハンドルを返します。図形が存在しない場合はNILを返します。'''
    return HANDLE

def ResList_FilterNonAct(uniqueID, callback):
    '''https://developer.vectorworks.net/index.php?title=VS:ResList_FilterNonAct'''
    return None

def BeginFolderN(type):
    '''https://developer.vectorworks.net/index.php?title=VS:BeginFolderN'''
    return None

def FSActLayer():
    '''https://developer.vectorworks.net/index.php?title=VS:FSActLayer
    \nhttps://developer.vectorworks.net/index.php?title=VS:FSActLayer/ja
    \nアクティブなレイヤ上で選択されている最上位の図形のハンドルを返します。図形が存在しない場合はNILを返します。'''
    return HANDLE

def NextLayer(h):
    '''https://developer.vectorworks.net/index.php?title=VS:NextLayer
    \nhttps://developer.vectorworks.net/index.php?title=VS:NextLayer/ja
    \nハンドルで指定したレイヤの次にあるレイヤのハンドルを返します。図形が存在しない場合はNILを返します。'''
    return HANDLE

def ResList_GetSel(uniqueID):
    '''https://developer.vectorworks.net/index.php?title=VS:ResList_GetSel
    \nhttps://developer.vectorworks.net/index.php?title=VS:ResList_GetSel/ja
    \nポップアップからリソースを選択します。 uniqueIDはこのコントロールを識別する固有の文字列です。'''
    return STRING

def BuildResourceList(type, folderIndex, subFolderName):
    '''https://developer.vectorworks.net/index.php?title=VS:BuildResourceList
    \nhttps://developer.vectorworks.net/index.php?title=VS:BuildResourceList/ja
    \n指定した種類のリソースリストを作成して、リソースリストの番号を返します。リソースリスト内の値は、GetNameFromResourceListを使って取得することができます。'''
    return (LONGINT, numItems)

def FSObject(h):
    '''https://developer.vectorworks.net/index.php?title=VS:FSObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:FSObject/ja
    \nハンドルで指定したレイヤ上で選択されている最上位の図形のハンドルを返します。図形が存在しない場合はNILを返します。'''
    return HANDLE

def NextObj(h):
    '''https://developer.vectorworks.net/index.php?title=VS:NextObj
    \nhttps://developer.vectorworks.net/index.php?title=VS:NextObj/ja
    \nハンドルで指定した図形の次にある図形のハンドルを返します。図形が存在しない場合はNILを返します。'''
    return HANDLE

def ResList_GetSelIsDoc(uniqueID):
    '''https://developer.vectorworks.net/index.php?title=VS:ResList_GetSelIsDoc
    \nhttps://developer.vectorworks.net/index.php?title=VS:ResList_GetSelIsDoc/ja
    \n選択されたリソースが現在の書類内にあるかどうかを返します。 uniqueIDはこのコントロールを識別する固有の文字列です。'''
    return BOOLEAN

def BuildResourceList2(type, folderIndex, subFolderName, useDefaultContent):
    '''https://developer.vectorworks.net/index.php?title=VS:BuildResourceList2
    \nhttps://developer.vectorworks.net/index.php?title=VS:BuildResourceList2/ja
    \n指定した種類のリソースリストを作成して、リソースリストの番号を返します。リソースリスト内の値は、GetNameFromResourceListを使って取得することができます。環境設定-標準リソースを表示 (#130)  にチェックが入っていて、folderIndexパラメータの値が0でない場合、指定したフォルダ内にあるすべてのドキュメントに含まれる指定した種類のリソースすべてを含みます。folderIndexパラメータの値が正の数の場合、アクティブなドキュメントと指定したフォルダ内にあるすべてのドキュメントに含まれる指定した種類のリソースがリソースリストに含まれます。folderIndexパラメータの値が0の場合、アクティブなドキュメントにある指定した種類のリソースがリソースリストに含まれます。folderIndexパラメータの値が負の数の場合、指定したフォルダ内にあるすべてのドキュメントに含まれる指定した種類のリソースがリソースリストに含まれます。'''
    return (LONGINT, numItems)

def FSymDef():
    '''https://developer.vectorworks.net/index.php?title=VS:FSymDef
    \nhttps://developer.vectorworks.net/index.php?title=VS:FSymDef/ja
    \nシンボルライブラリに登録されている最上位のシンボルのハンドルを返します。図形が存在しない場合はNILを返します。'''
    return HANDLE

def NextSObj(h):
    '''https://developer.vectorworks.net/index.php?title=VS:NextSObj
    \nhttps://developer.vectorworks.net/index.php?title=VS:NextSObj/ja
    \nハンドルで指定した図形の次にある図形のうち、選択されている図形のハンドルを返します。図形が存在しない場合はNILを返します。'''
    return HANDLE

def ResList_ImportItem(uniqueID):
    '''https://developer.vectorworks.net/index.php?title=VS:ResList_ImportItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:ResList_ImportItem/ja
    \n選択されているリソースをインポートします。 一般的にはBuildResourceList の呼びだしで作成されたリストです。 uniqueIDはこのコントロールを識別する固有の文字列です。'''
    return HANDLE

def BuildResourceListN(type, fullPath):
    '''https://developer.vectorworks.net/index.php?title=VS:BuildResourceListN
    \nhttps://developer.vectorworks.net/index.php?title=VS:BuildResourceListN/ja
    \n指定したファイルからリソースのリストを作成します。'''
    return (LONGINT, numItems)

def ForEachMaterial(onlyUsed, callback):
    '''https://developer.vectorworks.net/index.php?title=VS:ForEachMaterial'''
    return None

def NextSymDef(symHd):
    '''https://developer.vectorworks.net/index.php?title=VS:NextSymDef
    \nhttps://developer.vectorworks.net/index.php?title=VS:NextSymDef/ja
    \nハンドルで指定した登録シンボルの次にある登録シンボルのハンドルを返します。図形が存在しない場合はNILを返します。'''
    return HANDLE

def ResList_ImportItemN(uniqueID, doConflict):
    '''https://developer.vectorworks.net/index.php?title=VS:ResList_ImportItemN
    \nhttps://developer.vectorworks.net/index.php?title=VS:ResList_ImportItemN/ja
    \n選択されているリソースをインポートします。 doConflict: 0 - インポートしない; 1 - 置き換える; 2 - リネームする; 3 - UIで指定する; uniqueIDはこのコントロールを識別する固有の文字列です。'''
    return HANDLE

def BuildResourceListN2(type, fullPath, useDefaultContent):
    '''https://developer.vectorworks.net/index.php?title=VS:BuildResourceListN2
    \nhttps://developer.vectorworks.net/index.php?title=VS:BuildResourceListN2/ja
    \n指定したファイルからリソースのリストを作成します。'''
    return (LONGINT, numItems)

def GetActualNameFromResourceList(listID, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetActualNameFromResourceList
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetActualNameFromResourceList/ja
    \n指定したリソースリストにあるリソースの名前を返します。'''
    return STRING

def PrevDObj(h):
    '''https://developer.vectorworks.net/index.php?title=VS:PrevDObj
    \nhttps://developer.vectorworks.net/index.php?title=VS:PrevDObj/ja
    \nハンドルで指定した図形の前にある図形のうち、選択されていない図形のハンドルを返します。図形が存在しない場合はNILを返します。'''
    return HANDLE

def ResList_Init(uniqueID, objectType):
    '''https://developer.vectorworks.net/index.php?title=VS:ResList_Init
    \nhttps://developer.vectorworks.net/index.php?title=VS:ResList_Init/ja
    \nカテゴリリソースを指定したタイプのリソースで初期化します。 uniqueIDはこのコントロールを識別する固有の文字列です。'''
    return None

def DeleteResourceFromList(listID, index):
    '''https://developer.vectorworks.net/index.php?title=VS:DeleteResourceFromList
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeleteResourceFromList/ja
    \n指定したリソースリストから指定した番号の図形を削除します。'''
    return None

def GetNameFromResourceList(listID, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetNameFromResourceList
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNameFromResourceList/ja
    \n指定したリソースリストにあるリソースの名前を返します。'''
    return STRING

def PrevLayer(h):
    '''https://developer.vectorworks.net/index.php?title=VS:PrevLayer
    \nhttps://developer.vectorworks.net/index.php?title=VS:PrevLayer/ja
    \nハンドルで指定したレイヤの前にあるレイヤのハンドルを返します。'''
    return HANDLE

def ResList_InitDef(uniqueID, univName):
    '''https://developer.vectorworks.net/index.php?title=VS:ResList_InitDef
    \nhttps://developer.vectorworks.net/index.php?title=VS:ResList_InitDef/ja
    \nカテゴリリソースを指定した赤のシンボルリソースで初期化します。 uniqueIDはこのコントロールを識別する固有の文字列です。'''
    return None

def EndFolder():
    '''https://developer.vectorworks.net/index.php?title=VS:EndFolder
    \nhttps://developer.vectorworks.net/index.php?title=VS:EndFolder/ja
    \nBeginFolderを実行した後、この手続きを実行するまでの間に作成されたシンボルをシンボルフォルダに入れます。'''
    return None

def GetResourceFromList(listID, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetResourceFromList
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetResourceFromList/ja
    \nアクティブなドキュメントにリソースがある場合はリソースのハンドルを返します。ない場合は0を返します。'''
    return HANDLE

def PrevObj(h):
    '''https://developer.vectorworks.net/index.php?title=VS:PrevObj
    \nhttps://developer.vectorworks.net/index.php?title=VS:PrevObj/ja
    \nハンドルで指定した図形の前にある図形のハンドルを返します。図形が存在しない場合はNILを返します。'''
    return HANDLE

def ResList_IsSelValid(uniqueID):
    '''https://developer.vectorworks.net/index.php?title=VS:ResList_IsSelValid
    \nhttps://developer.vectorworks.net/index.php?title=VS:ResList_IsSelValid/ja
    \nリソースポップアップでの選択が有効かどうかを返します。 uniqueIDはこのコントロールを識別する固有の文字列です。'''
    return BOOLEAN

def FActLayer():
    '''https://developer.vectorworks.net/index.php?title=VS:FActLayer
    \nhttps://developer.vectorworks.net/index.php?title=VS:FActLayer/ja
    \nアクティブなレイヤ上にある最上位の図形のハンドルを返します。図形が存在しない場合はNILを返します。'''
    return HANDLE

def ImportResToCurFileN(listID, index, callback):
    '''https://developer.vectorworks.net/index.php?title=VS:ImportResToCurFileN
    \nhttps://developer.vectorworks.net/index.php?title=VS:ImportResToCurFileN/ja
    \nまだ存在ないものであれば、指定したリスト中の指定したリソースを現在の書類に取り込み、リソースへのハンドルを返します。重複したリソースを処理するためのコールバック関数を使います。'''
    return HANDLE

def PrevSObj(h):
    '''https://developer.vectorworks.net/index.php?title=VS:PrevSObj
    \nhttps://developer.vectorworks.net/index.php?title=VS:PrevSObj/ja
    \nハンドルで指定した図形の前にある図形のうち、選択されている図形のハンドルを返します。'''
    return HANDLE

def ResList_PropFilter(uniqueID, callback):
    '''https://developer.vectorworks.net/index.php?title=VS:ResList_PropFilter'''
    return None

def FIn3D(objectHd):
    '''https://developer.vectorworks.net/index.php?title=VS:FIn3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:FIn3D/ja
    \nハンドルで指定した3次元図形の中で最上位の図形のハンドルを返します。'''
    return HANDLE

def ImportResourceToCurrentFile(listID, index):
    '''https://developer.vectorworks.net/index.php?title=VS:ImportResourceToCurrentFile
    \nhttps://developer.vectorworks.net/index.php?title=VS:ImportResourceToCurrentFile/ja
    \n指定したリソースリストにあるリソースをアクティブなファイルに取り込みます。リソースがアクティブなファイルになかった場合、リソースのハンドルを返します。'''
    return HANDLE

def PrevSymDef(symHd):
    '''https://developer.vectorworks.net/index.php?title=VS:PrevSymDef
    \nhttps://developer.vectorworks.net/index.php?title=VS:PrevSymDef/ja
    \nハンドルで指定した登録シンボルの前にある登録シンボルのハンドルを返します。'''
    return HANDLE

def ResList_SelFAvail(uniqueID, onlyCurrentDocument, searchOnline, skipCurrentDocument):
    '''https://developer.vectorworks.net/index.php?title=VS:ResList_SelFAvail'''
    return itemName

def FInFolder(sfHd):
    '''https://developer.vectorworks.net/index.php?title=VS:FInFolder
    \nhttps://developer.vectorworks.net/index.php?title=VS:FInFolder/ja
    \nハンドルで指定したフォルダの中で最上位のシンボルのハンドルを返します。図形が存在しない場合はNILを返します。'''
    return HANDLE

def LActLayer():
    '''https://developer.vectorworks.net/index.php?title=VS:LActLayer
    \nhttps://developer.vectorworks.net/index.php?title=VS:LActLayer/ja
    \nアクティブなレイヤ上の最下位の図形のハンドルを返します。'''
    return HANDLE

def ResList_ActFolder(uniqueID, folder):
    '''https://developer.vectorworks.net/index.php?title=VS:ResList_ActFolder'''
    return None

def ResList_SetSel(uniqueID, itemName):
    '''https://developer.vectorworks.net/index.php?title=VS:ResList_SetSel
    \nhttps://developer.vectorworks.net/index.php?title=VS:ResList_SetSel/ja
    \nリソースポップアップの選択されたリソースを設定します。 uniqueIDはこのコントロールを識別する固有の文字列です。'''
    return None

def FInGroup(ObjectHd):
    '''https://developer.vectorworks.net/index.php?title=VS:FInGroup
    \nhttps://developer.vectorworks.net/index.php?title=VS:FInGroup/ja
    \nハンドルで指定したグループの中で最上位の図形のハンドルを返します。'''
    return HANDLE

def LNewObj():
    '''https://developer.vectorworks.net/index.php?title=VS:LNewObj
    \nhttps://developer.vectorworks.net/index.php?title=VS:LNewObj/ja
    \n直前に作成された図形のハンドルを返します。'''
    return HANDLE

def ResList_AddCont(uniqueID, folderSpec):
    '''https://developer.vectorworks.net/index.php?title=VS:ResList_AddCont
    \nhttps://developer.vectorworks.net/index.php?title=VS:ResList_AddCont/ja
    \nコンテンツの場所を追加します。 uniqueIDはこのコントロールを識別する固有の文字列です。'''
    return None

def ResourceListSize(listID):
    '''https://developer.vectorworks.net/index.php?title=VS:ResourceListSize
    \nhttps://developer.vectorworks.net/index.php?title=VS:ResourceListSize/ja
    \n指定したリソースリストにあるリソースの数を返します。'''
    return LONGINT

def FInLayer(h):
    '''https://developer.vectorworks.net/index.php?title=VS:FInLayer
    \nhttps://developer.vectorworks.net/index.php?title=VS:FInLayer/ja
    \nハンドルで指定したレイヤ上にある最上位の図形のハンドルを返します。図形が存在しない場合はNILを返します。'''
    return HANDLE

def LObject():
    '''https://developer.vectorworks.net/index.php?title=VS:LObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:LObject/ja
    \nドキュメント内にある最下位の図形のハンドルを返します。'''
    return HANDLE

def ResList_AddCont1(uniqueID, baseFolderSpec, folderName):
    '''https://developer.vectorworks.net/index.php?title=VS:ResList_AddCont1
    \nhttps://developer.vectorworks.net/index.php?title=VS:ResList_AddCont1/ja
    \nコンテンツの場所を追加します。 uniqueIDはこのコントロールを識別する固有の文字列です。'''
    return None

def SetParent(obj, container):
    '''https://developer.vectorworks.net/index.php?title=VS:SetParent
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetParent/ja
    \n現在のコンテナから図形を削除し、指定したコンテナへ置きます。'''
    return BOOLEAN

def DeleteAllDLComponents():
    '''https://developer.vectorworks.net/index.php?title=VS:DeleteAllDLComponents
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeleteAllDLComponents/ja
    \n「ダブルラインの設定」の全構成要素を削除します。'''
    return BOOLEAN

def GetDLOptions():
    '''https://developer.vectorworks.net/index.php?title=VS:GetDLOptions
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDLOptions/ja
    \n「ダブルラインの設定」オプションを取得します。（0：線を作る／1：面を作る／２：線と面を作る）'''
    return INTEGER

def InsertNewDLCompN(beforeIndex, widthDistance, fill, penWeightLeft, penWeightRight, penStyleLeft, penStyleRight):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertNewDLCompN'''
    return BOOLEAN

def SetDLOptions(options):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDLOptions
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDLOptions/ja
    \n「ダブルラインの設定」の「線と面の設定」を設定します。'''
    return None

def DeleteDLComponent(index):
    '''https://developer.vectorworks.net/index.php?title=VS:DeleteDLComponent
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeleteDLComponent/ja
    \n番号で指定した構成要素を「ダブルラインの設定」から削除します。'''
    return BOOLEAN

def GetDLSeparation():
    '''https://developer.vectorworks.net/index.php?title=VS:GetDLSeparation
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDLSeparation/ja
    \n「ダブルラインの設定」の幅を取得します。'''
    return REAL

def InsertNewDLComponent(beforeIndex, widthDistance, fill, penWeightLeft, penWeightRight, penStyleLeft, penStyleRight):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertNewDLComponent
    \nhttps://developer.vectorworks.net/index.php?title=VS:InsertNewDLComponent/ja
    \n「ダブルラインの設定」の、番号で指定した構成要素の前に新しい構成要素を挿入します。'''
    return BOOLEAN

def SetDLSeparation(separationDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDLSeparation
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDLSeparation/ja
    \n「ダブルラインの設定」の幅を設定します。'''
    return None

def DoubLines(doubleLineDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:DoubLines
    \nhttps://developer.vectorworks.net/index.php?title=VS:DoubLines/ja
    \nダブルラインの間隔を設定します。'''
    return None

def GetDefaultTextSize():
    '''https://developer.vectorworks.net/index.php?title=VS:GetDefaultTextSize
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDefaultTextSize/ja
    \nデフォルトの文字の大きさをポイントで返します。'''
    return REAL

def PenGrid(gridDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:PenGrid
    \nhttps://developer.vectorworks.net/index.php?title=VS:PenGrid/ja
    \nスナップグリッドの幅を設定します。'''
    return None

def SetDimStd(whichStandard):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDimStd
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDimStd/ja
    \nデフォルトの寸法線の種類を変更します。'''
    return None

def DrwSize(rows, columns):
    '''https://developer.vectorworks.net/index.php?title=VS:DrwSize
    \nhttps://developer.vectorworks.net/index.php?title=VS:DrwSize/ja
    \n印刷領域の大きさを設定します。各用紙の大きさは、プリンタの種類に応じて「ファイル」メニューの「用紙設定...」で設定します。'''
    return None

def GetDrawingSizeRect():
    '''https://developer.vectorworks.net/index.php?title=VS:GetDrawingSizeRect
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDrawingSizeRect/ja
    \n用紙の大きさを、左上と右下の座標で返します。'''
    return (p1, p2)

def RunGridSettingsDlg():
    '''https://developer.vectorworks.net/index.php?title=VS:RunGridSettingsDlg'''
    return None

def SetOrigin(x, y):
    '''https://developer.vectorworks.net/index.php?title=VS:SetOrigin
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetOrigin/ja
    \nファイルの原点位置を設定します。'''
    return None

def GetCurrentPlanarRefID():
    '''https://developer.vectorworks.net/index.php?title=VS:GetCurrentPlanarRefID
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCurrentPlanarRefID/ja
    \n現在の平面参照番号を返します。これはどんな平面であってもよいです　:　ワーキング平面、スクリーン平面、コンテナのグランドプレーン、任意の平面'''
    return LONGINT

def GetDrawingSizeRectN(hLayer):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDrawingSizeRectN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDrawingSizeRectN/ja
    \nオブジェクトが含まれるファイルの全域を囲む四角形の、左上と右下の座標を返します。'''
    return (p1, p2)

def SetConstrain(str):
    '''https://developer.vectorworks.net/index.php?title=VS:SetConstrain
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetConstrain/ja
    \nスナップパレットのON／OFFを設定します。'''
    return None

def SetOriginAbsolute(xValue, yValue):
    '''https://developer.vectorworks.net/index.php?title=VS:SetOriginAbsolute
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetOriginAbsolute/ja
    \n原点の位置を絶対座標で設定します。'''
    return None

def GetDLCompPenStylesN(index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDLCompPenStylesN'''
    return (BOOLEAN, penStyleLeft, penStyleRight)

def GetFName():
    '''https://developer.vectorworks.net/index.php?title=VS:GetFName
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetFName/ja
    \nアクティブなドキュメントの名前を返します。'''
    return STRING

def SetDLCompPenStylesN(index, penStyleLeft, penStyleRight):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDLCompPenStylesN'''
    return BOOLEAN

def SetPref(index, status):
    '''https://developer.vectorworks.net/index.php?title=VS:SetPref
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetPref/ja
    \n環境設定の指定した項目の選択状態をBOOLEAN型の値で設定します。'''
    return None

def GetDLComponentClass(index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDLComponentClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDLComponentClass/ja
    \n「ダブルラインの設定」の、番号で指定した構成要素のクラスを返します。'''
    return (BOOLEAN, componentClass)

def GetNumberOfDLComponents():
    '''https://developer.vectorworks.net/index.php?title=VS:GetNumberOfDLComponents
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNumberOfDLComponents/ja
    \n「ダブルラインの設定」の構成要素の数を取得します。'''
    return (BOOLEAN, numComponents)

def SetDLComponentClass(index, componentClass):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDLComponentClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDLComponentClass/ja
    \n「ダブルラインの設定」の、番号で指定した構成要素のクラスを設定します。'''
    return BOOLEAN

def SetPrefInt(index, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetPrefInt
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetPrefInt/ja
    \n環境設定の指定した項目をINTEGER型の値で設定します。'''
    return None

def GetDLComponentFill(index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDLComponentFill
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDLComponentFill/ja
    \n「ダブルラインの設定」で、指定した番号の構成要素から面の模様番号を取得します。'''
    return (BOOLEAN, fill)

def GetOrigin():
    '''https://developer.vectorworks.net/index.php?title=VS:GetOrigin
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetOrigin/ja
    \n現在の原点位置を座標で返します。GetOriginInDocUnits を参照してください。'''
    return (x, y)

def SetDLComponentFill(index, fill):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDLComponentFill
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDLComponentFill/ja
    \n「ダブルラインの設定」で、指定した番号の構成要素の面を模様番号で設定します。'''
    return BOOLEAN

def SetPrefLongInt(index, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetPrefLongInt
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetPrefLongInt/ja
    \n環境設定の指定した項目をLONGINT型の値で設定します。'''
    return None

def GetDLComponentFillColors(index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDLComponentFillColors
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDLComponentFillColors/ja
    \n「ダブルラインの設定」の、番号で指定した構成要素の面の色と地色を返します。'''
    return (BOOLEAN, fillForeColor, fillBackColor)

def GetOriginInDocUnits():
    '''https://developer.vectorworks.net/index.php?title=VS:GetOriginInDocUnits
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetOriginInDocUnits/ja
    \n用紙中心に対する原点の位置を、現在の単位で返します。GetOrigin の問題が改善されています。'''
    return (x, y)

def SetDLComponentFillColors(index, fillForeColor, fillBackColor):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDLComponentFillColors
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDLComponentFillColors/ja
    \n「ダブルラインの設定」の、番号で指定した構成要素の面の色と地色を設定します。'''
    return BOOLEAN

def SetPrefRGB(prefIndex, colorRV, colorGV, colorBV):
    '''https://developer.vectorworks.net/index.php?title=VS:SetPrefRGB
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetPrefRGB/ja
    \n指定した項目の色成分を設定します。値の範囲は0から65535までです。'''
    return None

def GetDLComponentName(index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDLComponentName
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDLComponentName/ja
    \n「ダブルラインの設定」の、番号で指定した構成要素の名前を返します。'''
    return STRING

def GetPref(prefIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPref
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPref/ja
    \n環境設定の指定した項目の選択状態をBOOLEAN型の値で返します。'''
    return BOOLEAN

def SetDLComponentName(index, componentName):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDLComponentName
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDLComponentName/ja
    \n「ダブルラインの設定」の、番号で指定した構成要素の名前を設定します。'''
    return BOOLEAN

def SetPrefReal(index, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetPrefReal
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetPrefReal/ja
    \n環境設定の指定した項目をREAL型の値で設定します。'''
    return None

def GetDLComponentPenColors(index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDLComponentPenColors
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDLComponentPenColors/ja
    \n「ダブルラインの設定」の、番号で指定した構成要素の左右の線の色と地色を返します。'''
    return (BOOLEAN, leftPenForeColor, leftPenBackColor, rightPenForeColor, rightPenBackColor)

def GetPrefInt(prefIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPrefInt
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPrefInt/ja
    \n環境設定の指定した項目に設定されているINTEGER型の値を返します。'''
    return INTEGER

def SetDLComponentPenColors(index, leftPenForeColor, leftPenBackColor, rightPenForeColor, rightPenBackColor):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDLComponentPenColors
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDLComponentPenColors/ja
    \n「ダブルラインの設定」の、番号で指定した構成要素の左右の線の色と地色を設定します。'''
    return BOOLEAN

def SetPrefString(index, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetPrefString
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetPrefString/ja
    \n環境設定の指定した項目をSTRING型の値で設定します。'''
    return None

def GetDLComponentPenStyles(index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDLComponentPenStyles
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDLComponentPenStyles/ja
    \n「ダブルラインの設定」で、指定した番号の構成要素から左右の線の種類を取得します。'''
    return (BOOLEAN, penStyleLeft, penStyleRight)

def GetPrefLongInt(prefIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPrefLongInt
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPrefLongInt/ja
    \n環境設定の指定した項目に設定されているLONGINT型の値を返します。'''
    return LONGINT

def SetDLComponentPenStyles(index, penStyleLeft, penStyleRight):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDLComponentPenStyles
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDLComponentPenStyles/ja
    \n「ダブルラインの設定」で、指定した番号の構成要素の左右の線の種類を設定します。'''
    return BOOLEAN

def SetPrimaryDim(h, showValue, boxText, leader, trailer, precision):
    '''https://developer.vectorworks.net/index.php?title=VS:SetPrimaryDim
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetPrimaryDim/ja
    \nハンドルで指定した基準寸法線を設定します。'''
    return None

def GetDLComponentPenWeights(index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDLComponentPenWeights
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDLComponentPenWeights/ja
    \n「ダブルラインの設定」で、指定した番号の構成要素から左右の線の太さを取得します。'''
    return (BOOLEAN, penWeightLeft, penWeightRight)

def GetPrefRGB(prefIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPrefRGB
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPrefRGB/ja
    \n指定した項目の色成分を返します。値の範囲は0から65535までです。'''
    return (colorRV, colorGV, colorBV)

def SetDLComponentPenWeights(index, penWeightLeft, penWeightRight):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDLComponentPenWeights
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDLComponentPenWeights/ja
    \n「ダブルラインの設定」で、指定した番号の構成要素の左右の線の太さを設定します。'''
    return BOOLEAN

def SetSecondaryDim(h, showValue, boxText, leader, trailer, precision):
    '''https://developer.vectorworks.net/index.php?title=VS:SetSecondaryDim
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetSecondaryDim/ja
    \nハンドルで指定した補助寸法線を設定します。'''
    return None

def GetDLComponentUseFillClassAttr(index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDLComponentUseFillClassAttr
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDLComponentUseFillClassAttr/ja
    \n「ダブルラインの設定」の、番号で指定した構成要素の面の模様に、クラス属性を使っている場合はTRUEを返します。'''
    return (BOOLEAN, useClassAttr)

def GetPrefReal(prefIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPrefReal
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPrefReal/ja
    \n環境設定の指定した項目に設定されているREAL型の値を返します。'''
    return REAL

def SetDLComponentUseFillClassAttr(index, useClassAttr):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDLComponentUseFillClassAttr
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDLComponentUseFillClassAttr/ja
    \n「ダブルラインの設定」の、番号で指定した構成要素の面の模様に、クラス属性を設定します。'''
    return BOOLEAN

def SetUnits(fraction, display, format, upi, name, squareName):
    '''https://developer.vectorworks.net/index.php?title=VS:SetUnits
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetUnits/ja
    \nアクティブなドキュメントの単位を設定します。'''
    return None

def GetDLComponentUsePenClassAttr(index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDLComponentUsePenClassAttr
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDLComponentUsePenClassAttr/ja
    \n「ダブルラインの設定」の、番号で指定した構成要素の左右の線種に、クラス属性を使っている場合はTRUEを返します。'''
    return (BOOLEAN, leftPenUseClassAttr, rightPenUseClassAttr)

def GetPrefString(prefIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPrefString
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPrefString/ja
    \n環境設定の指定した項目に設定されているSTRING型の値を返します。'''
    return STRING

def SetDLComponentUsePenClassAttr(index, leftPenUseClassAttr, rightPenUseClassAttr):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDLComponentUsePenClassAttr
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDLComponentUsePenClassAttr/ja
    \n「ダブルラインの設定」の、番号で指定した構成要素の左右の線種に、クラス属性を設定します。'''
    return BOOLEAN

def SetWallPrefStyle(sysName):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWallPrefStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWallPrefStyle/ja
    \nアクティブドキュメントのデフォルト壁スタイルを設定します。'''
    return BOOLEAN

def GetDLComponentWidth(index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDLComponentWidth
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDLComponentWidth/ja
    \n「ダブルラインの設定」で、指定した番号の構成要素から幅を取得します。'''
    return (BOOLEAN, width)

def GetWallPrefStyle():
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallPrefStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWallPrefStyle/ja
    \nアクティブドキュメントのデフォルト壁スタイルの名前が返ります。'''
    return STRING

def SetDLComponentWidth(index, widthDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDLComponentWidth
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDLComponentWidth/ja
    \n「ダブルラインの設定」で、指定した番号の構成要素の幅を設定します。'''
    return BOOLEAN

def GetDLControlOffset():
    '''https://developer.vectorworks.net/index.php?title=VS:GetDLControlOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDLControlOffset/ja
    \n「ダブルラインの設定」の、オフセットの値を返します。'''
    return REAL

def GridLines(gridDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:GridLines
    \nhttps://developer.vectorworks.net/index.php?title=VS:GridLines/ja
    \nグリッドの幅を設定します。'''
    return None

def SetDLControlOffset(controlOffsetDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDLControlOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDLControlOffset/ja
    \n「ダブルラインの設定」のオフセットを設定します。'''
    return None

def EA_ConvDoc2X(unitType, value):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_ConvDoc2X
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_ConvDoc2X/ja
    \n指定した実数値を、設定の単位からX単位系に変換します。VS:Energos Thirdparty Support のページを参照してください。'''
    return REAL

def EA_DataAccCompGet(acc):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_DataAccCompGet
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_DataAccCompGet/ja
    \nアクセス番号を指定して、オブジェクトの構成要素のデータを取得します。VS:Energos Thirdparty Support のページを参照してください。'''
    return (componentIndex, outInclude, outLambda, outThickness)

def EA_DataAccGetReal(acc, valueIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_DataAccGetReal
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_DataAccGetReal/ja
    \n指定したアクセス番号について、実数値のデータを返します。VS:Energos Thirdparty Support のページを参照してください。'''
    return REAL

def EA_DataAccSetReal(acc, valueIndex, value):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_DataAccSetReal
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_DataAccSetReal/ja
    \n指定したアクセス番号について、実数値のデータを設定します。VS:Energos Thirdparty Support のページを参照してください。'''
    return None

def EA_ConvStr2X(unitType, value):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_ConvStr2X
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_ConvStr2X/ja
    \n指定した文字列を、X単位系に変換します。VS:Energos Thirdparty Support のページを参照してください。'''
    return REAL

def EA_DataAccCpyInto(acc, h):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_DataAccCpyInto
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_DataAccCpyInto/ja
    \nアクセス番号を指定して、データをオブジェクトに複製します。'''
    return None

def EA_DataAccGetStr(acc, valueIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_DataAccGetStr
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_DataAccGetStr/ja
    \n指定したアクセス番号について、文字列のデータを返します。VS:Energos Thirdparty Support のページを参照してください。'''
    return STRING

def EA_DataAccSetStr(acc, valueIndex, value):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_DataAccSetStr
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_DataAccSetStr/ja
    \n指定したアクセス番号について、文字列のデータを設定します。VS:Energos Thirdparty Support のページを参照してください。'''
    return None

def EA_ConvX2Doc(unitType, value):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_ConvX2Doc
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_ConvX2Doc/ja
    \n指定した実数値を、X単位から設定の単位系に変換します。VS:Energos Thirdparty Support のページを参照してください。'''
    return REAL

def EA_DataAccCreate(type, h):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_DataAccCreate
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_DataAccCreate/ja
    \nアクセス番号を返します。ハンドルは、エネルギー解析対応のレコードフォーマットか図形を指定します。VS:Energos Thirdparty Support , Energos: Use Record Formats to define energy analysis data のページを参照してください。'''
    return INTEGER

def EA_DataAccMtrlDlg(acc):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_DataAccMtrlDlg
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_DataAccMtrlDlg/ja
    \nアクセス番号で指定されたλ値（熱伝導率）の設定ダイアログが表示されます。VS:Energos Thirdparty Support のページを参照してください。'''
    return (BOOLEAN, outLambda)

def EA_GetUnitStr(unitType):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_GetUnitStr
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_GetUnitStr/ja
    \n番号で指定した項目の単位を返します。VS:Energos Thirdparty Support のページを参照してください。'''
    return STRING

def EA_ConvX2DocStr(unitType, value, incUnitMark):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_ConvX2DocStr
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_ConvX2DocStr/ja
    \n指定した実数値を、X単位から設定の単位系に変換します。VS:Energos Thirdparty Support のページを参照してください。'''
    return STRING

def EA_DataAccDelete(acc):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_DataAccDelete
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_DataAccDelete/ja
    \nアクセス番号を解放します。ハンドルは、エネルギー解析対応のレコードフォーマットか図形を指定します。VS:Energos Thirdparty Support , Energos: Use Record Formats to define energy analysis data のページを参照してください。'''
    return None

def EA_DataAccSave(acc):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_DataAccSave
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_DataAccSave/ja
    \n指定したアクセス番号のオブジェクトにデータを保存します。'''
    return None

def EA_IsUsedUValue():
    '''https://developer.vectorworks.net/index.php?title=VS:EA_IsUsedUValue
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_IsUsedUValue/ja
    \nU値（熱貫流率）を使用している場合はTrueを、R値（熱抵抗値）を使用している場合はFalseを返します。'''
    return BOOLEAN

def EA_DataAccAdvDlg(acc):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_DataAccAdvDlg
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_DataAccAdvDlg/ja
    \nアクセス番号で指定された設定ダイアログが表示されます。VS:Energos Thirdparty Support のページを参照してください。'''
    return BOOLEAN

def EA_DataAccFillUI(acc, dialogID, ctrlID, uiIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_DataAccFillUI
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_DataAccFillUI/ja
    \nアクセス番号を指定し、ダイアログのポップアップのデータを作成します。VS:Energos Thirdparty Support のページを参照してください。'''
    return None

def EA_DataAccSelUI(acc, dialogID, ctrlID, uiIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_DataAccSelUI
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_DataAccSelUI/ja
    \nアクセス番号を指定し、ダイアログのポップアップのデータを更新・選択します。VS:Energos Thirdparty Support のページを参照してください。'''
    return None

def EA_UValueText(UValue):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_UValueText
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_UValueText/ja
    \n設定されている、U値（熱貫流率）または R値（熱抵抗値）を文字列で返します。'''
    return STRING

def EA_DataAccCompAdd(acc, include, lambda, thickness):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_DataAccCompAdd
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_DataAccCompAdd/ja
    \nアクセス番号を指定して、オブジェクトに構成要素を追加します。VS:Energos Thirdparty Support のページを参照してください。'''
    return None

def EA_DataAccGetBool(acc, valueIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_DataAccGetBool
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_DataAccGetBool/ja
    \n指定したアクセス番号について、True/False のデータを返します。VS:Energos Thirdparty Support のページを参照してください。'''
    return BOOLEAN

def EA_DataAccSetBool(acc, valueIndex, value):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_DataAccSetBool
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_DataAccSetBool/ja
    \n指定したアクセス番号について、True/False のデータを設定します。VS:Energos Thirdparty Support のページを参照してください。'''
    return None

def EA_DataAccCompDel(acc):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_DataAccCompDel
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_DataAccCompDel/ja
    \nアクセス番号を指定して、オブジェクトからすべての構成要素を削除します。VS:Energos Thirdparty Support のページを参照してください。'''
    return None

def EA_DataAccGetInt(acc, valueIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_DataAccGetInt
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_DataAccGetInt/ja
    \n指定したアクセス番号について、整数値のデータを返します。VS:Energos Thirdparty Support のページを参照してください。'''
    return INTEGER

def EA_DataAccSetInt(acc, valueIndex, value):
    '''https://developer.vectorworks.net/index.php?title=VS:EA_DataAccSetInt
    \nhttps://developer.vectorworks.net/index.php?title=VS:EA_DataAccSetInt/ja
    \n指定したアクセス番号について、整数値のデータを設定します。VS:Energos Thirdparty Support のページを参照してください。'''
    return None

def EXL_AddSheet(sheetName):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_AddSheet'''
    return BOOLEAN

def EXL_GetCellBorderT(sheetIndex, cellRow, cellColumn):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_GetCellBorderT'''
    return (BOOLEAN, outWeight, outColor, outEnabled, outStyle)

def EXL_GetSheetSize(sheetIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_GetSheetSize'''
    return (BOOLEAN, outRows, outColumns)

def EXL_SetCellBorderR(sheetIndex, cellRow, cellColumn, weight, color, style, enabled):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_SetCellBorderR'''
    return (BOOLEAN, outInconsistencyFound)

def EXL_CloseBook():
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_CloseBook'''
    return BOOLEAN

def EXL_GetCellFill(sheetIndex, cellRow, cellColumn):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_GetCellFill'''
    return (BOOLEAN, outStyle, outBgColor, outFgColor, outFillpattern, outInconsistencyFound)

def EXL_IsCellValid(sheetIndex, cellRow, cellColumn):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_IsCellValid'''
    return BOOLEAN

def EXL_SetCellBorderT(sheetIndex, cellRow, cellColumn, weight, color, style, enabled):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_SetCellBorderT'''
    return (BOOLEAN, outInconsistencyFound)

def EXL_DeleteSheet(sheetName):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_DeleteSheet'''
    return BOOLEAN

def EXL_GetCellFont(sheetIndex, cellRow, cellColumn):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_GetCellFont'''
    return (BOOLEAN, outFontStyle, outFontSize, outFontIndex, outTextColorIndex, outInconsistencyFound)

def EXL_NewBook(filePath):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_NewBook'''
    return BOOLEAN

def EXL_SetCellFont(sheetIndex, cellRow, cellColumn, fontStyle, fontSize, fontIndex, textColorIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_SetCellFont'''
    return (BOOLEAN, outInconsistencyFound)

def EXL_GetCellAlignment(sheetIndex, cellRow, cellColumn):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_GetCellAlignment'''
    return (BOOLEAN, outAlignmentH, outAlignmentV, outTextAngle, outWrapTextFlag, outInconsistencyFound)

def EXL_GetCellStyle(sheetIndex, cellRow, cellColumn):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_GetCellStyle'''
    return (BOOLEAN, outNumStyleClass, outAccuracy, outInconsistencyFound)

def EXL_ReadFile(FilePath):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_ReadFile'''
    return BOOLEAN

def EXL_SetCellNumFormula(sheetIndex, cellRow, cellColumn, formulaString, formulaValue):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_SetCellNumFormula'''
    return BOOLEAN

def EXL_GetCellBordeDiff(sheetIndex, cellRow, cellColumn):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_GetCellBordeDiff'''
    return (BOOLEAN, outInconsistencyFound)

def EXL_GetCellValue(sheetIndex, cellRow, cellColumn):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_GetCellValue'''
    return (BOOLEAN, outFormula, outString, outLeaderStr, outTrailerStr, outValue)

def EXL_SaveAndCloseBook(filePath):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_SaveAndCloseBook'''
    return BOOLEAN

def EXL_SetCellNumber(sheetIndex, cellRow, cellColumn, value):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_SetCellNumber'''
    return BOOLEAN

def EXL_GetCellBorderB(sheetIndex, cellRow, cellColumn):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_GetCellBorderB'''
    return (BOOLEAN, outWeight, outColor, outEnabled, outStyle)

def EXL_GetSheetCnt():
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_GetSheetCnt'''
    return (BOOLEAN, outSheetCount)

def EXL_SetCellAlignment(sheetIndex, cellRow, cellColumn, AlignmentH, AlignmentV, TextAngle, WrapTextFlag):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_SetCellAlignment'''
    return (BOOLEAN, outInconsistencyFound)

def EXL_SetCellStrFormula(sheetIndex, cellRow, cellColumn, formulaString, formulaValue):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_SetCellStrFormula'''
    return BOOLEAN

def EXL_GetCellBorderL(sheetIndex, cellRow, cellColumn):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_GetCellBorderL'''
    return (BOOLEAN, outWeight, outColor, outEnabled, outStyle)

def EXL_GetSheetIndex(sheetName):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_GetSheetIndex'''
    return (BOOLEAN, outSheetIndex)

def EXL_SetCellBorderB(sheetIndex, cellRow, cellColumn, weight, color, style, enabled):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_SetCellBorderB'''
    return (BOOLEAN, outInconsistencyFound)

def EXL_SetCellString(sheetIndex, cellRow, cellColumn, value):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_SetCellString'''
    return BOOLEAN

def EXL_GetCellBorderR(sheetIndex, cellRow, cellColumn):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_GetCellBorderR'''
    return (BOOLEAN, outWeight, outColor, outEnabled, outStyle)

def EXL_GetSheetName(sheetIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_GetSheetName'''
    return (BOOLEAN, outSheetName)

def EXL_SetCellBorderL(sheetIndex, cellRow, cellColumn, weight, color, style, enabled):
    '''https://developer.vectorworks.net/index.php?title=VS:EXL_SetCellBorderL'''
    return (BOOLEAN, outInconsistencyFound)

def Excel_Convert(FilePath):
    '''https://developer.vectorworks.net/index.php?title=VS:Excel_Convert'''
    return STRING

def Append(fileName):
    '''https://developer.vectorworks.net/index.php?title=VS:Append
    \nhttps://developer.vectorworks.net/index.php?title=VS:Append/ja
    \n指定したパスを持つファイルを追加モードで開きます。ファイル内の既存データは上書きされません。'''
    return None

def FindFile(whichPath, relFilePath):
    '''https://developer.vectorworks.net/index.php?title=VS:FindFile
    \nhttps://developer.vectorworks.net/index.php?title=VS:FindFile/ja
    \nフォルダ番号と相対ファイルパスでファイルを検索します。'''
    return (BOOLEAN, outPath)

def ImportIGES(fileName):
    '''https://developer.vectorworks.net/index.php?title=VS:ImportIGES
    \nhttps://developer.vectorworks.net/index.php?title=VS:ImportIGES/ja
    \nImportIGES'''
    return BOOLEAN

def Space(n):
    '''https://developer.vectorworks.net/index.php?title=VS:Space
    \nhttps://developer.vectorworks.net/index.php?title=VS:Space/ja
    \n指定した数のスペースを、現在書き込み中のファイルに出力します。'''
    return None

def Close(fileName):
    '''https://developer.vectorworks.net/index.php?title=VS:Close
    \nhttps://developer.vectorworks.net/index.php?title=VS:Close/ja
    \n指定したパスを持つファイルを閉じます。'''
    return None

def FindFileInPluginFolder(filename):
    '''https://developer.vectorworks.net/index.php?title=VS:FindFileInPluginFolder
    \nhttps://developer.vectorworks.net/index.php?title=VS:FindFileInPluginFolder/ja
    \nすべてのプラグインフォルダから指定した名前のファイルを検索します。ファイルがあればTRUE、なければFALSEを返します。ファイルがあった場合、pathパラメータに結果を返します。'''
    return (BOOLEAN, path)

def ImportParasolidXT(filePath):
    '''https://developer.vectorworks.net/index.php?title=VS:ImportParasolidXT'''
    return BOOLEAN

def StdRead():
    '''https://developer.vectorworks.net/index.php?title=VS:StdRead
    \nhttps://developer.vectorworks.net/index.php?title=VS:StdRead/ja
    \n開いているファイルからデータを読み込みます。'''
    return z

def ConvertHSF2PosixPath(HSFPath):
    '''https://developer.vectorworks.net/index.php?title=VS:ConvertHSF2PosixPath
    \nhttps://developer.vectorworks.net/index.php?title=VS:ConvertHSF2PosixPath/ja
    \nMacintoshのみ有効'''
    return (BOOLEAN, outPosixPath)

def GetFPathName():
    '''https://developer.vectorworks.net/index.php?title=VS:GetFPathName
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetFPathName/ja
    \nアクティブな書類のフルパスを取得します。'''
    return STRING

def ImportSAT(filePath, doSingleSym):
    '''https://developer.vectorworks.net/index.php?title=VS:ImportSAT
    \nhttps://developer.vectorworks.net/index.php?title=VS:ImportSAT/ja
    \nSATファイルを取り込みます。'''
    return HANDLE

def StdReadLn():
    '''https://developer.vectorworks.net/index.php?title=VS:StdReadLn
    \nhttps://developer.vectorworks.net/index.php?title=VS:StdReadLn/ja
    \n開いているファイルから1行分のデータを読み込みます。'''
    return z

def ConvertPosix2HSFPath(PosixPath):
    '''https://developer.vectorworks.net/index.php?title=VS:ConvertPosix2HSFPath
    \nhttps://developer.vectorworks.net/index.php?title=VS:ConvertPosix2HSFPath/ja
    \nMacintoshのみ有効'''
    return (BOOLEAN, outHSFPath)

def GetFile():
    '''https://developer.vectorworks.net/index.php?title=VS:GetFile
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetFile/ja
    \nファイルを開くダイアログを表示し、ユーザーが選択したファイルのパスを返します。'''
    return fileName

def ImportSketchup1(filePath, doSingleSym):
    '''https://developer.vectorworks.net/index.php?title=VS:ImportSketchup1'''
    return BOOLEAN

def Tab(n):
    '''https://developer.vectorworks.net/index.php?title=VS:Tab
    \nhttps://developer.vectorworks.net/index.php?title=VS:Tab/ja
    \n指定した数のタブを、現在書き込み中のファイルに出力します。'''
    return None

def CreateFolder(path):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateFolder
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateFolder/ja
    \nハードディスク上にフォルダーを作ります。'''
    return BOOLEAN

def GetFileInfo(filename):
    '''https://developer.vectorworks.net/index.php?title=VS:GetFileInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetFileInfo/ja
    \nファイルの属性を返します。'''
    return (fullReadPath, fullWritePath, readFileExists, writeFileExists, locked, hasReadPermission, hasWritePermission, hasFolderPermission)

def Open(fileName):
    '''https://developer.vectorworks.net/index.php?title=VS:Open
    \nhttps://developer.vectorworks.net/index.php?title=VS:Open/ja
    \n指定したファイルのパスを使って、ファイルを開きます。'''
    return None

def UseDefaultFileErrorHandling(enable):
    '''https://developer.vectorworks.net/index.php?title=VS:UseDefaultFileErrorHandling
    \nhttps://developer.vectorworks.net/index.php?title=VS:UseDefaultFileErrorHandling/ja
    \n入出力エラーダイアログの表示／非表示を設定します。 TRUE＝表示／FALSE＝非表示'''
    return None

def EOF(fileName):
    '''https://developer.vectorworks.net/index.php?title=VS:EOF
    \nhttps://developer.vectorworks.net/index.php?title=VS:EOF/ja
    \n開いているファイルの読み込み位置が、終端であればTRUEを返します。'''
    return BOOLEAN

def GetFileN(title, defaultFolder, mask):
    '''https://developer.vectorworks.net/index.php?title=VS:GetFileN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetFileN/ja
    \nファイル選択ダイアログを表示し、選択したファイルのフルパスを返します。'''
    return (BOOLEAN, fileName)

def PutFile(commentStr, defaultStr):
    '''https://developer.vectorworks.net/index.php?title=VS:PutFile
    \nhttps://developer.vectorworks.net/index.php?title=VS:PutFile/ja
    \nファイル保存ダイアログを表示し、ユーザーが指定したファイルのパスを返します。'''
    return fileName

def Write(z):
    '''https://developer.vectorworks.net/index.php?title=VS:Write
    \nhttps://developer.vectorworks.net/index.php?title=VS:Write/ja
    \n開いているファイルにデータを書き込みます。'''
    return None

def EOLN(fileName):
    '''https://developer.vectorworks.net/index.php?title=VS:EOLN
    \nhttps://developer.vectorworks.net/index.php?title=VS:EOLN/ja
    \n開いているファイルの読み込み位置が、行の終端であればTRUEを返します。'''
    return BOOLEAN

def GetFileSize(FilePath):
    '''https://developer.vectorworks.net/index.php?title=VS:GetFileSize
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetFileSize/ja'''
    return (LONGINT, FilePath)

def Read():
    '''https://developer.vectorworks.net/index.php?title=VS:Read
    \nhttps://developer.vectorworks.net/index.php?title=VS:Read/ja
    \n開いているファイルからデータを読み込みます。'''
    return z

def WriteBin(z):
    '''https://developer.vectorworks.net/index.php?title=VS:WriteBin'''
    return None

def ExportIGES(fileName, exportSolidAsSurface):
    '''https://developer.vectorworks.net/index.php?title=VS:ExportIGES
    \nhttps://developer.vectorworks.net/index.php?title=VS:ExportIGES/ja
    \nファイルをIGESファイルに取り出します。'''
    return BOOLEAN

def GetFilesInFolder(folderName, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetFilesInFolder
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetFilesInFolder/ja
    \nフォルダー中のN番目のファイル名を返します。'''
    return STRING

def ReadBin():
    '''https://developer.vectorworks.net/index.php?title=VS:ReadBin'''
    return z

def ExportSAT(filePath, solidAsSurface):
    '''https://developer.vectorworks.net/index.php?title=VS:ExportSAT
    \nhttps://developer.vectorworks.net/index.php?title=VS:ExportSAT/ja
    \n選択図形をSATファイルに取り出します。'''
    return BOOLEAN

def GetFolder(promptStr):
    '''https://developer.vectorworks.net/index.php?title=VS:GetFolder
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetFolder/ja
    \nユーザーの選択したフォルダーのパスを取得します。'''
    return (INTEGER, directoryPath)

def ReadLn():
    '''https://developer.vectorworks.net/index.php?title=VS:ReadLn
    \nhttps://developer.vectorworks.net/index.php?title=VS:ReadLn/ja
    \n開いているファイルから1行分のデータを読み込みます。'''
    return z

def WriteLnMac(z):
    '''https://developer.vectorworks.net/index.php?title=VS:WriteLnMac
    \nhttps://developer.vectorworks.net/index.php?title=VS:WriteLnMac/ja
    \n開いているファイルにデータを書き込み、改行します。ファイルはどのプラットフォームでもVectorScriptとして読み戻すことができます。'''
    return None

def ExportSTEP(filePath, exportSolidsAsSurfaces):
    '''https://developer.vectorworks.net/index.php?title=VS:ExportSTEP'''
    return BOOLEAN

def GetFolderPath(whichPath):
    '''https://developer.vectorworks.net/index.php?title=VS:GetFolderPath
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetFolderPath/ja
    \n指定した種類のフォルダへのパスを文字列で返します。'''
    return STRING

def Rewrite(fileName):
    '''https://developer.vectorworks.net/index.php?title=VS:Rewrite
    \nhttps://developer.vectorworks.net/index.php?title=VS:Rewrite/ja
    \n指定したファイルのパスに新しいファイルを作成します。'''
    return None

def WriteMac(z):
    '''https://developer.vectorworks.net/index.php?title=VS:WriteMac
    \nhttps://developer.vectorworks.net/index.php?title=VS:WriteMac/ja
    \n開いているファイルにデータを書き込みます。ファイルはどのプラットフォームでもVectorScriptとして読み戻すことができます。'''
    return None

def ExportSTL(filePath, exportBinary, percentTess, exportObjectsOptions):
    '''https://developer.vectorworks.net/index.php?title=VS:ExportSTL
    \nhttps://developer.vectorworks.net/index.php?title=VS:ExportSTL/ja
    \n図形をSTLファイルに取り出します。'''
    return BOOLEAN

def GetLastFileErr():
    '''https://developer.vectorworks.net/index.php?title=VS:GetLastFileErr
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLastFileErr/ja
    \nファイルの入出力作業でエラーが発生した場合に、エラーコードを返します。'''
    return INTEGER

def SaveActiveDocument(filePath):
    '''https://developer.vectorworks.net/index.php?title=VS:SaveActiveDocument
    \nhttps://developer.vectorworks.net/index.php?title=VS:SaveActiveDocument/ja
    \nダイアログを表示せずにファイルを保存します。'''
    return LONGINT

def BindLayerToArcGISFS(inURL, inFeatureId, inRequestAll):
    '''https://developer.vectorworks.net/index.php?title=VS:BindLayerToArcGISFS'''
    return None

def GetGISOrigin():
    '''https://developer.vectorworks.net/index.php?title=VS:GetGISOrigin
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetGISOrigin/ja
    \n地理的原点を取得します。'''
    return (BOOLEAN, outLat, outLon, outAngleToNorth)

def LegacyShapefileExp():
    '''https://developer.vectorworks.net/index.php?title=VS:LegacyShapefileExp
    \nhttps://developer.vectorworks.net/index.php?title=VS:LegacyShapefileExp/ja
    \nShapeファイルを取り出す為に、古いユーザインターフェースを使用します。'''
    return None

def UpdateLayerFromFS(inRequestAll):
    '''https://developer.vectorworks.net/index.php?title=VS:UpdateLayerFromFS'''
    return None

def BindLayerToWFSFS(inURL, inFeatureName, inRequestAll):
    '''https://developer.vectorworks.net/index.php?title=VS:BindLayerToWFSFS'''
    return None

def GetGISOriginN():
    '''https://developer.vectorworks.net/index.php?title=VS:GetGISOriginN'''
    return (BOOLEAN, outLat, outLon, outAngleToNorth)

def LegacyShapefileImp():
    '''https://developer.vectorworks.net/index.php?title=VS:LegacyShapefileImp
    \nhttps://developer.vectorworks.net/index.php?title=VS:LegacyShapefileImp/ja
    \nShapeファイルを取り込む為に、古いユーザインターフェースを使用します。'''
    return None

def VWCoordToGeog(inCoordX, inCoordY):
    '''https://developer.vectorworks.net/index.php?title=VS:VWCoordToGeog
    \nhttps://developer.vectorworks.net/index.php?title=VS:VWCoordToGeog/ja
    \n緯度経度を取得します。'''
    return (BOOLEAN, outLat, outLon)

def EditGeorefWithUI(hLayer):
    '''https://developer.vectorworks.net/index.php?title=VS:EditGeorefWithUI
    \nhttps://developer.vectorworks.net/index.php?title=VS:EditGeorefWithUI/ja
    \n指定されたレイヤのジオリファレンス設定を編集します。'''
    return BOOLEAN

def GetProjectionLocName(hLayer):
    '''https://developer.vectorworks.net/index.php?title=VS:GetProjectionLocName
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetProjectionLocName/ja
    \n投影方法のローカライズ名を取得します。'''
    return (BOOLEAN, outProj)

def RemoveGeoref(hLayer):
    '''https://developer.vectorworks.net/index.php?title=VS:RemoveGeoref'''
    return None

def VWCoordToGeogN(inCoordX, inCoordY):
    '''https://developer.vectorworks.net/index.php?title=VS:VWCoordToGeogN'''
    return (BOOLEAN, outLat, outLon)

def GeogCoordToVW(inLat, inLon):
    '''https://developer.vectorworks.net/index.php?title=VS:GeogCoordToVW
    \nhttps://developer.vectorworks.net/index.php?title=VS:GeogCoordToVW/ja
    \nVectorworks上の座標系の点を取得します。'''
    return (BOOLEAN, outCoord)

def GetProjectionProj4(hLayer, esriStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetProjectionProj4
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetProjectionProj4/ja
    \nProj4形式で投影の情報を得ます。'''
    return (BOOLEAN, outProj4)

def SetDocGeoRefByUsrOrg(EPSG):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDocGeoRefByUsrOrg'''
    return None

def GeogCoordToVWN(inLat, inLon):
    '''https://developer.vectorworks.net/index.php?title=VS:GeogCoordToVWN'''
    return (BOOLEAN, outCoord)

def GetProjectionWKT(hLayer, esriStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetProjectionWKT
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetProjectionWKT/ja
    \nWell Known Text (WKT) 形式で投影の情報を取得します。'''
    return (BOOLEAN, outWKT)

def SetGISLayer(hLayer):
    '''https://developer.vectorworks.net/index.php?title=VS:SetGISLayer
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetGISLayer/ja
    \nレイヤコンテキストを設定します。'''
    return BOOLEAN

def GetAngleToNorth():
    '''https://developer.vectorworks.net/index.php?title=VS:GetAngleToNorth
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetAngleToNorth/ja
    \n北方向の角度を取得します。'''
    return REAL

def IsGeoreferenced(hLayer):
    '''https://developer.vectorworks.net/index.php?title=VS:IsGeoreferenced
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsGeoreferenced/ja
    \nレイヤがジオリファレンス設定されているかどうかをチェクします。'''
    return BOOLEAN

def UpdateFeatureLayer():
    '''https://developer.vectorworks.net/index.php?title=VS:UpdateFeatureLayer'''
    return None

def AlignDistribute2D(MenuAction):
    '''https://developer.vectorworks.net/index.php?title=VS:AlignDistribute2D
    \nhttps://developer.vectorworks.net/index.php?title=VS:AlignDistribute2D/ja
    \n2Dオブジェクトの整列'''
    return AlignDist2DParms

def Forward():
    '''https://developer.vectorworks.net/index.php?title=VS:Forward
    \nhttps://developer.vectorworks.net/index.php?title=VS:Forward/ja
    \n選択されている図形の前後関係を、ひとつ前に移動させます。'''
    return None

def MirrorXY3D():
    '''https://developer.vectorworks.net/index.php?title=VS:MirrorXY3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:MirrorXY3D/ja
    \n選択されている3次元図形をXY座標を軸に反転します。'''
    return None

def RotatePoint(p, rotationAngle):
    '''https://developer.vectorworks.net/index.php?title=VS:RotatePoint
    \nhttps://developer.vectorworks.net/index.php?title=VS:RotatePoint/ja
    \n選択されている図形を、指定した座標を基点として回転させます。'''
    return None

def AlignDistribute3D(MenuAction):
    '''https://developer.vectorworks.net/index.php?title=VS:AlignDistribute3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:AlignDistribute3D/ja
    \n3Dオブジェクトの整列'''
    return AlignDist3DParms

def GetNumResourceTags(handle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetNumResourceTags
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNumResourceTags/ja
    \n指定したリソースに付いているタグの数を返します。'''
    return INTEGER

def MoveBack():
    '''https://developer.vectorworks.net/index.php?title=VS:MoveBack
    \nhttps://developer.vectorworks.net/index.php?title=VS:MoveBack/ja
    \n選択されている図形の前後関係を、最後に移動させます。'''
    return None

def Scale(scaleXR, scaleYR):
    '''https://developer.vectorworks.net/index.php?title=VS:Scale
    \nhttps://developer.vectorworks.net/index.php?title=VS:Scale/ja
    \nアクティブなレイヤ上の選択されている図形を拡大／縮小します。'''
    return None

def Backward():
    '''https://developer.vectorworks.net/index.php?title=VS:Backward
    \nhttps://developer.vectorworks.net/index.php?title=VS:Backward/ja
    \n選択されている図形の前後関係を、ひとつ後ろに移動させます。'''
    return None

def GetObjectTags(objHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjectTags'''
    return (BOOLEAN, outArrTags)

def MoveFront():
    '''https://developer.vectorworks.net/index.php?title=VS:MoveFront
    \nhttps://developer.vectorworks.net/index.php?title=VS:MoveFront/ja
    \n選択されている図形の前後関係を、最前に移動させます。'''
    return None

def SetObjectTags(objectHandle, arrTags):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjectTags'''
    return BOOLEAN

def CreateScriptResource(scriptName, paletteName, paletteOpen, script, python):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateScriptResource
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateScriptResource/ja
    \nファイルのスクリプトリソースを作成します。'''
    return BOOLEAN

def GetResourceTags(handle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetResourceTags
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetResourceTags/ja
    \n指定したリソースに付いているタグを返します。'''
    return tags

def ResetOrientation3D():
    '''https://developer.vectorworks.net/index.php?title=VS:ResetOrientation3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:ResetOrientation3D/ja
    \n3次元表示のパラメータをリセットします。'''
    return None

def SetResourceTags(handle, tags):
    '''https://developer.vectorworks.net/index.php?title=VS:SetResourceTags
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetResourceTags/ja
    \n指定したリソースにタグを付与します。'''
    return None

def FlipHor():
    '''https://developer.vectorworks.net/index.php?title=VS:FlipHor
    \nhttps://developer.vectorworks.net/index.php?title=VS:FlipHor/ja
    \n選択されている図形を水平反転させます。'''
    return None

def GetScriptResource(scriptName):
    '''https://developer.vectorworks.net/index.php?title=VS:GetScriptResource
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetScriptResource/ja
    \n指定したスクリプトリソースのスクリプトを返します。'''
    return (BOOLEAN, script, python)

def Rotate(rotationAngle):
    '''https://developer.vectorworks.net/index.php?title=VS:Rotate
    \nhttps://developer.vectorworks.net/index.php?title=VS:Rotate/ja
    \n選択されている図形を、中心を基点として回転させます。'''
    return None

def SetScriptResource(scriptName, script, python):
    '''https://developer.vectorworks.net/index.php?title=VS:SetScriptResource
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetScriptResource/ja
    \n指定したスクリプトリソースのスクリプトテキストを入力します。'''
    return BOOLEAN

def FlipVer():
    '''https://developer.vectorworks.net/index.php?title=VS:FlipVer
    \nhttps://developer.vectorworks.net/index.php?title=VS:FlipVer/ja
    \n選択されている図形を垂直反転させます。'''
    return None

def LckObjs():
    '''https://developer.vectorworks.net/index.php?title=VS:LckObjs
    \nhttps://developer.vectorworks.net/index.php?title=VS:LckObjs/ja
    \nアクティブなレイヤ上で選択されている図形をロックします。コピー、複製を行うことはできますが、その他の変更はできません。'''
    return None

def Rotate3D(xAngle, yAngle, zAngle):
    '''https://developer.vectorworks.net/index.php?title=VS:Rotate3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:Rotate3D/ja
    \n直前に作成された3次元図形を、指定した角度で回転させます。'''
    return None

def UnLckObjs():
    '''https://developer.vectorworks.net/index.php?title=VS:UnLckObjs
    \nhttps://developer.vectorworks.net/index.php?title=VS:UnLckObjs/ja
    \nアクティブなレイヤ上で選択されている図形のロックを解除します。'''
    return None

def CalcPolySegLen(hPoly, i1, i2):
    '''https://developer.vectorworks.net/index.php?title=VS:CalcPolySegLen
    \nhttps://developer.vectorworks.net/index.php?title=VS:CalcPolySegLen/ja
    \n多角形もしくは曲線の二つの分節間の距離を計算します。'''
    return REAL

def Eq(value1, value2, tolerance):
    '''https://developer.vectorworks.net/index.php?title=VS:Eq
    \nhttps://developer.vectorworks.net/index.php?title=VS:Eq/ja
    \n二つの実数が誤差の範囲で等しければTRUEを返します。'''
    return BOOLEAN

def GetWallHeight(hWall):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallHeight
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWallHeight/ja
    \n壁の始まりと終わりの高さを返します。'''
    return (dStartTopHght, dStartBotHght, dEndTopHght, dEndBotHght)

def PtInPoly(p, h):
    '''https://developer.vectorworks.net/index.php?title=VS:PtInPoly
    \nhttps://developer.vectorworks.net/index.php?title=VS:PtInPoly/ja
    \nハンドルで指定した多角形／曲線の内側に、指定した座標が入っていればTRUEを返します。'''
    return BOOLEAN

def Centroid(h):
    '''https://developer.vectorworks.net/index.php?title=VS:Centroid
    \nhttps://developer.vectorworks.net/index.php?title=VS:Centroid/ja
    \nオブジェクトの重心を返します。対応していないオブジェクトが渡った場合はFALSEを返します。'''
    return (BOOLEAN, x, y)

def EqPercent(value1, value2, percent):
    '''https://developer.vectorworks.net/index.php?title=VS:EqPercent
    \nhttps://developer.vectorworks.net/index.php?title=VS:EqPercent/ja
    \nnum1 と num2 が与えられたパーセントの範囲で等しければTRUEを返します。'''
    return BOOLEAN

def GetZatXY(hObject, X, Y):
    '''https://developer.vectorworks.net/index.php?title=VS:GetZatXY
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetZatXY/ja
    \n指定したオブジェクトの点（X、Y）におけるZ高さを返します。hObject = NILの場合は、表示されている全ての図形を対象にします。hObject = layerの場合はレイヤ上の全ての図形となります。'''
    return (BOOLEAN, outZ)

def PtInRect(point, rect1, rect2):
    '''https://developer.vectorworks.net/index.php?title=VS:PtInRect
    \nhttps://developer.vectorworks.net/index.php?title=VS:PtInRect/ja
    \n指定した四角形の座標の内側に、指定した座標が入っていればTRUEを返します。'''
    return BOOLEAN

def CircleCircleInters(cenPt1, cenPt2, radius1, radius2):
    '''https://developer.vectorworks.net/index.php?title=VS:CircleCircleInters
    \nhttps://developer.vectorworks.net/index.php?title=VS:CircleCircleInters/ja
    \n二つの円の交点を返します。'''
    return (BOOLEAN, pt1, pt2)

def EqPt(pt1, pt2, tolerance):
    '''https://developer.vectorworks.net/index.php?title=VS:EqPt
    \nhttps://developer.vectorworks.net/index.php?title=VS:EqPt/ja
    \n二つの2D点が誤差の範囲で等しければTRUEを返します。'''
    return BOOLEAN

def HCenter(h):
    '''https://developer.vectorworks.net/index.php?title=VS:HCenter
    \nhttps://developer.vectorworks.net/index.php?title=VS:HCenter/ja
    \nハンドルで指定した図形の中心の座標を返します。ほとんどの図形の場合、バウンダリボックスの中心を返します。円、円弧、円弧壁の場合、図形の中心を返します。'''
    return p

def PtOnArc(pt, cenPt, radius, startAng, sweepAng, tolerance):
    '''https://developer.vectorworks.net/index.php?title=VS:PtOnArc
    \nhttps://developer.vectorworks.net/index.php?title=VS:PtOnArc/ja
    \n点が円弧状にあるかどうか判定します。'''
    return BOOLEAN

def ClipPolygon(hPolygon, hClipper, dFuzz):
    '''https://developer.vectorworks.net/index.php?title=VS:ClipPolygon
    \nhttps://developer.vectorworks.net/index.php?title=VS:ClipPolygon/ja
    \nIntersectSurfaceと同様。ただし、まずhClipperがhPolygonのバウンディングボックスに入っているか確認することで性能が向上している。'''
    return HANDLE

def EqPt2D(pt1, pt2, tolerance):
    '''https://developer.vectorworks.net/index.php?title=VS:EqPt2D
    \nhttps://developer.vectorworks.net/index.php?title=VS:EqPt2D/ja
    \n二つの2D点が誤差の範囲で等しければTRUEを返します。'''
    return BOOLEAN

def LineCircleIntersect(begPt, endPt, cenPt, radius):
    '''https://developer.vectorworks.net/index.php?title=VS:LineCircleIntersect
    \nhttps://developer.vectorworks.net/index.php?title=VS:LineCircleIntersect/ja
    \n直線と円の交点を探します。'''
    return (BOOLEAN, pt1, pt2)

def PtOnLine(pt, begPt, endPt, tolerance):
    '''https://developer.vectorworks.net/index.php?title=VS:PtOnLine
    \nhttps://developer.vectorworks.net/index.php?title=VS:PtOnLine/ja'''
    return BOOLEAN

def ClosestPoints(h1, h2):
    '''https://developer.vectorworks.net/index.php?title=VS:ClosestPoints
    \nhttps://developer.vectorworks.net/index.php?title=VS:ClosestPoints/ja
    \n二つのオブジェクト上のお互いに最も近接する点を返します。曲線とNURBSを含む全てのVW基本図形で動作するはず。グループ、シンボルやプラグインオブジェクトに対応することすることが望ましい。3Dも対応できるとよい。'''
    return (pt1, pt2, touching)

def EqPt3D(pt1, pt2, tolerance):
    '''https://developer.vectorworks.net/index.php?title=VS:EqPt3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:EqPt3D/ja
    \n二つの3D点が誤差の範囲で等しければTRUEを返します。'''
    return BOOLEAN

def LineEllipseIntersect(a1, a2, upperRight, lowerLeft):
    '''https://developer.vectorworks.net/index.php?title=VS:LineEllipseIntersect
    \nhttps://developer.vectorworks.net/index.php?title=VS:LineEllipseIntersect/ja
    \n線分と楕円の交点を返します。'''
    return (int1, legal1, int2, legal2)

def PtPerpCircle(pt, cenPt, radius):
    '''https://developer.vectorworks.net/index.php?title=VS:PtPerpCircle
    \nhttps://developer.vectorworks.net/index.php?title=VS:PtPerpCircle/ja
    \n入力点に最も近い円上の点を返します。'''
    return VECTOR

def Cloud(h, rMin, rMax, hFactor, convex, removeIntersections):
    '''https://developer.vectorworks.net/index.php?title=VS:Cloud
    \nhttps://developer.vectorworks.net/index.php?title=VS:Cloud/ja
    \n雲型を描く。雲のもくもくをrMinからrMaxの間でランダムに変化させる。hFactorはそれぞれの円弧の高さである。'''
    return HANDLE

def EqualPt(p1, p2):
    '''https://developer.vectorworks.net/index.php?title=VS:EqualPt
    \nhttps://developer.vectorworks.net/index.php?title=VS:EqualPt/ja
    \n指定した2つの座標が同じならばTRUEを返します。'''
    return BOOLEAN

def LineLineIntersection(l1start, l1end, l2start, l2end):
    '''https://developer.vectorworks.net/index.php?title=VS:LineLineIntersection
    \nhttps://developer.vectorworks.net/index.php?title=VS:LineLineIntersection/ja
    \n2つの線分の交点座標を返します。'''
    return (parallel, intOnLines, sectpt)

def PtPerpLine(pt, begPt, endPt):
    '''https://developer.vectorworks.net/index.php?title=VS:PtPerpLine
    \nhttps://developer.vectorworks.net/index.php?title=VS:PtPerpLine/ja
    \n与えられた線上で、与えられた点に最も近い点を返します。点が線上にあるかどうかは確認しない。'''
    return VECTOR

def CombinePolygons(hPolygonA, hPolygonB, dFuzz):
    '''https://developer.vectorworks.net/index.php?title=VS:CombinePolygons
    \nhttps://developer.vectorworks.net/index.php?title=VS:CombinePolygons/ja
    \n二つの多角形を結合します。'''
    return HANDLE

def EqualRect(rectAp1, rectAp2, rectBp1, rectBp2):
    '''https://developer.vectorworks.net/index.php?title=VS:EqualRect
    \nhttps://developer.vectorworks.net/index.php?title=VS:EqualRect/ja
    \n指定した2つの四角形が同じならばTRUEを返します。'''
    return BOOLEAN

def OffsetPoly(h, offsetDistance, numberOfOffsets, consolidateVertices, sharpCorners, conversionRes, consolidationTolerance):
    '''https://developer.vectorworks.net/index.php?title=VS:OffsetPoly
    \nhttps://developer.vectorworks.net/index.php?title=VS:OffsetPoly/ja
    \n多角形や曲線をオフセットします。図形は閉じていても開いても動作するはずです。正の距離の場合は外側へ、負の場合は内側へオフセットされます。自己交差する線分は削除されます。スムージングのあるなしも選べます。'''
    return HANDLE

def RegularPolygon(centerX, centerY, radius, numSides, mode):
    '''https://developer.vectorworks.net/index.php?title=VS:RegularPolygon
    \nhttps://developer.vectorworks.net/index.php?title=VS:RegularPolygon/ja
    \n正多角形作成します。'''
    return None

def ConvertToArcPolyline(hPolygon, dFuzz):
    '''https://developer.vectorworks.net/index.php?title=VS:ConvertToArcPolyline
    \nhttps://developer.vectorworks.net/index.php?title=VS:ConvertToArcPolyline/ja
    \nハンドルで指定した図形（四角形、曲線、多角形など）を多角形または曲線に変換します。元の図形は残ります。'''
    return HANDLE

def FindObjAtPt_Create(hContainer, objOptions, travOptions, locX, locY, pickRadius):
    '''https://developer.vectorworks.net/index.php?title=VS:FindObjAtPt_Create
    \nhttps://developer.vectorworks.net/index.php?title=VS:FindObjAtPt_Create/ja
    \n指定した点から指定した半径何あるオブジェクトを返します。この関数は繰り返し（イテレーション）に対応している。'''
    return LONGINT

def OffsetPolyN(h, offsetDistance, smoothCorners):
    '''https://developer.vectorworks.net/index.php?title=VS:OffsetPolyN
    \nhttps://developer.vectorworks.net/index.php?title=VS:OffsetPolyN/ja
    \n多角形や曲線をオフセットします。Parasolidを使用します。ボロノイをもとにしたOffsetPolyと等価です。'''
    return HANDLE

def RelativeCoords(pt, begPt, endPt):
    '''https://developer.vectorworks.net/index.php?title=VS:RelativeCoords
    \nhttps://developer.vectorworks.net/index.php?title=VS:RelativeCoords/ja
    \nある点を異なる二つの点で定義される座標系へ変換します。'''
    return VECTOR

def ConvertToPolygon(h, resolution):
    '''https://developer.vectorworks.net/index.php?title=VS:ConvertToPolygon
    \nhttps://developer.vectorworks.net/index.php?title=VS:ConvertToPolygon/ja
    \nオブジェクトを多角形に変換します。'''
    return HANDLE

def FindObjAtPt_Create3D(hContainer, objOptions, travOptions, locX, locY, locZ, pickRadius):
    '''https://developer.vectorworks.net/index.php?title=VS:FindObjAtPt_Create3D'''
    return LONGINT

def OverlapLineArc(begPt, endpt, cenPt, radius, startAng, sweepAng, tolerance):
    '''https://developer.vectorworks.net/index.php?title=VS:OverlapLineArc
    \nhttps://developer.vectorworks.net/index.php?title=VS:OverlapLineArc/ja
    \n円弧と線分（直線）の重なる部分を探す。存在する場合は重なった線分を返します。'''
    return (BOOLEAN, lapPt1, lapPt2)

def Split2DObjectByLine(objectHd, p1, p2):
    '''https://developer.vectorworks.net/index.php?title=VS:Split2DObjectByLine
    \nhttps://developer.vectorworks.net/index.php?title=VS:Split2DObjectByLine/ja
    \nハンドルで指定した図形を2点で定義される直線で分割します。分割された図形はlistHdsハンドルでアクセスします。'''
    return listHds

def ConvertToPolyline(h):
    '''https://developer.vectorworks.net/index.php?title=VS:ConvertToPolyline
    \nhttps://developer.vectorworks.net/index.php?title=VS:ConvertToPolyline/ja
    \nあらゆる閉じた図形（円、四角形、楕円など）を多角形もしくは曲線に変換します。多角形化は行いません。'''
    return HANDLE

def FindObjAtPt_Delete(finderID):
    '''https://developer.vectorworks.net/index.php?title=VS:FindObjAtPt_Delete
    \nhttps://developer.vectorworks.net/index.php?title=VS:FindObjAtPt_Delete/ja
    \nfind object iteratorを削除します'''
    return None

def OverlapLineLine(begPt1, endPt1, begPt2, endPt2, tolerance):
    '''https://developer.vectorworks.net/index.php?title=VS:OverlapLineLine
    \nhttps://developer.vectorworks.net/index.php?title=VS:OverlapLineLine/ja
    \n二つの線分（直線）の重なる部分となる線分の二点を返します。'''
    return (BOOLEAN, lapPt1, lapPt2)

def SrndArea(p):
    '''https://developer.vectorworks.net/index.php?title=VS:SrndArea
    \nhttps://developer.vectorworks.net/index.php?title=VS:SrndArea/ja
    \n選択された多角形の中の、指定した測定点のある部分の面積を返します。'''
    return REAL

def CutProfileHoles(hWall):
    '''https://developer.vectorworks.net/index.php?title=VS:CutProfileHoles
    \nhttps://developer.vectorworks.net/index.php?title=VS:CutProfileHoles/ja
    \n輪郭グループに含まれる図形に穴を開ける。'''
    return None

def FindObjAtPt_GetCount(finderID):
    '''https://developer.vectorworks.net/index.php?title=VS:FindObjAtPt_GetCount
    \nhttps://developer.vectorworks.net/index.php?title=VS:FindObjAtPt_GetCount/ja
    \nfind iteratorのオブジェクト数を返します'''
    return INTEGER

def PointAlongPoly(h, dist):
    '''https://developer.vectorworks.net/index.php?title=VS:PointAlongPoly
    \nhttps://developer.vectorworks.net/index.php?title=VS:PointAlongPoly/ja
    \n多角形や曲線に沿って指定した距離にある点とその点での接戦ベクトルを返します。'''
    return (BOOLEAN, pt, tangent)

def Stipple(hProfileObject, shapeType, density, clipToProfile, minSize, maxSize, minAspectRatio, maxAspectRatio, randomRotate):
    '''https://developer.vectorworks.net/index.php?title=VS:Stipple
    \nhttps://developer.vectorworks.net/index.php?title=VS:Stipple/ja
    \n“輪郭図形”を埋める“点描図形”を生成します。'''
    return HANDLE

def Distance(x1, y1, x2, y2):
    '''https://developer.vectorworks.net/index.php?title=VS:Distance
    \nhttps://developer.vectorworks.net/index.php?title=VS:Distance/ja
    \n指定した2点間の距離を返します。'''
    return REAL

def FindObjAtPt_GetObj(finderID, objIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:FindObjAtPt_GetObj
    \nhttps://developer.vectorworks.net/index.php?title=VS:FindObjAtPt_GetObj/ja
    \nfind iteratorからオブジェクトを取得します'''
    return HANDLE

def PointAlongPolyN(h, dist, epsilon):
    '''https://developer.vectorworks.net/index.php?title=VS:PointAlongPolyN
    \nhttps://developer.vectorworks.net/index.php?title=VS:PointAlongPolyN/ja
    \n多角形や曲線に沿って指定した距離にある点とその点での接戦ベクトルを返します。PointAlongPolyと同様だが、イプシロン値を設定できる。'''
    return (BOOLEAN, pt, tangent)

def SubtractPolygon(hMinuedPoly, hSubtrahend, dFuzz):
    '''https://developer.vectorworks.net/index.php?title=VS:SubtractPolygon
    \nhttps://developer.vectorworks.net/index.php?title=VS:SubtractPolygon/ja
    \n一方の多角形から他方を切り欠きます。'''
    return HANDLE

def Distance3D(x1, y1, z1, x2, y2, z2):
    '''https://developer.vectorworks.net/index.php?title=VS:Distance3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:Distance3D/ja
    \n2点の三次元的距離を返します。Normと同じ。'''
    return REAL

def GetObjectHiddenLine(hGeometry3D, cuttingHeight, bottomOfCutPlane):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjectHiddenLine
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetObjectHiddenLine/ja
    \n指定したオブジェクトを隠線消去レンダリングで表現したときの線を生成します。'''
    return HANDLE

def PolyMedialAxis(h):
    '''https://developer.vectorworks.net/index.php?title=VS:PolyMedialAxis
    \nhttps://developer.vectorworks.net/index.php?title=VS:PolyMedialAxis/ja
    \n与えられた多角形の重み付き中心軸の線のグループを作成します。'''
    return HANDLE

def ThreePtCenter(pt1, pt2, pt3):
    '''https://developer.vectorworks.net/index.php?title=VS:ThreePtCenter
    \nhttps://developer.vectorworks.net/index.php?title=VS:ThreePtCenter/ja
    \n与えられた3点を通過する円の中心を返します。'''
    return VECTOR

def EllipseEllipseIntersect(upperLeft1, lowerRight1, upperLeft2, lowerRight2):
    '''https://developer.vectorworks.net/index.php?title=VS:EllipseEllipseIntersect
    \nhttps://developer.vectorworks.net/index.php?title=VS:EllipseEllipseIntersect/ja
    \n指定した2つの楕円の交点数と座標を計算します。'''
    return (INTEGER, int1, int2, int3, int4)

def GetPtInPoly(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPtInPoly
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPtInPoly/ja
    \n曲線の中の点を探す。'''
    return VECTOR

def Polygonize(h, segmentationLength, polygonizeStraight):
    '''https://developer.vectorworks.net/index.php?title=VS:Polygonize'''
    return HANDLE

def UnionRect(p1, p2, p3, p4, p5, p6):
    '''https://developer.vectorworks.net/index.php?title=VS:UnionRect
    \nhttps://developer.vectorworks.net/index.php?title=VS:UnionRect/ja
    \n指定した2つの四角形を囲む四角形の座標を返します。'''
    return (p5, p6)

def AddVectorFillLayer(xStart, yStart, xRepeat, yRepeat, xOffset, yOffset, dashFactor, lineWeight, colorIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:AddVectorFillLayer
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddVectorFillLayer/ja
    \nハッチングに線を追加します。'''
    return None

def CreateStaticHatchFromObject(inObj, inHatchName, p, rotationAngle):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateStaticHatchFromObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateStaticHatchFromObject/ja
    \nハンドルで指定した図形に指定した名前のハッチングを、挿入する位置と角度を指定して貼り付けます。'''
    return HANDLE

def GetVectorFill(theObj):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVectorFill
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVectorFill/ja
    \nハンドルで指定した図形のハッチングの名前を返します。'''
    return (BOOLEAN, hatchName)

def SetVectorFill(theObj, hatchName):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVectorFill
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetVectorFill/ja
    \nハンドルで指定した図形にハッチングを設定します。'''
    return BOOLEAN

def BeginVectorFillN(vectorFillName, pageSpace, rotateInWall, colorIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:BeginVectorFillN
    \nhttps://developer.vectorworks.net/index.php?title=VS:BeginVectorFillN/ja
    \n新しいハッチングを作成します。'''
    return vectorFillName

def DelVectorFill(vectorFillName):
    '''https://developer.vectorworks.net/index.php?title=VS:DelVectorFill
    \nhttps://developer.vectorworks.net/index.php?title=VS:DelVectorFill/ja
    \n指定したハッチングを削除します。'''
    return None

def GetVectorFillDefault():
    '''https://developer.vectorworks.net/index.php?title=VS:GetVectorFillDefault
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVectorFillDefault/ja
    \nデフォルトのハッチングの名前を返します。'''
    return (BOOLEAN, vectorFillName)

def SetVectorFillDefault(vectorFillName):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVectorFillDefault
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetVectorFillDefault/ja
    \nデフォルトのハッチングを変更します。'''
    return BOOLEAN

def CreateStaticHatch(inHatchName, p, rotationAngle):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateStaticHatch
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateStaticHatch/ja
    \n選択している図形に名前で指定したハッチングを、挿入する位置と角度を指定して貼り付けます。'''
    return HANDLE

def EndVectorFill():
    '''https://developer.vectorworks.net/index.php?title=VS:EndVectorFill
    \nhttps://developer.vectorworks.net/index.php?title=VS:EndVectorFill/ja
    \nハッチングの作成を終了します。'''
    return None

def NumVectorFills():
    '''https://developer.vectorworks.net/index.php?title=VS:NumVectorFills
    \nhttps://developer.vectorworks.net/index.php?title=VS:NumVectorFills/ja
    \nアクティブなドキュメント内のハッチングの数を返します。'''
    return LONGINT

def VectorFillList(index):
    '''https://developer.vectorworks.net/index.php?title=VS:VectorFillList
    \nhttps://developer.vectorworks.net/index.php?title=VS:VectorFillList/ja
    \n指定した索引番号をもつハッチングの名前を返します。'''
    return STRING

def IFC_AddDSField(objectName, dataSheetName, mainEntry, childEntry, fieldName, fieldLabel):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_AddDSField'''
    return BOOLEAN

def IFC_DMGetObjCond(strObjectName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMGetObjCond'''
    return (BOOLEAN, outStrObjectCondition)

def IFC_DMSetPSetFldOpt(strObjectName, strEntryName, strPSetName, strFieldName, bOptional):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMSetPSetFldOpt'''
    return BOOLEAN

def IFC_GetSpaceParamFO(hSpace, inStrParam):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_GetSpaceParamFO
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_GetSpaceParamFO/ja
    \nスペースのタイプ、名前および番号を取得します。'''
    return (BOOLEAN, outStrResult)

def IFC_AddObjectMapping(objectName, condition, category):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_AddObjectMapping'''
    return BOOLEAN

def IFC_DMGetObjCondAt(index):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMGetObjCondAt'''
    return (BOOLEAN, outStrObjectCondition)

def IFC_DMSetPSetFldType(strObjectName, strEntryName, strPSetName, strFieldName, type):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMSetPSetFldType'''
    return BOOLEAN

def IFC_GetStructureGUID(guidType, iBuilding, iStorey):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_GetStructureGUID'''
    return (BOOLEAN, outGuid)

def IFC_AddRecToObjMap(objectName, recordName, condition, bEnable):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_AddRecToObjMap'''
    return BOOLEAN

def IFC_DMGetObjNameAt(index):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMGetObjNameAt'''
    return (BOOLEAN, outStrObjectName)

def IFC_DefPsetAddMember(psetName, propName, propType):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DefPsetAddMember
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DefPsetAddMember/ja
    \n既存のカスタムプロパティセットに項目を加えます。'''
    return BOOLEAN

def IFC_GetZSGField(selector, fieldName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_GetZSGField'''
    return (BOOLEAN, ZSGName, outFieldValue)

def IFC_AttachPSetToZSG(selector, ZSGName, psetName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_AttachPSetToZSG'''
    return BOOLEAN

def IFC_DMGetObjectsCnt():
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMGetObjectsCnt'''
    return (BOOLEAN, outCount)

def IFC_DefPsetBegin(psetName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DefPsetBegin
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DefPsetBegin/ja
    \n新規のカスタムプロパティセット作成の始まりを示します。'''
    return BOOLEAN

def IFC_GetZSGPSetField(selector, ZSGName, psetName, psetField):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_GetZSGPSetField'''
    return (BOOLEAN, outPsetFieldValue)

def IFC_AttachPset(hObject, inStrPsetName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_AttachPset
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_AttachPset/ja
    \nオブジェクトにプロパティセットを追加します。'''
    return BOOLEAN

def IFC_DMGetPSetCond(strObjectName, strEntryName, psetIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMGetPSetCond'''
    return (BOOLEAN, outStrPSetCondition)

def IFC_DefPsetEnd(psetName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DefPsetEnd
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DefPsetEnd/ja
    \n新規のカスタムプロパティセット作成の終わりを示します。'''
    return BOOLEAN

def IFC_ImportLibrary(strFilePath, bKeepHierarchy):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_ImportLibrary
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_ImportLibrary/ja
    \nIFCライブラリのオブジェクトを取り込む'''
    return BOOLEAN

def IFC_ClearAllPsets(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_ClearAllPsets
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_ClearAllPsets/ja
    \nすべてのIFCプロパティセットを削除します。'''
    return BOOLEAN

def IFC_DMGetPSetFldMap(strObjectName, strEntryName, strPSetName, strFieldName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMGetPSetFldMap'''
    return (BOOLEAN, outStrMappingSrc)

def IFC_DefPsetImport(strFolderPath):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DefPsetImport
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DefPsetImport/ja
    \nカスタムプロパティセットをXMLファイルまたはテキストファイルから取り込みます。'''
    return BOOLEAN

def IFC_ImportNoUI(strFilePath):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_ImportNoUI
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_ImportNoUI/ja
    \nIFCファイルを取り込む。サイレントモード（UIなし）'''
    return None

def IFC_ClearIFCInfo(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_ClearIFCInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_ClearIFCInfo/ja
    \n全てのIFCデータを削除します。'''
    return BOOLEAN

def IFC_DMGetPSetFldName(strObjectName, strEntryName, strPSetName, index):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMGetPSetFldName'''
    return (BOOLEAN, outStrFieldName)

def IFC_DefPsetImport2(strFilePath):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DefPsetImport2'''
    return BOOLEAN

def IFC_ImportWithUI():
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_ImportWithUI
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_ImportWithUI/ja
    \nユーザーインタフェースを表示してIFCファイルを取り込む'''
    return None

def IFC_ClearPset(hObject, inStrPsetName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_ClearPset
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_ClearPset/ja
    \nオブジェクトの指定したプロパティセットを削除します。'''
    return BOOLEAN

def IFC_DMGetPSetFldType(strObjectName, strEntryName, strPSetName, strFieldName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMGetPSetFldType'''
    return (BOOLEAN, outType)

def IFC_DelRecFromObjMap(objectName, recordName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DelRecFromObjMap'''
    return BOOLEAN

def IFC_IsFieldVisible(objectName, mainEntry, childEntry, fieldName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_IsFieldVisible'''
    return (BOOLEAN, outVisible)

def IFC_CopyIFCData(hSource, hDestination, inMode):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_CopyIFCData
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_CopyIFCData/ja
    \n一つのオブジェクトから別のオブジェクトへIFCデータをコピーします。'''
    return BOOLEAN

def IFC_DMGetPSetFldsCnt(strObjectName, strEntryName, strPSetName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMGetPSetFldsCnt'''
    return (BOOLEAN, outFieldsCount)

def IFC_DeleteDS(objectName, dataSheetName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DeleteDS'''
    return BOOLEAN

def IFC_IsPsetCustom(pSetName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_IsPsetCustom'''
    return (BOOLEAN, bCustom)

def IFC_CreateDS(objectName, dataSheetName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_CreateDS'''
    return BOOLEAN

def IFC_DMGetPSetName(strObjectName, strEntryName, psetIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMGetPSetName'''
    return (BOOLEAN, outStrPSetName)

def IFC_DeleteDSField(objectName, dataSheetName, fieldLabel):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DeleteDSField'''
    return BOOLEAN

def IFC_IsPsetDefined(strPsetName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_IsPsetDefined
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_IsPsetDefined/ja
    \n指定した名前のカスタムプロパティセットが存在するかどうかを返します。'''
    return BOOLEAN

def IFC_CreateObjGUID(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_CreateObjGUID'''
    return BOOLEAN

def IFC_DMIsEntryEnabled(inStrObjName, inStrEntryName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMIsEntryEnabled
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMIsEntryEnabled/ja
    \n現在のIFCデータマッピングで、指定した項目が適用されるかどうか調べます。'''
    return BOOLEAN

def IFC_DeleteIFCInfo(hObject:HANDLE, true);
    return None

def IFC_IsRecEnabled(objectName, recordName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_IsRecEnabled'''
    return (BOOLEAN, outIsEnabled)

def IFC_CreateZSG(selector, ZSGName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_CreateZSG'''
    return BOOLEAN

def IFC_DMIsFieldEmpty(inStrObjName, inStrEntryName, inStrFieldName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMIsFieldEmpty
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMIsFieldEmpty/ja
    \n現在のIFCデータマッピングで、指定したフィールドのマッピング階層が空かどうか調べます。'''
    return BOOLEAN

def IFC_DeleteObjectMap(objectName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DeleteObjectMap'''
    return BOOLEAN

def IFC_LAreIFCResLocal(outbAreIFCResLocal):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_LAreIFCResLocal'''
    return BOOLEAN

def IFC_DMAddEntry(inStrObjName, inStrEntryName, bEnable):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMAddEntry
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMAddEntry/ja
    \n現在のIFCデータマッピングで、指定したオブジェクトに項目を追加します。'''
    return BOOLEAN

def IFC_DMIsFieldEnabled(inStrObjName, inStrEntryName, inStrFieldName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMIsFieldEnabled
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMIsFieldEnabled/ja
    \n現在のIFCデータマッピングで、指定したフィールドが適用されるかどうか調べます。'''
    return BOOLEAN

def IFC_ExportNoUI(strFullFilePath):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_ExportNoUI'''
    return BOOLEAN

def IFC_LGetLangFromDoc(outbIsIFCLocalized):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_LGetLangFromDoc'''
    return BOOLEAN

def IFC_DMAddField(inStrObjName, inStrEntryName, inStrFieldName, type, bOptional, bEnable, bEmpty):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMAddField
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMAddField/ja
    \n現在のIFCデータマッピングにフィールドを追加します。'''
    return BOOLEAN

def IFC_DMIsFieldOpt(inStrObjName, inStrEntryName, inStrFieldName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMIsFieldOpt
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMIsFieldOpt/ja
    \n現在のIFCデータマッピングで、指定したフィールドがオプション項目かどうか調べます。'''
    return BOOLEAN

def IFC_ExportWithUI(bExpSingleObj):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_ExportWithUI
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_ExportWithUI/ja
    \nIFCプロジェクト取り出しダイアログを表示して、IFCファイルを取り出します。'''
    return None

def IFC_LGetLocalName():
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_LGetLocalName'''
    return (BOOLEAN, strIFCName, inIFCTypeOfString, outLocalName)

def IFC_DMAddPSetFld(strObjectName, strEntryName, strPSetName, strFieldName, type, bOptional, bEnable, bEmpty):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMAddPSetFld'''
    return BOOLEAN

def IFC_DMIsObjEnabled(inStrObjName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMIsObjEnabled
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMIsObjEnabled/ja
    \n現在のIFCデータマッピングで、指定したオブジェクトが適用されるかどうか調べます。'''
    return BOOLEAN

def IFC_GetDSCount(objectName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_GetDSCount'''
    return (BOOLEAN, outDSCount)

def IFC_LGetUnivName():
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_LGetUnivName'''
    return (BOOLEAN, strIFCName, inIFCTypeOfString, outLocalName)

def IFC_DMAddPSetForEnt(strObjectName, strEntryName, strPSetName, bEnabled, strPSetCondition):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMAddPSetForEnt'''
    return BOOLEAN

def IFC_DMIsPSetEnabled(strObjectName, strEntryName, strPSetName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMIsPSetEnabled'''
    return BOOLEAN

def IFC_GetDSFieldInfoAt(objectName, dataSheetName, iField):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_GetDSFieldInfoAt'''
    return (BOOLEAN, outFieldLabel, outIsVisible, outIsByFormula)

def IFC_LSetLangInDoc(bIsIFCLocalized):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_LSetLangInDoc'''
    return BOOLEAN

def IFC_DMAddPSetInEntry(inStrObjName, inStrEntryName, inStrPsetName, bEnable, inStrPsetCondition):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMAddPSetInEntry'''
    return BOOLEAN

def IFC_DMIsPSetFldEmpty(strObjectName, strEntryName, strPSetName, strFieldName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMIsPSetFldEmpty'''
    return BOOLEAN

def IFC_GetDSFieldsCount(objectName, dataSheetName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_GetDSFieldsCount'''
    return (BOOLEAN, outFieldsCount)

def IFC_LSetLangInVW(bIsIFCLocalized):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_LSetLangInVW'''
    return BOOLEAN

def IFC_DMDelPSetFromEnt(strObjectName, strEntryName, strPSetName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMDelPSetFromEnt'''
    return BOOLEAN

def IFC_DMIsPSetFldEnbl(strObjectName, strEntryName, strPSetName, strFieldName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMIsPSetFldEnbl'''
    return BOOLEAN

def IFC_GetDSNameAt(objectName, iDataSheet):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_GetDSNameAt'''
    return (BOOLEAN, outDataSheetName)

def IFC_ReadProjectData(iPane, iParam, iBuilding):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_ReadProjectData'''
    return (BOOLEAN, outData)

def IFC_DMDeleteEntry(inStrObjName, inStrEntryName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMDeleteEntry
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMDeleteEntry/ja
    \n現在のIFCデータマッピングで、オブジェクトから指定した項目を削除します。'''
    return BOOLEAN

def IFC_DMIsPSetFldOpt(strObjectName, strEntryName, strPSetName, strFieldName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMIsPSetFldOpt'''
    return BOOLEAN

def IFC_GetEntityColor(inStrIfcType):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_GetEntityColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_GetEntityColor/ja
    \nIFCエンティティタイプのデフォルト色を取得します。'''
    return (BOOLEAN, outRed, outGreen, outBlue, outTransp)

def IFC_SetDSFieldVis(objectName, dataSheetName, fieldLabel, isVisible):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_SetDSFieldVis'''
    return BOOLEAN

def IFC_DMDeleteField(inStrObjName, inStrEntryName, inStrFieldName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMDeleteField
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMDeleteField/ja
    \n現在のIFCデータマッピングで、指定したフィールドを削除します。'''
    return BOOLEAN

def IFC_DMLoadSettings(inStrParam):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMLoadSettings
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMLoadSettings/ja
    \nIFCデータマッピングを読み込みます。'''
    return BOOLEAN

def IFC_GetEntityProp(hObject, inStrPropName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_GetEntityProp
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_GetEntityProp/ja
    \nIFCエンティティの選択したプロパティの値と種類を取得します。'''
    return (BOOLEAN, outStrPropValue, outTypeSelect)

def IFC_SetEntityColor(inStrIfcType, inRed, inGreen, inBlue, inTransp):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_SetEntityColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_SetEntityColor/ja
    \nある種類のIFCエンティティのデフォルト色を設定します。'''
    return BOOLEAN

def IFC_DMDeletePSetFld(strObjectName, strEntryName, strPSetName, strFieldName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMDeletePSetFld'''
    return BOOLEAN

def IFC_DMResToCOBieDef():
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMResToCOBieDef'''
    return BOOLEAN

def IFC_GetEntityProp2(hObject, propertyName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_GetEntityProp2'''
    return (BOOLEAN, outPropValue, outType, outMap)

def IFC_SetEntityProp(hObject, inStrPropName, inStrPropValue):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_SetEntityProp
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_SetEntityProp/ja
    \nIFCエンティティの選択したプロパティの値を設定します。'''
    return BOOLEAN

def IFC_DMEnableEntry(inStrObjName, inStrEntryName, bEnable):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMEnableEntry
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMEnableEntry/ja
    \n現在のIFCデータマッピングで、指定した項目を適用する/しないを設定します。'''
    return BOOLEAN

def IFC_DMResetToDef():
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMResetToDef
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMResetToDef/ja
    \nIFCデータマッピングをVectorworksデフォルトでリセットします。'''
    return BOOLEAN

def IFC_GetIFCEntity(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_GetIFCEntity
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_GetIFCEntity/ja
    \nIFCエンティティの種類を取得します。'''
    return (BOOLEAN, outStrName)

def IFC_SetFieldVisible(objectName, mainEntry, childEntry, fieldName, isVisible):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_SetFieldVisible'''
    return BOOLEAN

def IFC_DMEnableObject(inStrObjName, bEnable):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMEnableObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMEnableObject/ja
    \n現在のIFCデータマッピングで、指定したオブジェクトを適用する/しないを設定します。'''
    return BOOLEAN

def IFC_DMSaveSettings(inStrParam, inObjName, bFileSettings):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMSaveSettings
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMSaveSettings/ja
    \nIFCデータマッピングを保存します。'''
    return BOOLEAN

def IFC_GetIFCEntity2(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_GetIFCEntity2'''
    return (BOOLEAN, outType, outStrNameRec, outStrNameMap)

def IFC_SetIFCEntity(hObject, inStrIfcName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_SetIFCEntity
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_SetIFCEntity/ja
    \nIFCエンティティの種類を設定します。'''
    return BOOLEAN

def IFC_DMEnablePSet(strObjectName, strEntryName, strPSetName, bEnable):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMEnablePSet'''
    return BOOLEAN

def IFC_DMSetEntryType(strObjectName, strEntryName, type):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMSetEntryType'''
    return BOOLEAN

def IFC_GetIFCName(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_GetIFCName'''
    return (BOOLEAN, outStrIfcName)

def IFC_SetIFCEntity2(hObject, inStrIfcType):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_SetIFCEntity2'''
    return BOOLEAN

def IFC_DMGetEntPSetsCnt(strObjectName, strEntryName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMGetEntPSetsCnt'''
    return (BOOLEAN, outType)

def IFC_DMSetFieldEmpty(inStrObjName, inStrEntryName, inStrFieldName, bEmpty):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMSetFieldEmpty
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMSetFieldEmpty/ja
    \n指定したフィールドのマッピング階層をクリアします。'''
    return BOOLEAN

def IFC_GetIFCScheme():
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_GetIFCScheme
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_GetIFCScheme/ja
    \nアクティブなIFCバージョンを取得します。'''
    return (BOOLEAN, outScheme)

def IFC_SetIFCScheme(scheme):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_SetIFCScheme
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_SetIFCScheme/ja
    \nアクティブなIFCバージョンを設定します。'''
    return BOOLEAN

def IFC_DMGetEntriesCnt(inStrObjName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMGetEntriesCnt
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMGetEntriesCnt/ja
    \n現在のIFCデータマッピングで、指定したオブジェクトの項目の数を取得します。'''
    return (BOOLEAN, outCount)

def IFC_DMSetFieldEnable(inStrObjName, inStrEntryName, inStrFieldName, bEnable):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMSetFieldEnable
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMSetFieldEnable/ja
    \n指定したフィールドを適用するかどうか設定します。'''
    return BOOLEAN

def IFC_GetNumPsetProps(strPsetName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_GetNumPsetProps'''
    return (BOOLEAN, outNumPsets)

def IFC_SetProperty(hObject, pSetName, propertyName, propValue):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_SetProperty'''
    return BOOLEAN

def IFC_DMGetEntryName(index, inStrObjName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMGetEntryName
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMGetEntryName/ja
    \n現在のIFCデータマッピングで、指定したインデックスの項目の名前を取得します。'''
    return (BOOLEAN, outStrResult)

def IFC_DMSetFieldMap(inStrObjName, inStrEntryName, inStrFieldName, strMappingSrc):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMSetFieldMap
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMSetFieldMap/ja
    \n現在のIFCデータマッピングで、指定したフィールドのマッピング階層を設定します。'''
    return BOOLEAN

def IFC_GetNumPsets(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_GetNumPsets
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_GetNumPsets/ja
    \nオブジェクトに付加されているプロパティセットの数を取得します。'''
    return (BOOLEAN, outNumPsets)

def IFC_SetPsetProp(hObject, inStrPsetName, inStrPropName, inStrPropValue):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_SetPsetProp
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_SetPsetProp/ja
    \nプロパティセットの選択したプロパティの値を設定します。'''
    return BOOLEAN

def IFC_DMGetEntryType(strObjectName, index):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMGetEntryType'''
    return (BOOLEAN, outType)

def IFC_DMSetFieldOpt(inStrObjName, inStrEntryName, inStrFieldName, bOptional):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMSetFieldOpt
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMSetFieldOpt/ja
    \n指定したフィールドをオプション項目に設定します。'''
    return BOOLEAN

def IFC_GetNumPsets2(hObject, bAllPsets):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_GetNumPsets2'''
    return (BOOLEAN, outNumPsets)

def IFC_SetRecEnabled(objectName, recordName, bEnable):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_SetRecEnabled'''
    return BOOLEAN

def IFC_DMGetFieldMap(inStrObjName, inStrEntryName, inStrFieldName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMGetFieldMap
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMGetFieldMap/ja
    \n現在のIFCデータマッピングで、指定したフィールドのマッピング階層を取得します。'''
    return (BOOLEAN, outStrResult)

def IFC_DMSetFieldType(inStrObjName, inStrEntryName, inStrFieldName, type):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMSetFieldType
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMSetFieldType/ja
    \n現在のIFCデータマッピングで、指定したフィールドのタイプを設定します。'''
    return BOOLEAN

def IFC_GetPsetInfoAt(hObject, bAllPsets, index):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_GetPsetInfoAt'''
    return (BOOLEAN, outIfcPsetName, outType)

def IFC_SetStructureGUID(guidType, iBuilding, iStorey, Guid):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_SetStructureGUID'''
    return BOOLEAN

def IFC_DMGetFieldName(inStrObjName, inStrEntryName, index):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMGetFieldName
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMGetFieldName/ja
    \n現在のIFCデータマッピングで、指定したフィールドの名前を取得します。'''
    return (BOOLEAN, outStrFieldName)

def IFC_DMSetObjectCond(strObjectName, strCondition):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMSetObjectCond'''
    return BOOLEAN

def IFC_GetPsetName(hObject, inPsetIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_GetPsetName
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_GetPsetName/ja
    \n指定した番号のプロパティセットの名前を取得します。'''
    return ok, outStrPsetName

def IFC_SetZSGField(selector, ZSGName, fieldName, fieldValue):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_SetZSGField'''
    return BOOLEAN

def IFC_DMGetFieldType(inStrObjName, inStrEntryName, inStrFieldName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMGetFieldType
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMGetFieldType/ja
    \n現在のIFCデータマッピングで、指定したフィールドのタイプを取得します。'''
    return (BOOLEAN, outType)

def IFC_DMSetPSetFldEmpt(strObjectName, strEntryName, strPSetName, strFieldName, bEmpty):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMSetPSetFldEmpt'''
    return BOOLEAN

def IFC_GetPsetProp(hObject, inStrPsetName, inStrPropName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_GetPsetProp
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_GetPsetProp/ja
    \nプロパティセットの選択したプロパティの値と種類を取得します。'''
    return (BOOLEAN, outStrPropValue, outTypeSelect)

def IFC_SetZSGPSetField(selector, ZSGName, psetName, psetField, psetFieldValue):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_SetZSGPSetField'''
    return BOOLEAN

def IFC_DMGetFieldsCount(inStrObjName, inStrEntryName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMGetFieldsCount
    \nhttps://developer.vectorworks.net/index.php?title=VS:IFC_DMGetFieldsCount/ja
    \n現在のIFCデータマッピングで、指定した項目のフィールドの数を取得します。'''
    return (BOOLEAN, outCount)

def IFC_DMSetPSetFldEnbl(strObjectName, strEntryName, strPSetName, strFieldName, bEnable):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMSetPSetFldEnbl'''
    return BOOLEAN

def IFC_GetPsetProp2(hObject, pSetName, propertyName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_GetPsetProp2'''
    return (BOOLEAN, outPropValue, outType, outMap)

def IFC_WriteProjectData(iPane, iParam, iBuilding, data):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_WriteProjectData'''
    return BOOLEAN

def IFC_DMGetObjCategory(strObjectName):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMGetObjCategory'''
    return BOOLEAN, outMappingCategory

def IFC_DMSetPSetFldMap(strObjectName, strEntryName, strPSetName, strFieldName, strMappingSrc):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_DMSetPSetFldMap'''
    return BOOLEAN

def IFC_GetPsetPropName(strPsetName, indexProperty):
    '''https://developer.vectorworks.net/index.php?title=VS:IFC_GetPsetPropName'''
    return (BOOLEAN, outPsetPropName)

def ReplaceIFCWithMap(hObject, inStrObjName):
    '''https://developer.vectorworks.net/index.php?title=VS:ReplaceIFCWithMap'''
    return BOOLEAN

def DXFScaleString(scale):
    '''https://developer.vectorworks.net/index.php?title=VS:DXFScaleString
    \nhttps://developer.vectorworks.net/index.php?title=VS:DXFScaleString/ja
    \nDXFスケールの文字を返します。'''
    return STRING

def ImportDXFDWG():
    '''https://developer.vectorworks.net/index.php?title=VS:ImportDXFDWG
    \nhttps://developer.vectorworks.net/index.php?title=VS:ImportDXFDWG/ja
    \nDXF/DWGファイルまたはDWFファイルを１つまたは複数取り込みます。'''
    return None

def ImportSketchUp(filePath, bImportAsMesh):
    '''https://developer.vectorworks.net/index.php?title=VS:ImportSketchUp
    \nhttps://developer.vectorworks.net/index.php?title=VS:ImportSketchUp/ja
    \nSketchUp ( *.skp) ファイルを取り込みます。'''
    return BOOLEAN

def SetDXFColorToLW(dxfClrIndex, lineWeight):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDXFColorToLW
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDXFColorToLW/ja
    \n指定したDXFカラー番号を、線の太さに設定します。'''
    return None

def ExportDXFDWG():
    '''https://developer.vectorworks.net/index.php?title=VS:ExportDXFDWG
    \nhttps://developer.vectorworks.net/index.php?title=VS:ExportDXFDWG/ja
    \nDXF/DWGを取り出します'''
    return None

def ImportDXFDWGFile(fileName):
    '''https://developer.vectorworks.net/index.php?title=VS:ImportDXFDWGFile
    \nhttps://developer.vectorworks.net/index.php?title=VS:ImportDXFDWGFile/ja
    \n指定したDXF/DWGファイルを取り込みます。'''
    return INTEGER

def Init3DSServices():
    '''https://developer.vectorworks.net/index.php?title=VS:Init3DSServices
    \nhttps://developer.vectorworks.net/index.php?title=VS:Init3DSServices/ja
    \n取り込み、取り出しのために3DSサービスライブラリを初期化します。'''
    return None

def SetLTGeneration(ltGeneration):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLTGeneration'''
    return None

def GetDXFColorToLW(dxfClrIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDXFColorToLW
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDXFColorToLW/ja
    \nDXFカラーを線の太さとして返します。'''
    return INTEGER

def ImportOBJ(fileName, bAllMatAsRW):
    '''https://developer.vectorworks.net/index.php?title=VS:ImportOBJ
    \nhttps://developer.vectorworks.net/index.php?title=VS:ImportOBJ/ja
    \nWavefront (*.obj) ファイルを取り込みます。'''
    return BOOLEAN

def InitDWGServices():
    '''https://developer.vectorworks.net/index.php?title=VS:InitDWGServices
    \nhttps://developer.vectorworks.net/index.php?title=VS:InitDWGServices/ja
    \n取り出し・取り込みのDWGライブラリーサービスを初期化します。'''
    return None

def SetLastDXFImportOpt(selector, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLastDXFImportOpt
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLastDXFImportOpt/ja
    \n前回のDXF取り込み設定を使用します。'''
    return BOOLEAN

def GetLastDXFImportOpt(selector, value):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLastDXFImportOpt
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLastDXFImportOpt/ja
    \n前回使用したDXF取り込み設定を返します。'''
    return BOOLEAN

def ImportRevit(fileName):
    '''https://developer.vectorworks.net/index.php?title=VS:ImportRevit
    \nhttps://developer.vectorworks.net/index.php?title=VS:ImportRevit/ja
    \nRVT または RFA ファイルを取り込みます。'''
    return None

def InitRevitServices():
    '''https://developer.vectorworks.net/index.php?title=VS:InitRevitServices
    \nhttps://developer.vectorworks.net/index.php?title=VS:InitRevitServices/ja
    \n取り込み、取り出しのためにRevitサービスライブラリを初期化します。'''
    return None

def Import3DSFile(fileName, atOrigCoords, positionX, positionY):
    '''https://developer.vectorworks.net/index.php?title=VS:Import3DSFile'''
    return BOOLEAN

def ImportSingleDXFDWG():
    '''https://developer.vectorworks.net/index.php?title=VS:ImportSingleDXFDWG
    \nhttps://developer.vectorworks.net/index.php?title=VS:ImportSingleDXFDWG/ja
    \nDXF/DWGファイルを１つ取り込みます。'''
    return None

def PublishSavedSet(savedSetName, outputFolder):
    '''https://developer.vectorworks.net/index.php?title=VS:PublishSavedSet'''
    return BOOLEAN

def ActLayer():
    '''https://developer.vectorworks.net/index.php?title=VS:ActLayer
    \nhttps://developer.vectorworks.net/index.php?title=VS:ActLayer/ja
    \nアクティブなレイヤのハンドルを返します。'''
    return HANDLE

def GetLayerCutPlane(layer):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLayerCutPlane
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLayerCutPlane/ja
    \nレイヤの切断面の高さを返します。'''
    return REAL

def GetStoryElevation(story):
    '''https://developer.vectorworks.net/index.php?title=VS:GetStoryElevation
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetStoryElevation/ja
    \n指定したストーリの高さを返します。'''
    return REAL

def SetDefStoryLayerName(index, name):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDefStoryLayerName
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDefStoryLayerName/ja
    \n指定したストーリレイヤ初期設定の名前を設定します。'''
    return BOOLEAN

def AddLevelFromTemplate(storyHandle, index):
    '''https://developer.vectorworks.net/index.php?title=VS:AddLevelFromTemplate
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddLevelFromTemplate/ja
    \nストーリレベルテンプレートを使用して、指定したストーリにストーリレベルを追加します。 テンプレートのレベルタイプおよび高さの設定がストーリ内の既存のものと重複していない必要があります。 テンプレートにレイヤー名が設定されている場合、新しいレイヤーが作成され、ストーリーレベルに関連付けられます。'''
    return BOOLEAN

def GetLayerElevation(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLayerElevation
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLayerElevation/ja
    \nハンドルで指定したレイヤの高さ（Z）と厚み（ΔZ）を返します。'''
    return (baseElev, thickness)

def GetStoryElevationN(story):
    '''https://developer.vectorworks.net/index.php?title=VS:GetStoryElevationN'''
    return REAL

def SetLScale(h, scale):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLScale
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLScale/ja
    \nハンドルで指定したレイヤの縮尺を変更します。'''
    return None

def AddStoryLevel(storyHandle, levelType, elevation, layerName):
    '''https://developer.vectorworks.net/index.php?title=VS:AddStoryLevel
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddStoryLevel/ja
    \n指定したストーリにストーリレベルを追加します。 レベルタイプおよび高さの設定がストーリ内の既存のものと重複していない必要があります。 レイヤー名を指定した場合、ストーリーレベルに関連付けられます。'''
    return BOOLEAN

def GetLayerElevationN(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLayerElevationN'''
    return (baseElev, thickness)

def GetStoryLayerTemplateName(index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetStoryLayerTemplateName
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetStoryLayerTemplateName/ja
    \nファイルにあるn番目のストーリレイヤテンプレートの名前を返します。'''
    return STRING

def SetLayerCutPlane(layer, cutPlane):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLayerCutPlane
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLayerCutPlane/ja
    \nレイヤの切断面の高さを設定します。'''
    return None

def AddStoryLevelN(storyHandle, levelType, elevation, layerName):
    '''https://developer.vectorworks.net/index.php?title=VS:AddStoryLevelN'''
    return BOOLEAN

def GetLayerEnableCutPl(layer):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLayerEnableCutPl
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLayerEnableCutPl/ja
    \nレイヤの切断面が有効になっているかどうかを取得します。'''
    return BOOLEAN

def GetStoryOfLayer(layer):
    '''https://developer.vectorworks.net/index.php?title=VS:GetStoryOfLayer
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetStoryOfLayer/ja
    \n指定されたレイヤに関連付けられたストーリを返します。レイヤがストーリに関連付けられていない場合、NULLを返します。'''
    return HANDLE

def SetLayerElevation(h, baseElev, thickness):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLayerElevation
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLayerElevation/ja
    \nハンドルで指定したレイヤの高さ（Z）と厚み（ΔZ）を設定します。'''
    return None

def AssociateLayerWithStory(layer, story):
    '''https://developer.vectorworks.net/index.php?title=VS:AssociateLayerWithStory
    \nhttps://developer.vectorworks.net/index.php?title=VS:AssociateLayerWithStory/ja
    \nレイヤとストーリを関連付けます。レイヤがストーリに関連付けられている場合、レイヤの高さはストーリの高さからの相対的な高さになります。関連付けられたストーリの高さが変更された場合、レイヤの高さも連動して変更されます。'''
    return BOOLEAN

def GetLayerForStory(story, levelType):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLayerForStory
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLayerForStory/ja
    \n指定したストーリとレベルタイプをを持つレイヤを返します。'''
    return HANDLE

def GetStorySuffix(story):
    '''https://developer.vectorworks.net/index.php?title=VS:GetStorySuffix
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetStorySuffix/ja
    \n指定したストーリのレイヤ名の後記号を返します。'''
    return STRING

def SetLayerElevationN(h, baseElev, thickness):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLayerElevationN'''
    return None

def CopyMode(mode):
    '''https://developer.vectorworks.net/index.php?title=VS:CopyMode
    \nhttps://developer.vectorworks.net/index.php?title=VS:CopyMode/ja
    \nアクティブなレイヤの表示モードを設定します。'''
    return None

def GetLayerLevelType(layer):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLayerLevelType
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLayerLevelType/ja
    \nレイヤのレベルタイプを返します。'''
    return STRING

def GetZVals():
    '''https://developer.vectorworks.net/index.php?title=VS:GetZVals
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetZVals/ja
    \nアクティブなレイヤの高さ（Z）と厚み（ΔZ）を返します。'''
    return (zVal, deltaZVal)

def SetLayerEnableCutPl(layer, enableCutPlane):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLayerEnableCutPl
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLayerEnableCutPl/ja
    \nレイヤの切断面を有効にするかどうか設定します。'''
    return None

def CreateLayer(layerName, layerType):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateLayer
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateLayer/ja
    \n指定した種類のレイヤを作成します。'''
    return HANDLE

def GetLayerOptions():
    '''https://developer.vectorworks.net/index.php?title=VS:GetLayerOptions
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLayerOptions/ja
    \nアクティブなドキュメントの、他のレイヤの表示方法を値で返します。'''
    return INTEGER

def GrayLayer():
    '''https://developer.vectorworks.net/index.php?title=VS:GrayLayer
    \nhttps://developer.vectorworks.net/index.php?title=VS:GrayLayer/ja
    \nアクティブなレイヤをグレイ表示にします。'''
    return None

def SetLayerLevelType(layer, layerLevelType):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLayerLevelType
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLayerLevelType/ja
    \nレイヤのレベルタイプを設定します。もし、タイプが存在しないか、同じストーリの他のレイヤに使用されている場合は失敗します。'''
    return BOOLEAN

def CreateLayerLevelType(name):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateLayerLevelType
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateLayerLevelType/ja
    \nレイヤのレベルタイプを作成します。'''
    return BOOLEAN

def GetLayerRenderMode(theLayer):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLayerRenderMode
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLayerRenderMode/ja
    \nハンドルで指定したレイヤのレンダリングモードを返します。'''
    return INTEGER

def HGetLayerTransp(hLayer):
    '''https://developer.vectorworks.net/index.php?title=VS:HGetLayerTransp
    \nhttps://developer.vectorworks.net/index.php?title=VS:HGetLayerTransp/ja
    \n指定したレイヤの透明度を返します。'''
    return REAL

def SetLayerOptions(layerOpts):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLayerOptions
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLayerOptions/ja
    \n他のレイヤの表示状態を設定します。'''
    return None

def CreateLevelTemplate(layerName, scaleFactor, levelType, elevation, wallHeight):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateLevelTemplate
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateLevelTemplate/ja
    \nアクティブなファイルに新しいストーリレベルテンプレートを作成します。 作成したストーリレベルテンプレートはテンプレート一覧に追加されインデックスが設定されます。 ストーリーレベルにはレベルタイプ、高さ、関連付けるレイヤが含まれています。 ストーリレベルテンプレートは複数のストーリに追加できる一般的なレベルを定義します。'''
    return (BOOLEAN, index)

def GetLayerTransparency():
    '''https://developer.vectorworks.net/index.php?title=VS:GetLayerTransparency
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLayerTransparency/ja
    \n現在のレイヤの透明度を返します。'''
    return REAL

def HSetLayerTransp(hLayer, transparency):
    '''https://developer.vectorworks.net/index.php?title=VS:HSetLayerTransp
    \nhttps://developer.vectorworks.net/index.php?title=VS:HSetLayerTransp/ja
    \n指定したレイヤの透明度を設定します。'''
    return None

def SetLayerRenderMode(theLayer, newRenderMode, immediate, doProgress):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLayerRenderMode
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLayerRenderMode/ja
    \nレイヤのレンダリングモードを設定します。'''
    return None

def CreateLevelTemplateN(layerName, scaleFactor, levelType, elevation, wallHeight):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateLevelTemplateN'''
    return (BOOLEAN, index)

def GetLevelElevation(storyHandle, levelType):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLevelElevation
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLevelElevation/ja
    \nハンドルで指定したストーリ内のストーリレベルタイプの高さを返します。'''
    return REAL

def HideLayer():
    '''https://developer.vectorworks.net/index.php?title=VS:HideLayer
    \nhttps://developer.vectorworks.net/index.php?title=VS:HideLayer/ja
    \nアクティブなレイヤを隠します。'''
    return None

def SetLayerTransparency(transparency):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLayerTransparency
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLayerTransparency/ja
    \nアクティブなデザインレイヤの透明度（％）を設定します。'''
    return None

def CreateStory(name, suffix):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateStory
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateStory/ja
    \nストーリを作成します。'''
    return BOOLEAN

def GetLevelElevationN(storyHandle, levelType):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLevelElevationN'''
    return REAL

def IsLayerReferenced(layer):
    '''https://developer.vectorworks.net/index.php?title=VS:IsLayerReferenced
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsLayerReferenced/ja
    \nハンドルで指定したレイヤがファイル共有で参照されているレイヤの場合は、参照元ドキュメントへのパスを返します。'''
    return (BOOLEAN, pathname)

def SetLevelElevation(storyHandle, levelType, newElevation):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLevelElevation
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLevelElevation/ja
    \n指定したストーリ内のストーリレベルタイプの高さを設定します。'''
    return BOOLEAN

def CreateStoryLayerTemplate(name, scaleFactor, layerLevelType, elevationOffset, defaultWallHeight):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateStoryLayerTemplate
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateStoryLayerTemplate/ja
    \n現在のファイルにストーリレイヤテンプレートを作成します。'''
    return (BOOLEAN, index)

def GetLevelTemplateInfo(index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLevelTemplateInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLevelTemplateInfo/ja
    \n指定したインデックスのストーリレベルテンプレートの詳細を返します。 関連付けるレイヤの名前、レイヤの縮尺、レベルタイプ、ストーリレベルの高さ、および壁の高さのプロパティの設定値を返します。'''
    return (BOOLEAN, layerName, scaleFactor, levelType, elevation, wallHeight)

def LFillBack(color):
    '''https://developer.vectorworks.net/index.php?title=VS:LFillBack
    \nhttps://developer.vectorworks.net/index.php?title=VS:LFillBack/ja
    \nアクティブなレイヤの面の地色を設定します。値の範囲は0から65535までです。'''
    return None

def SetLevelElevationN(storyHandle, levelType, newElevation):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLevelElevationN'''
    return BOOLEAN

def DeleteLevelTemplate(index):
    '''https://developer.vectorworks.net/index.php?title=VS:DeleteLevelTemplate
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeleteLevelTemplate/ja
    \nアクティブなファイルから指定したインデックスのストーリレベルテンプレートを削除します。'''
    return BOOLEAN

def GetLevelTemplateName(index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLevelTemplateName
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLevelTemplateName/ja
    \nアクティブなファイルのストーリレベルテンプレートのリストのうち指定したインデックスの名前を返します。'''
    return STRING

def LFillFore(color):
    '''https://developer.vectorworks.net/index.php?title=VS:LFillFore
    \nhttps://developer.vectorworks.net/index.php?title=VS:LFillFore/ja
    \nアクティブなレイヤの面の色を設定します。値の範囲は0から65535までです。'''
    return None

def SetLevelTemplateName(index, name):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLevelTemplateName
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLevelTemplateName/ja
    \nインデックスで指定したストーリレベルテンプレートの名前を設定します。'''
    return BOOLEAN

def DeleteStoryLayerTemplate(index):
    '''https://developer.vectorworks.net/index.php?title=VS:DeleteStoryLayerTemplate
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeleteStoryLayerTemplate/ja
    \n現在のファイルからn番目のストーリレイヤテンプレートを削除します。'''
    return BOOLEAN

def GetLevelTmpltInfoN(index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLevelTmpltInfoN'''
    return (BOOLEAN, layerName, scaleFactor, levelType, elevation, wallHeight)

def LLayer():
    '''https://developer.vectorworks.net/index.php?title=VS:LLayer
    \nhttps://developer.vectorworks.net/index.php?title=VS:LLayer/ja
    \n最下位のレイヤのハンドルを返します。'''
    return HANDLE

def SetLevelTypeName(index, name):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLevelTypeName
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLevelTypeName/ja
    \n指定したレベルタイプの名前を設定します。'''
    return BOOLEAN

def DisplayLayerScaleDialog():
    '''https://developer.vectorworks.net/index.php?title=VS:DisplayLayerScaleDialog
    \nhttps://developer.vectorworks.net/index.php?title=VS:DisplayLayerScaleDialog/ja
    \n縮尺ダイアログを表示します。'''
    return None

def GetLevelTypeName(index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLevelTypeName
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLevelTypeName/ja
    \n指定したレベルタイプの名前を返します。'''
    return STRING

def LPenBack(color):
    '''https://developer.vectorworks.net/index.php?title=VS:LPenBack
    \nhttps://developer.vectorworks.net/index.php?title=VS:LPenBack/ja
    \nアクティブなレイヤの線の地色を設定します。値の範囲は0から65535までです。'''
    return None

def SetScale(actualSize):
    '''https://developer.vectorworks.net/index.php?title=VS:SetScale
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetScale/ja
    \nアクティブなレイヤの縮尺を設定します。'''
    return None

def FLayer():
    '''https://developer.vectorworks.net/index.php?title=VS:FLayer
    \nhttps://developer.vectorworks.net/index.php?title=VS:FLayer/ja
    \n最上位のレイヤのハンドルを返します。'''
    return HANDLE

def GetNumLayerLevelTypes():
    '''https://developer.vectorworks.net/index.php?title=VS:GetNumLayerLevelTypes
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNumLayerLevelTypes/ja
    \nファイルにあるレベルタイプの数を返します。'''
    return INTEGER

def LPenFore(color):
    '''https://developer.vectorworks.net/index.php?title=VS:LPenFore
    \nhttps://developer.vectorworks.net/index.php?title=VS:LPenFore/ja
    \nアクティブなレイヤの線の色を設定します。値の範囲は0から65535までです。'''
    return None

def SetSheetLayerUserOrigin(layerHandle, xOrigin, yOrigin):
    '''https://developer.vectorworks.net/index.php?title=VS:SetSheetLayerUserOrigin
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetSheetLayerUserOrigin/ja
    \n指定したシートレイヤの原点を設定します。'''
    return BOOLEAN

def GetDrawingArea():
    '''https://developer.vectorworks.net/index.php?title=VS:GetDrawingArea'''
    return (STRING, outDrawingArea, outIsOther, outIsOnePrintedPage)

def GetNumLevelTemplates():
    '''https://developer.vectorworks.net/index.php?title=VS:GetNumLevelTemplates
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNumLevelTemplates/ja
    \nファイル内のストーリレベルテンプレートの数を返します。 ストーリーレベルにはレベルタイプ、高さ、関連付けるレイヤが含まれています。 ストーリレベルテンプレートは複数のストーリに追加できる一般的なレベルを定義します。'''
    return INTEGER

def Layer(name):
    '''https://developer.vectorworks.net/index.php?title=VS:Layer
    \nhttps://developer.vectorworks.net/index.php?title=VS:Layer/ja
    \n新しいレイヤを指定した名前で作成し、そのレイヤをアクティブにします。指定した名前のレイヤがすでに存在する場合、そのレイヤをアクティブにします。'''
    return None

def SetStoryElevation(story, elevation):
    '''https://developer.vectorworks.net/index.php?title=VS:SetStoryElevation
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetStoryElevation/ja
    \n指定したストーリの高さを設定します。ストーリの高さが設定出来たかどうかを返します。変更によってストーリに関連付けられているレイヤが他のストーリに関連付けられているレイヤと重なる場合は設定されません。'''
    return BOOLEAN

def GetLName(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLName
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLName/ja
    \nハンドルで指定したレイヤの名前を返します。'''
    return STRING

def GetNumStories():
    '''https://developer.vectorworks.net/index.php?title=VS:GetNumStories
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNumStories/ja
    \nファイルにあるストーリの数を返します。'''
    return INTEGER

def LayerRef(layerName):
    '''https://developer.vectorworks.net/index.php?title=VS:LayerRef
    \nhttps://developer.vectorworks.net/index.php?title=VS:LayerRef/ja
    \n指定したレイヤとアクティブなレイヤを座標(0,0)でリンクさせます。'''
    return None

def SetStoryElevationN(story, elevation):
    '''https://developer.vectorworks.net/index.php?title=VS:SetStoryElevationN'''
    return BOOLEAN

def GetLScale(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLScale
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLScale/ja
    \nハンドルで指定したレイヤの縮尺を返します。'''
    return REAL

def GetNumStoryLayerTemplates():
    '''https://developer.vectorworks.net/index.php?title=VS:GetNumStoryLayerTemplates
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNumStoryLayerTemplates/ja
    \nファイルにあるストーリレイヤテンプレートの数を返します。'''
    return INTEGER

def NumLayers():
    '''https://developer.vectorworks.net/index.php?title=VS:NumLayers
    \nhttps://developer.vectorworks.net/index.php?title=VS:NumLayers/ja
    \nアクティブなドキュメント内のレイヤの数を返します。'''
    return INTEGER

def SetStorySuffix(story, suffix):
    '''https://developer.vectorworks.net/index.php?title=VS:SetStorySuffix
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetStorySuffix/ja
    \n指定したストーリのレイヤ名の後記号を設定します。後記号が設定出来たかどうかが返ります。後記号が他のストーリに使用されている場合、後記号は変更されません。'''
    return BOOLEAN

def GetLVis(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLVis
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLVis/ja
    \nハンドルで指定したレイヤの表示状態を返します。'''
    return INTEGER

def GetSheetLayerUserOrigin(layerHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetSheetLayerUserOrigin
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSheetLayerUserOrigin/ja
    \n指定したシートレイヤの原点を返します。'''
    return (BOOLEAN, xOrigin, yOrigin)

def NumObj(h):
    '''https://developer.vectorworks.net/index.php?title=VS:NumObj
    \nhttps://developer.vectorworks.net/index.php?title=VS:NumObj/ja
    \nハンドルで指定したレイヤ上の図形の数を返します。'''
    return LONGINT

def SetZVals(zDistance, deltaZDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:SetZVals
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetZVals/ja
    \nアクティブなレイヤの高さ（Z）と厚み（ΔZ）を設定します。'''
    return None

def GetLayer(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLayer
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLayer/ja
    \nハンドルで指定した図形が存在するレイヤのハンドルを返します。'''
    return HANDLE

def GetStoryAbove(story):
    '''https://developer.vectorworks.net/index.php?title=VS:GetStoryAbove
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetStoryAbove/ja
    \n指定したストーリの上のストーリを返します。見つからない場合はNULLを返します。ハンドルがNULLの場合は一番上のストーリを返します'''
    return HANDLE

def RemoveStoryLevel(storyHandle, levelType, bDeleteLayer):
    '''https://developer.vectorworks.net/index.php?title=VS:RemoveStoryLevel
    \nhttps://developer.vectorworks.net/index.php?title=VS:RemoveStoryLevel/ja
    \nストーリから指定したレベルタイプのストーリレベルを削除します。 'bDeleteLayer' をTRUEにすると、関連付けられているレイヤも削除します。'''
    return BOOLEAN

def ShowLayer():
    '''https://developer.vectorworks.net/index.php?title=VS:ShowLayer
    \nhttps://developer.vectorworks.net/index.php?title=VS:ShowLayer/ja
    \nアクティブなレイヤを表示します。'''
    return None

def GetLayerByName(layerName):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLayerByName
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLayerByName/ja
    \n指定した名前をもつレイヤのハンドルを返します。'''
    return HANDLE

def GetStoryBelow(story):
    '''https://developer.vectorworks.net/index.php?title=VS:GetStoryBelow
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetStoryBelow/ja
    \n指定したストーリの下のストーリを返します。見つからない場合はNULLを返します。ハンドルがNULLの場合は一番下のストーリを返します。'''
    return HANDLE

def ResetDefStoryLevels(bDeleteExisting):
    '''https://developer.vectorworks.net/index.php?title=VS:ResetDefStoryLevels
    \nhttps://developer.vectorworks.net/index.php?title=VS:ResetDefStoryLevels/ja
    \nデフォルトのストーリレベルをすべて消去し、ディスク上のXMLデータファイルから再生成します。'''
    return BOOLEAN

def Abs(v):
    '''https://developer.vectorworks.net/index.php?title=VS:Abs
    \nhttps://developer.vectorworks.net/index.php?title=VS:Abs/ja
    \n指定した数値（REAL、LONGINT、INTEGER）の絶対値を返します。'''
    return REAL

def Deg2Rad(degreeValue):
    '''https://developer.vectorworks.net/index.php?title=VS:Deg2Rad
    \nhttps://developer.vectorworks.net/index.php?title=VS:Deg2Rad/ja
    \n指定したデグリー値（度数）をラジアン値に変換して返します。'''
    return REAL

def Rad2Deg(radianValue):
    '''https://developer.vectorworks.net/index.php?title=VS:Rad2Deg
    \nhttps://developer.vectorworks.net/index.php?title=VS:Rad2Deg/ja
    \n指定したラジアン値をデグリー値（度数）に変換して返します。'''
    return REAL

def Sqrt(v):
    '''https://developer.vectorworks.net/index.php?title=VS:Sqrt
    \nhttps://developer.vectorworks.net/index.php?title=VS:Sqrt/ja
    \n指定した数値（REAL、LONGINT、INTEGER）の平方根を返します。'''
    return REAL

def ArcCos(v):
    '''https://developer.vectorworks.net/index.php?title=VS:ArcCos
    \nhttps://developer.vectorworks.net/index.php?title=VS:ArcCos/ja
    \n指定した数値（REAL、LONGINT、INTEGER）のアークコサインの値を返します。'''
    return REAL

def Exp(v):
    '''https://developer.vectorworks.net/index.php?title=VS:Exp
    \nhttps://developer.vectorworks.net/index.php?title=VS:Exp/ja
    \n指定した数値（REAL、LONGINT、INTEGER）の指数を返します。'''
    return REAL

def Random():
    '''https://developer.vectorworks.net/index.php?title=VS:Random
    \nhttps://developer.vectorworks.net/index.php?title=VS:Random/ja
    \n0.0から1.0までの乱数を実数で返します。'''
    return REAL

def Tan(v):
    '''https://developer.vectorworks.net/index.php?title=VS:Tan
    \nhttps://developer.vectorworks.net/index.php?title=VS:Tan/ja
    \n指定した数値（REAL、LONGINT、INTEGER）のタンジェントの値を返します。'''
    return REAL

def ArcSin(v):
    '''https://developer.vectorworks.net/index.php?title=VS:ArcSin
    \nhttps://developer.vectorworks.net/index.php?title=VS:ArcSin/ja
    \n指定した数値（REAL、LONGINT、INTEGER）のアークサインの値を返します。'''
    return REAL

def Ln(v):
    '''https://developer.vectorworks.net/index.php?title=VS:Ln
    \nhttps://developer.vectorworks.net/index.php?title=VS:Ln/ja
    \n指定した数値（REAL、LONGINT、INTEGER）の自然対数を返します。'''
    return REAL

def Round(v):
    '''https://developer.vectorworks.net/index.php?title=VS:Round
    \nhttps://developer.vectorworks.net/index.php?title=VS:Round/ja
    \n指定した実数を四捨五入して、LONGINT型の整数に変換して返します。'''
    return LONGINT

def Trunc(v):
    '''https://developer.vectorworks.net/index.php?title=VS:Trunc
    \nhttps://developer.vectorworks.net/index.php?title=VS:Trunc/ja
    \n指定した実数の小数点以下を切り捨て、LONGINT型の整数に変換して返します。'''
    return LONGINT

def ArcTan(v):
    '''https://developer.vectorworks.net/index.php?title=VS:ArcTan
    \nhttps://developer.vectorworks.net/index.php?title=VS:ArcTan/ja
    \n指定した数値（REAL、LONGINT、INTEGER）のアークタンジェントの値を返します。'''
    return REAL

def Max(val1, val2):
    '''https://developer.vectorworks.net/index.php?title=VS:Max
    \nhttps://developer.vectorworks.net/index.php?title=VS:Max/ja
    \n二つの値の最大値を返します。'''
    return REAL

def Sin(v):
    '''https://developer.vectorworks.net/index.php?title=VS:Sin
    \nhttps://developer.vectorworks.net/index.php?title=VS:Sin/ja
    \n指定した数値（REAL、LONGINT、INTEGER）のサインの値を返します。'''
    return REAL

def Cos(v):
    '''https://developer.vectorworks.net/index.php?title=VS:Cos
    \nhttps://developer.vectorworks.net/index.php?title=VS:Cos/ja
    \n指定した数値（REAL、LONGINT、INTEGER）のコサインの値を返します。'''
    return REAL

def Min(val1, val2):
    '''https://developer.vectorworks.net/index.php?title=VS:Min
    \nhttps://developer.vectorworks.net/index.php?title=VS:Min/ja
    \n二つの値の最小値を返します。'''
    return REAL

def Sqr(v):
    '''https://developer.vectorworks.net/index.php?title=VS:Sqr
    \nhttps://developer.vectorworks.net/index.php?title=VS:Sqr/ja
    \n指定した数値（REAL、LONGINT、INTEGER）の2乗の値を返します。'''
    return REAL

def Ang2Vec(angleR, Length):
    '''https://developer.vectorworks.net/index.php?title=VS:Ang2Vec
    \nhttps://developer.vectorworks.net/index.php?title=VS:Ang2Vec/ja
    \n指定した角度と距離を2次元のベクトルに変換して返します。'''
    return VECTOR

def CrossProduct(v1, v2):
    '''https://developer.vectorworks.net/index.php?title=VS:CrossProduct
    \nhttps://developer.vectorworks.net/index.php?title=VS:CrossProduct/ja
    \n指定した2つのベクトルの外積を返します。'''
    return VECTOR

def Perp(Vec):
    '''https://developer.vectorworks.net/index.php?title=VS:Perp
    \nhttps://developer.vectorworks.net/index.php?title=VS:Perp/ja
    \n指定されたベクトルに垂直なベクトルを返します。返されるベクトルの大きさは指定したベクトルと同じで、それらの内積は0になります。返されるベクトルの角度はVec2Ang(Vec) - 90と等しくなります。'''
    return VECTOR

def AngBVec(v1, v2):
    '''https://developer.vectorworks.net/index.php?title=VS:AngBVec
    \nhttps://developer.vectorworks.net/index.php?title=VS:AngBVec/ja
    \n2つのベクトルがなす角（0〜180度）を返します。'''
    return REAL

def DotProduct(v1, v2):
    '''https://developer.vectorworks.net/index.php?title=VS:DotProduct
    \nhttps://developer.vectorworks.net/index.php?title=VS:DotProduct/ja
    \n指定した2つのベクトルの内積を返します。'''
    return REAL

def UnitVec(Vect):
    '''https://developer.vectorworks.net/index.php?title=VS:UnitVec
    \nhttps://developer.vectorworks.net/index.php?title=VS:UnitVec/ja
    \n指定したベクトルの標準単位ベクトルを返します。'''
    return VECTOR

def Comp(v1, v2):
    '''https://developer.vectorworks.net/index.php?title=VS:Comp
    \nhttps://developer.vectorworks.net/index.php?title=VS:Comp/ja
    \nv3にはv1のv2方向成分、v4にはv1のv2に直角方向の成分を返します。'''
    return (v3, v4)

def Norm(Vec):
    '''https://developer.vectorworks.net/index.php?title=VS:Norm
    \nhttps://developer.vectorworks.net/index.php?title=VS:Norm/ja
    \n指定したベクトルの長さを返します。'''
    return REAL

def Vec2Ang(Vect):
    '''https://developer.vectorworks.net/index.php?title=VS:Vec2Ang
    \nhttps://developer.vectorworks.net/index.php?title=VS:Vec2Ang/ja
    \n指定したベクトルの角度（度数）を返します。Vectが3Dベクトルの場合、VectとX軸の間の角度を返します。Vectが{0,0,0}の場合、-90が返されます。'''
    return REAL

def DBDiagnose():
    '''https://developer.vectorworks.net/index.php?title=VS:DBDiagnose
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBDiagnose/ja
    \nODBCソースの連結テストを行い、アプリケーションフォルダにログファイルを出力します。 連結に成功した場合TRUEを返します。'''
    return BOOLEAN

def DBDocRemoveConn(databaseName):
    '''https://developer.vectorworks.net/index.php?title=VS:DBDocRemoveConn
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBDocRemoveConn/ja
    \n現在のドキュメントからデータベース接続を削除します。'''
    return BOOLEAN

def DBObjSQLSetWrite(hRecord, SQLSentence):
    '''https://developer.vectorworks.net/index.php?title=VS:DBObjSQLSetWrite
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBObjSQLSetWrite/ja
    \nODBCを書くためのオブジェクトのSQL文を設定します。'''
    return BOOLEAN

def DBSetFormatConn(formatName, database, tableName):
    '''https://developer.vectorworks.net/index.php?title=VS:DBSetFormatConn
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBSetFormatConn/ja
    \n指定された形式のためのODBC接続を設定します。'''
    return BOOLEAN

def DBDocAddConn(dsn, userName, password):
    '''https://developer.vectorworks.net/index.php?title=VS:DBDocAddConn
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBDocAddConn/ja
    \n現在のドキュメントにデータベース接続を追加します。'''
    return BOOLEAN

def DBDocSetColKey(databaseName, tableName, columnName, setIsKey):
    '''https://developer.vectorworks.net/index.php?title=VS:DBDocSetColKey
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBDocSetColKey/ja
    \nデータベースのテーブルカラムのキーを取得します。'''
    return BOOLEAN

def DBSQLExecute(database, SQLQuery):
    '''https://developer.vectorworks.net/index.php?title=VS:DBSQLExecute
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBSQLExecute/ja
    \n現在のドキュメントに関連づけられた指定されたデータベースのSQLを実行します。'''
    return (BOOLEAN, outColumnCnt, outResultSetInst)

def DBSetFormatFieldConn(formatName, fieldName, columnName, linkType):
    '''https://developer.vectorworks.net/index.php?title=VS:DBSetFormatFieldConn
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBSetFormatFieldConn/ja
    \n指定された形式フィールドのためのODBC接続を設定します。'''
    return BOOLEAN

def DBDocGetColumns(database, table):
    '''https://developer.vectorworks.net/index.php?title=VS:DBDocGetColumns
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBDocGetColumns/ja
    \n指定されたテーブルデータのコロンで区切られたリストをストリング表示で返します。'''
    return (BOOLEAN, outNames, outTypes, outCanBeKey, outIsKey)

def DBGetFormatConn(formatName):
    '''https://developer.vectorworks.net/index.php?title=VS:DBGetFormatConn
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBGetFormatConn/ja
    \n指定された形式のためのODBC接続を返します。'''
    return (BOOLEAN, outDatabase, outTable)

def DBSQLExecuteDSN(dsn, userName, password, SQLQuery):
    '''https://developer.vectorworks.net/index.php?title=VS:DBSQLExecuteDSN
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBSQLExecuteDSN/ja
    \nODBCマネージャに登録された指定されたDSNのSQLを実行します。'''
    return (BOOLEAN, outColumnCnt, outResultSetInst)

def DBShowDBTableDlg(database, table):
    '''https://developer.vectorworks.net/index.php?title=VS:DBShowDBTableDlg
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBShowDBTableDlg/ja
    \n指定したデータベースのテーブルダイアログを表示します'''
    return BOOLEAN

def DBDocGetConn(databaseName):
    '''https://developer.vectorworks.net/index.php?title=VS:DBDocGetConn
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBDocGetConn/ja
    \nデータベース接続情報を取得します。'''
    return (BOOLEAN, outUserName, outPassword)

def DBGetFormatFieldConn(formatName):
    '''https://developer.vectorworks.net/index.php?title=VS:DBGetFormatFieldConn
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBGetFormatFieldConn/ja
    \n指定された形式フィールドのためのODBC接続を取得します。'''
    return (BOOLEAN, fieldName, columnName, linkType)

def DBSQLExecuteDelete():
    '''https://developer.vectorworks.net/index.php?title=VS:DBSQLExecuteDelete
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBSQLExecuteDelete/ja
    \n「DBSQLExecute」か「DBSQLExecuteDSN」に作成されたresultSetInstanceを削除します。'''
    return resultSetInst

def DBShowManageDBsDlg():
    '''https://developer.vectorworks.net/index.php?title=VS:DBShowManageDBsDlg
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBShowManageDBsDlg/ja
    \nデータベースの管理ダイアログを表示します'''
    return None

def DBDocGetDB():
    '''https://developer.vectorworks.net/index.php?title=VS:DBDocGetDB
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBDocGetDB/ja
    \n指定された書類に関連づけられたデータベースのコロンで区切られたリストをストリング表示で返します。'''
    return (BOOLEAN, outDatabases)

def DBObjSQLGetRead(hRecord):
    '''https://developer.vectorworks.net/index.php?title=VS:DBObjSQLGetRead
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBObjSQLGetRead/ja
    \nODBCを読むためのオブジェクトのSQL文を取得します。'''
    return (BOOLEAN, SQLSentence)

def DBSQLExecuteError():
    '''https://developer.vectorworks.net/index.php?title=VS:DBSQLExecuteError
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBSQLExecuteError/ja
    \nODBC API 関数 で発生したエラーの情報を返します。'''
    return (BOOLEAN, message, state, code, internalDesc)

def DBShowObjConnDlg():
    '''https://developer.vectorworks.net/index.php?title=VS:DBShowObjConnDlg
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBShowObjConnDlg/ja
    \n選択されたオブジェクトのオブジェクト接続ダイアログを表示します'''
    return BOOLEAN

def DBDocGetTables(database):
    '''https://developer.vectorworks.net/index.php?title=VS:DBDocGetTables
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBDocGetTables/ja
    \n指定されたデータベースのコロンで区切られたテーブルのリストをストリング表示で返します。'''
    return (BOOLEAN, outTables)

def DBObjSQLGetWrite(hRecord):
    '''https://developer.vectorworks.net/index.php?title=VS:DBObjSQLGetWrite
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBObjSQLGetWrite/ja
    \nODBCを書くためのオブジェクトのSQL文を取得します。'''
    return (BOOLEAN, SQLSentence)

def DBSQLExecuteGet(resultSetInst, colIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:DBSQLExecuteGet
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBSQLExecuteGet/ja
    \n「DBSQLExecute」か「DBSQLExecuteDSN」に作成されたresultSetInstanceからの情報を検索します。'''
    return (BOOLEAN, outColumnName, outValue)

def DBDocHasConn():
    '''https://developer.vectorworks.net/index.php?title=VS:DBDocHasConn
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBDocHasConn/ja
    \n現在のドキュメントにODBCデータソースの接続があるかどうかをチェックします。'''
    return BOOLEAN

def DBObjSQLSetRead(hRecord, SQLSentence):
    '''https://developer.vectorworks.net/index.php?title=VS:DBObjSQLSetRead
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBObjSQLSetRead/ja
    \nODBCを読むためのオブジェクトのSQL文を設定します。'''
    return BOOLEAN

def DBSQLExecuteNext(resultSetInst):
    '''https://developer.vectorworks.net/index.php?title=VS:DBSQLExecuteNext
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBSQLExecuteNext/ja
    \n現在ポインタを次のエントリーに動かします。'''
    return BOOLEAN

def AddSubMtrlToMtrl(hMaterial, subMtrlName, fraction, makePrimary):
    '''https://developer.vectorworks.net/index.php?title=VS:AddSubMtrlToMtrl'''
    return Boolean

def GetMtlFillBackColor(material):
    '''https://developer.vectorworks.net/index.php?title=VS:GetMtlFillBackColor'''
    return (red, green, blue)

def IsObjectFlipped(h):
    '''https://developer.vectorworks.net/index.php?title=VS:IsObjectFlipped
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsObjectFlipped/ja
    \nハンドルで指定した3次元図形（回転体、柱状体、多段柱状体、シンボル、ソリッド、プラグインオブジェクト）が反転されている場合はTRUEを返します。'''
    return BOOLEAN

def SetMarkerByClass(h):
    '''https://developer.vectorworks.net/index.php?title=VS:SetMarkerByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetMarkerByClass/ja
    \nハンドルで指定した図形のマーカの種類に、現在のクラス属性を使います。'''
    return None

def CountFillSpaces(h):
    '''https://developer.vectorworks.net/index.php?title=VS:CountFillSpaces'''
    return INTEGER

def GetMtlFillForeColor(material):
    '''https://developer.vectorworks.net/index.php?title=VS:GetMtlFillForeColor'''
    return (red, green, blue)

def IsPenColorByClass(h):
    '''https://developer.vectorworks.net/index.php?title=VS:IsPenColorByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsPenColorByClass/ja
    \nハンドルで指定した図形の線の色が、クラス属性を使用していた場合はTRUEを返します。'''
    return BOOLEAN

def SetMaterialFillStyle(materialHandle, fillStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetMaterialFillStyle'''
    return BOOLEAN

def CreateFillSpace(owner):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateFillSpace'''
    return HANDLE

def GetMtlPenBackColor(material):
    '''https://developer.vectorworks.net/index.php?title=VS:GetMtlPenBackColor'''
    return (red, green, blue)

def IsPlanarObj(object):
    '''https://developer.vectorworks.net/index.php?title=VS:IsPlanarObj
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsPlanarObj/ja
    \n図形がプレイナー図形の場合には、trueを返します。'''
    return (BOOLEAN, refID)

def SetMaterialTexture(materialHandle, textureIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:SetMaterialTexture'''
    return (BOOLEAN, materialHandle)

def CreateMaterial(name, isSimpleMaterial):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateMaterial'''
    return HANDLE

def GetMtlPenForeColor(material):
    '''https://developer.vectorworks.net/index.php?title=VS:GetMtlPenForeColor'''
    return (red, green, blue)

def IsTextStyleByClass(objectId):
    '''https://developer.vectorworks.net/index.php?title=VS:IsTextStyleByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsTextStyleByClass/ja
    \n指定した図形がクラスの文字スタイルを使用しているかどうかを返します。'''
    return BOOLEAN

def SetMtlFillBackColor(material, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetMtlFillBackColor'''
    return None

def EnableDropShadow(h, enable):
    '''https://developer.vectorworks.net/index.php?title=VS:EnableDropShadow
    \nhttps://developer.vectorworks.net/index.php?title=VS:EnableDropShadow/ja'''
    return None

def GetObjArrow(obj):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjArrow
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetObjArrow/ja
    \nハンドルで指定した図形のマーカスタイルを返します。'''
    return (style, size, angle, start, end)

def RemoveSubMtrlFromMtl(hMaterial, subMtrlName):
    '''https://developer.vectorworks.net/index.php?title=VS:RemoveSubMtrlFromMtl'''
    return Boolean

def SetMtlFillForeColor(material, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetMtlFillForeColor'''
    return None

def GetClass(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClass/ja
    \nハンドルで指定した図形のクラスの名前を返します。'''
    return STRING

def GetObjBeginningMarker(obj):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjBeginningMarker
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetObjBeginningMarker/ja
    \nハンドルで指定した図形の始点マーカのすべての設定値を返します。正常終了するとTRUEが返されます。'''
    return (BOOLEAN, style, angle, size, width, thicknessBasis, thickness, visibility)

def SetClass(h, class):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClass/ja
    \nハンドルで指定した図形のクラスを変更します。'''
    return None

def SetMtlFillStyleByCls(materialHandle, isByClass):
    '''https://developer.vectorworks.net/index.php?title=VS:SetMtlFillStyleByCls'''
    return BOOLEAN

def GetDescriptionText(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDescriptionText
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDescriptionText/ja
    \n指定した図形に設定された任意の説明文を返します。 説明文字が設定されていない場合、”descriptionText”は空になります。'''
    return descriptionText

def GetObjEndMarker(obj):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjEndMarker
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetObjEndMarker/ja
    \nハンドルで指定した図形の終点マーカのすべての設定値を返します。正常終了するとTRUEが返されます。'''
    return (BOOLEAN, style, angle, size, width, thicknessBasis, thickness, visibility)

def SetClassN(h, class, descIntoGroup):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClassN'''
    return None

def SetMtlPenBackColor(material, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetMtlPenBackColor'''
    return None

def GetDropShadowByCls(H):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDropShadowByCls
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDropShadowByCls/ja'''
    return BOOLEAN

def GetObjMaterialHandle(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjMaterialHandle'''
    return HANDLE

def SetDescriptionText(hObject, descriptionText):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDescriptionText
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDescriptionText/ja
    \n図形にユーザ定義の説明文を設定します。説明文が未設定の場合データノードを追加します。'''
    return BOOLEAN

def SetMtlPenForeColor(material, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetMtlPenForeColor'''
    return None

def GetDropShadowData(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDropShadowData
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDropShadowData/ja'''
    return (BOOLEAN, nUnits, dOffset, dBlurRadius, dAngle, nOpacity, colorRV, colorGV, colorBV)

def GetObjMaterialName(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjMaterialName'''
    return (BOOLEAN, materialName)

def SetDropShadowByCls(h, byClassValue):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDropShadowByCls
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDropShadowByCls/ja'''
    return None

def SetObjArrow(obj, style, size, angle, start, end):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjArrow
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetObjArrow/ja
    \nハンドルで指定した図形にマーカを設定します。'''
    return None

def GetEntityMatrix(objectHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetEntityMatrix
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetEntityMatrix/ja
    \nプレイナー図形の平面マトリックスを取得します。'''
    return (BOOLEAN, offset, rotationXAngle, rotationYAngle, rotationZAngle)

def GetObjTypeProperties(ObjectType):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjTypeProperties'''
    return INTEGER

def SetDropShadowData(h, nUnits, dOffset, dBlurRadius, dAngle, nOpacity, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDropShadowData
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDropShadowData/ja'''
    return None

def SetObjBeginningMarker(obj, style, angle, size, width, thicknessBasis, thickness, visibility):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjBeginningMarker
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetObjBeginningMarker/ja
    \nハンドルで指定した図形の始点マーカのすべての設定値を設定します。正常終了するとTRUEが返されます。'''
    return BOOLEAN

def GetFPat(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetFPat
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetFPat/ja
    \nハンドルで指定した図形の面の模様番号を返します。'''
    return LONGINT

def GetOpacity(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetOpacity
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetOpacity/ja
    \nハンドルで指定した図形の不透明度を返します。'''
    return opacity

def SetEntityMatrix(objectHandle, offset, rotationXAngle, rotationYAngle, rotationZAngle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetEntityMatrix
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetEntityMatrix/ja
    \nプレイナー図形の平面マトリックスを設定します。すでに同じマトリックスを持つ平面が書類中にあれば、オブジェクトはその平面に設定されます。'''
    return BOOLEAN

def SetObjEndMarker(obj, style, angle, size, width, thicknessBasis, thickness, visibility):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjEndMarker
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetObjEndMarker/ja
    \nハンドルで指定した図形の終点マーカのすべての設定値を設定します。正常終了するとTRUEが返されます。'''
    return BOOLEAN

def GetFillBack(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetFillBack
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetFillBack/ja
    \nハンドルで指定した図形の面の地色の成分を返します。値の範囲は0から65535までです。'''
    return (red, green, blue)

def GetOpacityByClass(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetOpacityByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetOpacityByClass/ja
    \nハンドルで指定した図形がクラスの不透明度を使用しているかどうかを返します。'''
    return isByClass

def SetEntityMatrixN(objectHandle, u, v, w, offset):
    '''https://developer.vectorworks.net/index.php?title=VS:SetEntityMatrixN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetEntityMatrixN/ja
    \nプレイナー図形の平面マトリックスを設定します。すでに同じマトリックスを持つ平面が書類中にあれば、オブジェクトはその平面に設定されます。'''
    return BOOLEAN

def SetObjMaterialHandle(objectHandle, materialHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjMaterialHandle'''
    return (BOOLEAN, objectHandle)

def GetFillFore(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetFillFore
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetFillFore/ja
    \nハンドルで指定した図形の面の色成分を返します。値の範囲は0から65535までです。'''
    return (red, green, blue)

def GetOpacityByClassN(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetOpacityByClassN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetOpacityByClassN/ja'''
    return (isPenOpacityByClass, isFillOpacityByClass)

def SetFPat(h, fillPattern):
    '''https://developer.vectorworks.net/index.php?title=VS:SetFPat
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetFPat/ja
    \nハンドルで指定した図形の面の模様を、指定した模様番号に変更します。'''
    return None

def SetOpacity(h, opacity):
    '''https://developer.vectorworks.net/index.php?title=VS:SetOpacity
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetOpacity/ja
    \nハンドルで指定した図形の不透明度を設定します。'''
    return None

def GetFillIAxisEndPoint(objectHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetFillIAxisEndPoint
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetFillIAxisEndPoint/ja
    \nI軸の終点座標を返します。'''
    return (xIAxisEndPoint, yIAxisEndPoint)

def GetOpacityN(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetOpacityN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetOpacityN/ja'''
    return (Boolean, outPenOpacity, outFillOpacity)

def SetFPatByClass(h):
    '''https://developer.vectorworks.net/index.php?title=VS:SetFPatByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetFPatByClass/ja
    \nハンドルで指定した図形の面の模様に、現在のクラス属性を使います。'''
    return None

def SetOpacityByClass(h):
    '''https://developer.vectorworks.net/index.php?title=VS:SetOpacityByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetOpacityByClass/ja
    \nハンドルで指定した図形の不透明度に、現在のクラス属性を使います。'''
    return None

def GetFillJAxisEndPoint(objectHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetFillJAxisEndPoint
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetFillJAxisEndPoint/ja
    \nJ軸の終点座標を返します。'''
    return (xJAxisEndPoint, yJAxisEndPoint)

def GetPenBack(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPenBack
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPenBack/ja
    \nハンドルで指定した図形の線の地色の成分を返します。値の範囲は0から65535までです。'''
    return (red, green, blue)

def SetFillBack(h, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetFillBack
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetFillBack/ja
    \nハンドルで指定した図形の面の地色を、指定した色に変更します。値の範囲は0から65535までです。'''
    return None

def SetOpacityByClassN(h, inIsPenOpacityByClass, inIsFillOpacityByClass):
    '''https://developer.vectorworks.net/index.php?title=VS:SetOpacityByClassN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetOpacityByClassN/ja'''
    return None

def GetFillOriginPoint(objectHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetFillOriginPoint
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetFillOriginPoint/ja
    \n原点座標を返します。'''
    return (xOriginPoint, yOriginPoint)

def GetPenFore(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPenFore
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPenFore/ja
    \nハンドルで指定した図形の線の色成分を返します。値の範囲は0から65535までです。'''
    return (red, green, blue)

def SetFillColorByClass(h):
    '''https://developer.vectorworks.net/index.php?title=VS:SetFillColorByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetFillColorByClass/ja
    \nハンドルで指定した図形の面の色に、現在のクラス属性を使います。'''
    return None

def SetOpacityN(h, inPenOpacity, inFillOpacity):
    '''https://developer.vectorworks.net/index.php?title=VS:SetOpacityN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetOpacityN/ja'''
    return BOOLEAN

def GetFillPoints(objectHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetFillPoints
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetFillPoints/ja
    \n原点やI、J軸の終点座標を返します。'''
    return (xOriginPoint, yOriginPoint, xIAxisEndPoint, yIAxisEndPoint, xJAxisEndPoint, yJAxisEndPoint)

def GetViewMatrix(objectHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetViewMatrix
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetViewMatrix/ja
    \nレイヤやビューポートの見る方向を返します。'''
    return (BOOLEAN, offset, rotationXAng, rotationYAng, rotationZAng)

def SetFillFore(h, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetFillFore
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetFillFore/ja
    \nハンドルで指定した図形の面の色を、指定した色に変更します。値の範囲は0から65535までです。'''
    return None

def SetPenBack(h, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetPenBack
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetPenBack/ja
    \nハンドルで指定した図形の線の地色を、指定した色に変更します。値の範囲は0から65535までです。'''
    return None

def GetFillSpace(h, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetFillSpace'''
    return HANDLE

def HideSelectedObjects():
    '''https://developer.vectorworks.net/index.php?title=VS:HideSelectedObjects'''
    return None

def SetFillIAxisEndPoint(objectHandle, xIAxisEndPoint, yIAxisEndPoint):
    '''https://developer.vectorworks.net/index.php?title=VS:SetFillIAxisEndPoint
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetFillIAxisEndPoint/ja
    \nI軸の終点座標を設定します。'''
    return None

def SetPenColorByClass(h):
    '''https://developer.vectorworks.net/index.php?title=VS:SetPenColorByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetPenColorByClass/ja
    \nハンドルで指定した図形の線の色に、現在のクラス属性を使います。'''
    return None

def GetLS(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLS
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLS/ja
    \nハンドルで指定した図形の線の種類を返します。'''
    return INTEGER

def IsDropShadowEnabled(h):
    '''https://developer.vectorworks.net/index.php?title=VS:IsDropShadowEnabled
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsDropShadowEnabled/ja'''
    return BOOLEAN

def SetFillJAxisEndPoint(objectHandle, xJAxisEndPoint, yJAxisEndPoint):
    '''https://developer.vectorworks.net/index.php?title=VS:SetFillJAxisEndPoint
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetFillJAxisEndPoint/ja
    \nJ軸の終点座標を設定します。'''
    return None

def SetPenFore(h, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetPenFore
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetPenFore/ja
    \nハンドルで指定した図形の線の色を、指定した色に変更します。値の範囲は0から65535までです。'''
    return None

def GetLSN(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLSN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLSN/ja
    \nハンドルで指定した図形の線の種類を返します。'''
    return LONGINT

def IsFPatByClass(h):
    '''https://developer.vectorworks.net/index.php?title=VS:IsFPatByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsFPatByClass/ja
    \nハンドルで指定した図形の面の模様が、クラス属性を使用していた場合はTRUEを返します。'''
    return BOOLEAN

def SetFillOriginPoint(objectHandle, xOriginPoint, yOriginPoint):
    '''https://developer.vectorworks.net/index.php?title=VS:SetFillOriginPoint
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetFillOriginPoint/ja
    \n原点座標を設定します。'''
    return None

def SetTextStyleByClass(objectId):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextStyleByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextStyleByClass/ja
    \n指定した図形がクラスの文字スタイルを使用するように設定します。 設定を取り消すには、 SetTextStyleRef を使用します。'''
    return None

def GetLW(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLW
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLW/ja
    \nハンドルで指定した図形の線の太さを返します。'''
    return INTEGER

def IsFillColorByClass(h):
    '''https://developer.vectorworks.net/index.php?title=VS:IsFillColorByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsFillColorByClass/ja
    \nハンドルで指定した図形の面の色が、クラス属性を使用していた場合はTRUEを返します。'''
    return BOOLEAN

def SetLS(h, ls):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLS
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLS/ja
    \nハンドルで指定した図形の線の模様／種類を変更します。'''
    return None

def SetViewMatrix(objectHandle, offset, rotationXAng, rotationYAng, rotationZAng):
    '''https://developer.vectorworks.net/index.php?title=VS:SetViewMatrix
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetViewMatrix/ja
    \nレイヤやビューポートの見る方向を設定します。'''
    return BOOLEAN

def GetMarker(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetMarker
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetMarker/ja
    \nハンドルで指定した図形のマーカ情報を返します。'''
    return (start, end, style, size)

def IsLSByClass(h):
    '''https://developer.vectorworks.net/index.php?title=VS:IsLSByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsLSByClass/ja
    \nハンドルで指定した図形の線の種類が、クラス属性を使用していた場合はTRUEを返します。'''
    return BOOLEAN

def SetLSByClass(h):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLSByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLSByClass/ja
    \nハンドルで指定した図形の線の種類に、現在のクラス属性を使います。'''
    return None

def ShowOnlySelected():
    '''https://developer.vectorworks.net/index.php?title=VS:ShowOnlySelected'''
    return None

def GetMaterialArea(h, material):
    '''https://developer.vectorworks.net/index.php?title=VS:GetMaterialArea'''
    return REAL

def IsLWByClass(h):
    '''https://developer.vectorworks.net/index.php?title=VS:IsLWByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsLWByClass/ja
    \nハンドルで指定した図形の線の太さが、クラス属性を使用していた場合はTRUEを返します。'''
    return BOOLEAN

def SetLSN(h, ls):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLSN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLSN/ja
    \nハンドルで指定した図形の線の模様／種類を、0から71の値または負の値で設定します。'''
    return None

def UnHideObjects():
    '''https://developer.vectorworks.net/index.php?title=VS:UnHideObjects'''
    return None

def GetMaterialFillStyle(materialHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetMaterialFillStyle'''
    return LONGINT

def IsMarkerByClass(h):
    '''https://developer.vectorworks.net/index.php?title=VS:IsMarkerByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsMarkerByClass/ja
    \nハンドルで指定した図形のマーカの種類が、クラス属性を使用していた場合はTRUEを返します。'''
    return BOOLEAN

def SetLW(h, lw):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLW
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLW/ja
    \nハンドルで指定した図形の線の太さを変更します。'''
    return None

def UpdateSubMtrlInMtrl(hMaterial, subMtrlName, fraction, makePrimary):
    '''https://developer.vectorworks.net/index.php?title=VS:UpdateSubMtrlInMtrl'''
    return Boolean

def GetMaterialTexture(objectHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetMaterialTexture'''
    return LONGINT

def IsMaterialSimple(materialHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:IsMaterialSimple'''
    return BOOLEAN

def SetLWByClass(h):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLWByClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLWByClass/ja
    \nハンドルで指定した図形の線の太さに、現在のクラス属性を使います。'''
    return None

def UpdateThumbnailPreview(resourceHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:UpdateThumbnailPreview
    \nhttps://developer.vectorworks.net/index.php?title=VS:UpdateThumbnailPreview/ja
    \nVectorWorksのリソース（ハッチング、テクスチャ、シンボル、プラグインオブジェクトなど）のサムネイルプレビューを作成、または更新します。'''
    return BOOLEAN

def GetMaterialVolume(h, material):
    '''https://developer.vectorworks.net/index.php?title=VS:GetMaterialVolume'''
    return REAL

def IsMtrlFillStyleByCls(materialHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:IsMtrlFillStyleByCls'''
    return BOOLEAN

def SetMarker(h, start, end, style, size):
    '''https://developer.vectorworks.net/index.php?title=VS:SetMarker
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetMarker/ja
    \nハンドルで指定した図形にマーカを設定します。'''
    return None

def BeginMultipleDuplicate():
    '''https://developer.vectorworks.net/index.php?title=VS:BeginMultipleDuplicate
    \nhttps://developer.vectorworks.net/index.php?title=VS:BeginMultipleDuplicate/ja
    \nこの手続きを EndMultipleDuplicate と共に使用して、複製された図形の拘束を保持します。'''
    return None

def EditObjectSpecial(h, editMode):
    '''https://developer.vectorworks.net/index.php?title=VS:EditObjectSpecial
    \nhttps://developer.vectorworks.net/index.php?title=VS:EditObjectSpecial/ja
    \n指定した図形を編集します。'''
    return None

def HMoveForward(h, toFront):
    '''https://developer.vectorworks.net/index.php?title=VS:HMoveForward
    \nhttps://developer.vectorworks.net/index.php?title=VS:HMoveForward/ja
    \nハンドルで指定した図形を、前後関係の前へ移動します。'''
    return None

def Move3DObj(h, xDistance, yDistance, zDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:Move3DObj
    \nhttps://developer.vectorworks.net/index.php?title=VS:Move3DObj/ja
    \nハンドルで指定した3次元図形を、相対的な量で移動します。'''
    return None

def CreateDuplicateObjN(objectToDuplicate, containerHandle, maintainHeightRelativeToLayer):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateDuplicateObjN'''
    return HANDLE

def EndMultipleDuplicate():
    '''https://developer.vectorworks.net/index.php?title=VS:EndMultipleDuplicate
    \nhttps://developer.vectorworks.net/index.php?title=VS:EndMultipleDuplicate/ja
    \nこの手続きを BeginMultipleDuplicate と共に使用して、複製された図形の拘束を保持します。'''
    return None

def HRotate(h, center, rotationAngle):
    '''https://developer.vectorworks.net/index.php?title=VS:HRotate
    \nhttps://developer.vectorworks.net/index.php?title=VS:HRotate/ja
    \nハンドルで指定した図形を、指定した座標を基点として回転させます。'''
    return None

def MoveObjs(move, allLayers, allObjects):
    '''https://developer.vectorworks.net/index.php?title=VS:MoveObjs
    \nhttps://developer.vectorworks.net/index.php?title=VS:MoveObjs/ja
    \n選択されている図形を、相対的な量で移動します。'''
    return None

def CreateDuplicateObject(objectToDuplicate, containerHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateDuplicateObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateDuplicateObject/ja
    \nハンドルで指定した図形を複製し、新しく作成された図形をハンドルで指定したコンテナに挿入します。コンテナのハンドルがNILならば、新しく作成された図形をアクティブなコンテナに挿入します。'''
    return HANDLE

def GetAssociation(handle, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetAssociation'''
    return (HANDLE, associationkind, value)

def HScale2D(h, centerX, centerY, scaleX, scaleY, scaleText):
    '''https://developer.vectorworks.net/index.php?title=VS:HScale2D
    \nhttps://developer.vectorworks.net/index.php?title=VS:HScale2D/ja
    \n2Dオブジェクトのスケール（倍率）を変更します。'''
    return None

def OffsetHandle(h, offsetDistance, EdgeRestoration, FilletSharpEdges):
    '''https://developer.vectorworks.net/index.php?title=VS:OffsetHandle
    \nhttps://developer.vectorworks.net/index.php?title=VS:OffsetHandle/ja
    \n与えられた多角形の重み付き中心軸を一群の線として生成します。'''
    return HANDLE

def DelObject(h):
    '''https://developer.vectorworks.net/index.php?title=VS:DelObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:DelObject/ja
    \nハンドルで指定した図形、レイヤ、ワークシートを削除します。'''
    return None

def GetNumAssociations(handle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetNumAssociations'''
    return INTEGER

def HScale3D(h, centerX, centerY, centerZ, scaleX, scaleY, scaleZ):
    '''https://developer.vectorworks.net/index.php?title=VS:HScale3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:HScale3D/ja
    \n3Dオブジェクトのスケール（倍率）を変更します。'''
    return None

def ResetBBox(h):
    '''https://developer.vectorworks.net/index.php?title=VS:ResetBBox
    \nhttps://developer.vectorworks.net/index.php?title=VS:ResetBBox/ja
    \nハンドルで指定した図形の領域を再計算します。'''
    return None

def DeleteObjs():
    '''https://developer.vectorworks.net/index.php?title=VS:DeleteObjs
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeleteObjs/ja
    \nアクティブなレイヤ上の選択された図形を削除します。'''
    return None

def HDuplicate(objectHandle, x, y):
    '''https://developer.vectorworks.net/index.php?title=VS:HDuplicate
    \nhttps://developer.vectorworks.net/index.php?title=VS:HDuplicate/ja
    \nハンドルで指定した図形を複製し、指定した距離で動かします。'''
    return HANDLE

def Mirror(h, dup, p1, p2):
    '''https://developer.vectorworks.net/index.php?title=VS:Mirror
    \nhttps://developer.vectorworks.net/index.php?title=VS:Mirror/ja
    \n境界線を境に図形を反転します。'''
    return HANDLE

def SetBBox(h, p1, p2):
    '''https://developer.vectorworks.net/index.php?title=VS:SetBBox
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetBBox/ja
    \nハンドルで指定した図形の領域を、指定した座標で設定します。'''
    return None

def DeleteSymbolDefinition(hSymDef, bCompletely):
    '''https://developer.vectorworks.net/index.php?title=VS:DeleteSymbolDefinition
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeleteSymbolDefinition/ja
    \nドキュメントから参照中のシンボル定義を削除します。'''
    return None

def HMove(h, xOffset, yOffset):
    '''https://developer.vectorworks.net/index.php?title=VS:HMove
    \nhttps://developer.vectorworks.net/index.php?title=VS:HMove/ja
    \nハンドルで指定した図形を移動します。'''
    return None

def MirrorN(h, dup, p1, p2, preserveMatrix):
    '''https://developer.vectorworks.net/index.php?title=VS:MirrorN'''
    return HANDLE

def SetHDef(oldH, newH):
    '''https://developer.vectorworks.net/index.php?title=VS:SetHDef
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetHDef/ja
    \nワークシートやシンボル、リンクされたレイヤで参照されている図形を置き換えます。'''
    return None

def Duplicate(offset):
    '''https://developer.vectorworks.net/index.php?title=VS:Duplicate
    \nhttps://developer.vectorworks.net/index.php?title=VS:Duplicate/ja
    \n選択されている図形を複製し、指定した位置に移動させます。他のレイヤが「表示+スナップ+編集」の場合、他のレイヤ上の選択されている図形も複製されます。'''
    return None

def HMoveBackward(h, toBack):
    '''https://developer.vectorworks.net/index.php?title=VS:HMoveBackward
    \nhttps://developer.vectorworks.net/index.php?title=VS:HMoveBackward/ja
    \nハンドルで指定した図形を、前後関係の後ろへ移動します。'''
    return None

def Move3D(xDistance, yDistance, zDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:Move3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:Move3D/ja
    \n直前に作成された3次元図形を、相対的な量で移動します。'''
    return None

def SetRRDiam(h, xDiam, yDiam):
    '''https://developer.vectorworks.net/index.php?title=VS:SetRRDiam
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetRRDiam/ja
    \n隅の丸い四角形の隅のアール半径を設定します。'''
    return None

def AddAssociation(ioOwnerObj, inKind, ioTargetObj):
    '''https://developer.vectorworks.net/index.php?title=VS:AddAssociation
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddAssociation/ja'''
    return BOOLEAN

def vsoContextM_Add(locName, itemID, helpID):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoContextM_Add
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoContextM_Add/ja
    \nkObjOnContextMenuInitイベントでオブジェクトのコンテキストメニューに項目を追加します。'''
    return None

def vsoPrmName2WidgetID(recName, paramName):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoPrmName2WidgetID
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoPrmName2WidgetID/ja'''
    return (BOOLEAN, outWidgetID)

def vsoWidgetGetEnable(widgetID):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoWidgetGetEnable
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoWidgetGetEnable/ja'''
    return BOOLEAN

def GetEvent():
    '''https://developer.vectorworks.net/index.php?title=VS:GetEvent
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetEvent/ja'''
    return LONGINT

def vsoContextM_AddN(locName, itemID, helpID, helpStr):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoContextM_AddN
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoContextM_AddN/ja
    \nObjectContextMenuEvent::kAction_Initイベントでオブジェクトのコンテキストメニューに項目を追加します。'''
    return None

def vsoSetClosureGap(leftGapValue, rightGapValue, topGapValue, bottomGapValue):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoSetClosureGap'''
    return None

def vsoWidgetGetRecParam(widgetID):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoWidgetGetRecParam
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoWidgetGetRecParam/ja'''
    return STRING

def GetXPropVersion():
    '''https://developer.vectorworks.net/index.php?title=VS:GetXPropVersion
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetXPropVersion/ja'''
    return outVersion

def vsoContextM_AddSep(itemID):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoContextM_AddSep
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoContextM_AddSep/ja
    \nkObjOnContextMenuInitイベントでオブジェクトのコンテキストメニューに仕切り線を追加します'''
    return None

def vsoSetEventResult(inEventResult):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoSetEventResult
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoSetEventResult/ja'''
    return None

def vsoWidgetGetText(widgetID):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoWidgetGetText
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoWidgetGetText/ja'''
    return STRING

def RemoveAssociation(ioOwnerObj, inKind, ioTargetObj):
    '''https://developer.vectorworks.net/index.php?title=VS:RemoveAssociation
    \nhttps://developer.vectorworks.net/index.php?title=VS:RemoveAssociation/ja'''
    return BOOLEAN

def vsoContextM_Check(itemID, check):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoContextM_Check
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoContextM_Check/ja
    \nkObjOnContextMenuInitイベントでオブジェクトのコンテキストメニューの項目を確認します。'''
    return None

def vsoSetGlazingArea(GlazingArea):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoSetGlazingArea'''
    return None

def vsoWidgetGetVisible(widgetID):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoWidgetGetVisible
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoWidgetGetVisible/ja'''
    return BOOLEAN

def SetCntrlPtVis(inCustomObj, inContrlPtIndex, inIsVisible):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCntrlPtVis
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCntrlPtVis/ja'''
    return None

def vsoContextM_Enable(itemID, enable):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoContextM_Enable
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoContextM_Enable/ja
    \nkObjOnContextMenuInitイベントでオブジェクトのコンテキストメニューの項目を有効にします。'''
    return None

def vsoSetInCurtainWall(inCurtainWall):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoSetInCurtainWall
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoSetInCurtainWall/ja
    \nイベント52でオブジェクトがカーテンウォールオブジェクトかどうかの情報を取得します。'''
    return None

def vsoWidgetPopupAdd(widgetID, id, text):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoWidgetPopupAdd
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoWidgetPopupAdd/ja'''
    return None

def SetObjPropCharVS(PropertyID, PropertyVal):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjPropCharVS
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetObjPropCharVS/ja'''
    return BOOLEAN

def vsoContextM_GetItem():
    '''https://developer.vectorworks.net/index.php?title=VS:vsoContextM_GetItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoContextM_GetItem/ja
    \nkObjOnContextMenuEventイベントで、オブジェクトのコンテキストメニューで選択された項目を取得します。'''
    return INTEGER

def vsoSetIntSizeInfo(message, isz_index):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoSetIntSizeInfo'''
    return (newValue, isSupported)

def vsoWidgetPopupAddN(widgetID, isStaticChoice, id, text, toolTip, iconSpec):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoWidgetPopupAddN'''
    return None

def SetObjPropDoubleVS(PropertyID, PropertyVal):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjPropDoubleVS
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetObjPropDoubleVS/ja'''
    return BOOLEAN

def vsoDisableAttrs(attrsBits):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoDisableAttrs'''
    return None

def vsoSetObjToolName(eventData, toolName):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoSetObjToolName
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoSetObjToolName/ja
    \n類似オブジェクト作成のために、ツール名を設定します。kObjOnGetToolNameイベント内で使用します。'''
    return None

def vsoWidgetPopupClear(widgetID):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoWidgetPopupClear
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoWidgetPopupClear/ja'''
    return None

def SetObjPropTxtVS(PropertyID, PropertyVal):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjPropTxtVS
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetObjPropTxtVS/ja
    \n拡張プロパティにテキスト型の値を設定します。'''
    return BOOLEAN

def vsoEIDataGetContext(message):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoEIDataGetContext'''
    return INTEGER

def vsoSetQTOValue(valueType, int, real, string):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoSetQTOValue'''
    return None

def vsoWidgetPopupClearN(widgetID, staticChoices):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoWidgetPopupClearN'''
    return None

def SetObjPropVS(PropertyID, PropertyVal):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjPropVS
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetObjPropVS/ja'''
    return BOOLEAN

def vsoEquipItemDataGet(message, dataIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoEquipItemDataGet'''
    return (BOOLEAN, outValue)

def vsoSetSubtractPanels(inSubtractPanels):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoSetSubtractPanels
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoSetSubtractPanels/ja
    \nイベント58でカーテンウォールオブジェクトの中のパネルがフレームからインセットしているかどうかを返します。'''
    return None

def vsoWidgetPopupEnergy(widgetID, dataType):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoWidgetPopupEnergy
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoWidgetPopupEnergy/ja
    \nデータパレットにエネルギー解析データのウィジェットを連結します。VS:Energos Thirdparty Support のページを参照してください。'''
    return None

def vsoADPAddDimDef(message, startPt3, endPt3, dimOffset):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoADPAddDimDef'''
    return None

def vsoEquipItemDataSet(message, dataIndex, dataValue):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoEquipItemDataSet'''
    return None

def vsoStateAddCurrent(hObj, message):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoStateAddCurrent
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoStateAddCurrent/ja'''
    return LONGINT

def vsoWidgetPopupGet(widgetID, index):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoWidgetPopupGet
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoWidgetPopupGet/ja'''
    return (outId, outText)

def vsoADPAddDimPlace(message, dimType):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoADPAddDimPlace'''
    return None

def vsoGetCWInfo():
    '''https://developer.vectorworks.net/index.php?title=VS:vsoGetCWInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoGetCWInfo/ja
    \nカーテンウォール編集ツールでオブジェクトを配置するパネルの情報のうち、配置する長方形の中心点の位置と幅および高さを返します。'''
    return (width, height, centerX, centerY, index)

def vsoStateClear(hObj):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoStateClear
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoStateClear/ja'''
    return None

def vsoWidgetPopupGetCnt(widgetID):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoWidgetPopupGetCnt
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoWidgetPopupGetCnt/ja'''
    return LONGINT

def vsoADPBeginDimType(message, universalName, localizedName):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoADPBeginDimType'''
    return None

def vsoGetCatalogPath(folderSpec, relativePath):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoGetCatalogPath'''
    return None

def vsoStateGet(hObj, state):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoStateGet
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoStateGet/ja'''
    return BOOLEAN

def vsoWidgetPopupGetID(widgetID, text):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoWidgetPopupGetID'''
    return STRING

def vsoADPGetDimDefParms(message):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoADPGetDimDefParms'''
    return (viewType, universalName, dimType)

def vsoGetEventInfo():
    '''https://developer.vectorworks.net/index.php?title=VS:vsoGetEventInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoGetEventInfo/ja
    \nオブジェクトイベントに関する、コンプリートなメッセージ情報を取得します。'''
    return (outObjEvent, outEventData)

def vsoStateGetExitGroup(hObj):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoStateGetExitGroup
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoStateGetExitGroup/ja'''
    return (BOOLEAN, outGrpType)

def vsoWidgetPopupGetTxt(widgetID, id):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoWidgetPopupGetTxt'''
    return STRING

def vsoADPGetUniTypeName(message):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoADPGetUniTypeName'''
    return universalName

def vsoGetIntSizeInfo(message, isz_index, displayName, currentValue, defaultValue, readOnly, isSupported):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoGetIntSizeInfo'''
    return None

def vsoStateGetLayrChng(hObj):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoStateGetLayrChng
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoStateGetLayrChng/ja'''
    return (BOOLEAN, outOldScale, outNewScale, outScaleText)

def vsoWidgetPopupSet(widgetID, index, id, text):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoWidgetPopupSet
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoWidgetPopupSet/ja'''
    return None

def vsoADPGetViewType(message):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoADPGetViewType'''
    return viewType

def vsoGetPluginStyleSym():
    '''https://developer.vectorworks.net/index.php?title=VS:vsoGetPluginStyleSym
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoGetPluginStyleSym/ja
    \nオブジェクトにプラグインスタイルを適用可能とするために使用します。'''
    return hSymDef

def vsoStateGetNameChng(hObj):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoStateGetNameChng
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoStateGetNameChng/ja'''
    return (BOOLEAN, outOldName, outNewName)

def vsoWidgetSetBound(widgetID_Popup, widgetID_Offset, boundID, isTop, offsetLegPrm):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoWidgetSetBound
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoWidgetSetBound/ja'''
    return None

def vsoADPSetCatName(message, universalName, localizedName):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoADPSetCatName'''
    return None

def vsoGetQTOFunction(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoGetQTOFunction'''
    return (functionIndex, option)

def vsoStateGetObjChng(hObj):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoStateGetObjChng
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoStateGetObjChng/ja'''
    return (BOOLEAN, outChangeID)

def vsoWidgetSetEnable(widgetID, enabled):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoWidgetSetEnable
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoWidgetSetEnable/ja'''
    return None

def vsoADPSetLocTypeName(message, localizedName):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoADPSetLocTypeName'''
    return None

def vsoGetUseLyrCutPlane(usingLyrCutPLane):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoGetUseLyrCutPlane
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoGetUseLyrCutPlane/ja
    \nオブジェクトがレイヤの切断面と連動するかどうかを指定します。'''
    return None

def vsoStateGetParamChng(hObj):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoStateGetParamChng
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoStateGetParamChng/ja'''
    return (BOOLEAN, outWidgID, outPrmIdx, outOldVal)

def vsoWidgetSetIndLvl(widgetID, indentLevel):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoWidgetSetIndLvl
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoWidgetSetIndLvl/ja'''
    return None

def vsoAddParamWidget(widgetID, paramName, locName):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoAddParamWidget
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoAddParamWidget/ja
    \nオブジェクト情報パレットに表示するパラメータの、ウィジェットを追加します。'''
    return BOOLEAN

def vsoInsertAllParams():
    '''https://developer.vectorworks.net/index.php?title=VS:vsoInsertAllParams
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoInsertAllParams/ja
    \nプラグインオブジェクトの全てのパラメータを、オブジェクト情報パレットに表示するウィジェットとして、挿入します。'''
    return BOOLEAN

def vsoStateGetPos(hObj):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoStateGetPos
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoStateGetPos/ja'''
    return (BOOLEAN, outX, outY, outZ, outIs3D)

def vsoWidgetSetText(widgetID, text):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoWidgetSetText
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoWidgetSetText/ja'''
    return None

def vsoAddWidget(widgetID, widgetType, locName):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoAddWidget
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoAddWidget/ja
    \nデータパレットに、指定した種類とローカライズ名のウィジェットを追加します。'''
    return BOOLEAN

def vsoInsertParamWidget(position, parameterID, text, data):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoInsertParamWidget
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoInsertParamWidget/ja
    \nオブジェクト情報パレットに表示するウィジェットを設定します。'''
    return BOOLEAN

def vsoStateGetRot(hObj):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoStateGetRot
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoStateGetRot/ja'''
    return (BOOLEAN, outDiffAng, outIs3D)

def vsoWidgetSetType(widgetID, widgetType):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoWidgetSetType'''
    return None

def vsoAppendParamWidget(parameterID, text, data):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoAppendParamWidget
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoAppendParamWidget/ja
    \nオブジェクト情報パレットの、最後に表示するウィジェットを設定します。'''
    return BOOLEAN

def vsoInsertWidget(paramID, widgetType, mappingID, text, data):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoInsertWidget
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoInsertWidget/ja
    \nオブジェクト情報パレットに表示するウィジェットを設定します。'''
    return BOOLEAN

def vsoStateGetRotN(hObj):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoStateGetRotN'''
    return (BOOLEAN, outDiffAng, outIs3D)

def vsoWidgetSetVisible(widgetID, visible):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoWidgetSetVisible
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoWidgetSetVisible/ja'''
    return None

def vsoAppendWidget(widgetType, mappingID, text, data):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoAppendWidget
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoAppendWidget/ja
    \nオブジェクト情報パレットの、最後に表示するウィジェットを設定します。'''
    return BOOLEAN

def vsoPFCGetContext(message):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoPFCGetContext'''
    return (context, viewType, bgRenderMode, fgRenderMode)

def vsoStateMaterialChng(hObj):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoStateMaterialChng'''
    return (BOOLEAN, materialID, deleted, previousTexture)

def vsoButtonGetResource(paramName, objectType, folderSpec, folderName):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoButtonGetResource'''
    return BOOLEAN

def vsoPFCSetChanged(message, didChange):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoPFCSetChanged'''
    return None

def vsoStyleWidgetChoice():
    '''https://developer.vectorworks.net/index.php?title=VS:vsoStyleWidgetChoice
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoStyleWidgetChoice/ja
    \n選択されているプラグインスタイルウィジェットの項目を取得します。'''
    return choice

def vsoCanEditParam(canEditParam):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoCanEditParam
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoCanEditParam/ja
    \nパラメータをワークシートから編集できるようにするかどうか指定します。'''
    return None

def vsoParamName2Index(formatName, paramUnivName):
    '''https://developer.vectorworks.net/index.php?title=VS:vsoParamName2Index
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoParamName2Index/ja
    \nパラメータのユニバーサルな名前から、その項目番号を返します。なかった場合-1を返します。'''
    return INTEGER

def vsoWSGetParamForEdit():
    '''https://developer.vectorworks.net/index.php?title=VS:vsoWSGetParamForEdit
    \nhttps://developer.vectorworks.net/index.php?title=VS:vsoWSGetParamForEdit/ja
    \nワークシートで編集しようとしているパラメータ名を取得します。'''
    return paramName

def ConsolidatePlanar(obj1, obj2):
    '''https://developer.vectorworks.net/index.php?title=VS:ConsolidatePlanar
    \nhttps://developer.vectorworks.net/index.php?title=VS:ConsolidatePlanar/ja
    \n2 番目のプレイナー図形の平面を変更して、最初の図形の平面上に配置します。また、図形を移動して、平面の変更がその位置に影響を与えないようにします。ConsolidatePlanarObjectsの代わりに使います。'''
    return BOOLEAN

def GetObjectVariableString(h, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjectVariableString
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetObjectVariableString/ja
    \nハンドルで指定した図形の文字列（STRING）設定値を返します。'''
    return STRING

def HLength(h):
    '''https://developer.vectorworks.net/index.php?title=VS:HLength
    \nhttps://developer.vectorworks.net/index.php?title=VS:HLength/ja
    \nハンドルで指定した図形の長さを返します。'''
    return REAL

def SetObjectVariableInt(h, index, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjectVariableInt
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetObjectVariableInt/ja
    \nハンドルで指定した図形の整数（INTEGER）値を設定します。'''
    return None

def Get2DPt(obj, index):
    '''https://developer.vectorworks.net/index.php?title=VS:Get2DPt
    \nhttps://developer.vectorworks.net/index.php?title=VS:Get2DPt/ja
    \nハンドルで指定した2次元図形の頂点座標を返します。'''
    return loc

def GetParent(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetParent
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetParent/ja
    \nハンドルで指定した図形が内包されているコンテナのハンドルを返します。'''
    return HANDLE

def HPerim(h):
    '''https://developer.vectorworks.net/index.php?title=VS:HPerim
    \nhttps://developer.vectorworks.net/index.php?title=VS:HPerim/ja
    \nハンドルで指定した図形の周囲の長さを返します。'''
    return REAL

def SetObjectVariableLongInt(h, index, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjectVariableLongInt
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetObjectVariableLongInt/ja
    \nハンドルで指定した図形の整数（LONGINT）値を設定します。'''
    return None

def GetBBox(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetBBox
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetBBox/ja
    \nハンドルで指定した図形がおさまる最小の四角形の座標を返します。'''
    return (p1, p2)

def GetPlanarRef(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPlanarRef
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPlanarRef/ja
    \n指定した図形の平面参照番号を取得します。'''
    return LONGINT

def HPerimN(ObjectHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:HPerimN
    \nhttps://developer.vectorworks.net/index.php?title=VS:HPerimN/ja
    \nハンドルで指定した図形の周囲の長さを返します。曲線の場合、関数HPerimより正確です。'''
    return REAL

def SetObjectVariablePoint(h, index, p):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjectVariablePoint
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetObjectVariablePoint/ja
    \n図形の設定値を設定します。2D、3Dの点の設定値で利用します。'''
    return BOOLEAN

def GetObjectByUuid(UUID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjectByUuid'''
    return HANDLE

def GetSymLoc(symHd):
    '''https://developer.vectorworks.net/index.php?title=VS:GetSymLoc
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSymLoc/ja
    \nハンドルで指定したシンボルやプラグインオブジェクトの挿入点の座標を返します。'''
    return p

def HWidth(h):
    '''https://developer.vectorworks.net/index.php?title=VS:HWidth
    \nhttps://developer.vectorworks.net/index.php?title=VS:HWidth/ja
    \nハンドルで指定した図形の幅を返します。'''
    return REAL

def SetObjectVariableReal(h, index, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjectVariableReal
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetObjectVariableReal/ja
    \nハンドルで指定した図形の実数（REAL）値を設定します。'''
    return None

def GetObjectUuid(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjectUuid'''
    return STRING

def GetSymRot(symHd):
    '''https://developer.vectorworks.net/index.php?title=VS:GetSymRot
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSymRot/ja
    \nハンドルで指定したシンボルやプラグインオブジェクトの回転角度（度数）を返します。'''
    return REAL

def IsLocked(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:IsLocked'''
    return (BOOLEAN, hObject)

def SetObjectVariableString(h, index, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjectVariableString
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetObjectVariableString/ja
    \nハンドルで指定した図形の文字列（STRING）を設定します。'''
    return None

def GetObjectVariableBoolean(h, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjectVariableBoolean
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetObjectVariableBoolean/ja
    \nハンドルで指定した図形の論理（BOOLEAN）設定値を返します。'''
    return BOOLEAN

def GetType(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetType
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetType/ja
    \nハンドルで指定した図形の種類を番号で返します。'''
    return INTEGER

def ObjArea(h):
    '''https://developer.vectorworks.net/index.php?title=VS:ObjArea
    \nhttps://developer.vectorworks.net/index.php?title=VS:ObjArea/ja
    \nハンドルで指定した図形の面積を返します。値は「単位の設定」ダイアログで設定されている「面積」の単位になります。'''
    return REAL

def SetPlanarRef(h, refID):
    '''https://developer.vectorworks.net/index.php?title=VS:SetPlanarRef
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetPlanarRef/ja
    \n指定した図形の平面参照番号を設定します。'''
    return None

def GetObjectVariableHandle(h, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjectVariableHandle
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetObjectVariableHandle/ja
    \nハンドルで指定した図形の整数（INTEGER）設定値を返します。'''
    return HANDLE

def GetTypeN(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTypeN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTypeN/ja
    \nハンドルで指定した図形の種類を番号で返します。'''
    return INTEGER

def ObjAreaN(ObjectHandle ):
    '''https://developer.vectorworks.net/index.php?title=VS:ObjAreaN
    \nhttps://developer.vectorworks.net/index.php?title=VS:ObjAreaN/ja
    \nハンドルで指定した図形の面積を返します。値は「単位の設定」ダイアログで設定されている「面積」の単位になります。曲線の場合、関数ObjAreaより正確です。'''
    return REAL

def SetPlanarRefIDToGround(h):
    '''https://developer.vectorworks.net/index.php?title=VS:SetPlanarRefIDToGround
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetPlanarRefIDToGround/ja
    \n指定した図形を基準平面上に設定します。パラメトリックオブジェクトの中で使用します。'''
    return None

def GetObjectVariableInt(h, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjectVariableInt
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetObjectVariableInt/ja
    \nハンドルで指定した図形の整数（INTEGER）設定値を返します。'''
    return INTEGER

def HAngle(h):
    '''https://developer.vectorworks.net/index.php?title=VS:HAngle
    \nhttps://developer.vectorworks.net/index.php?title=VS:HAngle/ja
    \nハンドルで指定した線や円弧の角度を返します。'''
    return REAL

def SetAngle(h, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetAngle
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetAngle/ja
    \nハンドルで指定した図形の角度を設定します。'''
    return None

def SetWidth(h, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWidth
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWidth/ja
    \nハンドルで指定した図形の幅を設定します。'''
    return None

def GetObjectVariableLongInt(h, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjectVariableLongInt
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetObjectVariableLongInt/ja
    \nハンドルで指定した図形の整数（LONGINT）設定値を返します。'''
    return LONGINT

def HArea(h):
    '''https://developer.vectorworks.net/index.php?title=VS:HArea
    \nhttps://developer.vectorworks.net/index.php?title=VS:HArea/ja
    \nハンドルで指定した図形の面積を返します。'''
    return REAL

def SetHeight(h, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetHeight
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetHeight/ja
    \nハンドルで指定した図形の高さを設定します。'''
    return None

def GetObjectVariablePoint(h, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjectVariablePoint
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetObjectVariablePoint/ja
    \n図形の設定値を返します。2D、3Dの点を返す設定値で利用します。'''
    return (BOOLEAN, outP)

def HAreaN(ObjectHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:HAreaN
    \nhttps://developer.vectorworks.net/index.php?title=VS:HAreaN/ja
    \nハンドルで指定した図形の面積を返します。曲線の場合、関数HAreaより正確です。'''
    return REAL

def SetObjectVariableBoolean(h, index, status):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjectVariableBoolean
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetObjectVariableBoolean/ja
    \nハンドルで指定した図形の論理（BOOLEAN）値を設定します。'''
    return None

def GetObjectVariableReal(h, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjectVariableReal
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetObjectVariableReal/ja
    \nハンドルで指定した図形の実数（REAL）設定値を返します。'''
    return REAL

def HHeight(h):
    '''https://developer.vectorworks.net/index.php?title=VS:HHeight
    \nhttps://developer.vectorworks.net/index.php?title=VS:HHeight/ja
    \nハンドルで指定した図形の高さを返します。高さとは、3次元図形の高さではなく、Y方向の高さです。'''
    return REAL

def SetObjectVariableHandle(h, index, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjectVariableHandle
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetObjectVariableHandle/ja
    \n図形プロパティの値を設定します。'''
    return None

def DelName(name):
    '''https://developer.vectorworks.net/index.php?title=VS:DelName
    \nhttps://developer.vectorworks.net/index.php?title=VS:DelName/ja
    \n図形の名前をドキュメントから削除します。図形そのものは削除されません。'''
    return None

def GetName(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetName
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetName/ja
    \nハンドルで指定した図形の名前を返します。'''
    return STRING

def NameList(index):
    '''https://developer.vectorworks.net/index.php?title=VS:NameList
    \nhttps://developer.vectorworks.net/index.php?title=VS:NameList/ja
    \n指定した索引番号の名前を返します。'''
    return STRING

def SetDashLineTypeName(DashStyleIndex, DashStyleName):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDashLineTypeName'''
    return BOOLEAN

def GetColorName(ColorIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetColorName
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetColorName/ja
    \n指定した色番号の名前を返します。'''
    return STRING

def GetObject(name):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetObject/ja
    \n指定した名前が付いた図形のハンドルを返します。図形が存在しない場合はNILを返します。'''
    return HANDLE

def NameNum():
    '''https://developer.vectorworks.net/index.php?title=VS:NameNum
    \nhttps://developer.vectorworks.net/index.php?title=VS:NameNum/ja
    \nアクティブなドキュメント内の名前が付いている図形の数を返します。'''
    return LONGINT

def SetDashStyleName(DashStyleIndex, DashStyleName):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDashStyleName
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDashStyleName/ja
    \n指定した破線番号の名前を設定します。'''
    return BOOLEAN

def GetDashLineTypeName(DashStyleIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDashLineTypeName'''
    return STRING

def Index2Name(index):
    '''https://developer.vectorworks.net/index.php?title=VS:Index2Name
    \nhttps://developer.vectorworks.net/index.php?title=VS:Index2Name/ja
    \n内部で使用している索引番号を文字列で返します。'''
    return STRING

def NameObject(objName):
    '''https://developer.vectorworks.net/index.php?title=VS:NameObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:NameObject/ja
    \n直後に作成される図形やワークシートに名前を付けます。'''
    return None

def SetName(h, name):
    '''https://developer.vectorworks.net/index.php?title=VS:SetName
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetName/ja
    \nハンドルで指定した図形の名前を設定します。'''
    return None

def GetDashStyleName(DashStyleIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDashStyleName
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDashStyleName/ja
    \n指定した破線番号の名前を返します。'''
    return STRING

def Name2Index(name):
    '''https://developer.vectorworks.net/index.php?title=VS:Name2Index
    \nhttps://developer.vectorworks.net/index.php?title=VS:Name2Index/ja
    \n内部で使用している文字列の索引番号を返します。'''
    return LONGINT

def SetColorName(ColorIndex, ColorName):
    '''https://developer.vectorworks.net/index.php?title=VS:SetColorName
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetColorName/ja
    \n指定した色番号の名前を設定します。'''
    return BOOLEAN

def AddHole(objectToGetHole, holeTemplate):
    '''https://developer.vectorworks.net/index.php?title=VS:AddHole
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddHole/ja
    \nハンドルで指定した図形で図形に穴を開けます。実行後の図形属性は曲線になります。'''
    return (BOOLEAN, objectToGetHole)

def CreateRenderBkg(Background):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateRenderBkg
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateRenderBkg/ja'''
    return HANDLE

def Locus(p):
    '''https://developer.vectorworks.net/index.php?title=VS:Locus
    \nhttps://developer.vectorworks.net/index.php?title=VS:Locus/ja
    \n指定した座標の位置に基準点を作成します。'''
    return None

def RRectangleN(orgin, direction, width, height, xDiam, yDiam):
    '''https://developer.vectorworks.net/index.php?title=VS:RRectangleN
    \nhttps://developer.vectorworks.net/index.php?title=VS:RRectangleN/ja
    \n指定した座標と直径で隅の丸い四角形を作成します。'''
    return None

def AddSurface(s1, s2):
    '''https://developer.vectorworks.net/index.php?title=VS:AddSurface
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddSurface/ja
    \nハンドルで指定した2つの図形を貼り合わせて図形を作成します。'''
    return HANDLE

def GetArc(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetArc
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetArc/ja
    \nハンドルで指定した円弧の開始角度と円弧の角度を返します。'''
    return (startAngleR, arcAngleR)

def MakePolygon(inSourceObject):
    '''https://developer.vectorworks.net/index.php?title=VS:MakePolygon
    \nhttps://developer.vectorworks.net/index.php?title=VS:MakePolygon/ja
    \nハンドルで指定した図形から多角形を作成します。'''
    return HANDLE

def Rect(p1x, p1y, p2x, p2y):
    '''https://developer.vectorworks.net/index.php?title=VS:Rect
    \nhttps://developer.vectorworks.net/index.php?title=VS:Rect/ja
    \n指定した座標の四角形を作成します。'''
    return None

def Arc(p1, p2, StartAngle, ArcAngle):
    '''https://developer.vectorworks.net/index.php?title=VS:Arc
    \nhttps://developer.vectorworks.net/index.php?title=VS:Arc/ja
    \n指定した座標の四角形に内接する円弧を作成します。'''
    return None

def GetLocPt(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLocPt
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLocPt/ja
    \nハンドルで指定した基準点の座標を返します。'''
    return p

def MakePolyline(inSourceObject):
    '''https://developer.vectorworks.net/index.php?title=VS:MakePolyline
    \nhttps://developer.vectorworks.net/index.php?title=VS:MakePolyline/ja
    \nハンドルで指定した図形から曲線を作成します。'''
    return HANDLE

def RectangleN(orgin, direction, width, height):
    '''https://developer.vectorworks.net/index.php?title=VS:RectangleN
    \nhttps://developer.vectorworks.net/index.php?title=VS:RectangleN/ja
    \n指定した座標の四角形を作成します。'''
    return None

def ArcByCenter(x, y, radius, startAngl, sweepAngle):
    '''https://developer.vectorworks.net/index.php?title=VS:ArcByCenter
    \nhttps://developer.vectorworks.net/index.php?title=VS:ArcByCenter/ja
    \n中心点、半径、始発角度、円弧角から円弧を作成します。'''
    return None

def GetRRDiam(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetRRDiam
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetRRDiam/ja
    \nハンドルで指定した隅の丸い四角形の、隅の丸みの直径を返します。'''
    return (xDiam, yDiam)

def ModelPt2DToScreenPt(p):
    '''https://developer.vectorworks.net/index.php?title=VS:ModelPt2DToScreenPt
    \nhttps://developer.vectorworks.net/index.php?title=VS:ModelPt2DToScreenPt/ja
    \n平面の回転でワールド座標系からスクリーン座標にポイント変えます。'''
    return p

def ScreenPtToModelPt2D(p):
    '''https://developer.vectorworks.net/index.php?title=VS:ScreenPtToModelPt2D
    \nhttps://developer.vectorworks.net/index.php?title=VS:ScreenPtToModelPt2D/ja
    \n平面の回転で座標をスクリーン座標からモデル座標に変換します。'''
    return p

def ClipSurface(s1, s2):
    '''https://developer.vectorworks.net/index.php?title=VS:ClipSurface
    \nhttps://developer.vectorworks.net/index.php?title=VS:ClipSurface/ja
    \nハンドルで指定した図形2で図形1を切断します。'''
    return None

def GetSegPt1(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetSegPt1
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSegPt1/ja
    \nハンドルで指定した直線、壁、線形の寸法（寸法、斜め寸法）の始点の座標を返します。'''
    return p

def ModelVecToScreenVec(p):
    '''https://developer.vectorworks.net/index.php?title=VS:ModelVecToScreenVec
    \nhttps://developer.vectorworks.net/index.php?title=VS:ModelVecToScreenVec/ja
    \n平面の回転でベクトルをワールド座標系からスクリーン座標に変えます。 回転のみを考慮に入れます。'''
    return p

def ScreenVecToModelVec(p):
    '''https://developer.vectorworks.net/index.php?title=VS:ScreenVecToModelVec
    \nhttps://developer.vectorworks.net/index.php?title=VS:ScreenVecToModelVec/ja
    \n平面の回転でベクトルをスクリーン座標からモデル座標に変換します。 回転のみを考慮します。'''
    return p

def ClipSurfaceN(s1, s2):
    '''https://developer.vectorworks.net/index.php?title=VS:ClipSurfaceN
    \nhttps://developer.vectorworks.net/index.php?title=VS:ClipSurfaceN/ja
    \nハンドルで指定した図形2で図形1を切断します。変換後の図形のハンドルを返す以外は、元のClipSurfaceと同じ操作を行います。'''
    return HANDLE

def GetSegPt2(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetSegPt2
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSegPt2/ja
    \nハンドルで指定した直線、壁、線形の寸法（寸法、斜め寸法）の終点の座標を返します。'''
    return p

def OffsetPolyClosed(obj, offset, smoothCorners):
    '''https://developer.vectorworks.net/index.php?title=VS:OffsetPolyClosed'''
    return HANDLE

def SetArc(h, startAngle, arcAngle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetArc
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetArc/ja
    \nハンドルで指定した円弧の開始角度と円弧の角度を変更します。'''
    return None

def CombineIntoSurface(pt):
    '''https://developer.vectorworks.net/index.php?title=VS:CombineIntoSurface
    \nhttps://developer.vectorworks.net/index.php?title=VS:CombineIntoSurface/ja
    \n選択している図形から、指定した点を囲む曲線を作成します。'''
    return HANDLE

def IntersectSurface(s1, s2):
    '''https://developer.vectorworks.net/index.php?title=VS:IntersectSurface
    \nhttps://developer.vectorworks.net/index.php?title=VS:IntersectSurface/ja
    \nハンドルで指定した図形で図形を抜き取ります。ただし、グループ図形やシンボル図形にはこの機能は使えません。'''
    return HANDLE

def Oval(p1, p2):
    '''https://developer.vectorworks.net/index.php?title=VS:Oval
    \nhttps://developer.vectorworks.net/index.php?title=VS:Oval/ja
    \n指定した座標の四角形に内接する長円を作成します。'''
    return None

def SetSegPt1(h, p):
    '''https://developer.vectorworks.net/index.php?title=VS:SetSegPt1
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetSegPt1/ja
    \nハンドルで指定した直線や壁の始点の座標を、指定した座標に変更します。'''
    return None

def Create2DObjShadow(h, offsetVec):
    '''https://developer.vectorworks.net/index.php?title=VS:Create2DObjShadow
    \nhttps://developer.vectorworks.net/index.php?title=VS:Create2DObjShadow/ja
    \n任意の2D図形の影表現を、指定したオフセット値で作成します。'''
    return HANDLE

def Line(line):
    '''https://developer.vectorworks.net/index.php?title=VS:Line
    \nhttps://developer.vectorworks.net/index.php?title=VS:Line/ja
    \n現在のペン位置から、相対的に移動した座標の位置へ線を描画します。'''
    return None

def OvalN(orgin, direction, width, height):
    '''https://developer.vectorworks.net/index.php?title=VS:OvalN
    \nhttps://developer.vectorworks.net/index.php?title=VS:OvalN/ja
    \n指定した座標の四角形に内接する長円を作成します。'''
    return None

def SetSegPt2(h, p):
    '''https://developer.vectorworks.net/index.php?title=VS:SetSegPt2
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetSegPt2/ja
    \nハンドルで指定した直線や壁の終点の座標を、指定した座標に変更します。'''
    return None

def CreateRWBackground(imageResource):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateRWBackground
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateRWBackground/ja
    \nハンドルで指定したイメージリソースを使用して、背景テクスチャリソースを作成します。幅と高さはデフォルト値 (ページサイズとの相対サイズ) に設定されます。'''
    return HANDLE

def LineTo(p):
    '''https://developer.vectorworks.net/index.php?title=VS:LineTo
    \nhttps://developer.vectorworks.net/index.php?title=VS:LineTo/ja
    \n現在のペン位置から、絶対座標の位置へ線を描画します。'''
    return None

def RRect(p1, p2, Diam):
    '''https://developer.vectorworks.net/index.php?title=VS:RRect
    \nhttps://developer.vectorworks.net/index.php?title=VS:RRect/ja
    \n指定した座標の四角形を、指定した直径で隅を丸く作成します。'''
    return None

def Add3DPt(p):
    '''https://developer.vectorworks.net/index.php?title=VS:Add3DPt
    \nhttps://developer.vectorworks.net/index.php?title=VS:Add3DPt/ja
    \nBeginPoly3DとEndPoly3Dの間で使います。'''
    return None

def CreateExtrudeAlongPath(pathHandle, profileHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateExtrudeAlongPath
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateExtrudeAlongPath/ja
    \n輪郭、パスを示す図形から3Dパス図形を作成します。パスの図形属性はNURBS曲線（111）でなければなりません。輪郭の図形属性はNURBS曲線、多角形、曲線、円弧、四角形、隅の丸い四角形、線、長円でなければなりません。'''
    return HANDLE

def Flip3DObj(h, horiz):
    '''https://developer.vectorworks.net/index.php?title=VS:Flip3DObj
    \nhttps://developer.vectorworks.net/index.php?title=VS:Flip3DObj/ja
    \n3D図形をX軸かY軸で反転させる。'''
    return None

def MeshToGroup(meshObj):
    '''https://developer.vectorworks.net/index.php?title=VS:MeshToGroup
    \nhttps://developer.vectorworks.net/index.php?title=VS:MeshToGroup/ja
    \nハンドルで指定したメッシュ図形を3D多角形で構成されたグループ図形に変換します。'''
    return HANDLE

def AddVertex3D(objectHd, p):
    '''https://developer.vectorworks.net/index.php?title=VS:AddVertex3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddVertex3D/ja
    \nハンドルで指定した3D多角形に頂点を追加します。'''
    return None

def CreateImageProp(propName, textureRef, height, width, enforceImageAspectRatio, crossedPlanes, createPlugin, autoRotate, createSymbol):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateImageProp
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateImageProp/ja
    \nオプションを指定して添景を作成します。'''
    return HANDLE

def Get3DCntr(h):
    '''https://developer.vectorworks.net/index.php?title=VS:Get3DCntr
    \nhttps://developer.vectorworks.net/index.php?title=VS:Get3DCntr/ja
    \nハンドルで指定した3次元図形の中心の座標を返します。'''
    return (p, zValue)

def Moments3D(obj):
    '''https://developer.vectorworks.net/index.php?title=VS:Moments3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:Moments3D/ja
    \n図形の質量中心を通る軸での慣性モーメントを返します。'''
    return (BOOLEAN, lxx, lyy, lzz)

def BeginMXtrd(startDistance, endDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:BeginMXtrd
    \nhttps://developer.vectorworks.net/index.php?title=VS:BeginMXtrd/ja
    \nこの手続きを実行した後、EndMXtrdが実行されるまでに作成された2次元図形をもとに多段柱状体を作成します。'''
    return None

def CreateTaperedExtrd2(profileH, angle, height):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateTaperedExtrd2
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateTaperedExtrd2/ja
    \n錐状体を作成します。CreateTaperedExtrudeでは複数のNURBS曲面となり、CreateTaperedExtrd2では汎用ソリッドとなります。'''
    return HANDLE

def Get3DInfo(h):
    '''https://developer.vectorworks.net/index.php?title=VS:Get3DInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:Get3DInfo/ja
    \nハンドルで指定した3次元図形の高さ、幅、奥行きを返します。'''
    return (height, width, depth)

def Poly3D(p):
    '''https://developer.vectorworks.net/index.php?title=VS:Poly3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:Poly3D/ja
    \n座標を指定して3D多角形を作成します。'''
    return None

def BeginMesh():
    '''https://developer.vectorworks.net/index.php?title=VS:BeginMesh
    \nhttps://developer.vectorworks.net/index.php?title=VS:BeginMesh/ja
    \nこの手続きを実行した後、EndMeshが実行されるまでに作成された図形をもとにメッシュ図形を作成します。'''
    return None

def CreateTaperedExtrude(profileH, angle, height):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateTaperedExtrude
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateTaperedExtrude/ja
    \n錐状体を作成します。CreateTaperedExtrudeでは複数のNURBS曲面となり、CreateTaperedExtrd2では汎用ソリッドとなります。'''
    return HANDLE

def Get3DOrientation(h):
    '''https://developer.vectorworks.net/index.php?title=VS:Get3DOrientation
    \nhttps://developer.vectorworks.net/index.php?title=VS:Get3DOrientation/ja
    \nハンドルで指定した3次元図形の回転角度を返します。'''
    return (BOOLEAN, xRot, yRot, zRot, isMirroredXY)

def Products3D(obj):
    '''https://developer.vectorworks.net/index.php?title=VS:Products3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:Products3D/ja
    \n図形の質量中心を通る平面での慣性乗数を返します。'''
    return (BOOLEAN, lxy, lyz, lzx)

def BeginPoly3D():
    '''https://developer.vectorworks.net/index.php?title=VS:BeginPoly3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:BeginPoly3D/ja
    \nこの手続きを実行した後、EndPoly3Dが実行されるまでに追加された頂点をもとに3D多角形を作成します。'''
    return None

def EndMXtrd():
    '''https://developer.vectorworks.net/index.php?title=VS:EndMXtrd
    \nhttps://developer.vectorworks.net/index.php?title=VS:EndMXtrd/ja
    \nBeginMXtrdを実行した後、この手続きが実行されるまでに作成された2次元図形をもとに多段柱状体を作成します。'''
    return None

def GetLocus3D(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLocus3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLocus3D/ja
    \nハンドルで指定した3D基準点の座標を返します。'''
    return p

def Set3DInfo(h, heightDistance, widthDistance, depthDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:Set3DInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:Set3DInfo/ja
    \nハンドルで指定した3次元図形の高さ、幅、奥行きを変更します。'''
    return None

def BeginSweep(startAngle, arcAngle, incAngle, PitchDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:BeginSweep
    \nhttps://developer.vectorworks.net/index.php?title=VS:BeginSweep/ja
    \nこの手続きが実行した後、EndSweepが実行されるまでに作成された2次元図形をもとに回転体を作成します。'''
    return None

def EndMesh():
    '''https://developer.vectorworks.net/index.php?title=VS:EndMesh
    \nhttps://developer.vectorworks.net/index.php?title=VS:EndMesh/ja
    \nBeginMeshを実行した後、この手続きが実行されるまでに作成された図形をもとにメッシュ図形を作成します。'''
    return None

def GetMeshVertex(hMesh, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetMeshVertex
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetMeshVertex/ja
    \nメッシュオブジェクトの指定された頂点を返します。'''
    return outPt

def Set3DRot(h, xAngle, yAngle, zAngle, xDistance, yDistance, zDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:Set3DRot
    \nhttps://developer.vectorworks.net/index.php?title=VS:Set3DRot/ja
    \nハンドルで指定した3次元図形を、指定した回転軸を中心に回転させます。'''
    return None

def BeginXtrd(startDistance, endDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:BeginXtrd
    \nhttps://developer.vectorworks.net/index.php?title=VS:BeginXtrd/ja
    \nこの手続きを実行した後、EndXtrdが実行されるまでに作成された2次元図形を底面とする柱状体を作成します。'''
    return None

def EndPoly3D():
    '''https://developer.vectorworks.net/index.php?title=VS:EndPoly3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:EndPoly3D/ja
    \nBeginPoly3Dを実行した後、この手続きを実行するまでに実行されたAdd3DPを頂点とする3D多角形を作成します。'''
    return None

def GetMeshVertsCnt(hMesh):
    '''https://developer.vectorworks.net/index.php?title=VS:GetMeshVertsCnt
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetMeshVertsCnt/ja
    \n渡されたメッシュハンドルの頂点の数を返します。'''
    return INTEGER

def SetMeshVertex(hMesh, index, pt):
    '''https://developer.vectorworks.net/index.php?title=VS:SetMeshVertex
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetMeshVertex/ja
    \nメッシュの頂点を設定します。'''
    return None

def Centroid3D(obj):
    '''https://developer.vectorworks.net/index.php?title=VS:Centroid3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:Centroid3D/ja
    \nハンドルで指定した3次元図形の質量中心の座標を返します。計算できた場合は、TRUEを返します。'''
    return (BOOLEAN, xCG, yCG, zCG)

def EndSweep():
    '''https://developer.vectorworks.net/index.php?title=VS:EndSweep
    \nhttps://developer.vectorworks.net/index.php?title=VS:EndSweep/ja
    \nBeginSweepを実行した後、この手続きが実行されるまでに作成された2次元図形をもとに回転体を作成します。'''
    return None

def GetPolyPt3D(objectHd, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPolyPt3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPolyPt3D/ja
    \nハンドルで指定したメッシュ、3D多角形、NURBS曲線の指定した頂点番号の座標を返します。'''
    return p

def SetPolyPt3D(objectHd, index, p, zValue):
    '''https://developer.vectorworks.net/index.php?title=VS:SetPolyPt3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetPolyPt3D/ja
    \nハンドルで指定した3D多角形の指定した頂点番号の座標を変更します。'''
    return None

def ConvertTo3DPolys(original):
    '''https://developer.vectorworks.net/index.php?title=VS:ConvertTo3DPolys
    \nhttps://developer.vectorworks.net/index.php?title=VS:ConvertTo3DPolys/ja
    \nハンドルで指定した図形（四角形、円、円弧、曲線、多角形、長円、線、壁、円弧壁、屋根）を3D多角形に変換します。'''
    return HANDLE

def EndXtrd():
    '''https://developer.vectorworks.net/index.php?title=VS:EndXtrd
    \nhttps://developer.vectorworks.net/index.php?title=VS:EndXtrd/ja
    \nBeginXtrdが実行された後、この手続きが実行されるまでに作成された2次元図形を底面とする柱状体を作成します。'''
    return None

def HExtrude(objectH, bottom, top):
    '''https://developer.vectorworks.net/index.php?title=VS:HExtrude
    \nhttps://developer.vectorworks.net/index.php?title=VS:HExtrude/ja
    \n柱状体を作成します。'''
    return HANDLE

def SetRot3D(h, xAngle, yAngle, zAngle, xDistance, yDistance, zDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:SetRot3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetRot3D/ja
    \nハンドルで指定した3次元図形を、指定した角度（度数）と軸で回転させます。'''
    return None

def CreateContourCurves(inSourceObject, delta, ptOnPlane, normal):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateContourCurves
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateContourCurves/ja
    \nハンドルで指定したソリッド図形に、指定した間隔で等高線を作成します。'''
    return HANDLE

def ExtrudeAlongPath(pathHandle, profileHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:ExtrudeAlongPath
    \nhttps://developer.vectorworks.net/index.php?title=VS:ExtrudeAlongPath/ja
    \n3Dパス図形を作成します。輪郭をパスに沿って引き延ばした図形が作成されます。'''
    return HANDLE

def Locus3D(p):
    '''https://developer.vectorworks.net/index.php?title=VS:Locus3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:Locus3D/ja
    \n座標を指定して3D基準点を作成します。'''
    return None

def BeginColumn(columnDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:BeginColumn
    \nhttps://developer.vectorworks.net/index.php?title=VS:BeginColumn/ja
    \n柱の高さを設定します。この手続きを実行してから、EndGroupが実行されるまでの間に作成された2次元図形を底面とする柱を作成します。'''
    return None

def GetCompWallAssMod(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompWallAssMod
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompWallAssMod/ja
    \nオブジェクトの構成要素の壁結合時の端部の調整を取得します。'''
    return (BOOLEAN, wallAssociatedModification)

def GetSlabHeight(slab):
    '''https://developer.vectorworks.net/index.php?title=VS:GetSlabHeight
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSlabHeight/ja
    \nスラブの高さを取得します。'''
    return REAL

def SetCompUseClassRPW(object, componentIndex, useClassPenWeightForRightPen):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompUseClassRPW
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompUseClassRPW/ja
    \nオブジェクトの構成要素の線種（右側）にクラス属性の線の太さを使用するかどうかのフラグを設定します。'''
    return BOOLEAN

def BeginFloor(thicknessDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:BeginFloor
    \nhttps://developer.vectorworks.net/index.php?title=VS:BeginFloor/ja
    \n床の厚みを設定します。この手続きを実行してから、EndObjectが実行されるまでの間に作成された2次元図形から床を作成します。'''
    return None

def GetComponentAutoBoundEdgeOffset(obj, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponentAutoBoundEdgeOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetComponentAutoBoundEdgeOffset/ja
    \n図形の構成要素の自動設定された境界の辺のオフセットを取得します。'''
    return (BOOLEAN, autoBoundEdgeOffset)

def GetSlabPreferences():
    '''https://developer.vectorworks.net/index.php?title=VS:GetSlabPreferences
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSlabPreferences/ja
    \nスラブ設定を取得します。構成要素関連のコールやスタイルの選択とあわせて使用します。'''
    return HANDLE

def SetCompWallAssBound(object, componentIndex, wallAssociatedBound):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompWallAssBound
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompWallAssBound/ja
    \nオブジェクトの構成要素の壁結合時の端部の境界を設定します。'''
    return BOOLEAN

def ConvertToUnstyledSlab(slab):
    '''https://developer.vectorworks.net/index.php?title=VS:ConvertToUnstyledSlab
    \nhttps://developer.vectorworks.net/index.php?title=VS:ConvertToUnstyledSlab/ja
    \nスラブスタイルを「なし」に設定します。'''
    return None

def GetComponentClass(obj, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponentClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetComponentClass/ja
    \nハンドルで指定した壁の、指定した番号の構成要素からクラスを取得します。ハンドルがNILならば、この関数はデフォルト壁スタイルに作用します。'''
    return (BOOLEAN, componentClass)

def GetSlabPreferencesStyle():
    '''https://developer.vectorworks.net/index.php?title=VS:GetSlabPreferencesStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSlabPreferencesStyle/ja
    \nスラブ設定のスラブスタイルを取得します。'''
    return LONGINT

def SetCompWallAssMod(object, componentIndex, wallAssociatedModification):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompWallAssMod
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompWallAssMod/ja
    \nオブジェクトの構成要素の壁結合時の端部の調整を設定します。'''
    return BOOLEAN

def CreateRoofStyle(roofStyleName):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateRoofStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateRoofStyle/ja
    \n指定した名前の新しい屋根スタイルを作成します。すでに名前が使われている場合は次に可能な名前となります。'''
    return HANDLE

def GetComponentFill(obj, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponentFill
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetComponentFill/ja
    \n壁の中心線の線の模様を返します。成功した場合はTRUEを返します。'''
    return (BOOLEAN, fill)

def GetSlabStyle(slab):
    '''https://developer.vectorworks.net/index.php?title=VS:GetSlabStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSlabStyle/ja
    \nスラブのスラブスタイルを取得します。'''
    return LONGINT

def SetComponentAutoBoundEdgeOffset(obj, componentIndex, autoBoundEdgeOffset):
    '''https://developer.vectorworks.net/index.php?title=VS:SetComponentAutoBoundEdgeOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetComponentAutoBoundEdgeOffset/ja
    \n図形の構成要素の自動設定された境界の辺のオフセットを設定します。'''
    return BOOLEAN

def CreateSlab(profile):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateSlab
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateSlab/ja
    \nスラブを作成します。'''
    return HANDLE

def GetComponentFillColors(obj, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponentFillColors
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetComponentFillColors/ja
    \nハンドルで指定した壁の、指定した番号の構成要素から面の色と地色を取得します。ハンドルがNILならば、この関数はデフォルト壁スタイルに作用します。'''
    return (BOOLEAN, fillForeColor, fillBackColor)

def GetStoryLayerInfo(index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetStoryLayerInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetStoryLayerInfo/ja
    \nインデックスを使用して、ストーリの情報を返します。'''
    return (Boolean, name, scaleFactor, layerLevelType, eleveationOffset, defaultWallHeight)

def SetComponentClass(obj, componentIndex, componentClass):
    '''https://developer.vectorworks.net/index.php?title=VS:SetComponentClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetComponentClass/ja
    \nハンドルで指定した壁の、指定した番号の構成要素のクラスを設定します。ハンドルがNILならば、この関数はデフォルト壁スタイルに作用します。'''
    return BOOLEAN

def CreateSlabStyle(slabStyleName):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateSlabStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateSlabStyle/ja
    \n指定した名前の新しいスラブスタイルを作成します。すでに名前が使われている場合は次に可能な名前となります。'''
    return HANDLE

def GetComponentFollowBottomWallPeaks(obj, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponentFollowBottomWallPeaks
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetComponentFollowBottomWallPeaks/ja
    \n図形の構成要素が壁の下端に端を合わせるかどうかのフラグを取得します。'''
    return (BOOLEAN, followBottomWallPeaks)

def GetTaperedComponent(object):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTaperedComponent
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTaperedComponent/ja
    \nテーパが設定されている構成要素のインデックスを取得します。'''
    return INTEGER

def SetComponentFill(obj, componentIndex, fill):
    '''https://developer.vectorworks.net/index.php?title=VS:SetComponentFill
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetComponentFill/ja
    \nハンドルで指定した壁で、指定した番号の構成要素の面を模様番号で設定します。ハンドルがNILならば、デフォルト壁スタイルに作用します。'''
    return BOOLEAN

def DelObjStoryBound(obj, boundID):
    '''https://developer.vectorworks.net/index.php?title=VS:DelObjStoryBound
    \nhttps://developer.vectorworks.net/index.php?title=VS:DelObjStoryBound/ja
    \nハンドルで指定した図形の高さ基準を削除します。'''
    return None

def GetComponentFollowTopWallPeaks(obj, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponentFollowTopWallPeaks
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetComponentFollowTopWallPeaks/ja
    \n図形の構成要素が壁の上端に端を合わせるかどうかのフラグを取得します。'''
    return (BOOLEAN, followTopWallPeaks)

def GetWallPreferences():
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallPreferences
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWallPreferences/ja
    \n壁設定を取得します。これは構成要素の関数やスタイル選択に使えます。'''
    return HANDLE

def SetComponentFillColors(obj, componentIndex, fillForeColor, fillBackColor):
    '''https://developer.vectorworks.net/index.php?title=VS:SetComponentFillColors
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetComponentFillColors/ja
    \nハンドルで指定した壁の、指定した番号の構成要素の面の色と地色を設定します。ハンドルがNILならば、この関数はデフォルト壁スタイルに作用します。'''
    return BOOLEAN

def DelObjStoryBounds(obj):
    '''https://developer.vectorworks.net/index.php?title=VS:DelObjStoryBounds
    \nhttps://developer.vectorworks.net/index.php?title=VS:DelObjStoryBounds/ja
    \nハンドルで指定した図形の高さ基準をすべて削除します。'''
    return None

def GetComponentFunction(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponentFunction'''
    return (BOOLEAN, func)

def HasObjStoryBound(obj, boundID):
    '''https://developer.vectorworks.net/index.php?title=VS:HasObjStoryBound
    \nhttps://developer.vectorworks.net/index.php?title=VS:HasObjStoryBound/ja
    \nハンドルで指定した図形が高さ基準を持つ図形であるかを返します。'''
    return BOOLEAN

def SetComponentFollowBottomWallPeaks(obj, componentIndex, followBottomWallPeaks):
    '''https://developer.vectorworks.net/index.php?title=VS:SetComponentFollowBottomWallPeaks
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetComponentFollowBottomWallPeaks/ja
    \n図形の構成要素が壁の下端に端を合わせるかどうかのフラグを設定します。'''
    return BOOLEAN

def DeleteAllComponents(obj):
    '''https://developer.vectorworks.net/index.php?title=VS:DeleteAllComponents
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeleteAllComponents/ja
    \nハンドルで指定した壁または壁スタイルの全構成要素を削除します。ハンドルがNILならば、デフォルト壁スタイルに作用します。'''
    return BOOLEAN

def GetComponentManualEdgeOffset(obj, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponentManualEdgeOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetComponentManualEdgeOffset/ja
    \n図形の構成要素の手動設定された境界の辺のオフセットを取得します。'''
    return (BOOLEAN, manualEdgeOffset)

def HasObjStoryBounds(obj):
    '''https://developer.vectorworks.net/index.php?title=VS:HasObjStoryBounds
    \nhttps://developer.vectorworks.net/index.php?title=VS:HasObjStoryBounds/ja
    \nハンドルで指定した図形が高さ基準を持つ図形であるかを返します。'''
    return BOOLEAN

def SetComponentFollowTopWallPeaks(obj, componentIndex, followTopWallPeaks):
    '''https://developer.vectorworks.net/index.php?title=VS:SetComponentFollowTopWallPeaks
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetComponentFollowTopWallPeaks/ja
    \n図形の構成要素が壁の上端に端を合わせるかどうかのフラグを設定します。'''
    return BOOLEAN

def DeleteComponent(obj, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:DeleteComponent
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeleteComponent/ja
    \n壁の構成要素を番号を指定して削除します。'''
    return BOOLEAN

def GetComponentMaterial(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponentMaterial'''
    return (BOOLEAN, material)

def InsertNewComponent(obj, beforeComponentIndex, width, fill, leftPenWeight, rightPenWeight, leftPenStyle, rightPenStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertNewComponent
    \nhttps://developer.vectorworks.net/index.php?title=VS:InsertNewComponent/ja
    \nハンドルで指定した壁で、指定した番号の構成要素の前に、新しい構成要素を追加します。ハンドルがNILならば、デフォルト壁スタイルに作用します。'''
    return BOOLEAN

def SetComponentFunction(object, componentIndex, func):
    '''https://developer.vectorworks.net/index.php?title=VS:SetComponentFunction'''
    return BOOLEAN

def GetCompABoundEOffOff(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompABoundEOffOff
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompABoundEOffOff/ja
    \n図形の構成要素の自動設定された境界の辺のオフセットを取得します。'''
    return (BOOLEAN, autoBoundEdgeOffsetOffset)

def GetComponentName(obj, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponentName
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetComponentName/ja
    \nハンドルで指定した壁の、指定した番号の構成要素から名前を取得します。ハンドルがNILならば、この関数はデフォルト壁スタイルに作用します。'''
    return STRING

def InsertNewComponentN(object, beforeComponentIndex, width, fill, leftPenWeight, rightPenWeight, leftPenStyle, rightPenStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertNewComponentN'''
    return BOOLEAN

def SetComponentManualEdgeOffset(obj, componentIndex, manualEdgeOffset):
    '''https://developer.vectorworks.net/index.php?title=VS:SetComponentManualEdgeOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetComponentManualEdgeOffset/ja
    \n図形の構成要素の手動設定された境界の辺のオフセットを設定します。'''
    return BOOLEAN

def GetCompAltSecFill(obj, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompAltSecFill
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompAltSecFill/ja
    \nオブジェクトの構成要素の切り替え位置の面のスタイルを取得します。'''
    return (BOOLEAN, alternateSectionFill)

def GetComponentNetArea(obj, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponentNetArea
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetComponentNetArea/ja
    \n図形の構成要素の正味の面積を取得します。'''
    return REAL

def ModifySlab(slab, modifier, isClipObject, componentFlags):
    '''https://developer.vectorworks.net/index.php?title=VS:ModifySlab
    \nhttps://developer.vectorworks.net/index.php?title=VS:ModifySlab/ja
    \nスラブの貼り合わせ、切り欠き'''
    return BOOLEAN

def SetComponentMaterial(object, componentIndex, material):
    '''https://developer.vectorworks.net/index.php?title=VS:SetComponentMaterial'''
    return BOOLEAN

def GetCompAltSecFillCl(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompAltSecFillCl
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompAltSecFillCl/ja
    \nオブジェクトの構成要素の切り替え位置の面の前景色/背景色を取得します。'''
    return (BOOLEAN, alternateSectionFillForeColor, alternateSectionFillBackColor)

def GetComponentNetVolume(obj, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponentNetVolume
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetComponentNetVolume/ja
    \n図形の構成要素の正味の体積を取得します。'''
    return REAL

def SetCompABoundEOffOff(object, componentIndex, autoBoundEdgeOffsetOffset):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompABoundEOffOff
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompABoundEOffOff/ja
    \n図形の構成要素に自動設定される境界の辺のオフセットを設定します。'''
    return BOOLEAN

def SetComponentName(obj, componentIndex, componentName):
    '''https://developer.vectorworks.net/index.php?title=VS:SetComponentName
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetComponentName/ja
    \nハンドルで指定した壁の、指定した番号の構成要素の名前を設定します。ハンドルがNILならば、この関数はデフォルト壁スタイルに作用します。'''
    return BOOLEAN

def GetCompAutoJoinCap(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompAutoJoinCap
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompAutoJoinCap/ja
    \nオブジェクトの構成要素を常に突合わせ結合モードで自動結合させるかどうかのフラグを取得します。'''
    return (BOOLEAN, alwaysAutoJoinInCappedJoinMode)

def GetComponentPenColors(obj, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponentPenColors
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetComponentPenColors/ja
    \nハンドルで指定した壁の、指定した番号の構成要素から線の色を取得します。ハンドルがNILならば、この関数はデフォルト壁スタイルに作用します。'''
    return (BOOLEAN, leftPenForeColor, leftPenBackColor, rightPenForeColor, rightPenBackColor)

def SetCompAltSecFill(object, componentIndex, alternateSectionFill):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompAltSecFill
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompAltSecFill/ja
    \nオブジェクトの構成要素の切り替え位置の面のスタイルを設定します。'''
    return BOOLEAN

def SetComponentPenColors(obj, componentIndex, leftPenForeColor, leftPenBackColor, rightPenForeColor, rightPenBackColor):
    '''https://developer.vectorworks.net/index.php?title=VS:SetComponentPenColors
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetComponentPenColors/ja
    \nハンドルで指定した壁の、指定した番号の構成要素の線の色を設定します。ハンドルがNILならば、この関数はデフォルト壁スタイルに作用します。'''
    return BOOLEAN

def GetCompBotIsRelStory(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompBotIsRelStory
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompBotIsRelStory/ja
    \n壁の構成要素の下端がストーリを基準にしているかどうかを返します。'''
    return (BOOLEAN, bottomIsRelativeToStory)

def GetComponentPenStyles(obj, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponentPenStyles
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetComponentPenStyles/ja
    \nハンドルで指定した壁で、指定した番号の構成要素から左右の線の種類を取得します。ハンドルがNILならば、デフォルト壁スタイルの値を取得します。'''
    return (BOOLEAN, leftPenStyle, rightPenStyle)

def SetCompAltSecFillCl(object, componentIndex, alternateSectionFillForeColor, alternateSectionFillBackColor):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompAltSecFillCl
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompAltSecFillCl/ja
    \nオブジェクトの構成要素の切り替え位置の面の前景色/背景色を設定します。'''
    return BOOLEAN

def SetComponentPenStyles(obj, componentIndex, leftPenStyle, rightPenStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetComponentPenStyles
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetComponentPenStyles/ja
    \nハンドルで指定した壁で、指定した番号の構成要素の左右の線の種類を設定します。ハンドルがNILならば、デフォルト壁スタイルに作用します。'''
    return BOOLEAN

def GetCompBoundOffset(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompBoundOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompBoundOffset/ja
    \nオブジェクトの構成要素の境界のオフセットを取得します。'''
    return (BOOLEAN, boundOffset)

def GetComponentPenWeights(obj, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponentPenWeights
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetComponentPenWeights/ja
    \nハンドルで指定した壁で、指定した番号の構成要素から左右の線の太さを取得します。ハンドルがNILならば、デフォルト壁スタイルに作用します。'''
    return (BOOLEAN, leftPenWeight, rightPenWeight)

def SetCompAutoJoinCap(object, componentIndex, alwaysAutoJoinInCappedJoinMode):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompAutoJoinCap
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompAutoJoinCap/ja
    \nオブジェクトの構成要素を常に突合わせ結合モードで自動結合させるかどうかのフラグを設定します。'''
    return BOOLEAN

def SetComponentPenWeights(obj, componentIndex, leftPenWeight, rightPenWeight):
    '''https://developer.vectorworks.net/index.php?title=VS:SetComponentPenWeights
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetComponentPenWeights/ja
    \nハンドルで指定した壁で、指定した番号の構成要素の左右の線の太さを設定します。ハンドルがNILならば、デフォルト壁スタイルに作用します。'''
    return BOOLEAN

def GetCompDatTopOfComp(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompDatTopOfComp
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompDatTopOfComp/ja
    \nオブジェクトの構成要素の基準面が構成要素の上端かどうかのフラグを取得します。'''
    return (BOOLEAN, datumIsTopOfComponent)

def GetComponentTexture(obj, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponentTexture
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetComponentTexture/ja
    \n図形の構成要素のテクスチャを取得します。'''
    return (BOOLEAN, texture)

def SetCompBotIsRelStory(object, componentIndex, bottomIsRelativeToStory):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompBotIsRelStory
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompBotIsRelStory/ja
    \n構成要素の下端をストーリを基準にするかどうか設定します。'''
    return BOOLEAN

def SetComponentTexture(obj, componentIndex, texture):
    '''https://developer.vectorworks.net/index.php?title=VS:SetComponentTexture
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetComponentTexture/ja
    \n図形の構成要素のテクスチャを設定します。'''
    return BOOLEAN

def GetCompInsertLoc(object):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompInsertLoc'''
    return INTEGER

def GetComponentUseFillClassAttr(obj, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponentUseFillClassAttr
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetComponentUseFillClassAttr/ja
    \nハンドルで指定した壁の、指定した番号の構成要素で面の模様で、クラス属性を使用しているかどうかを返します。ハンドルがNILならば、この関数はデフォルト壁スタイルに作用します。'''
    return (BOOLEAN, useFillClassAttributes)

def SetCompBoundOffset(object, componentIndex, boundOffset):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompBoundOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompBoundOffset/ja
    \nオブジェクトの構成要素の境界のオフセットを設定します。'''
    return BOOLEAN

def SetComponentUseFillClassAttr(obj, componentIndex, useFillClassAttributes):
    '''https://developer.vectorworks.net/index.php?title=VS:SetComponentUseFillClassAttr
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetComponentUseFillClassAttr/ja
    \nハンドルで指定した壁の、指定した番号の構成要素の面の模様に、クラス属性を設定します。ハンドルがNILならば、この関数はデフォルト壁スタイルに作用します。'''
    return BOOLEAN

def GetCompInsertLocOff(object):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompInsertLocOff'''
    return REAL

def GetComponentUsePenClassAttr(obj, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponentUsePenClassAttr
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetComponentUsePenClassAttr/ja
    \nハンドルで指定した壁の、指定した番号の構成要素で左右の線種で、クラス属性を使用しているかどうかを返します。ハンドルがNILならば、この関数はデフォルト壁スタイルに作用します。'''
    return (BOOLEAN, useLeftPenClassAttributes, useRightPenClassAttributes)

def SetCompDatTopOfComp(object, componentIndex, datumIsTopOfComponent):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompDatTopOfComp
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompDatTopOfComp/ja
    \nオブジェクトの構成要素の基準面が構成要素の上端かどうかのフラグを設定します。'''
    return BOOLEAN

def SetComponentUsePenClassAttr(obj, componentIndex, useLeftPenClassAttributes, useRightPenClassAttributes):
    '''https://developer.vectorworks.net/index.php?title=VS:SetComponentUsePenClassAttr
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetComponentUsePenClassAttr/ja
    \nハンドルで指定した壁の、指定した番号の構成要素の構成要素の左右の線種に、クラス属性を設定します。ハンドルがNILならば、この関数はデフォルト壁スタイルに作用します。'''
    return BOOLEAN

def GetCompManualBound(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompManualBound
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompManualBound/ja
    \nオブジェクトの構成要素の手動境界を取得します。'''
    return (BOOLEAN, manualBound)

def GetComponentWallBottomOffset(obj, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponentWallBottomOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetComponentWallBottomOffset/ja
    \n図形の構成要素の壁の下端からのオフセットを取得します。'''
    return (BOOLEAN, offsetFromWallBottom)

def SetCompInsertLoc(object, insertLocation):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompInsertLoc'''
    return None

def SetComponentWallBottomOffset(obj, componentIndex, offsetFromWallBottom):
    '''https://developer.vectorworks.net/index.php?title=VS:SetComponentWallBottomOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetComponentWallBottomOffset/ja
    \n図形の構成要素の壁の下端からのオフセットを設定します。'''
    return BOOLEAN

def GetCompMasterSnaps(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompMasterSnaps
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompMasterSnaps/ja
    \nオブジェクトの構成要素のマスタースナップを取得します。'''
    return (BOOLEAN, masterSnapOnLeft, masterSnapOnRight)

def GetComponentWallTopOffset(obj, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponentWallTopOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetComponentWallTopOffset/ja
    \n図形の構成要素の壁の上端からのオフセットを取得します。'''
    return (BOOLEAN, offsetFromWallTop)

def SetCompInsertLocOff(object, insertLocationOffset):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompInsertLocOff'''
    return None

def SetComponentWallTopOffset(obj, componentIndex, offsetFromWallTop):
    '''https://developer.vectorworks.net/index.php?title=VS:SetComponentWallTopOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetComponentWallTopOffset/ja
    \n図形の構成要素の壁の上端からのオフセットを設定します。'''
    return BOOLEAN

def GetCompPenStylesN(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompPenStylesN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompPenStylesN/ja
    \nオブジェクトの構成要素の線のスタイルを取得します。'''
    return (BOOLEAN, leftPenStyle, rightPenStyle)

def GetComponentWidth(obj, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponentWidth
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetComponentWidth/ja
    \nハンドルで指定した壁で、指定した番号の構成要素から幅を取得します。ハンドルがNILならば、デフォルト壁スタイルに作用します。'''
    return (BOOLEAN, width)

def SetCompManualBound(object, componentIndex, manualBound):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompManualBound
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompManualBound/ja
    \nオブジェクトの構成要素の手動境界を設定します。'''
    return BOOLEAN

def SetComponentWidth(obj, componentIndex, width):
    '''https://developer.vectorworks.net/index.php?title=VS:SetComponentWidth
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetComponentWidth/ja
    \nハンドルで指定した壁で、指定した番号の構成要素の幅を設定します。ハンドルがNILならば、デフォルト壁スタイルに作用します。'''
    return BOOLEAN

def GetCompSecFillChgPt(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompSecFillChgPt
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompSecFillChgPt/ja
    \nオブジェクトの構成要素の壁結合時の切り替え位置を取得します。'''
    return (BOOLEAN, wallAssociatedSectionFillChangePoint)

def GetComponents(object):
    '''https://developer.vectorworks.net/index.php?title=VS:GetComponents
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetComponents/ja
    \n図形の構成要素のハンドルを返します。'''
    return HANDLE

def SetCompMasterSnaps(object, componentIndex, masterSnapOnLeft, masterSnapOnRight):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompMasterSnaps
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompMasterSnaps/ja
    \nオブジェクトの構成要素のマスタースナップを設定します。'''
    return BOOLEAN

def SetCoreWallComponent(obj, coreWallComponent):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCoreWallComponent
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCoreWallComponent/ja
    \n壁、円弧壁、壁スタイル、壁設定のコアを設定します。'''
    return None

def GetCompTopIsRelStory(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompTopIsRelStory
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompTopIsRelStory/ja
    \n壁の構成要素の上端がストーリを基準にしているかどうかを返します。'''
    return (BOOLEAN, topIsRelativeToStory)

def GetCoreWallComponent(obj):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCoreWallComponent
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCoreWallComponent/ja
    \n壁の構成要素の中のコア指定されている番号を返します。'''
    return INTEGER

def SetCompPenStylesN(object, componentIndex, leftPenStyle, rightPenStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompPenStylesN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompPenStylesN/ja
    \nオブジェクトの構成要素の線のスタイルを設定します。'''
    return BOOLEAN

def SetDatumRoofComp(object, datumRoofComponent):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDatumRoofComp
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDatumRoofComp/ja
    \n図形の構成要素の屋根基準面を設定します。'''
    return None

def GetCompUseClassASF(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompUseClassASF
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompUseClassASF/ja
    \nオブジェクトの構成要素の切り替え位置の面にクラス属性のスタイルを使用しているかどうかのフラグを取得します。'''
    return (BOOLEAN, useClassFillStyleForAlternateSectionFill)

def GetDatumRoofComp(object):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDatumRoofComp
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDatumRoofComp/ja
    \n図形の構成要素の屋根基準面を取得します。'''
    return INTEGER

def SetCompSecFillChgPt(object, componentIndex, wallAssociatedSectionFillChangePoint):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompSecFillChgPt
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompSecFillChgPt/ja
    \nオブジェクトの構成要素の壁結合時の切り替え位置を設定します。'''
    return BOOLEAN

def SetDatumSlabComponent(obj, datumSlabComponent):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDatumSlabComponent
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDatumSlabComponent/ja
    \n図形の構成要素のスラブ基準面を設定します。.'''
    return None

def GetCompUseClassASFCl(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompUseClassASFCl
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompUseClassASFCl/ja
    \nオブジェクトの構成要素の切り替え位置の面にクラス属性の色を使用しているかどうかのフラグを取得します。'''
    return (BOOLEAN, useClassFillColorsForAlternateSectionFill)

def GetDatumSlabComponent(obj):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDatumSlabComponent
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDatumSlabComponent/ja
    \n図形の構成要素のスラブ基準面を取得します。'''
    return INTEGER

def SetCompTopIsRelStory(object, componentIndex, topIsRelativeToStory):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompTopIsRelStory
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompTopIsRelStory/ja
    \n構成要素の上端をストーリを基準にするかどうか設定します。'''
    return BOOLEAN

def SetDefGenStoryBound(format, boundType, boundStory, layerLevelType, offSet):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDefGenStoryBound
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDefGenStoryBound/ja
    \nkObjXPropSupportGenericStoryLevelプロパティを持つプラグインオブジェクトのデフォルトのストーリ高さ基準情報を設定します。'''
    return BOOLEAN

def GetCompUseClassFCl(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompUseClassFCl
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompUseClassFCl/ja
    \nオブジェクトの構成要素の面にクラス属性の面の色を使用しているかどうかのフラグを取得します。'''
    return (BOOLEAN, useClassFillColorsForFill)

def GetDefGenStoryBound(format):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDefGenStoryBound
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDefGenStoryBound/ja
    \nkObjXPropSupportGenericStoryLevelプロパティを持つプラグインオブジェクトのデフォルトのストーリ高さ基準情報を取得します。取得した高さ情報は関数の戻り値がTRUEのときのみ有効です。'''
    return (BOOLEAN, boundType, boundStory, layerLevelType, offset)

def SetCompUseClassASF(object, componentIndex, useClassFillStyleForAlternateSectionFill):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompUseClassASF
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompUseClassASF/ja
    \nオブジェクトの構成要素の切り替え位置の面にクラス属性のスタイルを使用するかどうかのフラグを設定します。'''
    return BOOLEAN

def SetInsertLocComp(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:SetInsertLocComp'''
    return None

def GetCompUseClassFill(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompUseClassFill
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompUseClassFill/ja
    \nオブジェクトの構成要素の面にクラス属性の面のスタイルを使用しているかどうかのフラグを取得します。'''
    return (BOOLEAN, useClassFillStyleForFill)

def GetInsertLocComp(object):
    '''https://developer.vectorworks.net/index.php?title=VS:GetInsertLocComp'''
    return INTEGER

def SetCompUseClassASFCl(object, componentIndex, useClassFillColorsForAlternateSectionFill):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompUseClassASFCl
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompUseClassASFCl/ja
    \nオブジェクトの構成要素の切り替え位置の面にクラス属性の色を使用するかどうかのフラグを設定します。'''
    return BOOLEAN

def SetObjectStoryBound(obj, boundID, boundType, boundStory, layerLevelType, offset):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjectStoryBound
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetObjectStoryBound/ja
    \nハンドルで指定した図形の高さ基準に関するデータを設定します。'''
    return None

def GetCompUseClassLPCl(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompUseClassLPCl
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompUseClassLPCl/ja
    \nオブジェクトの構成要素の線種（左側）にクラス属性の線の色を使用しているかどうかのフラグを取得します。'''
    return (BOOLEAN, useClassPenColorsForLeftPen)

def GetNumberOfComponents(obj):
    '''https://developer.vectorworks.net/index.php?title=VS:GetNumberOfComponents
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNumberOfComponents/ja
    \nハンドルで指定した壁の構成要素の数を取得します。ハンドルがNILならば、デフォルト壁スタイルに作用します。'''
    return (BOOLEAN, numComponents)

def SetCompUseClassFCl(object, componentIndex, useClassFillColorsForFill):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompUseClassFCl
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompUseClassFCl/ja
    \nオブジェクトの構成要素の面にクラス属性の面の色を使用するかどうかのフラグを設定します。'''
    return BOOLEAN

def SetRoofPrefStyle(roofStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetRoofPrefStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetRoofPrefStyle/ja
    \n屋根の設定の屋根スタイルを設定します。'''
    return None

def GetCompUseClassLPS(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompUseClassLPS
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompUseClassLPS/ja
    \nオブジェクトの構成要素の線種（左側）にクラス属性のスタイルを使用しているかどうかのフラグを取得します。'''
    return (BOOLEAN, useClassPenStyleForLeftPen)

def GetObjBoundElevation(obj, boundID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjBoundElevation
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetObjBoundElevation/ja
    \n指定した図形のあるレイヤの高さ基準の値を返します。'''
    return REAL

def SetCompUseClassFill(object, componentIndex, useClassFillStyleForFill):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompUseClassFill
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompUseClassFill/ja
    \nオブジェクトの構成要素の面にクラス属性の面のスタイルを使用するかどうかのフラグを設定します。'''
    return BOOLEAN

def SetSlabHeight(slab, height):
    '''https://developer.vectorworks.net/index.php?title=VS:SetSlabHeight
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetSlabHeight/ja
    \nスラブの高さを設定します。'''
    return None

def GetCompUseClassLPW(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompUseClassLPW
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompUseClassLPW/ja
    \nオブジェクトの構成要素の線種（左側）にクラス属性の線の太さを使用しているかどうかのフラグを取得します。'''
    return (BOOLEAN, useClassPenWeightForLeftPen)

def GetObjStoryBound(obj, boundID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjStoryBound
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetObjStoryBound/ja
    \nハンドルで指定した図形の高さ基準に関するデータを返します。'''
    return (BOOLEAN, boundType, boundStory, layerLevelType, offset)

def SetCompUseClassLPCl(object, componentIndex, useClassPenColorsForLeftPen):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompUseClassLPCl
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompUseClassLPCl/ja
    \nオブジェクトの構成要素の線種（左側）にクラス属性の線の色を使用するかどうかのフラグを設定します。'''
    return BOOLEAN

def SetSlabPreferencesStyle(slabStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetSlabPreferencesStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetSlabPreferencesStyle/ja
    \nスラブ設定のスラブスタイルを設定します。'''
    return None

def GetCompUseClassRPCl(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompUseClassRPCl
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompUseClassRPCl/ja
    \nオブジェクトの構成要素の線種（右側）にクラス属性の線の色を使用しているかどうかのフラグを取得します。'''
    return (BOOLEAN, useClassPenColorsForRightPen)

def GetObjStoryBoundsAt(obj, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjStoryBoundsAt
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetObjStoryBoundsAt/ja
    \nハンドルで指定した図形の高さ基準に関するデータを返します。'''
    return INTEGER

def SetCompUseClassLPS(object, componentIndex, useClassPenStyleForLeftPen):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompUseClassLPS
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompUseClassLPS/ja
    \nオブジェクトの構成要素の線種（左側）にクラス属性のスタイルを使用するかどうかのフラグを設定します。'''
    return BOOLEAN

def SetSlabStyle(slab, slabStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetSlabStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetSlabStyle/ja
    \nスラブのスラブスタイルを設定します。'''
    return None

def GetCompUseClassRPS(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompUseClassRPS
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompUseClassRPS/ja
    \nオブジェクトの構成要素の線種（右側）にクラス属性のスタイルを使用しているかどうかのフラグを取得します。'''
    return (BOOLEAN, useClassPenStyleForRightPen)

def GetObjStoryBoundsCnt(obj):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjStoryBoundsCnt
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetObjStoryBoundsCnt/ja
    \nハンドルで指定した図形に定義されたの高さ基準の個数を返します。'''
    return INTEGER

def SetCompUseClassLPW(object, componentIndex, useClassPenWeightForLeftPen):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompUseClassLPW
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompUseClassLPW/ja
    \nオブジェクトの構成要素の線種（左側）にクラス属性の線の太さを使用するかどうかのフラグを設定します。'''
    return BOOLEAN

def SetTaperedComponent(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTaperedComponent
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTaperedComponent/ja
    \n図形の構成要素にテーパを設定します。'''
    return None

def GetCompUseClassRPW(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompUseClassRPW
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompUseClassRPW/ja
    \nオブジェクトの構成要素の線種（右側）にクラス属性の線の太さを使用しているかどうかのフラグを取得します。'''
    return (BOOLEAN, useClassPenWeightForRightPen)

def GetRoofPrefStyle():
    '''https://developer.vectorworks.net/index.php?title=VS:GetRoofPrefStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetRoofPrefStyle/ja
    \n屋根の設定の屋根スタイルを取得します。'''
    return LONGINT

def SetCompUseClassRPCl(object, componentIndex, useClassPenColorsForRightPen):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompUseClassRPCl
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompUseClassRPCl/ja
    \nオブジェクトの構成要素の線種（右側）にクラス属性の線の色を使用するかどうかのフラグを設定します。'''
    return BOOLEAN

def SlabFromPoly(poly):
    '''https://developer.vectorworks.net/index.php?title=VS:SlabFromPoly
    \nhttps://developer.vectorworks.net/index.php?title=VS:SlabFromPoly/ja
    \nハンドルで指定した曲線からスラブを作成します。新しいスラブには現在のスラブ設定が適用されます。'''
    return None

def GetCompWallAssBound(object, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCompWallAssBound
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCompWallAssBound/ja
    \nオブジェクトの構成要素の壁結合時の端部の境界を取得します。'''
    return (BOOLEAN, wallAssociatedBound)

def GetRoofPreferences():
    '''https://developer.vectorworks.net/index.php?title=VS:GetRoofPreferences
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetRoofPreferences/ja
    \n屋根の設定を取得します。これは構成要素関連のコールやスタイル選択と共に使用することができます。'''
    return HANDLE

def SetCompUseClassRPS(object, componentIndex, useClassPenStyleForRightPen):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCompUseClassRPS
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCompUseClassRPS/ja
    \nオブジェクトの構成要素の線種（右側）にクラス属性のスタイルを使用するかどうかのフラグを設定します。'''
    return BOOLEAN

def SyncMatrixToBound(obj, BoundID):
    '''https://developer.vectorworks.net/index.php?title=VS:SyncMatrixToBound
    \nhttps://developer.vectorworks.net/index.php?title=VS:SyncMatrixToBound/ja
    \n指定したストーリの高さ基準とオブジェクトのマトリックスを同期させます。'''
    return None

def AddObjectTo2DComp(objectHandle, objToAddHandle, component):
    '''https://developer.vectorworks.net/index.php?title=VS:AddObjectTo2DComp'''
    return BOOLEAN

def GetHorizSecCPByStyle(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:GetHorizSecCPByStyle'''
    return BOOLEAN

def GetWallInsertLocOff(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallInsertLocOff'''
    return REAL

def SetHorizSecCutPlane(hObject, objectCutPlane):
    '''https://developer.vectorworks.net/index.php?title=VS:SetHorizSecCutPlane'''
    return BOOLEAN

def AddToPIOStyleEdit(hObj, keyName, editType, displayName):
    '''https://developer.vectorworks.net/index.php?title=VS:AddToPIOStyleEdit'''
    return BOOLEAN

def GetHorizSecCutPlane(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:GetHorizSecCutPlane'''
    return INTEGER

def GetWallRecessGroup(objectHand):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallRecessGroup'''
    return HANDLE

def SetMirrorEmpty2DComp(objectHandle, doMirror):
    '''https://developer.vectorworks.net/index.php?title=VS:SetMirrorEmpty2DComp'''
    return BOOLEAN

def CreateCustomObject(objectName, p, rotationAngle):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateCustomObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateCustomObject/ja
    \n位置と角度を指定してプラグインオブジェクトを配置し、そのハンドルを返します。'''
    return HANDLE

def GetLocalizedPluginChoice(inPluginName, inParameterName, inChoiceIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLocalizedPluginChoice
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLocalizedPluginChoice/ja
    \nプラグイン、パラメータの名前、メニュー項目番号からローカライズ後の名前を返します。'''
    return (BOOLEAN, outChoice)

def GetWllHoleObjIgnClsr(object):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWllHoleObjIgnClsr'''
    return BOOLEAN

def SetMrEm2DCompByStyle(hObject, byStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetMrEm2DCompByStyle'''
    return BOOLEAN

def CreateCustomObjectN(objectName, p, rotationAngle, showPref):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateCustomObjectN
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateCustomObjectN/ja
    \n位置と角度を指定してプラグインオブジェクトを作成し、そのハンドルを返します。また、設定ダイアログの表示／非表示を設定できます。'''
    return HANDLE

def GetLocalizedPluginName(inPluginName):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLocalizedPluginName
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLocalizedPluginName/ja
    \nプラグインの名前からローカライズ後の名前を返します。'''
    return (BOOLEAN, outName)

def GtExWllClsrFrmStBStl(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:GtExWllClsrFrmStBStl'''
    return BOOLEAN

def SetParamStyleType(hStyle, paramName, styleType):
    '''https://developer.vectorworks.net/index.php?title=VS:SetParamStyleType
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetParamStyleType/ja'''
    return INTEGER

def CreateCustomObjectPath(objectName, path, profileGroup):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateCustomObjectPath
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateCustomObjectPath/ja
    \nパスを用いたプラグインオブジェクトを作成し、そのハンドルを返します。'''
    return HANDLE

def GetLocalizedPluginParameter(inPluginName, inParameterName):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLocalizedPluginParameter
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLocalizedPluginParameter/ja
    \nプラグイン、パラメータの名前からローカライズ後の名前を返します。'''
    return (BOOLEAN, outParameter)

def HasPlugin(itemUniversalName):
    '''https://developer.vectorworks.net/index.php?title=VS:HasPlugin
    \nhttps://developer.vectorworks.net/index.php?title=VS:HasPlugin/ja
    \nツールアイテムやメニューコマンドがアクティブな作業画面に存在している場合は、そのパレットやメニューの名前とTRUEを返します。'''
    return (BOOLEAN, PaletteName)

def SetParameterVisibility(inPlugin, inParameterName, inSetVisible):
    '''https://developer.vectorworks.net/index.php?title=VS:SetParameterVisibility
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetParameterVisibility/ja
    \nプラグインのパラメータに連動している編集可能なアイテムの表示／非表示を設定します。'''
    return None

def CreateGroupOutline(objectHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateGroupOutline
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateGroupOutline/ja
    \nグループの外郭に相当する多角形のハンドルを返します。'''
    return HANDLE

def GetMirrorEmpty2DComp(objectHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetMirrorEmpty2DComp'''
    return BOOLEAN

def IsCatalogParameter(hObj, paramName):
    '''https://developer.vectorworks.net/index.php?title=VS:IsCatalogParameter'''
    return BOOLEAN

def SetPartDataID(objectHandle, dataID):
    '''https://developer.vectorworks.net/index.php?title=VS:SetPartDataID'''
    return None

def DefineCustomObj(pluginName, prefWhen):
    '''https://developer.vectorworks.net/index.php?title=VS:DefineCustomObj
    \nhttps://developer.vectorworks.net/index.php?title=VS:DefineCustomObj/ja
    \n与えられたプラグイン名、設定に対して GS_DefineCustomObject を呼ぶ。'''
    return HANDLE

def GetMrEm2DCompByStyle(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:GetMrEm2DCompByStyle'''
    return BOOLEAN

def IsNewCustomObject(objectName):
    '''https://developer.vectorworks.net/index.php?title=VS:IsNewCustomObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsNewCustomObject/ja
    \n指定した名前のプラグインオブジェクトが最初に生成された場合はTRUEを返します。'''
    return BOOLEAN

def SetPartInstanceName(objectHandle, uniqueInstanceName):
    '''https://developer.vectorworks.net/index.php?title=VS:SetPartInstanceName'''
    return None

def EnableParameter(inPlugin, inParameterName, inSetEnabled):
    '''https://developer.vectorworks.net/index.php?title=VS:EnableParameter
    \nhttps://developer.vectorworks.net/index.php?title=VS:EnableParameter/ja
    \nプラグインのパラメータに連動している編集可能なアイテムの動作を設定します。'''
    return None

def GetParamStyleType(hStyle, paramName):
    '''https://developer.vectorworks.net/index.php?title=VS:GetParamStyleType
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetParamStyleType/ja
    \nプラグインスタイル定義から指定したパラメータがスタイルの値を使用するかインスタンスの値を使用するかを返します。'''
    return INTEGER

def IsObjectTaggedAsPart(objectHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:IsObjectTaggedAsPart'''
    return BOOLEAN

def SetPluginStyle(hObject, styleName):
    '''https://developer.vectorworks.net/index.php?title=VS:SetPluginStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetPluginStyle/ja
    \nプラグインオブジェクトにスタイルを設定します。'''
    return BOOLEAN

def FlipHybMatrixObj(ioHybMatObj, inFlipSpecifier):
    '''https://developer.vectorworks.net/index.php?title=VS:FlipHybMatrixObj
    \nhttps://developer.vectorworks.net/index.php?title=VS:FlipHybMatrixObj/ja
    \ninFlipSpecifier = 0 ならば flipH、 inFlipSpecifier = 1 ならば FlipV'''
    return None

def GetPartDataID(objectHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPartDataID'''
    return LONGINT

def IsPluginFormat(theFormat):
    '''https://developer.vectorworks.net/index.php?title=VS:IsPluginFormat
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsPluginFormat/ja
    \nレコードフォーマットがプラグインオブジェクト、プラグインツール、プラグインメニューのパラメータに使われている／いないを返します。'''
    return BOOLEAN

def SetTopPlan2DComp(objectHandle, component):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTopPlan2DComp'''
    return BOOLEAN

def Generate2DFrom3DComp(objectHandle, component, renderMode, levelOfDetail):
    '''https://developer.vectorworks.net/index.php?title=VS:Generate2DFrom3DComp'''
    return BOOLEAN

def GetPartInstanceName(objectHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPartInstanceName'''
    return STRING

def NumCustomObjectChoices(objectName, parameterName):
    '''https://developer.vectorworks.net/index.php?title=VS:NumCustomObjectChoices
    \nhttps://developer.vectorworks.net/index.php?title=VS:NumCustomObjectChoices/ja
    \nプラグイン、パラメータの名前からメニュー項目の数を返します。'''
    return INTEGER

def SetTpPl2DCompByStyle(hObject, byStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTpPl2DCompByStyle'''
    return BOOLEAN

def Get2DCompByStyle(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:Get2DCompByStyle'''
    return BOOLEAN

def GetPartTypeInfo(objectHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPartTypeInfo'''
    return (BOOLEAN, partTypeName, dataID, uniqueInstanceName)

def RemovePIOStyleEdit(hObj, keyName):
    '''https://developer.vectorworks.net/index.php?title=VS:RemovePIOStyleEdit'''
    return BOOLEAN

def SetUseWallClosure(hObject, useWallClosure):
    '''https://developer.vectorworks.net/index.php?title=VS:SetUseWallClosure'''
    return BOOLEAN

def Get2DCompLocation(hObject, component):
    '''https://developer.vectorworks.net/index.php?title=VS:Get2DCompLocation'''
    return (onBoundsCube, offset)

def GetPartTypeName(objectHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPartTypeName'''
    return STRING

def RemovePartTag(objectHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:RemovePartTag'''
    return BOOLEAN

def SetUseWllClsrByStyle(hObject, byStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetUseWllClsrByStyle'''
    return BOOLEAN

def Get2DComponentGroup(objectHandle, component):
    '''https://developer.vectorworks.net/index.php?title=VS:Get2DComponentGroup'''
    return HANDLE

def GetPluginChoiceIndex(inPluginName, inParameterName, inChoiceName):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPluginChoiceIndex
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPluginChoiceIndex/ja
    \nプラグイン、パラメータ、メニュー項目の名前からメニュー項目番号を返します。'''
    return (BOOLEAN, outIndex)

def SelectPluginCatalog(hSymbol):
    '''https://developer.vectorworks.net/index.php?title=VS:SelectPluginCatalog'''
    return BOOLEAN

def SetVertSecCPByStyle(hObject, byStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVertSecCPByStyle'''
    return BOOLEAN

def GetCatalogItem(hObj):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCatalogItem'''
    return BOOLEAN

def GetPluginInfo():
    '''https://developer.vectorworks.net/index.php?title=VS:GetPluginInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPluginInfo/ja
    \n実行されているプラグインの名前とレコードのハンドルを返します。'''
    return (BOOLEAN, pluginName, recordHand)

def Set2DCompByStyle(hObject, byStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:Set2DCompByStyle'''
    return BOOLEAN

def SetVertSecCutPlane(hObject, objectCutPlane):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVertSecCutPlane'''
    return BOOLEAN

def GetCatalogPath(inhObject):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCatalogPath'''
    return (BOOLEAN, outFolderSpec, outRelativePath)

def GetPluginString(stringIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPluginString
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPluginString/ja
    \n索引番号で指定された文字列を返します。文字列は「プラグインコマンド編集」ダイアログの「ストリング...」ボタンをクリックすると作成できます。'''
    return STRING

def Set2DCompLocation(hObject, component, onBoundsCube, offset):
    '''https://developer.vectorworks.net/index.php?title=VS:Set2DCompLocation'''
    return BOOLEAN

def SetWInsLocOffByStyle(hObject, byStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWInsLocOffByStyle'''
    return BOOLEAN

def GetClassByStyle(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClassByStyle'''
    return BOOLEAN

def GetPluginStyle(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPluginStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPluginStyle/ja
    \nオブジェクトのプラグインスタイルの名前を取得します。'''
    return STRING

def Set2DComponentGroup(objectHandle, groupHandle, component):
    '''https://developer.vectorworks.net/index.php?title=VS:Set2DComponentGroup'''
    return BOOLEAN

def SetWallClosureGroup(objectHandle, closureHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWallClosureGroup'''
    return BOOLEAN

def GetCustomFeedback(ParametricHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCustomFeedback
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCustomFeedback/ja
    \n画面上の表示にのみ使用されているパラメトリック図形に連結している図形グループを返します。このグループは取り出しやプリントはされません。'''
    return (Boolean, FeedbackGroup)

def GetPluginStyleSymbol(hObject, hSymDef):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPluginStyleSymbol
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPluginStyleSymbol/ja
    \nオブジェクトに割り当てられたプラグインスタイルを定義しているシンボルのハンドルを返します。'''
    return (BOOLEAN, hSymDef)

def SetAllStyleParams(hStyle, styleType):
    '''https://developer.vectorworks.net/index.php?title=VS:SetAllStyleParams
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetAllStyleParams/ja'''
    return None

def SetWallInsLocByStyle(hObject, byStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWallInsLocByStyle'''
    return BOOLEAN

def GetCustomObjSecPath(objectHand):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCustomObjSecPath'''
    return HANDLE

def GetTopPlan2DComp(objectHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTopPlan2DComp'''
    return INTEGER

def SetClassByStyle(hObject, byStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClassByStyle'''
    return BOOLEAN

def SetWallInsertLoc(hObject, insertLocation):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWallInsertLoc'''
    return BOOLEAN

def GetCustomObjectChoice(objectName, parameterName, choiceIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCustomObjectChoice
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCustomObjectChoice/ja
    \nプラグイン、パラメータの名前、メニュー項目番号からメニュー項目の名前を返します。'''
    return STRING

def GetTpPl2DCompByStyle(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTpPl2DCompByStyle'''
    return BOOLEAN

def SetCustomFeedback(ParametricHandle, FeedbackGroup):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCustomFeedback
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCustomFeedback/ja
    \n画面上の表示にのみ使用されているパラメトリック図形のグループを連結します。このグループは取り出しやプリントはされません。'''
    return Boolean

def SetWallInsertLocOff(hObject, insertLocationOffset):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWallInsertLocOff'''
    return BOOLEAN

def GetCustomObjectColor(objectHand, inTagID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCustomObjectColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCustomObjectColor/ja
    \nSetCustomObjectColorで設定され「objectHand」に設定されている色を返します。色はinTagIDに保持されます。'''
    return (BOOLEAN, outColorIndex)

def GetUseWallClosure(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:GetUseWallClosure'''
    return BOOLEAN

def SetCustomObjectColor(objectHand, inTagID, inColoIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCustomObjectColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCustomObjectColor/ja
    \n「objectHand」に色を保管/設定します。GetCustomObjectColorを使ってこの色を使用できます。色はinTagIDに保持されます。'''
    return BOOLEAN

def SetWallRecessGroup(objectHand, geometryGroup):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWallRecessGroup'''
    return None

def GetCustomObjectInfo():
    '''https://developer.vectorworks.net/index.php?title=VS:GetCustomObjectInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCustomObjectInfo/ja
    \nプラグインオブジェクトのソースコード内で利用され、そのプラグインオブジェクトの情報を返します。オブジェクトが壊れている場合にのみ、FALSEを返します。'''
    return (BOOLEAN, objectName, objectHand, recordHand, wallHand)

def GetUseWllClsrByStyle(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:GetUseWllClsrByStyle'''
    return BOOLEAN

def SetCustomObjectPath(objectHand, path):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCustomObjectPath
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCustomObjectPath/ja
    \nハンドルで指定したプラグインオブジェクトのパス図形を設定します。'''
    return BOOLEAN

def SetWllHoleObjIgnClsr(object, ignoreClosure):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWllHoleObjIgnClsr'''
    return None

def GetCustomObjectPath(objectHand):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCustomObjectPath
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCustomObjectPath/ja
    \nハンドルで指定したプラグインオブジェクトのパス図形のハンドルを返します。'''
    return HANDLE

def GetVertSecCPByStyle(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVertSecCPByStyle'''
    return BOOLEAN

def SetCustomObjectProfileGroup(objectHand, profileGroupHand):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCustomObjectProfileGroup
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCustomObjectProfileGroup/ja
    \nハンドルで指定したプラグインオブジェクトの輪郭図形のハンドルを設定します。'''
    return BOOLEAN

def StExWllClsrFrmStBStl(hObject, byStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:StExWllClsrFrmStBStl'''
    return BOOLEAN

def GetCustomObjectProfileGroup(objectHand):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCustomObjectProfileGroup
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCustomObjectProfileGroup/ja
    \nハンドルで指定したプラグインオブジェクトの輪郭図形のハンドルを返します。'''
    return HANDLE

def GetVertSecCutPlane(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVertSecCutPlane'''
    return INTEGER

def SetCustomObjectSelectionGroup(objectHand, selGroup):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCustomObjectSelectionGroup
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCustomObjectSelectionGroup/ja
    \nハンドルで指定したプラグインオブジェクトが選択された際に、強調表示する形状を設定します。'''
    return BOOLEAN

def TagSubObjectAsPart(objectHandle, partTypeName, dataID, instanceName):
    '''https://developer.vectorworks.net/index.php?title=VS:TagSubObjectAsPart'''
    return None

def GetCustomObjectSelectionGroup(objectHand):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCustomObjectSelectionGroup
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCustomObjectSelectionGroup/ja
    \nグループのハンドルを返します。このグループには、パラメータで指定したプラグインオブジェクトが選択された際に、強調表示する形状が含まれています。'''
    return HANDLE

def GetWInsLocOffByStyle(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWInsLocOffByStyle'''
    return BOOLEAN

def SetCustomObjectWallHoleGroup(objectHand, holeGroup):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCustomObjectWallHoleGroup
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCustomObjectWallHoleGroup/ja
    \nハンドルで指定したプラグインオブジェクトが壁に挿入された際に、壁に作られる開口部の形状を設定します。'''
    return BOOLEAN

def UpdateStyledObjects(styleName):
    '''https://developer.vectorworks.net/index.php?title=VS:UpdateStyledObjects
    \nhttps://developer.vectorworks.net/index.php?title=VS:UpdateStyledObjects/ja
    \n指定したスタイルのすべてのオブジェクトを更新します。'''
    return None

def GetCustomObjectWallHoleGroup(objectHand):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCustomObjectWallHoleGroup
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCustomObjectWallHoleGroup/ja
    \nグループのハンドルを返します。このグループには、パラメータで指定したプラグインオブジェクトが壁に挿入された際に、壁に作られる開口部を定義するする形状が含まれています。'''
    return HANDLE

def GetWallClosureGroup(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallClosureGroup'''
    return HANDLE

def SetDisplayWith2DComp(objectHandle, component, isVisible):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDisplayWith2DComp'''
    return BOOLEAN

def GetDisplayWith2DComp(objectHandle, component):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDisplayWith2DComp'''
    return BOOLEAN

def GetWallInsLocByStyle(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallInsLocByStyle'''
    return BOOLEAN

def SetExWllClsrFrmSt(hObject, left, right, top, bottom):
    '''https://developer.vectorworks.net/index.php?title=VS:SetExWllClsrFrmSt'''
    return BOOLEAN

def GetExWllClsrFrmSt(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:GetExWllClsrFrmSt'''
    return (left, right, top, bottom)

def GetWallInsertLoc(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallInsertLoc'''
    return INTEGER

def SetHorizSecCPByStyle(hObject, byStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetHorizSecCPByStyle'''
    return BOOLEAN

def AddVPAnnotationObject(viewportHandle, annotationHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:AddVPAnnotationObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddVPAnnotationObject/ja
    \n指定したビューポートに指定した注釈を追加します。'''
    return BOOLEAN

def GetVPClassVisibility(viewportHandle, className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPClassVisibility
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVPClassVisibility/ja
    \n指定したビューポートの指定したクラスの表示形式を返します。'''
    return (BOOLEAN, visibilityType)

def Group():
    '''https://developer.vectorworks.net/index.php?title=VS:Group
    \nhttps://developer.vectorworks.net/index.php?title=VS:Group/ja
    \nアクティブなレイヤ上の選択されている図形をグループ化します。'''
    return None

def SetVPCropObject(viewportHandle, cropHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVPCropObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetVPCropObject/ja
    \n指定したビューポートに指定した枠を設定します。新しい図形が枠図形として有効であれば、置き換えられます。'''
    return BOOLEAN

def BeginGroup():
    '''https://developer.vectorworks.net/index.php?title=VS:BeginGroup
    \nhttps://developer.vectorworks.net/index.php?title=VS:BeginGroup/ja
    \nこの手続きを実行した後、EndGroupが実行されるまでの間に作成された図形をグループ化します。'''
    return None

def GetVPCropObject(viewportHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPCropObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVPCropObject/ja
    \n指定したビューポートの枠のハンドルを返します。'''
    return HANDLE

def GroupToMesh(groupObj):
    '''https://developer.vectorworks.net/index.php?title=VS:GroupToMesh
    \nhttps://developer.vectorworks.net/index.php?title=VS:GroupToMesh/ja
    \nハンドルで指定したグループ図形をメッシュ図形に変換します。'''
    return HANDLE

def SetVPLayerVisibility(viewportHandle, layerHandle, visibilityType):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVPLayerVisibility
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetVPLayerVisibility/ja
    \n指定したビューポートの指定したレイヤの表示形式を設定します。'''
    return BOOLEAN

def BeginGroupN(groupHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:BeginGroupN
    \nhttps://developer.vectorworks.net/index.php?title=VS:BeginGroupN/ja
    \nグループのハンドルを指定し、既存のグループに図形を作成して追加します。nilに初期化されたハンドルを渡した場合は新しいグループが作成されます。'''
    return groupHandle

def GetVPGroup(viewportHandle, groupType):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPGroup
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVPGroup/ja
    \n指定したビューポートのグループの種類を返します。'''
    return HANDLE

def HUngroup(h):
    '''https://developer.vectorworks.net/index.php?title=VS:HUngroup
    \nhttps://developer.vectorworks.net/index.php?title=VS:HUngroup/ja
    \nハンドルで指定した図形をグループ解除します。'''
    return None

def Ungroup():
    '''https://developer.vectorworks.net/index.php?title=VS:Ungroup
    \nhttps://developer.vectorworks.net/index.php?title=VS:Ungroup/ja
    \nアクティブなレイヤ上の選択されている図形をグループ解除します。'''
    return None

def CreateVP(parentHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateVP
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateVP/ja
    \nビューポートを作成します。表示されているレイヤや、表示されているレイヤの中にあるグループのハンドルをコンテナのハンドルとして渡します。'''
    return HANDLE

def GetVPGroupParent(groupHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPGroupParent
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVPGroupParent/ja
    \n指定したビューポートグループのコンテナである、ビューポートのハンドルを返します。'''
    return HANDLE

def IsVPGroupContainedObject(objectHandle, groupType):
    '''https://developer.vectorworks.net/index.php?title=VS:IsVPGroupContainedObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsVPGroupContainedObject/ja
    \n指定した図形がビューポートグループに含まれている／いないを返します。'''
    return BOOLEAN

def UpdateVP(viewportHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:UpdateVP
    \nhttps://developer.vectorworks.net/index.php?title=VS:UpdateVP/ja
    \n指定したビューポートを更新します。ワイヤーフレームレンダリング以外は再度レンダリングが行われます。'''
    return None

def EndGroup():
    '''https://developer.vectorworks.net/index.php?title=VS:EndGroup
    \nhttps://developer.vectorworks.net/index.php?title=VS:EndGroup/ja
    \nBeginGroupを実行した後、この手続きを実行するまでの間に作成された図形をグループ化します。'''
    return None

def GetVPLayerVisibility(viewportHandle, layerHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPLayerVisibility
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVPLayerVisibility/ja
    \n指定したビューポートの指定したレイヤの表示形式を返します。'''
    return (BOOLEAN, visibilityType)

def SetVPClassVisibility(viewportHandle, className, visibilityType):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVPClassVisibility
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetVPClassVisibility/ja
    \n指定したビューポートの指定したクラスの表示形式を設定します。'''
    return BOOLEAN

def VPHasCropObject(viewportHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:VPHasCropObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:VPHasCropObject/ja
    \n指定したビューポートに枠が含まれている／いないを返します。'''
    return BOOLEAN

def ContainsLight(containerObject):
    '''https://developer.vectorworks.net/index.php?title=VS:ContainsLight
    \nhttps://developer.vectorworks.net/index.php?title=VS:ContainsLight/ja
    \nハンドルで指定したコンテナ（グループ、シンボル、レイヤ）内に光源が含まれている場合はTRUEを返します。'''
    return BOOLEAN

def GetLightColorRGB(light):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLightColorRGB
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLightColorRGB/ja
    \nハンドルで指定した光源の放射光の色成分を返します。'''
    return (red, green, blue)

def GetSpreadAngle(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetSpreadAngle
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSpreadAngle/ja
    \nハンドルで指定した光源（スポットライト）の拡散光の角度を返します。'''
    return spreadAngleR

def SetLightDirection(h, panAngleR, tiltAngleR):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLightDirection
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLightDirection/ja
    \nハンドルで指定した光源のパン角度（パノラマ上の開き）と傾きを設定します。'''
    return None

def CreateLight(pXR, pYR, pZR, lightType, isOn, castShadow):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateLight
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateLight/ja
    \n座標を指定して光源を作成し、そのハンドルを返します。'''
    return HANDLE

def GetLightDirection(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLightDirection
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLightDirection/ja
    \nハンドルで指定した光源の、パン角度（パノラマ上の開き）と傾きを返します。'''
    return (panAngleR, tiltAngleR)

def SetBeamAngle(h, beamAngleR):
    '''https://developer.vectorworks.net/index.php?title=VS:SetBeamAngle
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetBeamAngle/ja
    \nハンドルで指定した光源（スポットライト）の光束の角度を設定します。'''
    return None

def SetLightFalloff(light, distFalloff, angFalloff):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLightFalloff
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLightFalloff/ja
    \nハンドルで指定した光源の、減衰距離と減衰角度を設定します。'''
    return None

def GetBeamAngle(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetBeamAngle
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetBeamAngle/ja
    \nハンドルで指定した光源（スポットライト）の光束の角度を返します。'''
    return beamAngleR

def GetLightFalloff(light):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLightFalloff
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLightFalloff/ja
    \nハンドルで指定した光源の、減衰距離と減衰角度を返します。'''
    return (distFalloff, angFalloff)

def SetLayerAmbientColor(layer, red, green, blue):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLayerAmbientColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLayerAmbientColor/ja
    \nハンドルで指定したレイヤの背景放射光の色成分を設定します。値の範囲は0から65535までです。'''
    return None

def SetLightInfo(h, lightType, brightness, isOn, castShadow):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLightInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLightInfo/ja
    \nハンドルで指定した光源の情報を設定します。'''
    return None

def GetLayerAmbientColor(layer):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLayerAmbientColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLayerAmbientColor/ja
    \nハンドルで指定したレイヤの背景放射光の色成分を返します。値の範囲は0から65535までです。'''
    return (red, green, blue)

def GetLightInfo(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLightInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLightInfo/ja
    \nハンドルで指定した光源の情報を返します。'''
    return (lightType, brightness, isOn, castShadow)

def SetLayerAmbientInfo(layer, isOn, brightness):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLayerAmbientInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLayerAmbientInfo/ja
    \nハンドルで指定したレイヤの背景放射光の情報（スイッチ、明るさ）を設定します。'''
    return None

def SetLightLocation(h, p, zValue):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLightLocation
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLightLocation/ja
    \nハンドルで指定した光源の位置を設定します。'''
    return None

def GetLayerAmbientInfo(layer):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLayerAmbientInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLayerAmbientInfo/ja
    \nハンドルで指定したレイヤの背景放射光の情報（スイッチ、明るさ）を返します。'''
    return (isOn, brightness)

def GetLightLocation(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLightLocation
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLightLocation/ja
    \nハンドルで指定した光源の位置を座標で返します。'''
    return p

def SetLightColorRGB(light, red, green, blue):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLightColorRGB
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLightColorRGB/ja
    \nハンドルで指定した光源が放射する光の色を設定します。'''
    return None

def SetSpreadAngle(h, spreadAngleR):
    '''https://developer.vectorworks.net/index.php?title=VS:SetSpreadAngle
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetSpreadAngle/ja
    \nハンドルで指定した光源（スポットライト）の拡散光の角度を設定します。'''
    return None

def ConvertToNURBS(h, keepOrig):
    '''https://developer.vectorworks.net/index.php?title=VS:ConvertToNURBS
    \nhttps://developer.vectorworks.net/index.php?title=VS:ConvertToNURBS/ja
    \nハンドルで指定した図形をNURBS図形やNURBS図形のグループに変換します。'''
    return HANDLE

def EvaluateNurbsSurfacePointAndNormal(surfaceHandle, u, v):
    '''https://developer.vectorworks.net/index.php?title=VS:EvaluateNurbsSurfacePointAndNormal
    \nhttps://developer.vectorworks.net/index.php?title=VS:EvaluateNurbsSurfacePointAndNormal/ja
    \nU方向／V方向の値を指定してNURBS曲面上の頂点を決定します。'''
    return (BOOLEAN, point, normal)

def NurbsCurveType(objectHd, index):
    '''https://developer.vectorworks.net/index.php?title=VS:NurbsCurveType
    \nhttps://developer.vectorworks.net/index.php?title=VS:NurbsCurveType/ja
    \nハンドルで指定したNURBS曲線の、指定した辺の種類を返します。'''
    return isByFit

def NurbsSetKnot(objectHd, index1, index2, knot):
    '''https://developer.vectorworks.net/index.php?title=VS:NurbsSetKnot
    \nhttps://developer.vectorworks.net/index.php?title=VS:NurbsSetKnot/ja
    \nハンドルで指定したNURBS曲線／曲面の、指定した頂点の結び目を設定します。'''
    return None

def CreateInterpolatedSurface(surfaceHandle, numUPts, numVPts, uDegree, vDegree):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateInterpolatedSurface
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateInterpolatedSurface/ja
    \n度数と頂点数を指定して補間点によるNURBS曲面を作成します。'''
    return HANDLE

def ExtendNurbsCurve(curveHandle, distance, bStart, bLinear):
    '''https://developer.vectorworks.net/index.php?title=VS:ExtendNurbsCurve
    \nhttps://developer.vectorworks.net/index.php?title=VS:ExtendNurbsCurve/ja
    \n始点または終点からの距離を指定してNURBS曲線を延長します。直線状または曲率に沿って延長することができます。'''
    return HANDLE

def NurbsDegree(objectHd, index):
    '''https://developer.vectorworks.net/index.php?title=VS:NurbsDegree
    \nhttps://developer.vectorworks.net/index.php?title=VS:NurbsDegree/ja
    \nハンドルで指定したNURBS曲線／曲面の、指定した辺の角度を返します。'''
    return INTEGER

def NurbsSetPt3D(objectHd, index1, index2, p):
    '''https://developer.vectorworks.net/index.php?title=VS:NurbsSetPt3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:NurbsSetPt3D/ja
    \nハンドルで指定したNURBS曲線／曲面の、指定した頂点の座標を設定します。'''
    return None

def CreateLoftSurfaces(groupCurvesHd, bRule, bClose, bSolid):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateLoftSurfaces
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateLoftSurfaces/ja
    \n曲線の交点のグループに補間法を用いることでNURBS曲面を作成します。'''
    return HANDLE

def ExtendNurbsSurface(surfaceHandle, distance, bStart, bLinear, bUDir):
    '''https://developer.vectorworks.net/index.php?title=VS:ExtendNurbsSurface
    \nhttps://developer.vectorworks.net/index.php?title=VS:ExtendNurbsSurface/ja
    \nU方向やV方向の始点または終点までの距離を指定してNURBS曲面を延長します。'''
    return HANDLE

def NurbsDelVertex(objectHd, index1, index2):
    '''https://developer.vectorworks.net/index.php?title=VS:NurbsDelVertex
    \nhttps://developer.vectorworks.net/index.php?title=VS:NurbsDelVertex/ja
    \nハンドルで指定したNURBS曲線／曲面の、指定した頂点を消去します。'''
    return None

def NurbsSetWeight(objectHd, index1, index2, weight):
    '''https://developer.vectorworks.net/index.php?title=VS:NurbsSetWeight
    \nhttps://developer.vectorworks.net/index.php?title=VS:NurbsSetWeight/ja
    \nハンドルで指定したNURBS曲線／曲面の、指定した頂点の重みを設定します。'''
    return None

def CreateNurbsCurve(first, byCtrlPts, degree):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateNurbsCurve
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateNurbsCurve/ja
    \nNURBS曲線を作成します。'''
    return HANDLE

def GetNurbsObjectDistanceFromPoint(h, point):
    '''https://developer.vectorworks.net/index.php?title=VS:GetNurbsObjectDistanceFromPoint
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNurbsObjectDistanceFromPoint/ja
    \nNURBS図形と点の間の距離を返します。'''
    return (BOOLEAN, distance)

def NurbsGetNumPts(objectHd, index):
    '''https://developer.vectorworks.net/index.php?title=VS:NurbsGetNumPts
    \nhttps://developer.vectorworks.net/index.php?title=VS:NurbsGetNumPts/ja
    \nハンドルで指定したNURBS曲線／曲面の頂点数を返します。'''
    return LONGINT

def NurbsSurfaceEvalPt(objectHd, u, v):
    '''https://developer.vectorworks.net/index.php?title=VS:NurbsSurfaceEvalPt
    \nhttps://developer.vectorworks.net/index.php?title=VS:NurbsSurfaceEvalPt/ja
    \nハンドルで指定したNURBS曲面上の結び目u,vの座標を返します。'''
    return p

def CreateNurbsSurface(numUPts, numVPts, uDegree, vDegree):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateNurbsSurface
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateNurbsSurface/ja
    \nNURBS曲面を作成します。'''
    return HANDLE

def GetParameterOnNurbsCurve(h, point):
    '''https://developer.vectorworks.net/index.php?title=VS:GetParameterOnNurbsCurve
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetParameterOnNurbsCurve/ja
    \nNURBS曲線のハンドルと点から、点を投影して確定された点のパラメータを返します。この関数はまた、点が投影されたNURBS曲線の番号も返します。'''
    return (BOOLEAN, parameter, index)

def NurbsGetPt3D(objectHd, index1, index2):
    '''https://developer.vectorworks.net/index.php?title=VS:NurbsGetPt3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:NurbsGetPt3D/ja
    \nハンドルで指定したNURBS曲線／曲面の、指定した頂点の座標を返します。'''
    return p

def RevolveWithRail(profileH, railH, axisH):
    '''https://developer.vectorworks.net/index.php?title=VS:RevolveWithRail
    \nhttps://developer.vectorworks.net/index.php?title=VS:RevolveWithRail/ja
    \n輪郭を示す曲線を軸やパスに沿って回転させて、NURBS曲面またはNURBS曲面のグループを作成します。'''
    return HANDLE

def CreateOffsetNurbsObjectHandle(h, offsetDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateOffsetNurbsObjectHandle
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateOffsetNurbsObjectHandle/ja
    \nハンドルで指定したNURBS図形オフセットしてNURBS図形を新規に作成し、そのハンドルを返します。'''
    return HANDLE

def GetPointAndParameterOnNurbsCurveAtGivenLength(inNurbCurve, inPercentOfLength):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPointAndParameterOnNurbsCurveAtGivenLength
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPointAndParameterOnNurbsCurveAtGivenLength/ja
    \nNURBS曲線上の指定した点の位置、パラメータの位置、番号を返します。'''
    return (BOOLEAN, p, outParam, outIndex)

def NurbsGetWeight(objectHd, index1, index2):
    '''https://developer.vectorworks.net/index.php?title=VS:NurbsGetWeight
    \nhttps://developer.vectorworks.net/index.php?title=VS:NurbsGetWeight/ja
    \nハンドルで指定したNURBS曲線／曲面の、指定した頂点の重みを返します。'''
    return weight

def TrimNurbsSurface(surfaceHandle, curveHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:TrimNurbsSurface
    \nhttps://developer.vectorworks.net/index.php?title=VS:TrimNurbsSurface/ja
    \n任意のNURBS曲線でNURBS曲面をトリミングします。'''
    return BOOLEAN

def CreateSurfacefromCurvesNetwork():
    '''https://developer.vectorworks.net/index.php?title=VS:CreateSurfacefromCurvesNetwork
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateSurfacefromCurvesNetwork/ja
    \n選択されている交差した曲線からNURBS曲面を作成します。'''
    return BOOLEAN

def NurbsCurveEvalPt(objectHd, index, u):
    '''https://developer.vectorworks.net/index.php?title=VS:NurbsCurveEvalPt
    \nhttps://developer.vectorworks.net/index.php?title=VS:NurbsCurveEvalPt/ja
    \nハンドルで指定したNURBS曲線上の結び目uの座標を返します。'''
    return p

def NurbsKnot(objectHd, index1, index2):
    '''https://developer.vectorworks.net/index.php?title=VS:NurbsKnot
    \nhttps://developer.vectorworks.net/index.php?title=VS:NurbsKnot/ja
    \nハンドルで指定したNURBS曲線／曲面の、指定した頂点の結び目を返します。'''
    return knot

def DrawNurbsObject(h):
    '''https://developer.vectorworks.net/index.php?title=VS:DrawNurbsObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:DrawNurbsObject/ja
    \nNURBS図形を描画します。'''
    return None

def NurbsCurveGetNumPieces(objectHd):
    '''https://developer.vectorworks.net/index.php?title=VS:NurbsCurveGetNumPieces
    \nhttps://developer.vectorworks.net/index.php?title=VS:NurbsCurveGetNumPieces/ja
    \nハンドルで指定したNURBS曲線の辺の数を返します。'''
    return INTEGER

def NurbsNumKnots(objectHd, index):
    '''https://developer.vectorworks.net/index.php?title=VS:NurbsNumKnots
    \nhttps://developer.vectorworks.net/index.php?title=VS:NurbsNumKnots/ja
    \nハンドルで指定したNURBS曲線／曲面の結び目の数を返します。'''
    return LONGINT

def Add2DVertex(p, vertexType, arcRadius):
    '''https://developer.vectorworks.net/index.php?title=VS:Add2DVertex
    \nhttps://developer.vectorworks.net/index.php?title=VS:Add2DVertex/ja
    \nポリラインに制御点を座標指定によって追加します。０から４のタイプがあり、タイプ３及び４は半径をパラメータとして持ちます。タイプ４は頂点によって挟まれなければなりません。また、タイプ４の場合、制御点は円弧の中点となります。タイプ０で半径が設定されなかった場合、自動的に算出されます。'''
    return None

def DelVertex(objectHd, vertexNum):
    '''https://developer.vectorworks.net/index.php?title=VS:DelVertex
    \nhttps://developer.vectorworks.net/index.php?title=VS:DelVertex/ja
    \nハンドルで指定した多角形／曲線から、指定した番号の頂点を削除します。'''
    return None

def GetVertNum(PolyHd):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVertNum
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVertNum/ja
    \nハンドルで指定した多角形／曲線の頂点の数を返します。'''
    return INTEGER

def SetPolyPt(objectHd, index, xR, yR):
    '''https://developer.vectorworks.net/index.php?title=VS:SetPolyPt
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetPolyPt/ja
    \nハンドルで指定した多角形／曲線の頂点の座標を設定します。'''
    return None

def AddPoint(p):
    '''https://developer.vectorworks.net/index.php?title=VS:AddPoint
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddPoint/ja
    \n多角形に頂点を加えます。BeginPolyとEndPolyの間で使用します。'''
    return None

def EndPoly():
    '''https://developer.vectorworks.net/index.php?title=VS:EndPoly
    \nhttps://developer.vectorworks.net/index.php?title=VS:EndPoly/ja
    \n多角形／曲線の作成を終了します。'''
    return None

def GetVertexVisibility(h, vertnum):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVertexVisibility
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVertexVisibility/ja
    \nハンドルで指定した多角形／曲線の頂点が表示／非表示を返します。'''
    return BOOLEAN

def SetPolylineVertex(obj, vertexNum, p, vertexType, arcRadiusDistance, recalcBounds):
    '''https://developer.vectorworks.net/index.php?title=VS:SetPolylineVertex
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetPolylineVertex/ja
    \nハンドルで指定した多角形／曲線の頂点の値を設定します。'''
    return None

def ArcTo(p, radiusDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:ArcTo
    \nhttps://developer.vectorworks.net/index.php?title=VS:ArcTo/ja
    \n円弧の座標を頂点として追加します。BeginPolyとEndPolyの間で使用します。'''
    return None

def GetHole(inOutsidePolyline, inIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetHole
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetHole/ja
    \nハンドルで指定した曲線の、指定した番号の穴図形のハンドルを返します。'''
    return (BOOLEAN, outHole)

def InsertVertex(objectHandle, x, y, beforeVertexNum, vertexType, arcRadius):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertVertex
    \nhttps://developer.vectorworks.net/index.php?title=VS:InsertVertex/ja
    \n新しい頂点を多角形／曲線に挿入します。頂点の種類が0でない場合は、図形を曲線に変換します。'''
    return None

def SetVertexVisibility(h, vertnum, vis):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVertexVisibility
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetVertexVisibility/ja
    \nハンドルで指定した多角形／曲線の頂点の表示／非表示を設定します。'''
    return None

def BeginPoly():
    '''https://developer.vectorworks.net/index.php?title=VS:BeginPoly
    \nhttps://developer.vectorworks.net/index.php?title=VS:BeginPoly/ja
    \n多角形／曲線の作成を開始します。BeginPolyとEndPolyの間にAddPointで頂点を指定します。'''
    return None

def GetNumHoles(inPolyline):
    '''https://developer.vectorworks.net/index.php?title=VS:GetNumHoles
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNumHoles/ja
    \nハンドルで指定した曲線の穴の数を返します。その曲線に穴が空いていない場合はFALSEを返します。'''
    return (BOOLEAN, outNumHoles)

def IsPolyClosed(polyHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:IsPolyClosed
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsPolyClosed/ja
    \n曲線や多角形が閉じていればTRUE、そうでなければFALSEを返します。'''
    return BOOLEAN

def Smooth(smoothType):
    '''https://developer.vectorworks.net/index.php?title=VS:Smooth
    \nhttps://developer.vectorworks.net/index.php?title=VS:Smooth/ja
    \n多角形／曲線のスムージングの種類を設定します。'''
    return None

def ClosePoly():
    '''https://developer.vectorworks.net/index.php?title=VS:ClosePoly
    \nhttps://developer.vectorworks.net/index.php?title=VS:ClosePoly/ja
    \n以降に作成される多角形の始点と終点を自動的に閉じます。'''
    return None

def GetPolyPt(objectHd, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPolyPt
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPolyPt/ja
    \nハンドルで指定した多角形／曲線の頂点番号から頂点座標を返します。'''
    return p

def OpenPoly():
    '''https://developer.vectorworks.net/index.php?title=VS:OpenPoly
    \nhttps://developer.vectorworks.net/index.php?title=VS:OpenPoly/ja
    \n以降に作成される多角形の始点と終点を開きます。'''
    return None

def CurveThrough(p):
    '''https://developer.vectorworks.net/index.php?title=VS:CurveThrough
    \nhttps://developer.vectorworks.net/index.php?title=VS:CurveThrough/ja
    \nキュービックスプラインの座標を通過する部分を頂点として追加します。'''
    return None

def GetPolylineArcMaxRadius(hPoly, vertexNum):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPolylineArcMaxRadius
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPolylineArcMaxRadius/ja
    \n指定した円弧タイプの頂点、もしくはポリラインの最大半径を返します。'''
    return REAL

def Poly(p):
    '''https://developer.vectorworks.net/index.php?title=VS:Poly
    \nhttps://developer.vectorworks.net/index.php?title=VS:Poly/ja
    \n指定した頂点を結び多角形を作成します。'''
    return None

def CurveTo(p):
    '''https://developer.vectorworks.net/index.php?title=VS:CurveTo
    \nhttps://developer.vectorworks.net/index.php?title=VS:CurveTo/ja
    \nベジェ曲線の座標を頂点として追加します。'''
    return None

def GetPolylineVertex(obj, vertexNum):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPolylineVertex
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPolylineVertex/ja
    \nハンドルで指定した多角形／曲線の頂点の値を返します。'''
    return (p, vertexType, arcRadius)

def SetPolyClosed(polyHandle, isClosed):
    '''https://developer.vectorworks.net/index.php?title=VS:SetPolyClosed
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetPolyClosed/ja
    \n多角形、曲線の閉じる／開く状態を設定します。'''
    return None

def AppendRoofEdge(theRoof, edgePt, slopeAngle, projectionDistance, eaveHeightDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:AppendRoofEdge
    \nhttps://developer.vectorworks.net/index.php?title=VS:AppendRoofEdge/ja
    \nハンドルで指定した屋根に、新しい縁を追加します。'''
    return None

def GetBatAttributes(roofObject, dormerID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetBatAttributes
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetBatAttributes/ja
    \nハンドルで指定した屋根の中の、波型のドーマーの情報を返します。'''
    return (useHeight, heightDepth, bottomWidth, topWidth, baseHeight, controlPoint, topSlope)

def GetRoofFaceCoords(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetRoofFaceCoords
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetRoofFaceCoords/ja
    \nハンドルで指定した屋根の傾きを取得します。'''
    return (axis1, axis2, Zaxis, upslope)

def SetDormerThick(roofObject, wallThickDistance, roofThickDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDormerThick
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDormerThick/ja
    \nハンドルで指定したドーマーの、壁と屋根の厚みを設定します。'''
    return None

def BeginRoof(p1, p2, upslope, riseDistance, runDistance, miter, vertPart):
    '''https://developer.vectorworks.net/index.php?title=VS:BeginRoof
    \nhttps://developer.vectorworks.net/index.php?title=VS:BeginRoof/ja
    \nこの手続きを実行してから、EndGroupが実行されるまでに作成された2次元図形を平面とする屋根を作成します。'''
    return None

def GetDormerAttributes(roofObject, dormerID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDormerAttributes
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDormerAttributes/ja
    \nハンドルで指定した屋根の中の、ドーマーの情報を返します。'''
    return (edgeIndex, cornerOffset, isPerpOffset, perpOrHeightOffset, symName, centerSymbol, symOffset)

def GetRoofStyle(roof):
    '''https://developer.vectorworks.net/index.php?title=VS:GetRoofStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetRoofStyle/ja
    \n屋根の屋根スタイルを返します。'''
    return LONGINT

def SetGableAttributes(roofObject, dormerID, useHeight, heightDepthDistance, bottomWidthDistance, overhangDistance, leftAngle, rightAngle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetGableAttributes
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetGableAttributes/ja
    \nハンドルで指定した屋根の中の、切り妻のドーマーを設定します。'''
    return None

def ConvToUnstyledRoof(roof):
    '''https://developer.vectorworks.net/index.php?title=VS:ConvToUnstyledRoof
    \nhttps://developer.vectorworks.net/index.php?title=VS:ConvToUnstyledRoof/ja
    \n屋根を スタイルなし に設定します。'''
    return None

def GetDormerThick(roofObject):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDormerThick
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetDormerThick/ja
    \nハンドルで指定したドーマーの、壁と屋根の厚みを返します。'''
    return (wallThick, roofThick)

def GetRoofVertices(roofObject):
    '''https://developer.vectorworks.net/index.php?title=VS:GetRoofVertices
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetRoofVertices/ja
    \nハンドルで指定した屋根が持つ、縁の数を返します。'''
    return INTEGER

def SetHipAttributes(roofObject, dormerID, useHeight, heightDepthDistance, bottomWidthDistance, overhangDistance, leftAngle, rightAngle, frontAngle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetHipAttributes
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetHipAttributes/ja
    \nハンドルで指定した屋根の中の、寄せ棟のドーマーを設定します。'''
    return None

def CreateBatDormer(roofObject):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateBatDormer
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateBatDormer/ja
    \nハンドルで指定した屋根に、波形のドーマーを追加します。'''
    return INTEGER

def GetGableAttributes(roofObject, dormerID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetGableAttributes
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetGableAttributes/ja
    \nハンドルで指定した屋根の中の、切り妻のドーマーの情報を返します。'''
    return (useHeight, heightDepth, bottomWidth, overhang, leftSlope, rightSlope)

def GetShedAttributes(roofObject, dormerID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetShedAttributes
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetShedAttributes/ja
    \nハンドルで指定した屋根の中の、片流れのドーマーの情報を返します。'''
    return (useHeight, heightDepth, bottomWidth, overhang, topSlope)

def SetRoofAttributes(roofObject, genGableWall, bearingInsetDistance, roofThickDistance, miterType, vertMiterDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:SetRoofAttributes
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetRoofAttributes/ja
    \nハンドルで指定した屋根を設定します。'''
    return None

def CreateGableDormer(roofObject):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateGableDormer
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateGableDormer/ja
    \nハンドルで指定した屋根に、切り妻のドーマーを追加します。'''
    return INTEGER

def GetHipAttributes(roofObject, dormerID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetHipAttributes
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetHipAttributes/ja
    \nハンドルで指定した屋根の中の、寄せ棟のドーマーの情報を返します。'''
    return (useHeight, heightDepth, bottomWidth, overhang, leftSlope, rightSlope, frontSlope)

def GetSkylight(roofObject, skylightID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetSkylight
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSkylight/ja
    \nハンドルで指定した屋根の中の、天窓の情報を返します。'''
    return (edgeIndex, cornerOffset, perpOffset, symName)

def SetRoofEdge(roofObject, index, vertexPt, edgeAngle, projectionDistance, eaveHeightDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:SetRoofEdge
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetRoofEdge/ja
    \nハンドルで指定した屋根の中の、縁を設定します。'''
    return None

def CreateHipDormer(roofObject):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateHipDormer
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateHipDormer/ja
    \nハンドルで指定した屋根に、寄せ棟のドーマーを追加します。'''
    return INTEGER

def GetNumRoofElements(roofObject):
    '''https://developer.vectorworks.net/index.php?title=VS:GetNumRoofElements
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNumRoofElements/ja
    \nハンドルで指定した屋根の中の、ドーマーの数を返します。'''
    return INTEGER

def GetTrapeziumAttributes(roofObject, dormerID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTrapeziumAttributes
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTrapeziumAttributes/ja
    \nハンドルで指定した屋根の中の、台形のドーマーの情報を返します。'''
    return (useHeight, heightDepth, bottomWidth, useTopWidth, topWidth, leftSlope, rightSlope, topSlope)

def SetRoofStyle(roof, roofStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetRoofStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetRoofStyle/ja
    \n屋根の屋根スタイルを設定します。'''
    return None

def CreateRoof(genGableWall, bearingInsetDistance, roofThickDistance, miterType, vertMiterDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateRoof
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateRoof/ja
    \n新しい屋根を作成し、そのハンドルを返します。'''
    return HANDLE

def GetRoofAttributes(theRoof):
    '''https://developer.vectorworks.net/index.php?title=VS:GetRoofAttributes
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetRoofAttributes/ja
    \nハンドルで指定した屋根の情報を返します。'''
    return (BOOLEAN, genGableWall, bearingInset, roofThick, miterType, vertMiter)

def RemoveRoofEdge(roofObject, index):
    '''https://developer.vectorworks.net/index.php?title=VS:RemoveRoofEdge
    \nhttps://developer.vectorworks.net/index.php?title=VS:RemoveRoofEdge/ja
    \nハンドルで指定した屋根の中の、番号で指定した縁を削除します。'''
    return BOOLEAN

def SetShedAttributes(roofObject, dormerID, useHeight, heightDepthDistance, bottomWidthDistance, overhangDistance, topAngle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetShedAttributes
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetShedAttributes/ja
    \nハンドルで指定した屋根の中の、片流れのドーマーを設定します。'''
    return None

def CreateShedDormer(roofObject):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateShedDormer
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateShedDormer/ja
    \nハンドルで指定した屋根に、片流れのドーマーを追加します。'''
    return INTEGER

def GetRoofEdge(theRoof, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetRoofEdge
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetRoofEdge/ja
    \nハンドルで指定した屋根の中の、番号で指定した縁の情報を返します。'''
    return (BOOLEAN, vertexPt, slope, projection, eaveHeight)

def RemoveRoofElement(roofObject, id):
    '''https://developer.vectorworks.net/index.php?title=VS:RemoveRoofElement
    \nhttps://developer.vectorworks.net/index.php?title=VS:RemoveRoofElement/ja
    \nハンドルで指定した屋根の中の、番号で指定したドーマーを削除します。'''
    return None

def SetSkylight(roofObject, skylightID, edgeIndex, cornerOffsetDistance, perpOffsetDistance, symName):
    '''https://developer.vectorworks.net/index.php?title=VS:SetSkylight
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetSkylight/ja
    \nハンドルで指定した屋根の中の、天窓を設定します。'''
    return None

def CreateSkylight(roofObject):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateSkylight
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateSkylight/ja
    \nハンドルで指定した屋根に、天窓を追加します。'''
    return INTEGER

def GetRoofElementType(roofObject, dormerID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetRoofElementType
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetRoofElementType/ja
    \nハンドルで指定した屋根の情報を返します。'''
    return (edgeIndex, isDormer, dormerType)

def SetBatAttributes(roofObject, dormerID, useHeight, heightDepthValueDistance, bottomWidthDistance, topWidthDistance, baseHeightDistance, controlPointDistance, topAngle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetBatAttributes
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetBatAttributes/ja
    \nハンドルで指定した屋根の中の、波形のドーマーを設定します。'''
    return None

def SetTrapeziumAttributes(roofObject, dormerID, useHeight, heightDpthDistance, bottomWidthDistance, useTopWidth, topWidthDistance, leftAngle, rightAngle, topAngle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTrapeziumAttributes
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTrapeziumAttributes/ja
    \nハンドルで指定した屋根の中の、台形のドーマーを設定します。'''
    return None

def CreateTrapeziumDormer(roofObject):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateTrapeziumDormer
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateTrapeziumDormer/ja
    \nハンドルで指定した屋根に、台形のドーマーを追加します。'''
    return INTEGER

def GetRoofFaceAttrib(roofFace):
    '''https://developer.vectorworks.net/index.php?title=VS:GetRoofFaceAttrib
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetRoofFaceAttrib/ja
    \nハンドルで指定した屋根の属性を返します。'''
    return (roofRise, roofRun, miterType, holeStyle, vertPart, thickness)

def SetDormerAttributes(roofObject, dormerID, edgeIndex, cornerOffsetDistance, isPerpOffset, perpOrHeightOffsetDistance, symName, centerSymbol, symOffsetDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDormerAttributes
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDormerAttributes/ja
    \nハンドルで指定した屋根の中の、ドーマーを設定します。'''
    return None

def AddSolid(obj1, obj2):
    '''https://developer.vectorworks.net/index.php?title=VS:AddSolid
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddSolid/ja
    \nハンドルで指定した2つの3次元図形を噛み合わせます。作成された図形のハンドルはnewSolidに返されます。'''
    return (INTEGER, newSolid)

def CreateCone(center, tip, radiusDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateCone
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateCone/ja
    \n円錐を作成します。'''
    return HANDLE

def IntersectSolid(obj1, obj2):
    '''https://developer.vectorworks.net/index.php?title=VS:IntersectSolid
    \nhttps://developer.vectorworks.net/index.php?title=VS:IntersectSolid/ja
    \nハンドルで指定した2つの3次元図形の重なった部分を残します。作成された図形のハンドルはnewSolidに返されます。'''
    return (INTEGER, newSolid)

def SubtractSolid(obj1, obj2):
    '''https://developer.vectorworks.net/index.php?title=VS:SubtractSolid
    \nhttps://developer.vectorworks.net/index.php?title=VS:SubtractSolid/ja
    \nハンドルで指定した2つの3次元図形を削り取ります。作成された図形のハンドルはnewSolidに返されます。'''
    return (INTEGER, newSolid)

def CalcSurfaceArea(solidObject):
    '''https://developer.vectorworks.net/index.php?title=VS:CalcSurfaceArea
    \nhttps://developer.vectorworks.net/index.php?title=VS:CalcSurfaceArea/ja
    \nハンドルで指定した3次元図形（ソリッド）の表面積を返します。'''
    return REAL

def CreateHemisphere(center, top):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateHemisphere
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateHemisphere/ja
    \n半球を作成します。'''
    return HANDLE

def ObjSurfAreaInWorldC(solidObject):
    '''https://developer.vectorworks.net/index.php?title=VS:ObjSurfAreaInWorldC'''
    return REAL

def CalcVolume(solidObject):
    '''https://developer.vectorworks.net/index.php?title=VS:CalcVolume
    \nhttps://developer.vectorworks.net/index.php?title=VS:CalcVolume/ja
    \nハンドルで指定した3次元図形（ソリッド）の体積を返します。'''
    return REAL

def CreateShell(surface, thickness):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateShell
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateShell/ja
    \nNURBS曲面からシェルソリッドを作成します。'''
    return Handle

def ObjSurfaceArea(solidObject):
    '''https://developer.vectorworks.net/index.php?title=VS:ObjSurfaceArea
    \nhttps://developer.vectorworks.net/index.php?title=VS:ObjSurfaceArea/ja
    \nハンドルで指定した3次元図形（ソリッド）の表面積を返します。値は「単位の設定」ダイアログで設定されている「体積」の単位になります。'''
    return REAL

def CnvrtToGenericSolid(solid):
    '''https://developer.vectorworks.net/index.php?title=VS:CnvrtToGenericSolid
    \nhttps://developer.vectorworks.net/index.php?title=VS:CnvrtToGenericSolid/ja
    \nソリッド図形を汎用ソリッドに変換します。ソリッドの履歴を削除してメモリを節約します。'''
    return HANDLE

def CreateSphere(center, radiusDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateSphere
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateSphere/ja
    \n球を作成します。'''
    return HANDLE

def ObjVolume(solidObject):
    '''https://developer.vectorworks.net/index.php?title=VS:ObjVolume
    \nhttps://developer.vectorworks.net/index.php?title=VS:ObjVolume/ja
    \nハンドルで指定した3次元図形（ソリッド）の体積を返します。値は「単位の設定」ダイアログで設定されている「体積」の単位になります。'''
    return REAL

def StairGet2D3DCompType(stair):
    '''https://developer.vectorworks.net/index.php?title=VS:StairGet2D3DCompType'''
    return INTEGER

def StairGetSideLengthsM(stair):
    '''https://developer.vectorworks.net/index.php?title=VS:StairGetSideLengthsM'''
    return (BOOLEAN, LengthSide1M, LengthSide2M, LengthSide3M, LengthSide4M, LengthSide5M)

def StairSetConfigType(stair, ConfigurationType):
    '''https://developer.vectorworks.net/index.php?title=VS:StairSetConfigType'''
    return BOOLEAN

def StairSetTopGrUpFlMode(stair, TopGraphicOnOtherFloorMode):
    '''https://developer.vectorworks.net/index.php?title=VS:StairSetTopGrUpFlMode'''
    return BOOLEAN

def StairGetConfigType(stair):
    '''https://developer.vectorworks.net/index.php?title=VS:StairGetConfigType'''
    return INTEGER

def StairGetTopGrUpFlMode(stair):
    '''https://developer.vectorworks.net/index.php?title=VS:StairGetTopGrUpFlMode'''
    return INTEGER

def StairSetConstType(stair, ConstructionType):
    '''https://developer.vectorworks.net/index.php?title=VS:StairSetConstType'''
    return BOOLEAN

def StairSetTotalRiseM(stair, TotalRise):
    '''https://developer.vectorworks.net/index.php?title=VS:StairSetTotalRiseM'''
    return BOOLEAN

def StairGetConstType(stair):
    '''https://developer.vectorworks.net/index.php?title=VS:StairGetConstType'''
    return INTEGER

def StairGetTotalRiseM(stair):
    '''https://developer.vectorworks.net/index.php?title=VS:StairGetTotalRiseM'''
    return REAL

def StairSetNumRisers(stair, NumRisers1, NumRisers2, NumRisers3, NumRisers4):
    '''https://developer.vectorworks.net/index.php?title=VS:StairSetNumRisers'''
    return BOOLEAN

def StairSetWFlight1M(stair, WidthOfFirstFlight):
    '''https://developer.vectorworks.net/index.php?title=VS:StairSetWFlight1M'''
    return BOOLEAN

def StairGetNumRisers(stair):
    '''https://developer.vectorworks.net/index.php?title=VS:StairGetNumRisers'''
    return (BOOLEAN, NumRisers1, NumRisers2, NumRisers3, NumRisers4)

def StairGetWFlight1M(stair):
    '''https://developer.vectorworks.net/index.php?title=VS:StairGetWFlight1M'''
    return REAL

def StairSetOptTotalRise(stair, OptionTotalRise):
    '''https://developer.vectorworks.net/index.php?title=VS:StairSetOptTotalRise'''
    return BOOLEAN

def StairGetOptTotalRise(stair):
    '''https://developer.vectorworks.net/index.php?title=VS:StairGetOptTotalRise'''
    return INTEGER

def StairSet2D3DCompType(stair, ComponentType2D3D):
    '''https://developer.vectorworks.net/index.php?title=VS:StairSet2D3DCompType'''
    return BOOLEAN

def StairSetSideLengthsM(stair, LengthSide1M, LengthSide2M, LengthSide3M, LengthSide4M, LengthSide5M):
    '''https://developer.vectorworks.net/index.php?title=VS:StairSetSideLengthsM'''
    return BOOLEAN

def ActSymDef():
    '''https://developer.vectorworks.net/index.php?title=VS:ActSymDef
    \nhttps://developer.vectorworks.net/index.php?title=VS:ActSymDef/ja
    \n現在リソースパレット上で選択されている登録シンボルのハンドルを返します。'''
    return HANDLE

def GetSDName(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetSDName
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSDName/ja
    \nハンドルで指定したシンボルの名前を返します。'''
    return STRING

def GetSymbolType(objectHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetSymbolType
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSymbolType/ja
    \nシンボルの種類（0：2Dのみ／1：3Dのみ／3：ハイブリッド）を返します。'''
    return INTEGER

def SetSymbolOptionsN(name, insertMode, breakMode, className):
    '''https://developer.vectorworks.net/index.php?title=VS:SetSymbolOptionsN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetSymbolOptionsN/ja
    \nシンボルの挿入位置と壁の処理、デフォルトのクラスを設定します。'''
    return None

def ActSymDefN(allowConflictDlg):
    '''https://developer.vectorworks.net/index.php?title=VS:ActSymDefN'''
    return HANDLE

def GetSymBrightMult(symbol):
    '''https://developer.vectorworks.net/index.php?title=VS:GetSymBrightMult
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSymBrightMult/ja
    \nハンドルで指定したシンボルの、光源の明るさの乗数をパーセンテージで返します。'''
    return INTEGER

def InsertSymbolInFolder(targetFolder, symbolDef):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertSymbolInFolder
    \nhttps://developer.vectorworks.net/index.php?title=VS:InsertSymbolInFolder/ja
    \nハンドルで指定したシンボルをシンボルフォルダに入れます。'''
    return None

def SymDefNum():
    '''https://developer.vectorworks.net/index.php?title=VS:SymDefNum
    \nhttps://developer.vectorworks.net/index.php?title=VS:SymDefNum/ja
    \nアクティブなドキュメントに登録されているシンボルの数を返します。'''
    return LONGINT

def AddToPluginStyle(hSymDef, itemName, styleType):
    '''https://developer.vectorworks.net/index.php?title=VS:AddToPluginStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddToPluginStyle/ja
    \nプラグインスタイルに新しい項目を追加します。'''
    return BOOLEAN

def GetSymDefSubType(hSymDef):
    '''https://developer.vectorworks.net/index.php?title=VS:GetSymDefSubType
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSymDefSubType/ja
    \nシンボル定義に定義された図形の種類（サブタイプ）を返します。 プラグインスタイルの作成時や使用時に利用します。'''
    return INTEGER

def RemoveFrmPluginStyle(hSymDef, itemName):
    '''https://developer.vectorworks.net/index.php?title=VS:RemoveFrmPluginStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:RemoveFrmPluginStyle/ja
    \nプラグインスタイルから項目を削除します。'''
    return BOOLEAN

def Symbol(symbolName, p, rotationAngle):
    '''https://developer.vectorworks.net/index.php?title=VS:Symbol
    \nhttps://developer.vectorworks.net/index.php?title=VS:Symbol/ja
    \nアクティブなレイヤ上の指定した座標に、シンボルを配置します。'''
    return None

def BeginSym(symbolName):
    '''https://developer.vectorworks.net/index.php?title=VS:BeginSym
    \nhttps://developer.vectorworks.net/index.php?title=VS:BeginSym/ja
    \nこの手続きを実行した後、EndSymを実行するまでの間に作成された図形をシンボルとして登録します。'''
    return None

def GetSymLoc3D(objectHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetSymLoc3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSymLoc3D/ja
    \n3次元空間でのシンボルやプラグインオブジェクトの位置を返します。'''
    return (x, y, z)

def SetActSymbol(name):
    '''https://developer.vectorworks.net/index.php?title=VS:SetActSymbol
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetActSymbol/ja
    \n名前で指定したシンボルをアクティブにします。'''
    return None

def SymbolToGroup(h, convertAction):
    '''https://developer.vectorworks.net/index.php?title=VS:SymbolToGroup
    \nhttps://developer.vectorworks.net/index.php?title=VS:SymbolToGroup/ja
    \nオプションを指定してシンボルをグループに変換します。'''
    return None

def CopySymbol(filePath, symbol):
    '''https://developer.vectorworks.net/index.php?title=VS:CopySymbol
    \nhttps://developer.vectorworks.net/index.php?title=VS:CopySymbol/ja
    \n他のドキュメントから、アクティブなドキュメントにシンボルを取り込みます。'''
    return BOOLEAN

def GetSymName(symHd):
    '''https://developer.vectorworks.net/index.php?title=VS:GetSymName
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSymName/ja
    \nハンドルで指定したシンボルの名前を返します。'''
    return STRING

def SetSymBrightMult(symbol, brightnessMultiplier):
    '''https://developer.vectorworks.net/index.php?title=VS:SetSymBrightMult
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetSymBrightMult/ja
    \nハンドルで指定したシンボルの、光源の明るさの乗数をパーセンテージで設定します。'''
    return None

def EndSym():
    '''https://developer.vectorworks.net/index.php?title=VS:EndSym
    \nhttps://developer.vectorworks.net/index.php?title=VS:EndSym/ja
    \nBeginSymを実行した後、この手続きを実行するまでの間に作成された図形をシンボルとして登録します。'''
    return None

def GetSymbolOptionsN(name):
    '''https://developer.vectorworks.net/index.php?title=VS:GetSymbolOptionsN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSymbolOptionsN/ja
    \nシンボルの挿入位置と壁の処理、クラスの設定を返します。'''
    return (insertMode, breakMode, className)

def SetSymDefSubType(hSymDef, subType):
    '''https://developer.vectorworks.net/index.php?title=VS:SetSymDefSubType
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetSymDefSubType/ja
    \nプラグインスタイルを定義するシンボル定義の図形の種類（サブタイプ）を設定します。'''
    return None

def GetTextOrientation(theText):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTextOrientation
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTextOrientation/ja
    \nハンドルで指定した文字図形の座標と角度を返します。'''
    return (textOrigin, textAng, textIsMirrored)

def SetTextFont(objectHd, Start, Count, FontNum):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextFont
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextFont/ja
    \nハンドルで指定した文字図形の指定した位置から、指定した長さまでのフォントを設定します。'''
    return None

def SetTextWidth(theText, widthDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextWidth
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextWidth/ja
    \nハンドルで指定した文字図形の幅を設定します。'''
    return None

def CreateText(theText):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateText
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateText/ja
    \n現在のペン位置に文字図形を作成します。'''
    return None

def GetTextSize(TextHd, Position):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTextSize
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTextSize/ja
    \nハンドルで指定した文字図形の、指定した位置の文字の大きさを返します。'''
    return REAL

def SetTextJust(TextHd, JustFlag):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextJust
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextJust/ja
    \nハンドルで指定した文字図形の位置揃えを設定します。'''
    return None

def SetTextWrap(theText, wrap):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextWrap
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextWrap/ja
    \nハンドルで指定した文字図形でラップテキストの有効／無効を設定します。'''
    return None

def CreateTextStyleRes(name):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateTextStyleRes
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateTextStyleRes/ja
    \n指定した名前で新規に文字スタイルを作成します。 作成したリソースへのハンドルを返します。 リソース作成後、各属性を適切に設定する必要があります。'''
    return HANDLE

def GetTextSpace(theText):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTextSpace
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTextSpace/ja
    \nハンドルで指定した文字図形の行間隔を返します。'''
    return INTEGER

def SetTextJustN(TextHd, JustFlag):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextJustN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextJustN/ja
    \nハンドルで指定した文字図形の位置を変えずに位置揃えを設定します。'''
    return None

def TextFace(s):
    '''https://developer.vectorworks.net/index.php?title=VS:TextFace
    \nhttps://developer.vectorworks.net/index.php?title=VS:TextFace/ja
    \n文字のスタイルを設定します。複数組み合わせる場合は,でつなぎます。'''
    return None

def GetTextStyle(TextHd, Position):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTextStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTextStyle/ja
    \nハンドルで指定した文字図形の、指定した位置の文字のスタイルを返します。指定した位置に文字が存在しない場合は0が返ります。'''
    return INTEGER

def SetTextLeading(theText, leading):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextLeading
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextLeading/ja
    \n指定した文字図形の文字の行間隔を設定します。'''
    return None

def TextFlip(FlipType):
    '''https://developer.vectorworks.net/index.php?title=VS:TextFlip
    \nhttps://developer.vectorworks.net/index.php?title=VS:TextFlip/ja
    \n以降に作成する文字を垂直か水平に反転します。'''
    return None

def GetCharColor(theText, position):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCharColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCharColor/ja
    \n任意の文字図形の、指定した位置にある文字の色を返します。'''
    return (red, green, blue)

def GetTextStyleRef(objectId):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTextStyleRef
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTextStyleRef/ja
    \n指定した図形の文字スタイルのインデックスを返します。 対象の図形がクラスの文字スタイルを使用している場合、クラスに設定されているスタイルを返します。'''
    return LONGINT

def SetTextOrientation(theText, textOrigin, textAngle, textIsMirrored):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextOrientation
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextOrientation/ja
    \n指定した文字図形の座標と角度を設定します。'''
    return None

def TextFont(fontID):
    '''https://developer.vectorworks.net/index.php?title=VS:TextFont
    \nhttps://developer.vectorworks.net/index.php?title=VS:TextFont/ja
    \nドキュメントのアクティブなフォントを番号で設定します。'''
    return None

def GetFontID(fontName):
    '''https://developer.vectorworks.net/index.php?title=VS:GetFontID
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetFontID/ja
    \nフォントの番号を返します。'''
    return INTEGER

def GetTextStyleRefN(objectId, position):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTextStyleRefN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTextStyleRefN/ja
    \n文字図形のうち指定した位置の文字の文字スタイルのインデックスを返します。 文字スタイルが使用されていない場合は 0 を返します。文字図形がクラスの文字スタイルを使用している場合、クラスに設定されているスタイルを返します。'''
    return LONGINT

def SetTextSize(objectHd, Start, Count, Size):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextSize
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextSize/ja
    \nハンドルで指定した文字図形の指定した位置から、指定した長さまでのフォントの大きさを設定します。'''
    return None

def TextJust(justify):
    '''https://developer.vectorworks.net/index.php?title=VS:TextJust
    \nhttps://developer.vectorworks.net/index.php?title=VS:TextJust/ja
    \n文字の位置揃えを設定します。'''
    return None

def GetFontListSize():
    '''https://developer.vectorworks.net/index.php?title=VS:GetFontListSize
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetFontListSize/ja
    \nローカルシステム上で利用可能なフォントの数を返します。'''
    return INTEGER

def GetTextVerticalAlign(TextHd):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTextVerticalAlign
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTextVerticalAlign/ja
    \nハンドルで指定した文字図形の垂直方向の位置揃えを返します。'''
    return INTEGER

def SetTextSpace(theText, spacing):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextSpace
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextSpace/ja
    \nハンドルで指定した文字図形の行間隔を設定します。'''
    return None

def TextLeading(leading):
    '''https://developer.vectorworks.net/index.php?title=VS:TextLeading
    \nhttps://developer.vectorworks.net/index.php?title=VS:TextLeading/ja
    \n文字の行間隔を設定します。'''
    return None

def GetFontName(fontID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetFontName
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetFontName/ja
    \nフォントの名前を返します。'''
    return STRING

def GetTextWidth(theText):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTextWidth
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTextWidth/ja
    \nハンドルで指定した文字図形の幅を返します。'''
    return REAL

def SetTextStyle(objectHd, Start, Count, Style):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextStyle/ja
    \nハンドルで指定した文字図形の指定した位置から、指定した長さまでのフォントのスタイルを設定します。'''
    return None

def TextOrigin(p):
    '''https://developer.vectorworks.net/index.php?title=VS:TextOrigin
    \nhttps://developer.vectorworks.net/index.php?title=VS:TextOrigin/ja
    \n作成する文字図形の左上の座標を設定します。'''
    return None

def GetText(objectHd):
    '''https://developer.vectorworks.net/index.php?title=VS:GetText
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetText/ja
    \nハンドルで指定した文字図形の文字列を返します。'''
    return DYNARRAY[] of CHAR

def GetTextWrap(theText):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTextWrap
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTextWrap/ja
    \nハンドルで指定した文字図形でラップテキストが有効の場合はTRUEを返します。'''
    return BOOLEAN

def SetTextStyleByClassN(objectId, start, count):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextStyleByClassN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextStyleByClassN/ja
    \n文字図形のうち指定した部分の文字列がクラスの文字スタイルを使用するように設定します。 設定を取り消すには、 SetTextStyleRef または SetTextStyleRefN を使用します。'''
    return BOOLEAN

def TextRotate(Rotation):
    '''https://developer.vectorworks.net/index.php?title=VS:TextRotate
    \nhttps://developer.vectorworks.net/index.php?title=VS:TextRotate/ja
    \n以降に作成する文字を回転させます。'''
    return None

def GetTextFont(objectHd, Position):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTextFont
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTextFont/ja
    \nハンドルで指定した文字図形の、指定した位置の文字のフォント番号を返します。'''
    return INTEGER

def IsTextStyleByClassN(objectId, position):
    '''https://developer.vectorworks.net/index.php?title=VS:IsTextStyleByClassN
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsTextStyleByClassN/ja
    \n文字図形の文字列のうち指定した位置の文字がクラスの文字スタイルを使用しているかどうかを返します。'''
    return BOOLEAN

def SetTextStyleRef(objectId, textStyleRef):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextStyleRef
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextStyleRef/ja
    \n図形がインデックスで指定した文字スタイルを使用するように設定します。 文字スタイルを使用しない(解除する)場合は0を指定します。'''
    return None

def TextSize(size):
    '''https://developer.vectorworks.net/index.php?title=VS:TextSize
    \nhttps://developer.vectorworks.net/index.php?title=VS:TextSize/ja
    \n文字の大きさを設定します。'''
    return None

def GetTextJust(TextHd):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTextJust
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTextJust/ja
    \nハンドルで指定した文字図形の位置揃えを返します。'''
    return INTEGER

def ReplaceText(objectHd, oldText, newText, replaceAll, isCaseSens):
    '''https://developer.vectorworks.net/index.php?title=VS:ReplaceText'''
    return None

def SetTextStyleRefN(objectId, start, count, textStyleRef):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextStyleRefN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextStyleRefN/ja
    \n文字図形のうち指定した部分の文字列がインデックスで指定した文字スタイルを使用するように設定します。文字スタイルを使用しない(解除する)場合は0を指定します。'''
    return BOOLEAN

def TextSpace(spacing):
    '''https://developer.vectorworks.net/index.php?title=VS:TextSpace
    \nhttps://developer.vectorworks.net/index.php?title=VS:TextSpace/ja
    \n文字の行間隔を設定します。'''
    return None

def GetTextLeading(theText):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTextLeading
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTextLeading/ja
    \nハンドルで指定した文字図形の行間隔を返します。'''
    return REAL

def SetText(objectHd, text):
    '''https://developer.vectorworks.net/index.php?title=VS:SetText
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetText/ja
    \nハンドルで指定した文字図形の文字列を設定します。'''
    return None

def SetTextVertAlignN(TextHd, verticalAlignment):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextVertAlignN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextVertAlignN/ja
    \nハンドルで指定した文字図形の位置を変えずに垂直方向の配置を設定します。'''
    return None

def TextVerticalAlign(verticalAlignment):
    '''https://developer.vectorworks.net/index.php?title=VS:TextVerticalAlign
    \nhttps://developer.vectorworks.net/index.php?title=VS:TextVerticalAlign/ja
    \n垂直方向の位置揃えを設定します。'''
    return None

def GetTextLength(TextHd):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTextLength
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTextLength/ja
    \nハンドルで指定した文字図形の文字の数を返します。'''
    return INTEGER

def SetTextAdorner(textBlock, textAdorner, p):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextAdorner
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextAdorner/ja
    \nこの関数は、指定したテキストブロックとテキスト装飾の間の関係を作成します。'''
    return Boolean

def SetTextVerticalAlign(TextHd, verticalAlignment):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextVerticalAlign
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextVerticalAlign/ja
    \nハンドルで指定した文字図形の垂直方向の位置揃えを設定します。'''
    return None

def TrueTypeToPoly(textHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:TrueTypeToPoly
    \nhttps://developer.vectorworks.net/index.php?title=VS:TrueTypeToPoly/ja
    \nTrueTypeToPolyは文字列オブジェクトを似た形の多角形や曲線のグループに変換します。'''
    return (LONGINT, polyGroupHandle)

def AddCavity(pair, leftOffDistance, rightOffDistance, pairFill):
    '''https://developer.vectorworks.net/index.php?title=VS:AddCavity
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddCavity/ja
    \n壁に中心線を追加します。'''
    return None

def GetObjWallBreakMode(objH, wallH, breakMode):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjWallBreakMode
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetObjWallBreakMode/ja
    \n壁に挿入したオブジェクトの、壁の処理モードを返します。'''
    return (Boolean, breakMode)

def GetWallWidth():
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallWidth
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWallWidth/ja
    \nデフォルトの壁の幅を返します。'''
    return REAL

def SetWallBelCutPlClass(wall, belowCutPlaneClass):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWallBelCutPlClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWallBelCutPlClass/ja
    \n壁の切断面より下の属性のクラスを設定します。'''
    return None

def AddSymToWall(wallHd, offDistance, heightDistance, flip, right, symbolName):
    '''https://developer.vectorworks.net/index.php?title=VS:AddSymToWall
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddSymToWall/ja
    \nハンドルで指定した壁に、シンボルを挿入します。'''
    return None

def GetObjWallInsLocOff(objectHandle, wallHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjWallInsLocOff'''
    return (BOOLEAN, insertLocationOffset)

def HWallHeight(wallHd, startHeightDistance, endHeightDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:HWallHeight
    \nhttps://developer.vectorworks.net/index.php?title=VS:HWallHeight/ja
    \nハンドルで指定した壁の始点と終点の高さを設定します。'''
    return None

def SetWallCapAttributesType(wall, wallCapAttributesType):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWallCapAttributesType
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWallCapAttributesType/ja
    \n壁の端の属性を設定します。'''
    return None

def AddSymToWallEdge(h, alongDistance, heightDistance, flip, right, symbolName, insertMode):
    '''https://developer.vectorworks.net/index.php?title=VS:AddSymToWallEdge
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddSymToWallEdge/ja
    \nハンドルで指定した壁に、挿入モードを指定してシンボルを挿入します。'''
    return None

def GetObjWallInsertMode(objH, wallH, insertMode):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjWallInsertMode
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetObjWallInsertMode/ja
    \n壁に挿入したオブジェクトの、壁への挿入位置を返します。'''
    return (Boolean, insertMode)

def HWallWidth(wallHd, widthDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:HWallWidth
    \nhttps://developer.vectorworks.net/index.php?title=VS:HWallWidth/ja
    \nハンドルで指定した壁の幅を設定します。'''
    return None

def SetWallCaps(theWall, leftCap, rightCap, round):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWallCaps
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWallCaps/ja
    \n壁の端部の表示状態、形状を設定します。'''
    return BOOLEAN

def AddWallBottomPeak(wallHd, offDistance, heightDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:AddWallBottomPeak
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddWallBottomPeak/ja
    \nハンドルで指定した壁の底面に、頂点を追加します。'''
    return None

def GetObjectWallHeight(objH, wallH):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjectWallHeight
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetObjectWallHeight/ja
    \n壁の中の図形の高さを返します。 図形(objH)が壁(wallH)の中に含まれている必要があります。'''
    return (BOOLEAN, height)

def InsertSymbol(offsetDistance, heightDistance, flipped, right, capped, symbolName):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertSymbol
    \nhttps://developer.vectorworks.net/index.php?title=VS:InsertSymbol/ja
    \n壁の中の指定した位置にシンボルを配置します。'''
    return None

def SetWallCapsOffsets(theWall, leftCapLeftDistance, leftCapRightDistance, rightCapLeftDistance, rightCapRightDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWallCapsOffsets
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWallCapsOffsets/ja
    \n壁の端部のオフセットを設定します。'''
    return BOOLEAN

def AddWallPeak(wallHd, offDistance, heightDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:AddWallPeak
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddWallPeak/ja
    \nハンドルで指定した壁に頂点を追加します。'''
    return None

def GetObjectWallOffset(objH, wallH):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjectWallOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetObjectWallOffset/ja
    \n壁の中の図形のオフセットを返します。 図形(objH)が壁(wallH)の中に含まれている必要があります。'''
    return (BOOLEAN, offset)

def IsCurtainWall(hWall):
    '''https://developer.vectorworks.net/index.php?title=VS:IsCurtainWall
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsCurtainWall/ja
    \n壁がカーテンウォールの場合はTRUEを返します。'''
    return BOOLEAN

def SetWallControlOffset(offset):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWallControlOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWallControlOffset/ja
    \n壁のオフセットの値を設定します。'''
    return None

def BreakWall(offsetDistance, breakWidthDistance, right):
    '''https://developer.vectorworks.net/index.php?title=VS:BreakWall
    \nhttps://developer.vectorworks.net/index.php?title=VS:BreakWall/ja
    \n直前に作成された壁を、指定した位置と長さで切り欠きます。'''
    return None

def GetObjectWallPerpOff(objectHandle, wallHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjectWallPerpOff'''
    return (BOOLEAN, perpendicularOffset)

def IsWallPeakTop(hWall, peakIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:IsWallPeakTop
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsWallPeakTop/ja
    \n（番号で）指定した壁の頂点が上端にあるならばTRUEを返します。'''
    return BOOLEAN

def SetWallCornerHeights(theWall, startHeightTop, startHeightBottom, endHeightTop, endHeightBottom):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWallCornerHeights
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWallCornerHeights/ja
    \n壁または円弧壁のコーナーの高さを設定します。'''
    return BOOLEAN

def ClearCavities():
    '''https://developer.vectorworks.net/index.php?title=VS:ClearCavities
    \nhttps://developer.vectorworks.net/index.php?title=VS:ClearCavities/ja
    \n壁の中心線をすべて消去します。'''
    return None

def GetWallBelCutPlClass(wall):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallBelCutPlClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWallBelCutPlClass/ja
    \n壁の切断面より下の属性のクラスを取得します。'''
    return LONGINT

def JoinWalls(firstWall, secondWall, firstWall, secondWall, joinModifier, capped, showAlerts):
    '''https://developer.vectorworks.net/index.php?title=VS:JoinWalls
    \nhttps://developer.vectorworks.net/index.php?title=VS:JoinWalls/ja
    \n壁結合ツールのインターフェイスをVectorScriptで提供します。'''
    return BOOLEAN

def SetWallHeights(h, startHtDistance, endHtDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWallHeights
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWallHeights/ja
    \n仕様が設定されていない壁の高さを設定します。仕様が設定されている壁の場合はFALSEを返します。'''
    return BOOLEAN

def ClearWallPeaks(h):
    '''https://developer.vectorworks.net/index.php?title=VS:ClearWallPeaks
    \nhttps://developer.vectorworks.net/index.php?title=VS:ClearWallPeaks/ja
    \nハンドルで指定した壁の頂点を、すべて消去します。'''
    return None

def GetWallCapAttributesType(wall):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallCapAttributesType
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWallCapAttributesType/ja
    \n壁の端の属性を返します。'''
    return INTEGER

def MoveWallByOffset(theWall, offset):
    '''https://developer.vectorworks.net/index.php?title=VS:MoveWallByOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:MoveWallByOffset/ja
    \nARCHITECTでのみ利用可能です。すべての壁の連結を維持したまま、壁を指定した値で定義した線に垂直に動かします。壁の移動の幾何学的に拘束されているので、実際に壁が動いた値を返します。'''
    return offset

def SetWallOverallHeights(theWall, botBoundType, botBoundStory, botLayerLevelType, botOffset, topBoundType, topBoundStory, topLayerLevelType, topOffset):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWallOverallHeights
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWallOverallHeights/ja
    \n壁または円弧壁の全高を設定します。'''
    return BOOLEAN

def ConvertToUnstyledWall(h):
    '''https://developer.vectorworks.net/index.php?title=VS:ConvertToUnstyledWall
    \nhttps://developer.vectorworks.net/index.php?title=VS:ConvertToUnstyledWall/ja
    \n壁を&lt;unstyled&gt;に設定します。成功した場合はTRUEを返します。'''
    return BOOLEAN

def GetWallCaps(theWall):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallCaps
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWallCaps/ja
    \n壁の端部の表示状況、形状を取得します。'''
    return (leftCap, rightCap, round)

def ReverseWallSides(theWall):
    '''https://developer.vectorworks.net/index.php?title=VS:ReverseWallSides
    \nhttps://developer.vectorworks.net/index.php?title=VS:ReverseWallSides/ja
    \nハンドルで指定した壁の向きを逆にすることで壁の左右を切り替えます。'''
    return None

def SetWallStyle(theWall, wallStyle, selectedOffDistance, replacingOffDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWallStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWallStyle/ja
    \nハンドルで指定した壁に、壁スタイルを設定し、指定したオフセットに揃えます。'''
    return BOOLEAN

def CreateWallFeature(wall, profile, wallFeatureType):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateWallFeature
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateWallFeature/ja
    \n壁フィーチャーを輪郭形状から作成します。'''
    return HANDLE

def GetWallCapsOffsets(theWall):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallCapsOffsets
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWallCapsOffsets/ja
    \n壁の端部のオフセットを取得します。'''
    return (leftCapLeftOffset, leftCapRightOffset, rightCapLeftOffset, rightCapRightOffset)

def RoundWall(centerPt, startPt, endPt):
    '''https://developer.vectorworks.net/index.php?title=VS:RoundWall
    \nhttps://developer.vectorworks.net/index.php?title=VS:RoundWall/ja
    \n円弧の壁を作成します。'''
    return None

def SetWallThickness(h, thicknessDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWallThickness
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWallThickness/ja
    \nスタイルも設定されておらず、構成要素もない壁の厚みを設定します。'''
    return BOOLEAN

def CreateWallStyle(wallStyleName):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateWallStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateWallStyle/ja
    \n新しい壁スタイルを指定した名前で作成します。指定した名前の壁スタイルが存在する場合は、指定した名前に文字を追加し、利用できる名前で作成します。'''
    return HANDLE

def GetWallCompEndPts(wall, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallCompEndPts
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWallCompEndPts/ja
    \n壁の構成要素の終点の座標を取得します。'''
    return (leftPoint, centerPoint, rightPoint)

def SetCurtainWallCutPl(wall, curtainWallCutPlane):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCurtainWallCutPl
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCurtainWallCutPl/ja
    \nカーテンウォールの断面高さを設定します。'''
    return None

def SetWallWidth(widthDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWallWidth
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWallWidth/ja
    \nドキュメントでデフォルトとする壁の幅を設定します。'''
    return None

def DeleteWallPeak(wallHandle, index):
    '''https://developer.vectorworks.net/index.php?title=VS:DeleteWallPeak
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeleteWallPeak/ja
    \n指定した番号の壁の頂点を削除します。'''
    return None

def GetWallCompStartPts(wall, componentIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallCompStartPts
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWallCompStartPts/ja
    \n壁の構成要素の始点の座標を取得します。'''
    return (leftPoint, centerPoint, rightPoint)

def SetIsCurtainWall(wall, isCurtainWall):
    '''https://developer.vectorworks.net/index.php?title=VS:SetIsCurtainWall
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetIsCurtainWall/ja
    \n壁をカーテンウォールにする／しないを設定します。'''
    return None

def Wall(p1, p2):
    '''https://developer.vectorworks.net/index.php?title=VS:Wall
    \nhttps://developer.vectorworks.net/index.php?title=VS:Wall/ja
    \n指定した座標に壁を作成します。'''
    return None

def DeleteWallSym(symbolHd):
    '''https://developer.vectorworks.net/index.php?title=VS:DeleteWallSym
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeleteWallSym/ja
    \nハンドルで指定したシンボルを、選択された壁から削除します。削除に成功した場合はTRUEを返します。'''
    return BOOLEAN

def GetWallControlOffset():
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallControlOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWallControlOffset/ja
    \n壁のオフセットの値を返します。'''
    return REAL

def SetLayerDeltaZOffset(theWall, layerDeltaZOffset):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLayerDeltaZOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLayerDeltaZOffset/ja
    \nハンドルで指定した壁の高さの、レイヤの厚み（ΔZ）からのオフセット値を設定します。'''
    return BOOLEAN

def WallCap(atStart, closed, round, rightOffDistance, leftOffDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:WallCap
    \nhttps://developer.vectorworks.net/index.php?title=VS:WallCap/ja
    \n壁の端の処理を設定します。'''
    return None

def GetCWFramesFromPt(hWall, testPt, includeBottomFrame):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCWFramesFromPt
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCWFramesFromPt/ja
    \n壁のポイントからカーテンウォールのフレーム情報を取得します。カーテンウォールのパネルの中にオブジェクトを配置するために使用します。壁の中のオブジェクトの中心点を渡すと、カーテンウォールのパネルを探し出し、パネル周辺のフレームの情報を返します。'''
    return (BOOLEAN, panelThickness, panelOffset, frameInsetTop, frameInsetBottom, frameInsetRight, frameInsetLeft)

def GetWallCornerHeights(theWall):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallCornerHeights
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWallCornerHeights/ja
    \n壁または円弧壁のコーナーの高さを取得します。'''
    return (startHeightTop, startHeightBottom, endHeightTop, endHeightBottom)

def SetLinkHeightToLayerDeltaZ(theWall, linkToLayerDeltaZ):
    '''https://developer.vectorworks.net/index.php?title=VS:SetLinkHeightToLayerDeltaZ
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetLinkHeightToLayerDeltaZ/ja
    \nハンドルで指定した壁の高さを、レイヤの厚み（ΔZ）にリンクする／しないを設定します。'''
    return BOOLEAN

def WallFootPrint(wallHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:WallFootPrint
    \nhttps://developer.vectorworks.net/index.php?title=VS:WallFootPrint/ja
    \n壁の設置跡を表す曲線を作成し、そのハンドルを返します。'''
    return HANDLE

def GetCWPanelFromPt(hWall, testPt, includeBottomFrame):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCWPanelFromPt
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCWPanelFromPt/ja
    \nカーテンウォールの指定した点にあるパネルに関する情報を返します。カーテンウォールのパネルの中にオブジェクトを配置するために使用します。壁の中のオブジェクトの中心点を渡すと、カーテンウォールのパネルを探し出し、パネルの中心点、高さ、幅を返します。'''
    return (BOOLEAN, centerPt, width, height)

def GetWallHalfBreakInfo(wallH, breakIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallHalfBreakInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWallHalfBreakInfo/ja
    \n壁の線に沿った、壁内の半破断線の始点、中心点、終点を取得します。'''
    return (BOOLEAN, startPt, centerPt, endPt)

def SetObjWallBreakMode(objH, wallH, breakMode):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjWallBreakMode
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetObjWallBreakMode/ja
    \n壁に挿入したオブジェクトの、壁の処理モードを設定します。'''
    return Boolean

def WallHeight(wallHd):
    '''https://developer.vectorworks.net/index.php?title=VS:WallHeight
    \nhttps://developer.vectorworks.net/index.php?title=VS:WallHeight/ja
    \nハンドルで指定した壁の始点と終点の高さを返します。'''
    return (startHt, endHt)

def GetCurtainWallCutPl(wall):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCurtainWallCutPl
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCurtainWallCutPl/ja
    \nカーテンウォールの断面高さを取得します。'''
    return REAL

def GetWallOverallHeights(theWall):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallOverallHeights
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWallOverallHeights/ja
    \n壁または円弧壁の全高を取得します。'''
    return (overallHeightTop, overallHeightBottom)

def SetObjWallInsLocOff(objectHandle, wallHandle, insertLocationOffset):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjWallInsLocOff'''
    return BOOLEAN

def WallPeak(alongDistance, heightDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:WallPeak
    \nhttps://developer.vectorworks.net/index.php?title=VS:WallPeak/ja
    \n壁の上部に頂点を追加します。'''
    return None

def GetLayerDeltaZOffset(theWall):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLayerDeltaZOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLayerDeltaZOffset/ja
    \nハンドルで指定した壁の、レイヤの厚み（ΔZ）からのオフセット値を返します。'''
    return REAL

def GetWallPathType(wall):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallPathType'''
    return INTEGER

def SetObjWallInsertMode(objH, wallH, insertMode):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjWallInsertMode
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetObjWallInsertMode/ja
    \n壁に挿入したオブジェクトの、壁への挿入位置を設定します。'''
    return Boolean

def WallTo(p):
    '''https://developer.vectorworks.net/index.php?title=VS:WallTo
    \nhttps://developer.vectorworks.net/index.php?title=VS:WallTo/ja
    \n現在のペン位置から指定した座標まで壁を作成します。'''
    return None

def GetLinkHeightToLayerDeltaZ(theWall):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLinkHeightToLayerDeltaZ
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLinkHeightToLayerDeltaZ/ja
    \nハンドルで指定した壁の高さが、レイヤの厚み（ΔZ）にリンクしている／いないを返します。'''
    return BOOLEAN

def GetWallPeak(h, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallPeak
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWallPeak/ja
    \nハンドルで指定した壁の頂点座標を返します。'''
    return (xPeak, yPeak, zPeak)

def SetObjectAsCornerBreak(objH, wallH, cornerBreak):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjectAsCornerBreak
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetObjectAsCornerBreak/ja
    \n図形の頂点レコードのコーナー頂点フラグを設定します。'''
    return BOOLEAN

def WallWidth(wallHd):
    '''https://developer.vectorworks.net/index.php?title=VS:WallWidth
    \nhttps://developer.vectorworks.net/index.php?title=VS:WallWidth/ja
    \nハンドルで指定した壁の幅を返します。'''
    return REAL

def GetNumOfWallBreaks(wallH):
    '''https://developer.vectorworks.net/index.php?title=VS:GetNumOfWallBreaks
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNumOfWallBreaks/ja
    \nハンドルで指定した壁の、切断箇所数を返します。'''
    return (BOOLEAN, numWallBreaks)

def GetWallPerpOffOfData(wall, insertLocation, insertLocationOffset):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallPerpOffOfData'''
    return REAL

def SetObjectAsSpanBreak(objH, wallH, spanWallBreak):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjectAsSpanBreak
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetObjectAsSpanBreak/ja
    \n図形の頂点レコードの壁の長さに合わせるフラグを設定します。図形(objH)が壁(wallH)の中に含まれている必要があります。'''
    return BOOLEAN

def GetNumWallPeaks(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetNumWallPeaks
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNumWallPeaks/ja
    \nハンドルで指定した壁の頂点の数を返します。'''
    return INTEGER

def GetWallStyle(theWall):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWallStyle/ja
    \n壁スタイルの名前を返します。'''
    return STRING

def SetObjectWallHeight(objH, wallH, height):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjectWallHeight
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetObjectWallHeight/ja
    \n壁の中の図形の高さを設定します。 図形(objH)が壁(wallH)の中に含まれている必要があります。'''
    return BOOLEAN

def GetObjExtentsInWall(symH, wallH):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjExtentsInWall
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetObjExtentsInWall/ja
    \nハンドルで指定した壁に挿入されているプラグインオブジェクトまたはシンボルの、挿入位置の始点座標と終点座標を返します。'''
    return (BOOLEAN, startPt, endPt)

def GetWallThickness(h):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallThickness
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWallThickness/ja
    \n壁の厚みを返します。'''
    return (BOOLEAN, thicknessDist)

def SetObjectWallOffset(objH, wallH, offset):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjectWallOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetObjectWallOffset/ja
    \n壁の中の図形のオフセットを設定します。'''
    return BOOLEAN

def PDF_AnnotationsFromBlob(inBlobPtr, inBlobSize, inCurPage, boundsX, boundsY, ioSnapGeom):
    '''https://developer.vectorworks.net/index.php?title=VS:PDF_AnnotationsFromBlob
    \nhttps://developer.vectorworks.net/index.php?title=VS:PDF_AnnotationsFromBlob/ja
    \nPDFメモリ領域から注釈を描画します。'''
    return BOOLEAN

def PDF_FlushCache():
    '''https://developer.vectorworks.net/index.php?title=VS:PDF_FlushCache
    \nhttps://developer.vectorworks.net/index.php?title=VS:PDF_FlushCache/ja
    \n全てのドキュメントキャッシュ（Document Cache）を消去します。'''
    return BOOLEAN

def PDF_PrintBlob(inBlobPtr, inBlobSize, inSettings):
    '''https://developer.vectorworks.net/index.php?title=VS:PDF_PrintBlob
    \nhttps://developer.vectorworks.net/index.php?title=VS:PDF_PrintBlob/ja
    \nPDFメモリ領域からページを印刷します。'''
    return BOOLEAN

def PDF_ThreadInitialize():
    '''https://developer.vectorworks.net/index.php?title=VS:PDF_ThreadInitialize
    \nhttps://developer.vectorworks.net/index.php?title=VS:PDF_ThreadInitialize/ja
    \nライブラリはスレッドごとに初期化する必要があります。'''
    return BOOLEAN

def PDF_CreateBlob(inFilePath, ioBlobPtr, ioBlobSize, ioCurPage):
    '''https://developer.vectorworks.net/index.php?title=VS:PDF_CreateBlob
    \nhttps://developer.vectorworks.net/index.php?title=VS:PDF_CreateBlob/ja
    \n指定した書類のページを格納したメモリ領域を確保します。'''
    return BOOLEAN

def PDF_GetNumOfAnnotations(inBlobPtr, inBlobSize, inCurPage):
    '''https://developer.vectorworks.net/index.php?title=VS:PDF_GetNumOfAnnotations
    \nhttps://developer.vectorworks.net/index.php?title=VS:PDF_GetNumOfAnnotations/ja
    \nPDFのページにあるPDF注釈の数を返します。'''
    return BOOLEAN

def PDF_SetPageImage(inBlobPtr):
    '''https://developer.vectorworks.net/index.php?title=VS:PDF_SetPageImage
    \nhttps://developer.vectorworks.net/index.php?title=VS:PDF_SetPageImage/ja
    \nPDFページオブジェクトから、イメージを作成し、子の中に入れます。'''
    return BOOLEAN

def PDF_VerifyLibrary():
    '''https://developer.vectorworks.net/index.php?title=VS:PDF_VerifyLibrary
    \nhttps://developer.vectorworks.net/index.php?title=VS:PDF_VerifyLibrary/ja
    \nライブラリが準備されロードされていることを確認します。'''
    return BOOLEAN

def PDF_CreatePDFABlobFromBlob(inBlobPtr, inBlobSize, inPDFAFormat, ioBlobPtr, ioBlobSize):
    '''https://developer.vectorworks.net/index.php?title=VS:PDF_CreatePDFABlobFromBlob
    \nhttps://developer.vectorworks.net/index.php?title=VS:PDF_CreatePDFABlobFromBlob/ja
    \nメモリ領域からPDFA形式の領域を確保します'''
    return BOOLEAN

def PDF_GetPageCount(inFilePath):
    '''https://developer.vectorworks.net/index.php?title=VS:PDF_GetPageCount
    \nhttps://developer.vectorworks.net/index.php?title=VS:PDF_GetPageCount/ja
    \n選択した書類ファイルのページ数を返します。'''
    return INTEGER

def PDF_SetProgressBar(progressPtr, status):
    '''https://developer.vectorworks.net/index.php?title=VS:PDF_SetProgressBar
    \nhttps://developer.vectorworks.net/index.php?title=VS:PDF_SetProgressBar/ja
    \nPDF取り込みメニューコマンドのプログレスバーを設定します。'''
    return BOOLEAN

def PDF_DestroyBlob(ioBlobPtr):
    '''https://developer.vectorworks.net/index.php?title=VS:PDF_DestroyBlob
    \nhttps://developer.vectorworks.net/index.php?title=VS:PDF_DestroyBlob/ja
    \nメモリ領域を確保してコピーしたあとはこの関数を呼びメモリ領域を開放してください。'''
    return BOOLEAN

def PDF_GetPageMatrixFromBlob(inBlobPtr, inBlobSize, inCurPage, inMatrix):
    '''https://developer.vectorworks.net/index.php?title=VS:PDF_GetPageMatrixFromBlob
    \nhttps://developer.vectorworks.net/index.php?title=VS:PDF_GetPageMatrixFromBlob/ja
    \nPDFのデフォルトマトリックスを取得します。'''
    return BOOLEAN

def PDF_SnapGeomFromBlob(inBlobPtr, inBlobSize, inCurPage, boundsX, boundsY, ioSnapGeom):
    '''https://developer.vectorworks.net/index.php?title=VS:PDF_SnapGeomFromBlob
    \nhttps://developer.vectorworks.net/index.php?title=VS:PDF_SnapGeomFromBlob/ja
    \nPDFメモリ領域からベクトルグラフィックをioSnapGeomに収集します。'''
    return BOOLEAN

def PDF_DrawDCFromBlob(inBlobPtr, inBlobSize, inCurPage, inDC, inDrawMatrix, inInvalRect, inCancelCB):
    '''https://developer.vectorworks.net/index.php?title=VS:PDF_DrawDCFromBlob
    \nhttps://developer.vectorworks.net/index.php?title=VS:PDF_DrawDCFromBlob/ja
    \nPDF DocID を渡された DC へ描く'''
    return BOOLEAN

def PDF_GetPageSizeFromBlob(inBlobPtr, inBlobSize, inPageBoxID, inCurPage, outBoxLeft, outBoxTop, outBoxRight,  outBoxBottom):
    '''https://developer.vectorworks.net/index.php?title=VS:PDF_GetPageSizeFromBlob
    \nhttps://developer.vectorworks.net/index.php?title=VS:PDF_GetPageSizeFromBlob/ja
    \nメモリ領域から対応するページ領域の長方形を返します。'''
    return BOOLEAN

def PDF_ThreadDeInitialize():
    '''https://developer.vectorworks.net/index.php?title=VS:PDF_ThreadDeInitialize
    \nhttps://developer.vectorworks.net/index.php?title=VS:PDF_ThreadDeInitialize/ja
    \nスレッドが終了したときライブラリを初期化します。'''
    return BOOLEAN

def BuildConstraintModelForObject(h, traverseContainers):
    '''https://developer.vectorworks.net/index.php?title=VS:BuildConstraintModelForObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:BuildConstraintModelForObject/ja
    \n拘束マネージャーの指定した図形の拘束モデルを作成します。'''
    return None

def GetBinaryConstraint(constrType, obj1, obj2, obj1VertA, obj1VertB, obj2VertA, obj2VertB, containedObj1, containedObj2):
    '''https://developer.vectorworks.net/index.php?title=VS:GetBinaryConstraint
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetBinaryConstraint/ja
    \nハンドルで指定した図形間に設定されている拘束のハンドルを返します。'''
    return HANDLE

def HasConstraint(h):
    '''https://developer.vectorworks.net/index.php?title=VS:HasConstraint
    \nhttps://developer.vectorworks.net/index.php?title=VS:HasConstraint/ja
    \nハンドルで指定した図形が拘束されていた場合は、TRUEを返します。'''
    return BOOLEAN

def SetConstraintValue(constraint, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetConstraintValue
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetConstraintValue/ja
    \n拘束の値を設定します。'''
    return None

def DeleteConstraint(obj, constraint):
    '''https://developer.vectorworks.net/index.php?title=VS:DeleteConstraint
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeleteConstraint/ja
    \nハンドルで指定した図形から、指定した拘束を解除します。'''
    return None

def GetSingularConstraint(typeOfConstraint, obj, vertexA, vertexB):
    '''https://developer.vectorworks.net/index.php?title=VS:GetSingularConstraint
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSingularConstraint/ja
    \nハンドルで指定した図形に設定されている拘束のハンドルを返します。'''
    return HANDLE

def SetBinaryConstraint(typeOfConstraint, h1, h2, obj1VertA, obj1VertB, obj2VertA, obj2VertB, containedObj1, containedObj2):
    '''https://developer.vectorworks.net/index.php?title=VS:SetBinaryConstraint
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetBinaryConstraint/ja
    \n2つの図形に対して拘束を設定します。'''
    return BOOLEAN

def SetSingularConstraint(typeOfConstraint, h, vertexA, vertexB):
    '''https://developer.vectorworks.net/index.php?title=VS:SetSingularConstraint
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetSingularConstraint/ja
    \n1つの図形に対して拘束を設定します。'''
    return BOOLEAN

def Plant_CreateDupPlant(plantToCreateFrom):
    '''https://developer.vectorworks.net/index.php?title=VS:Plant_CreateDupPlant
    \nhttps://developer.vectorworks.net/index.php?title=VS:Plant_CreateDupPlant/ja
    \n現在選択されている植栽から新しい植栽を作成します。'''
    return None

def Plant_GetToolPlantNm():
    '''https://developer.vectorworks.net/index.php?title=VS:Plant_GetToolPlantNm
    \nhttps://developer.vectorworks.net/index.php?title=VS:Plant_GetToolPlantNm/ja
    \nツールがロードした植栽を取得します。'''
    return STRING

def Plant_ReplacePlant(plantToReplace):
    '''https://developer.vectorworks.net/index.php?title=VS:Plant_ReplacePlant
    \nhttps://developer.vectorworks.net/index.php?title=VS:Plant_ReplacePlant/ja
    \n選択されている植栽を置き換える。'''
    return None

def Plant_UpdatePlaceTool(plantToUpdateWith):
    '''https://developer.vectorworks.net/index.php?title=VS:Plant_UpdatePlaceTool
    \nhttps://developer.vectorworks.net/index.php?title=VS:Plant_UpdatePlaceTool/ja
    \n植栽がリソースブラウザーでダブルクリックされたら植栽ツールを更新します。'''
    return None

def Plant_EditPlantDefRB(plantToEdit):
    '''https://developer.vectorworks.net/index.php?title=VS:Plant_EditPlantDefRB
    \nhttps://developer.vectorworks.net/index.php?title=VS:Plant_EditPlantDefRB/ja
    \nユーザーがリソースブラウザーで植栽を編集したときに、定義を更新します。'''
    return None

def Plant_GetToolPlcMode():
    '''https://developer.vectorworks.net/index.php?title=VS:Plant_GetToolPlcMode
    \nhttps://developer.vectorworks.net/index.php?title=VS:Plant_GetToolPlcMode/ja
    \n植栽ツールの現在の配置モードを取得します。'''
    return INTEGER

def Plant_ReplacePlantParam(origPlantObj):
    '''https://developer.vectorworks.net/index.php?title=VS:Plant_ReplacePlantParam
    \nhttps://developer.vectorworks.net/index.php?title=VS:Plant_ReplacePlantParam/ja
    \n植栽のパラメータを置き換えます。'''
    return HANDLE

def Plant_UpdateTranslat(newSymbolName, oldID, newID, masterPlant, currentPlant):
    '''https://developer.vectorworks.net/index.php?title=VS:Plant_UpdateTranslat
    \nhttps://developer.vectorworks.net/index.php?title=VS:Plant_UpdateTranslat/ja
    \n植栽レコードを新しいIDで更新します。'''
    return None

def Plant_GetToolInit():
    '''https://developer.vectorworks.net/index.php?title=VS:Plant_GetToolInit
    \nhttps://developer.vectorworks.net/index.php?title=VS:Plant_GetToolInit/ja
    \n植栽ツールが初期化されていればTRUEを返します。'''
    return BOOLEAN

def Plant_GetToolSpacing():
    '''https://developer.vectorworks.net/index.php?title=VS:Plant_GetToolSpacing
    \nhttps://developer.vectorworks.net/index.php?title=VS:Plant_GetToolSpacing/ja
    \n植栽ツールの配置間隔を取得します。'''
    return REAL

def Plant_ResetPlantInst(plantSymbolName):
    '''https://developer.vectorworks.net/index.php?title=VS:Plant_ResetPlantInst
    \nhttps://developer.vectorworks.net/index.php?title=VS:Plant_ResetPlantInst/ja
    \n編集された植栽シンボル定義の全てのシンボルをリセットします。'''
    return None

def GetCheckoutsComment():
    '''https://developer.vectorworks.net/index.php?title=VS:GetCheckoutsComment
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCheckoutsComment/ja
    \nチェックアウトと反映に使用されるコメントを返します。'''
    return (BOOLEAN, comment)

def GetProjectFullPath():
    '''https://developer.vectorworks.net/index.php?title=VS:GetProjectFullPath
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetProjectFullPath/ja
    \nプロジェクト共有用のプロジェクトファイルのパスとファイル名を返します。'''
    return (BOOLEAN, fullPath)

def GetProjectUserNames():
    '''https://developer.vectorworks.net/index.php?title=VS:GetProjectUserNames
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetProjectUserNames/ja
    \n現在のプロジェクトの一部であるユーザIDのリストを返します。'''
    return (BOOLEAN, userArray)

def IsProjectOffline():
    '''https://developer.vectorworks.net/index.php?title=VS:IsProjectOffline
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsProjectOffline/ja
    \n現在のファイルがオフラインモードで動作しているかチェックします。'''
    return BOOLEAN

def GetCurrentUserId():
    '''https://developer.vectorworks.net/index.php?title=VS:GetCurrentUserId
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCurrentUserId/ja
    \n現在のユーザのユーザIDを返します。'''
    return (BOOLEAN, userid)

def GetProjectName():
    '''https://developer.vectorworks.net/index.php?title=VS:GetProjectName'''
    return (BOOLEAN, name)

def GetWorkingFileId():
    '''https://developer.vectorworks.net/index.php?title=VS:GetWorkingFileId
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWorkingFileId/ja
    \nワーキングファイル固有のIDを返します。これはファイル名ではありません。'''
    return (BOOLEAN, uuid)

def SetCheckoutsComment(comment):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCheckoutsComment
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCheckoutsComment/ja
    \nチェックアウトと反映に使用されるコメントを設定します。'''
    return BOOLEAN

def GetLayerProjectInfo(layer):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLayerProjectInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLayerProjectInfo/ja
    \nプロジェクト共有ダイアログのレイヤタブにあるものに近い値を返します。'''
    return (BOOLEAN, masterLayer, modificationDate, checkoutDate, checkoutOwner, workingFileId, comment, outOfDate)

def GetProjectUser(userId):
    '''https://developer.vectorworks.net/index.php?title=VS:GetProjectUser
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetProjectUser/ja
    \n現在のプロジェクトのユーザの詳細を返します。'''
    return (BOOLEAN, fullName, permission)

def IsAWorkingFile():
    '''https://developer.vectorworks.net/index.php?title=VS:IsAWorkingFile
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsAWorkingFile/ja
    \n現在のファイルがプロジェクト共有のワーキングファイルの場合には、TRUEを返します。'''
    return BOOLEAN

def Prot_DisableModule(module):
    '''https://developer.vectorworks.net/index.php?title=VS:Prot_DisableModule'''
    return None

def Prot_GetLicenseID():
    '''https://developer.vectorworks.net/index.php?title=VS:Prot_GetLicenseID'''
    return STRING

def Prot_GetSeatsNum():
    '''https://developer.vectorworks.net/index.php?title=VS:Prot_GetSeatsNum
    \nhttps://developer.vectorworks.net/index.php?title=VS:Prot_GetSeatsNum/ja
    \nサーバで使用可能なライセンスの数を返します。'''
    return INTEGER

def Prot_IsFundamentals():
    '''https://developer.vectorworks.net/index.php?title=VS:Prot_IsFundamentals'''
    return BOOLEAN

def Prot_GetDistribCode():
    '''https://developer.vectorworks.net/index.php?title=VS:Prot_GetDistribCode'''
    return STRING

def Prot_GetLicenseType():
    '''https://developer.vectorworks.net/index.php?title=VS:Prot_GetLicenseType'''
    return LONGINT

def Prot_GetUsedSeatsNum():
    '''https://developer.vectorworks.net/index.php?title=VS:Prot_GetUsedSeatsNum
    \nhttps://developer.vectorworks.net/index.php?title=VS:Prot_GetUsedSeatsNum/ja
    \nネットワークで使用しているライセンスの数を返します。'''
    return INTEGER

def Prot_IsModuleEnabled(module):
    '''https://developer.vectorworks.net/index.php?title=VS:Prot_IsModuleEnabled'''
    return BOOLEAN

def Road_GetStationCount(hRoadwayObject):
    '''https://developer.vectorworks.net/index.php?title=VS:Road_GetStationCount
    \nhttps://developer.vectorworks.net/index.php?title=VS:Road_GetStationCount/ja
    \n道路（曲線）オブジェクトの測点の数を返します。'''
    return LONGINT

def Road_GetStationPoint(hRoadwayObject, index):
    '''https://developer.vectorworks.net/index.php?title=VS:Road_GetStationPoint
    \nhttps://developer.vectorworks.net/index.php?title=VS:Road_GetStationPoint/ja
    \n道路（曲線）オブジェクトの測点の3D座標を返します。'''
    return RETURN

def Road_InsertStation(hRoadwayObject, point):
    '''https://developer.vectorworks.net/index.php?title=VS:Road_InsertStation
    \nhttps://developer.vectorworks.net/index.php?title=VS:Road_InsertStation/ja
    \n道路（曲線）オブジェクトに新しい測点を配置します。'''
    return None

def DSelectAll():
    '''https://developer.vectorworks.net/index.php?title=VS:DSelectAll
    \nhttps://developer.vectorworks.net/index.php?title=VS:DSelectAll/ja
    \nアクティブなレイヤ上の、表示されているすべての図形の選択状態を解除します。'''
    return None

def NumSelectedObjects():
    '''https://developer.vectorworks.net/index.php?title=VS:NumSelectedObjects
    \nhttps://developer.vectorworks.net/index.php?title=VS:NumSelectedObjects/ja
    \n選択されている図形数を返します。'''
    return LONGINT

def Selected(h):
    '''https://developer.vectorworks.net/index.php?title=VS:Selected
    \nhttps://developer.vectorworks.net/index.php?title=VS:Selected/ja
    \nハンドルで指定した図形の選択状態を返します。図形が選択されている場合は、TRUEを返します。'''
    return BOOLEAN

def SetSelect(h):
    '''https://developer.vectorworks.net/index.php?title=VS:SetSelect
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetSelect/ja
    \nハンドルで指定した図形を選択します。'''
    return None

def NumSObj(h):
    '''https://developer.vectorworks.net/index.php?title=VS:NumSObj
    \nhttps://developer.vectorworks.net/index.php?title=VS:NumSObj/ja
    \nハンドルで指定したレイヤ上の、選択されている図形の数を返します。'''
    return LONGINT

def SelectAll():
    '''https://developer.vectorworks.net/index.php?title=VS:SelectAll
    \nhttps://developer.vectorworks.net/index.php?title=VS:SelectAll/ja
    \nアクティブなレイヤ上の、すべての図形を選択します。'''
    return None

def SetDSelect(h):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDSelect
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDSelect/ja
    \nハンドルで指定した図形の選択を解除します。'''
    return None

def DTM6_ClearModelCache(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:DTM6_ClearModelCache
    \nhttps://developer.vectorworks.net/index.php?title=VS:DTM6_ClearModelCache/ja
    \nサイトモデルのキャッシュをクリアします。'''
    return None

def DTM6_IsObjectReady(hDTMObject):
    '''https://developer.vectorworks.net/index.php?title=VS:DTM6_IsObjectReady
    \nhttps://developer.vectorworks.net/index.php?title=VS:DTM6_IsObjectReady/ja
    \nDTMオブジェクトが使用できるかどうかチェックします。もしFALSEが戻るなら、ハンドルのに「ResetObject」をするべきです。'''
    return BOOLEAN

def DTM6_ShowSendEdgeDlg(objWEdgeType):
    '''https://developer.vectorworks.net/index.php?title=VS:DTM6_ShowSendEdgeDlg
    \nhttps://developer.vectorworks.net/index.php?title=VS:DTM6_ShowSendEdgeDlg/ja
    \n造成辺を持つ造成図形に対して敷地表面に移動ダイアログを表示します。'''
    return INTEGER

def SetFenceAttrs(fFenceHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetFenceAttrs
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetFenceAttrs/ja
    \nハンドルで指定した図形に法面の属性を適用します。'''
    return None

def DTM6_GetDTMObject(hLayer, bPickUpModel):
    '''https://developer.vectorworks.net/index.php?title=VS:DTM6_GetDTMObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:DTM6_GetDTMObject/ja
    \nDTMを取得します。 それがドキュメントのレイヤの上の1であるだけであれば、それを返します。 多くのDTMsがあれば、1つを選ぶようにユーザに頼んでください。'''
    return HANDLE

def DTM6_IsTypeVisible(hDTMObject, TINType):
    '''https://developer.vectorworks.net/index.php?title=VS:DTM6_IsTypeVisible
    \nhttps://developer.vectorworks.net/index.php?title=VS:DTM6_IsTypeVisible/ja
    \n指定されたDTMタイプが目に見えるなら、TRUEが返ります。'''
    return BOOLEAN

def DegFromStr(fSlopeDef, fSlopeValue):
    '''https://developer.vectorworks.net/index.php?title=VS:DegFromStr
    \nhttps://developer.vectorworks.net/index.php?title=VS:DegFromStr/ja
    \n勾配を表す文字列を、角度(deg)の実数値に変換します。'''
    return (BOOLEAN, fAngle)

def SetPadAttrs(hPadHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetPadAttrs
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetPadAttrs/ja
    \nハンドルで指定した図形に造成面の属性を適用します。'''
    return None

def DTM6_GetDTMOver(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:DTM6_GetDTMOver
    \nhttps://developer.vectorworks.net/index.php?title=VS:DTM6_GetDTMOver/ja
    \n指定されたオブジェクトの上にDTMを取得します。'''
    return HANDLE

def DTM6_RestoreDefaults(hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:DTM6_RestoreDefaults
    \nhttps://developer.vectorworks.net/index.php?title=VS:DTM6_RestoreDefaults/ja
    \nサイトモデルの設定をデフォルトに戻します。'''
    return None

def MakeModifierClass(modifierClass):
    '''https://developer.vectorworks.net/index.php?title=VS:MakeModifierClass
    \nhttps://developer.vectorworks.net/index.php?title=VS:MakeModifierClass/ja
    \n造成図形のクラスを作成します。'''
    return None

def DTM6_GetZatXY(hDTMObject, TINType, x, y):
    '''https://developer.vectorworks.net/index.php?title=VS:DTM6_GetZatXY
    \nhttps://developer.vectorworks.net/index.php?title=VS:DTM6_GetZatXY/ja
    \n指定されたDTMでx、yを指定されるところの高度を取得します。 DTMが存在していないか、またはDTMの外にポイントがあるなら、FALSEが返ります。 TINタイプ0: 現況地形 1: 計画地形 2: 計画+現況地形'''
    return (BOOLEAN, outZ)

def DTM6_RiseToSurface(hDTMObject, hObject, TINType, sendType):
    '''https://developer.vectorworks.net/index.php?title=VS:DTM6_RiseToSurface
    \nhttps://developer.vectorworks.net/index.php?title=VS:DTM6_RiseToSurface/ja
    \n与えられたオブジェクトがDTMの表面に配置されるように加工します。'''
    return BOOLEAN

def PercStrFromDeg(fSlopeDeg):
    '''https://developer.vectorworks.net/index.php?title=VS:PercStrFromDeg
    \nhttps://developer.vectorworks.net/index.php?title=VS:PercStrFromDeg/ja
    \n角度(deg)の勾配の値を、パーセントの表現に変換します。'''
    return STRING

def DTM6_IsDTM6Object(hDTMObject):
    '''https://developer.vectorworks.net/index.php?title=VS:DTM6_IsDTM6Object
    \nhttps://developer.vectorworks.net/index.php?title=VS:DTM6_IsDTM6Object/ja
    \nオブジェクトハンドルがSiteModelオブジェクトタイプであるかチェックします。'''
    return BOOLEAN

def DTM6_SendToSurface(hDTMObject, hObject, TINType):
    '''https://developer.vectorworks.net/index.php?title=VS:DTM6_SendToSurface
    \nhttps://developer.vectorworks.net/index.php?title=VS:DTM6_SendToSurface/ja
    \n渡されたオブジェクトをDTMの表面に載せます。'''
    return BOOLEAN

def RiseRunFromDeg(fSlopeDeg):
    '''https://developer.vectorworks.net/index.php?title=VS:RiseRunFromDeg
    \nhttps://developer.vectorworks.net/index.php?title=VS:RiseRunFromDeg/ja
    \n角度(deg)の勾配の値を、比率の表現に変換します。'''
    return STRING

def Space_AddAreaModifierToSpace(space, modifier):
    '''https://developer.vectorworks.net/index.php?title=VS:Space_AddAreaModifierToSpace'''
    return None

def Space_CountAssignedZones(space):
    '''https://developer.vectorworks.net/index.php?title=VS:Space_CountAssignedZones
    \nhttps://developer.vectorworks.net/index.php?title=VS:Space_CountAssignedZones/ja
    \nスペース図形に割り当てられたゾーンの数を返します。'''
    return INTEGER

def Space_GetGrossVolume(space):
    '''https://developer.vectorworks.net/index.php?title=VS:Space_GetGrossVolume
    \nhttps://developer.vectorworks.net/index.php?title=VS:Space_GetGrossVolume/ja
    \n指定したスペース図形の体積(グロス)の値を返します。'''
    return REAL

def Space_ItemAvailableZones(item):
    '''https://developer.vectorworks.net/index.php?title=VS:Space_ItemAvailableZones
    \nhttps://developer.vectorworks.net/index.php?title=VS:Space_ItemAvailableZones/ja
    \nスペース図形に割り当て可能なゾーンの名前を返します。'''
    return STRING

def Space_AddDiscription(space, discription):
    '''https://developer.vectorworks.net/index.php?title=VS:Space_AddDiscription'''
    return None

def Space_CountAvailableZones():
    '''https://developer.vectorworks.net/index.php?title=VS:Space_CountAvailableZones
    \nhttps://developer.vectorworks.net/index.php?title=VS:Space_CountAvailableZones/ja
    \nスペースツールで使用可能なゾーンの数を返します。'''
    return INTEGER

def Space_GetNetArea(space):
    '''https://developer.vectorworks.net/index.php?title=VS:Space_GetNetArea
    \nhttps://developer.vectorworks.net/index.php?title=VS:Space_GetNetArea/ja
    \n指定したスペース図形の面積(ネット)の値を返します。'''
    return REAL

def Space_Net3DBoundary(space):
    '''https://developer.vectorworks.net/index.php?title=VS:Space_Net3DBoundary
    \nhttps://developer.vectorworks.net/index.php?title=VS:Space_Net3DBoundary/ja
    \n指定したスペース図形の3D高さ基準(ネット)のハンドルを返します。'''
    return HANDLE

def Space_AddName(space, name):
    '''https://developer.vectorworks.net/index.php?title=VS:Space_AddName'''
    return None

def Space_CreateSpace(space, spaceHeight):
    '''https://developer.vectorworks.net/index.php?title=VS:Space_CreateSpace
    \nhttps://developer.vectorworks.net/index.php?title=VS:Space_CreateSpace/ja
    \n指定した多角形からスペース図形を作成します。'''
    return HANDLE

def Space_GetNetPoly(space):
    '''https://developer.vectorworks.net/index.php?title=VS:Space_GetNetPoly
    \nhttps://developer.vectorworks.net/index.php?title=VS:Space_GetNetPoly/ja
    \n指定したスペース図形の境界線(ネット)から多角形を作成し、そのハンドルを返します。'''
    return HANDLE

def Space_RenameAssignedZoneX(space, index, zoneType, zoneName):
    '''https://developer.vectorworks.net/index.php?title=VS:Space_RenameAssignedZoneX'''
    return None

def Space_AddRoomID(space, roomID):
    '''https://developer.vectorworks.net/index.php?title=VS:Space_AddRoomID'''
    return None

def Space_DeassignZone(space, zoneType, zoneName):
    '''https://developer.vectorworks.net/index.php?title=VS:Space_DeassignZone'''
    return None

def Space_GetNetVolume(space):
    '''https://developer.vectorworks.net/index.php?title=VS:Space_GetNetVolume
    \nhttps://developer.vectorworks.net/index.php?title=VS:Space_GetNetVolume/ja
    \n指定したスペース図形の体積(ネット)の値を返します。'''
    return REAL

def Space_Set3DGrossHeightOffset(space, offset, selObj):
    '''https://developer.vectorworks.net/index.php?title=VS:Space_Set3DGrossHeightOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:Space_Set3DGrossHeightOffset/ja
    \n指定したスペース図形の3D高さ基準のグロスオフセットの値を設定します。'''
    return None

def Space_AddZone(zoneType, zoneName):
    '''https://developer.vectorworks.net/index.php?title=VS:Space_AddZone'''
    return None

def Space_GetGrossArea(space):
    '''https://developer.vectorworks.net/index.php?title=VS:Space_GetGrossArea
    \nhttps://developer.vectorworks.net/index.php?title=VS:Space_GetGrossArea/ja
    \n指定したスペース図形の面積(グロス)の値を返します。'''
    return REAL

def Space_Gross3DBoundary(space):
    '''https://developer.vectorworks.net/index.php?title=VS:Space_Gross3DBoundary
    \nhttps://developer.vectorworks.net/index.php?title=VS:Space_Gross3DBoundary/ja
    \n指定したスペース図形の3D高さ基準(グロス)のハンドルを返します。'''
    return HANDLE

def Space_Set3DGrossHeightOffset1(space, offset, selObj):
    '''https://developer.vectorworks.net/index.php?title=VS:Space_Set3DGrossHeightOffset1'''
    return None

def Space_AssignZone(space, zoneType, zoneName):
    '''https://developer.vectorworks.net/index.php?title=VS:Space_AssignZone
    \nhttps://developer.vectorworks.net/index.php?title=VS:Space_AssignZone/ja
    \nスペース図形にゾーンの割り当てを行います。'''
    return None

def Space_GetGrossPoly(space):
    '''https://developer.vectorworks.net/index.php?title=VS:Space_GetGrossPoly
    \nhttps://developer.vectorworks.net/index.php?title=VS:Space_GetGrossPoly/ja
    \n指定したスペース図形の境界線(グロス)から多角形を作成し、そのハンドルを返します。'''
    return HANDLE

def Space_ItemAssignedZones(space, item):
    '''https://developer.vectorworks.net/index.php?title=VS:Space_ItemAssignedZones
    \nhttps://developer.vectorworks.net/index.php?title=VS:Space_ItemAssignedZones/ja
    \nスペース図形に割り当て済みのゾーンの名前を返します。'''
    return STRING

def Space_Set3DNetHeightOffset(space, offset, selObj):
    '''https://developer.vectorworks.net/index.php?title=VS:Space_Set3DNetHeightOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:Space_Set3DNetHeightOffset/ja
    \n指定したスペース図形の3D高さ基準のネットオフセットの値を設定します。'''
    return None

def QTCloseMovieFile(movieRef):
    '''https://developer.vectorworks.net/index.php?title=VS:QTCloseMovieFile
    \nhttps://developer.vectorworks.net/index.php?title=VS:QTCloseMovieFile/ja
    \n指定したQuickTimeファイルを閉じます。'''
    return None

def QTGetMovieOptions(movieRef):
    '''https://developer.vectorworks.net/index.php?title=VS:QTGetMovieOptions
    \nhttps://developer.vectorworks.net/index.php?title=VS:QTGetMovieOptions/ja
    \n指定したQuickTimeファイルに設定されているフレームと基本フレーム単位の情報を返します。'''
    return (frameRate, keyFrameRate)

def QTOpenMovieFile(fileName):
    '''https://developer.vectorworks.net/index.php?title=VS:QTOpenMovieFile
    \nhttps://developer.vectorworks.net/index.php?title=VS:QTOpenMovieFile/ja
    \nQuickTimeファイルを作成または開きます。'''
    return INTEGER

def QTSetMovieOptionsN(movieRef, frameRate, keyFrameRate, useDLG, useDlgPreview, frameWidth, frameHeight):
    '''https://developer.vectorworks.net/index.php?title=VS:QTSetMovieOptionsN'''
    return None

def QTCloseMovieFileN(movieRef):
    '''https://developer.vectorworks.net/index.php?title=VS:QTCloseMovieFileN'''
    return None

def QTGetMovieOptionsN(movieRef):
    '''https://developer.vectorworks.net/index.php?title=VS:QTGetMovieOptionsN'''
    return (frameRate, keyFrameRate, frameWidth, frameHeight)

def QTOpenMovieFileN(movieRef, fileName, frameWidth, frameHeight):
    '''https://developer.vectorworks.net/index.php?title=VS:QTOpenMovieFileN'''
    return INTEGER

def QTTerminate():
    '''https://developer.vectorworks.net/index.php?title=VS:QTTerminate
    \nhttps://developer.vectorworks.net/index.php?title=VS:QTTerminate/ja
    \nQuickTimeが動作しないようにします。'''
    return None

def QTCreateMovieRefID():
    '''https://developer.vectorworks.net/index.php?title=VS:QTCreateMovieRefID'''
    return INTEGER

def QTInitialize():
    '''https://developer.vectorworks.net/index.php?title=VS:QTInitialize
    \nhttps://developer.vectorworks.net/index.php?title=VS:QTInitialize/ja
    \nQuickTimeを初期化し、QuickTimeのバージョンを返します。'''
    return INTEGER

def QTSetMovieOptions(movieRef, frameRate, keyFrameRate, useDlg, useDlgPreview):
    '''https://developer.vectorworks.net/index.php?title=VS:QTSetMovieOptions
    \nhttps://developer.vectorworks.net/index.php?title=VS:QTSetMovieOptions/ja
    \nQuickTimeファイルのフレームと基本フレーム単位を設定します。'''
    return None

def QTWriteFrame(movieRef):
    '''https://developer.vectorworks.net/index.php?title=VS:QTWriteFrame
    \nhttps://developer.vectorworks.net/index.php?title=VS:QTWriteFrame/ja
    \n現在の画面をQuickTimeファイルへ書き出します。'''
    return None

def AdditionalDefRecords():
    '''https://developer.vectorworks.net/index.php?title=VS:AdditionalDefRecords
    \nhttps://developer.vectorworks.net/index.php?title=VS:AdditionalDefRecords/ja
    \nデフォルトレコードフォーマットを追加ダイアログを表示します。'''
    return None

def DBeam_SetBShutDepth(depth):
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_SetBShutDepth
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_SetBShutDepth/ja'''
    return None

def HO_GetHoistColorLbl(value, maxValue):
    '''https://developer.vectorworks.net/index.php?title=VS:HO_GetHoistColorLbl'''
    return (BOOLEAN, colorIndex)

def LDevice_ResetVisual(h):
    '''https://developer.vectorworks.net/index.php?title=VS:LDevice_ResetVisual
    \nhttps://developer.vectorworks.net/index.php?title=VS:LDevice_ResetVisual/ja
    \n指定した照明器具の描画キャッシュをきれいにします。'''
    return None

def ApplyLightInfoRecord(hSymboL, hObject):
    '''https://developer.vectorworks.net/index.php?title=VS:ApplyLightInfoRecord
    \nhttps://developer.vectorworks.net/index.php?title=VS:ApplyLightInfoRecord/ja
    \nシンボルから図形に、光源情報をわたします。'''
    return None

def DBeam_SetBeamAngle(angle):
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_SetBeamAngle
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_SetBeamAngle/ja'''
    return None

def HO_GetHoistOriginAt(index):
    '''https://developer.vectorworks.net/index.php?title=VS:HO_GetHoistOriginAt'''
    return STRING

def LDevice_SetAccCell(handle, cellIndex, accessoryIndex, newCellIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:LDevice_SetAccCell'''
    return None

def DBeam_Begin():
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_Begin
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_Begin/ja
    \n照射ルーチンの描画スタート'''
    return None

def DBeam_SetBeamAngle2(angle):
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_SetBeamAngle2
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_SetBeamAngle2/ja'''
    return None

def HO_GetNumHoistOrigin():
    '''https://developer.vectorworks.net/index.php?title=VS:HO_GetNumHoistOrigin'''
    return LONGINT

def LDevice_SetAccPos2D(handle, cellIndex, accessoryIndex, position, rotation):
    '''https://developer.vectorworks.net/index.php?title=VS:LDevice_SetAccPos2D'''
    return None

def DBeam_BeginShttGet():
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_BeginShttGet
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_BeginShttGet/ja
    \n3次元シャッターオブジェクトの生成のスタート'''
    return None

def DBeam_SetFallOffDist(dist):
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_SetFallOffDist
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_SetFallOffDist/ja'''
    return None

def IsLDSchematicViewObj(handle):
    '''https://developer.vectorworks.net/index.php?title=VS:IsLDSchematicViewObj'''
    return BOOLEAN

def LDevice_SetAccPos3D(handle, cellIndex, accessoryIndex, position3D, rotation3D):
    '''https://developer.vectorworks.net/index.php?title=VS:LDevice_SetAccPos3D'''
    return None

def DBeam_End():
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_End
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_End/ja
    \n照射ルーチンの描画エンド'''
    return None

def DBeam_SetFocusPoint(pt):
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_SetFocusPoint
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_SetFocusPoint/ja
    \n照明器具のフォーカスポイントを設定します。'''
    return None

def LDevice_AddAccessory(handle, cellIndex, accessorySymbol):
    '''https://developer.vectorworks.net/index.php?title=VS:LDevice_AddAccessory'''
    return LONGINT

def LDevice_SetParamBool(handle, cellIndex, accessoryIndex, universalName, newValue):
    '''https://developer.vectorworks.net/index.php?title=VS:LDevice_SetParamBool'''
    return None

def DBeam_EndShttGet(bUseLampRotFlag):
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_EndShttGet
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_EndShttGet/ja
    \n3次元シャッターオブジェクトの生成のエンド'''
    return None

def DBeam_SetLShutAngle(angle):
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_SetLShutAngle
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_SetLShutAngle/ja'''
    return None

def LDevice_DeleteAcc(handle, cellIndex, accessoryIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:LDevice_DeleteAcc'''
    return None

def LDevice_SetParamLong(handle, cellIndex, accessoryIndex, universalName, newValue):
    '''https://developer.vectorworks.net/index.php?title=VS:LDevice_SetParamLong'''
    return None

def DBeam_Get2DLines():
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_Get2DLines
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_Get2DLines/ja
    \n最も最近作った、照明オブジェクトのハンドルを返します。'''
    return HANDLE

def DBeam_SetLShutDepth(depth):
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_SetLShutDepth
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_SetLShutDepth/ja'''
    return None

def LDevice_DlgResource(LayoutID, ControlID, SymbolName):
    '''https://developer.vectorworks.net/index.php?title=VS:LDevice_DlgResource'''
    return None

def LDevice_SetParamReal(handle, cellIndex, accessoryIndex, universalName, newValue):
    '''https://developer.vectorworks.net/index.php?title=VS:LDevice_SetParamReal'''
    return None

def DBeam_Get2DLn2FOff():
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_Get2DLn2FOff
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_Get2DLn2FOff/ja
    \n最も最近作った、照明オブジェクトのハンドルを返します。'''
    return HANDLE

def DBeam_SetLampRot(rot):
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_SetLampRot
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_SetLampRot/ja'''
    return None

def LDevice_GetAccCount(handle, cellIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:LDevice_GetAccCount'''
    return LONGINT

def LDevice_SetParamStr(handle, cellIndex, accessoryIndex, universalName, newValue):
    '''https://developer.vectorworks.net/index.php?title=VS:LDevice_SetParamStr'''
    return None

def DBeam_Get2DObjAtFs():
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_Get2DObjAtFs
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_Get2DObjAtFs/ja
    \n最も最近作った、照明オブジェクトのハンドルを返します。'''
    return HANDLE

def DBeam_SetLightOrigin(origin):
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_SetLightOrigin
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_SetLightOrigin/ja
    \n照明器具の原点を設定します。'''
    return None

def LDevice_GetAccPos2D(handle, cellIndex, accessoryIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:LDevice_GetAccPos2D'''
    return (outPosition, outRotation)

def LightingInvExport():
    '''https://developer.vectorworks.net/index.php?title=VS:LightingInvExport
    \nhttps://developer.vectorworks.net/index.php?title=VS:LightingInvExport/ja
    \n照明器具インベントリをデータ交換ファイルに出力します。'''
    return None

def DBeam_Get2DObjFOff():
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_Get2DObjFOff
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_Get2DObjFOff/ja
    \n最も最近作った、照明オブジェクトのハンドルを返します。'''
    return HANDLE

def DBeam_SetRShutAngle(angle):
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_SetRShutAngle
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_SetRShutAngle/ja'''
    return None

def LDevice_GetAccPos3D(handle, cellIndex, accessoryIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:LDevice_GetAccPos3D'''
    return (outPosition3D, outRotation3D)

def LightingInvImport():
    '''https://developer.vectorworks.net/index.php?title=VS:LightingInvImport
    \nhttps://developer.vectorworks.net/index.php?title=VS:LightingInvImport/ja
    \n照明器具インベントリをデータ交換ファイルから取り込みます。 取り込みに成功した場合TRUEを返します。'''
    return BOOLEAN

def DBeam_Get3DShutter():
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_Get3DShutter
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_Get3DShutter/ja
    \n3次元シャッターオブジェクトのハンドルを返します。'''
    return HANDLE

def DBeam_SetRShutDepth(depth):
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_SetRShutDepth
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_SetRShutDepth/ja'''
    return None

def LDevice_GetActSym():
    '''https://developer.vectorworks.net/index.php?title=VS:LDevice_GetActSym'''
    return HANDLE

def LightingUnivExport():
    '''https://developer.vectorworks.net/index.php?title=VS:LightingUnivExport
    \nhttps://developer.vectorworks.net/index.php?title=VS:LightingUnivExport/ja
    \n照明器具のユニバースの設定をデータ交換ファイルに出力します。'''
    return None

def DBeam_GetLast2DObj():
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_GetLast2DObj
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_GetLast2DObj/ja
    \n最も最近作った、２次元照明オブジェクトのハンドルを返します。'''
    return HANDLE

def DBeam_SetShow3DType(typeFlag):
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_SetShow3DType
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_SetShow3DType/ja'''
    return None

def LDevice_GetCellCount(handle):
    '''https://developer.vectorworks.net/index.php?title=VS:LDevice_GetCellCount'''
    return LONGINT

def LightingUnivImport():
    '''https://developer.vectorworks.net/index.php?title=VS:LightingUnivImport
    \nhttps://developer.vectorworks.net/index.php?title=VS:LightingUnivImport/ja
    \n照明器具のユニバースの設定をデータ交換ファイルを取り込みます。 取り込みに成功した場合TRUEを返します。'''
    return BOOLEAN

def DBeam_GetLastObject():
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_GetLastObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_GetLastObject/ja
    \n最も最近作った、照明オブジェクトのハンドルを返します。'''
    return HANDLE

def DBeam_SetShowAtPoint(showFlag):
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_SetShowAtPoint
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_SetShowAtPoint/ja'''
    return None

def LDevice_GetParamBool(handle, cellIndex, accessoryIndex, universalName):
    '''https://developer.vectorworks.net/index.php?title=VS:LDevice_GetParamBool'''
    return BOOLEAN

def SL_Export(exportType, instHand, fieldName):
    '''https://developer.vectorworks.net/index.php?title=VS:SL_Export
    \nhttps://developer.vectorworks.net/index.php?title=VS:SL_Export/ja
    \nスポットライトデータをXMLファイルに取り出す。'''
    return None

def DBeam_GetLines():
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_GetLines
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_GetLines/ja
    \n最も最近作った、照明オブジェクトのハンドルを返します。'''
    return HANDLE

def DBeam_SetTShutAngle(angle):
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_SetTShutAngle
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_SetTShutAngle/ja'''
    return None

def LDevice_GetParamLong(handle, cellIndex, accessoryIndex, universalName):
    '''https://developer.vectorworks.net/index.php?title=VS:LDevice_GetParamLong'''
    return LONGINT

def SL_Import(paramSelfHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:SL_Import
    \nhttps://developer.vectorworks.net/index.php?title=VS:SL_Import/ja
    \nXMLファイルからスポットライトデータを取り込む。'''
    return None

def DBeam_GetLines2FOff():
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_GetLines2FOff
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_GetLines2FOff/ja
    \n最も最近作った、照明オブジェクトのハンドルを返します。'''
    return HANDLE

def DBeam_SetTShutDepth(depth):
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_SetTShutDepth
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_SetTShutDepth/ja'''
    return None

def LDevice_GetParamReal(handle, cellIndex, accessoryIndex, universalName):
    '''https://developer.vectorworks.net/index.php?title=VS:LDevice_GetParamReal'''
    return REAL

def SL_UpdateSAcc(InstHand, InstUID):
    '''https://developer.vectorworks.net/index.php?title=VS:SL_UpdateSAcc
    \nhttps://developer.vectorworks.net/index.php?title=VS:SL_UpdateSAcc/ja
    \nデータ交換ファイルの既存の静的アクセサリーUIDを更新します。'''
    return None

def DBeam_GetObjAtFocus():
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_GetObjAtFocus
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_GetObjAtFocus/ja
    \n最も最近作った、照明オブジェクトのハンドルを返します。'''
    return HANDLE

def DBeam_ShowBeamLines(showFlag):
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_ShowBeamLines
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_ShowBeamLines/ja'''
    return None

def LDevice_GetParamStr(handle, cellIndex, accessoryIndex, universalName):
    '''https://developer.vectorworks.net/index.php?title=VS:LDevice_GetParamStr'''
    return STRING

def SL_UpdateUID(oldUID, newUID):
    '''https://developer.vectorworks.net/index.php?title=VS:SL_UpdateUID
    \nhttps://developer.vectorworks.net/index.php?title=VS:SL_UpdateUID/ja
    \nデータ交換ファイルの既存ののUIDを変更します。'''
    return None

def DBeam_GetObjFallOff():
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_GetObjFallOff
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_GetObjFallOff/ja
    \n最も最近作った、照明オブジェクトのハンドルを返します。'''
    return HANDLE

def GetLoadParent(handle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLoadParent'''
    return HANDLE

def LDevice_ReleaseRes():
    '''https://developer.vectorworks.net/index.php?title=VS:LDevice_ReleaseRes'''
    return None

def SetVisionMapping(color, universe, gobo, name, channel):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVisionMapping'''
    return None

def DBeam_SetBShutAngle(angle):
    '''https://developer.vectorworks.net/index.php?title=VS:DBeam_SetBShutAngle
    \nhttps://developer.vectorworks.net/index.php?title=VS:DBeam_SetBShutAngle/ja'''
    return None

def GetVisionMapping():
    '''https://developer.vectorworks.net/index.php?title=VS:GetVisionMapping'''
    return (color, universe, gobo, name, channel)

def LDevice_Reset(h):
    '''https://developer.vectorworks.net/index.php?title=VS:LDevice_Reset
    \nhttps://developer.vectorworks.net/index.php?title=VS:LDevice_Reset/ja
    \n指定した照明器具図形をリセットします。'''
    return None

def Angle2Str(value):
    '''https://developer.vectorworks.net/index.php?title=VS:Angle2Str
    \nhttps://developer.vectorworks.net/index.php?title=VS:Angle2Str/ja
    \n現在のファイルの設定を用いて、角度値を実数から文字列に変換します。'''
    return STRING

def GetResourceString(id, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetResourceString
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetResourceString/ja
    \nリソースファイルから文字列を返します。'''
    return theString

def Num2StrF(vDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:Num2StrF
    \nhttps://developer.vectorworks.net/index.php?title=VS:Num2StrF/ja
    \n実数を文字列に変換します。数値は現在の画面上の単位で表します。'''
    return STRING

def Str2Volume(str):
    '''https://developer.vectorworks.net/index.php?title=VS:Str2Volume
    \nhttps://developer.vectorworks.net/index.php?title=VS:Str2Volume/ja
    \n体積値の文字列表現を実数に変換します。'''
    return REAL

def Area2Str(value):
    '''https://developer.vectorworks.net/index.php?title=VS:Area2Str
    \nhttps://developer.vectorworks.net/index.php?title=VS:Area2Str/ja
    \n現在のファイルの設定を用いて、面積値を実数から文字列に変換します。'''
    return STRING

def GetVWRString(resIdentifier, stringIdentifier):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVWRString
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVWRString/ja
    \nGetResourceStringの代わりに使う。 -- VWR ファイルから文字列を読み出す。'''
    return outputString

def Ord(v):
    '''https://developer.vectorworks.net/index.php?title=VS:Ord
    \nhttps://developer.vectorworks.net/index.php?title=VS:Ord/ja
    \n指定したキャラクタのASCIIコードを返します。'''
    return INTEGER

def SubString(text, delimiter, index):
    '''https://developer.vectorworks.net/index.php?title=VS:SubString
    \nhttps://developer.vectorworks.net/index.php?title=VS:SubString/ja
    \nSubString はdelimiterの文字でtext文字列を分解し、index番目のトークンを返します。最初のトークンは、1番である。エラーの場合は、(空文字列)を返します。indexが1より小さいか、トークン数よりも大きい場合、(空文字列)を返します。'''
    return DYNARRAY[] of CHAR

def Chr(v):
    '''https://developer.vectorworks.net/index.php?title=VS:Chr
    \nhttps://developer.vectorworks.net/index.php?title=VS:Chr/ja
    \n指定したASCIIコードのキャラクタを返します。ASCIIコードの値の範囲は1から255です。'''
    return CHAR

def Insert(source, index):
    '''https://developer.vectorworks.net/index.php?title=VS:Insert
    \nhttps://developer.vectorworks.net/index.php?title=VS:Insert/ja
    \n指定した文字列を、指定した位置に挿入します。'''
    return dest

def Pos(subStr, str):
    '''https://developer.vectorworks.net/index.php?title=VS:Pos
    \nhttps://developer.vectorworks.net/index.php?title=VS:Pos/ja
    \n指定した文字列から指定した文字を検索し、その位置を返します。該当する文字が含まれていない場合は0が返されます。'''
    return INTEGER

def UniChr(v):
    '''https://developer.vectorworks.net/index.php?title=VS:UniChr'''
    return STRING

def Concat(txt):
    '''https://developer.vectorworks.net/index.php?title=VS:Concat
    \nhttps://developer.vectorworks.net/index.php?title=VS:Concat/ja
    \n指定したすべての文字列を連結します。'''
    return DYNARRAY[] of CHAR

def Len(v):
    '''https://developer.vectorworks.net/index.php?title=VS:Len
    \nhttps://developer.vectorworks.net/index.php?title=VS:Len/ja
    \n指定した文字列の文字数を返します。'''
    return INTEGER

def Str2Angle(str):
    '''https://developer.vectorworks.net/index.php?title=VS:Str2Angle
    \nhttps://developer.vectorworks.net/index.php?title=VS:Str2Angle/ja
    \n角度値の文字列表現を実数に変換します。'''
    return REAL

def UprString(str):
    '''https://developer.vectorworks.net/index.php?title=VS:UprString
    \nhttps://developer.vectorworks.net/index.php?title=VS:UprString/ja
    \n指定した文字列をすべて大文字に変換します。'''
    return str

def Copy(source, index, count):
    '''https://developer.vectorworks.net/index.php?title=VS:Copy
    \nhttps://developer.vectorworks.net/index.php?title=VS:Copy/ja
    \n指定した文字列から、指定した位置と長さの文字列を返します。'''
    return DYNARRAY[] of CHAR

def LenEncoding(v, encoding):
    '''https://developer.vectorworks.net/index.php?title=VS:LenEncoding'''
    return INTEGER

def Str2Area(str):
    '''https://developer.vectorworks.net/index.php?title=VS:Str2Area
    \nhttps://developer.vectorworks.net/index.php?title=VS:Str2Area/ja
    \n面積値の文字列表現を実数に変換します。'''
    return REAL

def Volume2Str(value):
    '''https://developer.vectorworks.net/index.php?title=VS:Volume2Str
    \nhttps://developer.vectorworks.net/index.php?title=VS:Volume2Str/ja
    \n現在のファイルの設定を用いて、体積値を実数から文字列に変換します。'''
    return STRING

def Delete(source, index, count):
    '''https://developer.vectorworks.net/index.php?title=VS:Delete
    \nhttps://developer.vectorworks.net/index.php?title=VS:Delete/ja
    \n指定した文字列から、指定した位置と長さで文字列を削除します。'''
    return source

def Num2Str(decPlace, v):
    '''https://developer.vectorworks.net/index.php?title=VS:Num2Str
    \nhttps://developer.vectorworks.net/index.php?title=VS:Num2Str/ja
    \n実数を文字列に変換します。'''
    return STRING

def Str2Num(s):
    '''https://developer.vectorworks.net/index.php?title=VS:Str2Num
    \nhttps://developer.vectorworks.net/index.php?title=VS:Str2Num/ja
    \n文字列を実数に変換します。'''
    return REAL

def AddCustomTexPart(obj, partID, partName):
    '''https://developer.vectorworks.net/index.php?title=VS:AddCustomTexPart
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddCustomTexPart/ja
    \n指定したIDと名前と共に、カスタムテクスチャを貼る範囲を追加します。既存のテクスチャを貼る範囲(partID)との競合を避けるため、100から始まるpartIDを使用してください。'''
    return None

def GetTexBFeatureEnd(textureBitmap):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexBFeatureEnd
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexBFeatureEnd/ja
    \nハンドルで指定したビットマップのノードの終点座標を返します。'''
    return (featureEndX, featureEndY)

def GetTextureShininess(texture):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTextureShininess
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTextureShininess/ja
    \nハンドルで指定したテクスチャの反射率をパーセンテージで返します。反射率の範囲は0から100で、0の場合は鈍い反射です。'''
    return INTEGER

def SetTexBitRepVert(textureBitmap, repeatVert):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexBitRepVert
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexBitRepVert/ja
    \nハンドルで指定したビットマップの垂直方向の繰り返しの有無を設定します。'''
    return None

def ApplyCustomTexPart(srcObj, destObj, partID):
    '''https://developer.vectorworks.net/index.php?title=VS:ApplyCustomTexPart
    \nhttps://developer.vectorworks.net/index.php?title=VS:ApplyCustomTexPart/ja
    \n指定した元オブジェクトのカスタムテクスチャを貼る範囲(partID)を、指定したオブジェクトに適用します。 例えば、柱状体の全体に対しては、プラグインオブジェクトテクスチャ partID 100 を適用します。適用先のオブジェクトが元オブジェクトのマッピング形式をサポートしていない場合、デフォルトのマッピングが使用されます。'''
    return None

def GetTexBFeatureStart(textureBitmap):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexBFeatureStart
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexBFeatureStart/ja
    \nハンドルで指定したビットマップのノードの始点座標を返します。'''
    return (featureStartX, featureStartY)

def GetTextureSize(texture):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTextureSize
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTextureSize/ja
    \nハンドルで指定したテクスチャの大きさを返します。'''
    return REAL

def SetTexBitmapOrigin(textureBitmap, originX, originY):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexBitmapOrigin
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexBitmapOrigin/ja
    \nハンドルで指定したビットマップのノードの原点座標を設定します。'''
    return None

def AttachDefaultTextureSpace(obj, partID):
    '''https://developer.vectorworks.net/index.php?title=VS:AttachDefaultTextureSpace
    \nhttps://developer.vectorworks.net/index.php?title=VS:AttachDefaultTextureSpace/ja
    \nハンドルで指定した3次元図形にデフォルトのテクスチャスペースを設定します。'''
    return None

def GetTexBitFeatureSize(textureBitmap):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexBitFeatureSize
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexBitFeatureSize/ja
    \nハンドルで指定したビットマップのノードの大きさを返します。'''
    return REAL

def GetTextureSpace(obj, partID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTextureSpace
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTextureSpace/ja
    \nハンドルで指定した3次元図形のテクスチャスペースを返します。'''
    return HANDLE

def SetTexMapBool(h, partID, selector, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexMapBool
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexMapBool/ja
    \nハンドルで指定した図形の指定した部分番号でのマッピング情報をBOOLEAN値で設定します。部分番号を3に指定すると全体になります。'''
    return None

def CreatePaintFromImage(image):
    '''https://developer.vectorworks.net/index.php?title=VS:CreatePaintFromImage
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreatePaintFromImage/ja
    \nイメージからペイントノードを作成します。'''
    return HANDLE

def GetTexBitPaintNode(textureBitmap):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexBitPaintNode
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexBitPaintNode/ja
    \nハンドルで指定したビットマップのペイントノードを返します。'''
    return HANDLE

def GetTextureTransp(texture):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTextureTransp
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTextureTransp/ja
    \nハンドルで指定したテクスチャの透明度をパーセンテージで返します。透明度の範囲は0から100で、0の場合は不透明、100の場合は透明です。'''
    return INTEGER

def SetTexMapBoolN(obj, texPartID, texLayerID, selector, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexMapBoolN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexMapBoolN/ja
    \nハンドルで指定した図形の指定した部分番号でのマッピング情報をBOOLEAN値で設定します。部分番号を3に指定すると全体になります。 Selector: init:1, flip:2, repH:3, repV:4, long edge:5, worldZ:6, auto align:7'''
    return None

def CreatePaintFromImgN(image, locPt, rotDeg):
    '''https://developer.vectorworks.net/index.php?title=VS:CreatePaintFromImgN
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreatePaintFromImgN/ja
    \n指定された位置と回転で画像リソースからペイントノードを作成します。'''
    return HANDLE

def GetTexBitRepHoriz(textureBitmap):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexBitRepHoriz
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexBitRepHoriz/ja
    \nハンドルで指定したビットマップで、水平方向の繰り返しの有効／無効を返します。'''
    return BOOLEAN

def GetWallHoleTexturePart(obj):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWallHoleTexturePart
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWallHoleTexturePart/ja
    \nプラグインオブジェクトや、シンボル定義の壁穴グループの図形の壁テクスチャを返す。'''
    return INTEGER

def SetTexMapInt(h, partID, selector, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexMapInt
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexMapInt/ja
    \nハンドルで指定した図形の指定した部分番号でのマッピング情報をINTEGER値で設定します。部分番号を3に指定すると全体になります。'''
    return None

def CreateShaderRecord(texture, family, prototype):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateShaderRecord
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateShaderRecord/ja
    \n指定した属性をもつ、テクスチャを作成します。（1：色属性／2：反射属性／3：透明属性／4：バンプ属性）'''
    return HANDLE

def GetTexBitRepVert(textureBitmap):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexBitRepVert
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexBitRepVert/ja
    \nハンドルで指定したビットマップで、垂直方向の繰り返しが有効な場合は、TRUEを返します。'''
    return BOOLEAN

def IsImageCropVisible(obj):
    '''https://developer.vectorworks.net/index.php?title=VS:IsImageCropVisible
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsImageCropVisible/ja
    \nイメージの枠が表示されているか確認します。'''
    return BOOLEAN

def SetTexMapIntN(obj, texPartID, texLayerID, selector, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexMapIntN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexMapIntN/ja
    \nハンドルで指定した図形の指定した部分番号でのマッピング情報をINTEGER値で設定します。部分番号を3に指定すると全体になります。テクスチャマッピングの種類を整数で設定するには、セレクタを 1に設定します。'''
    return None

def CreateTexture():
    '''https://developer.vectorworks.net/index.php?title=VS:CreateTexture
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateTexture/ja
    \n新しいテクスチャを作成します。'''
    return HANDLE

def GetTexBitmapOrigin(textureBitmap):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexBitmapOrigin
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexBitmapOrigin/ja
    \nハンドルで指定したビットマップのノードの原点座標を返します。'''
    return (originX, originY)

def IsImageCropped(obj):
    '''https://developer.vectorworks.net/index.php?title=VS:IsImageCropped
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsImageCropped/ja
    \n指定したイメージがクロップされているか確認します。'''
    return BOOLEAN

def SetTexMapReal(h, partID, selector, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexMapReal
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexMapReal/ja
    \nハンドルで指定した図形の指定した部分番号でのマッピング情報をREAL値で設定します。部分番号を3に指定すると全体になります。'''
    return None

def CreateTextureBitmap():
    '''https://developer.vectorworks.net/index.php?title=VS:CreateTextureBitmap
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateTextureBitmap/ja
    \nテクスチャ用のビットマップを作成します。'''
    return HANDLE

def GetTexMapBool(h, partID, selector):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexMapBool
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexMapBool/ja
    \nハンドルで指定した図形の指定した部分番号でのマッピング情報をBOOLEAN値で返します。部分番号を3に指定すると全体になります。'''
    return BOOLEAN

def IsRW():
    '''https://developer.vectorworks.net/index.php?title=VS:IsRW
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsRW/ja
    \nRenderWorks利用が可能／不可能かを返します。'''
    return BOOLEAN

def SetTexMapRealN(obj, texPartID, texLayerID, selector, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexMapRealN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexMapRealN/ja
    \nハンドルで指定した図形の指定した部分番号でのマッピング情報をREAL値で設定します。部分番号を3に指定すると全体になります。 Selector: offsetX:1, offsetY:2, scale2D:3, rotate2D:4, radius:5, matrix mat00 through mat32: 6-17'''
    return None

def CreateTextureBitmapD(parentShaderRecord):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateTextureBitmapD'''
    return HANDLE

def GetTexMapBoolN(obj, texPartID, texLayerID, selector):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexMapBoolN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexMapBoolN/ja
    \nハンドルで指定した図形の指定した部分番号でのマッピング情報をBOOLEAN値で返します。部分番号を3に指定すると全体になります。 Selector: init:1, flip:2, repH:3, repV:4, long edge:5, worldZ:6, auto align:7'''
    return BOOLEAN

def IsTextureableObject(obj):
    '''https://developer.vectorworks.net/index.php?title=VS:IsTextureableObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsTextureableObject/ja
    \nハンドルで指定した3次元図形にテクスチャが設定されていた場合はTRUEを返します。'''
    return BOOLEAN

def SetTexSpace2DOffset(textureSpace, offsetU, offsetV):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexSpace2DOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexSpace2DOffset/ja
    \nハンドルで指定したビットマップのオフセット座標を設定します。'''
    return None

def CreateTextureBitmapN(shaderRecord):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateTextureBitmapN
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateTextureBitmapN/ja
    \n指定した属性で、ビットマップテクスチャを作成します。イメージファイルを選択するダイアログが表示されます。「キャンセル」ボタンが押されたり、属性がイメージでない場合はNILを返します。'''
    return HANDLE

def GetTexMapInt(h, partID, selector):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexMapInt
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexMapInt/ja
    \nハンドルで指定した図形の指定した部分番号でのマッピング情報をINTEGER値で返します。部分番号を3に指定すると全体になります。テクスチャマッピングの種類を整数で返すには、セレクタを 1に設定します。'''
    return INTEGER

def RemoveCustomTexParts(obj):
    '''https://developer.vectorworks.net/index.php?title=VS:RemoveCustomTexParts
    \nhttps://developer.vectorworks.net/index.php?title=VS:RemoveCustomTexParts/ja
    \nオブジェクトからすべてのカスタムのテクスチャを貼る範囲を削除します。'''
    return None

def SetTexSpace2DRadius(textureSpace, radius):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexSpace2DRadius
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexSpace2DRadius/ja
    \nハンドルで指定したビットマップのマッピングの半径を設定します。'''
    return None

def CustomTexPartExists(obj, partID):
    '''https://developer.vectorworks.net/index.php?title=VS:CustomTexPartExists
    \nhttps://developer.vectorworks.net/index.php?title=VS:CustomTexPartExists/ja
    \nオブジェクトが指定したカスタムのテクスチャを貼る範囲 (partID) を使用しているかどうかを返します。'''
    return BOOLEAN

def GetTexMapIntN(obj, texPartID, texLayerID, selector):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexMapIntN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexMapIntN/ja
    \nハンドルで指定した図形の指定した部分番号でのマッピング情報をINTEGER値で返します。部分番号を3に指定すると全体になります。テクスチャマッピングの種類を整数で返すには、セレクタを 1に設定します。'''
    return INTEGER

def ResolveByClassTextureRef(obj, partID):
    '''https://developer.vectorworks.net/index.php?title=VS:ResolveByClassTextureRef
    \nhttps://developer.vectorworks.net/index.php?title=VS:ResolveByClassTextureRef/ja
    \nハンドルで指定した3次元図形のテクスチャがクラス定義だった場合（部分番号が-1の場合）は、クラスのテクスチャ番号を返します。'''
    return LONGINT

def SetTexSpace2DRot(textureSpace, rotationDegrees):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexSpace2DRot
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexSpace2DRot/ja
    \nハンドルで指定したビットマップのマッピングの回転角度を設定します。'''
    return None

def DeleteTextureSpace(obj, partID):
    '''https://developer.vectorworks.net/index.php?title=VS:DeleteTextureSpace
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeleteTextureSpace/ja
    \nハンドルで指定した3次元図形から指定した部分番号をもつテクスチャスペースを削除します。'''
    return None

def GetTexMapReal(h, partID, selector):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexMapReal
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexMapReal/ja
    \nハンドルで指定した図形の指定した部分番号でのマッピング情報をREAL値で返します。部分番号を3に指定すると全体になります。'''
    return REAL

def SetClTextureC(className, textureRef):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClTextureC
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClTextureC/ja
    \n指定したクラス属性の、壁の中央のテクスチャを設定します。'''
    return None

def SetTexSpace2DScale(textureSpace, scale):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexSpace2DScale
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexSpace2DScale/ja
    \nハンドルで指定したビットマップのマッピングの拡大率を設定します。'''
    return None

def EditShaderRecord(shaderRecord):
    '''https://developer.vectorworks.net/index.php?title=VS:EditShaderRecord
    \nhttps://developer.vectorworks.net/index.php?title=VS:EditShaderRecord/ja
    \n属性を設定するための編集ダイアログが表示されます。「OK」ボタンが押された場合は、TRUEを返します。'''
    return BOOLEAN

def GetTexMapRealN(obj, texPartID, texLayerID, selector):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexMapRealN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexMapRealN/ja
    \nハンドルで指定した図形の指定した部分番号でのマッピング情報をREAL値で返します。部分番号を3に指定すると全体になります。 Selector: offsetX:1, offsetY:2, scale2D:3, rotate2D:4, radius:5, matrix mat00 through mat32: 6-17'''
    return REAL

def SetClTextureD(className, textureRef):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClTextureD
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClTextureD/ja
    \n指定したクラス属性の、屋根のテクスチャを設定します。'''
    return None

def SetTexSpaceEndCap(textureSpace, endCapTextured):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexSpaceEndCap
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexSpaceEndCap/ja
    \nハンドルで指定したビットマップの底面のマッピングの有無を設定します。'''
    return None

def EditTexture(texture):
    '''https://developer.vectorworks.net/index.php?title=VS:EditTexture
    \nhttps://developer.vectorworks.net/index.php?title=VS:EditTexture/ja
    \nハンドルで指定したテクスチャを編集するダイアログを表示します。'''
    return BOOLEAN

def GetTexSpace2DOffset(textureSpace):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexSpace2DOffset
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexSpace2DOffset/ja
    \nハンドルで指定したビットマップのオフセット座標を返します。'''
    return (offsetU, offsetV)

def SetClTextureG(className, textureRef):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClTextureG
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClTextureG/ja
    \n指定したクラス属性の、テクスチャを設定します。'''
    return None

def SetTexSpaceKind(textureSpace, kind):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexSpaceKind
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexSpaceKind/ja
    \nハンドルで指定したビットマップのマッピングの種類を設定します。'''
    return None

def EditTextureBitmap(textureBitmap):
    '''https://developer.vectorworks.net/index.php?title=VS:EditTextureBitmap
    \nhttps://developer.vectorworks.net/index.php?title=VS:EditTextureBitmap/ja
    \nハンドルで指定したビットマップテクスチャを編集するダイアログを表示します。'''
    return BOOLEAN

def GetTexSpace2DRadius(textureSpace):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexSpace2DRadius
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexSpace2DRadius/ja
    \nハンドルで指定したビットマップのマッピングの半径を返します。'''
    return REAL

def SetClTextureL(className, textureRef):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClTextureL
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClTextureL/ja
    \n指定したクラス属性の、壁の左側のテクスチャを設定します。'''
    return None

def SetTexSpaceOrientU(textureSpace, uXAxis, uYAxis, uZAxis):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexSpaceOrientU
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexSpaceOrientU/ja
    \nハンドルで指定したビットマップのＵ軸の座標を設定します。'''
    return None

def EditTextureSpace(obj, partID):
    '''https://developer.vectorworks.net/index.php?title=VS:EditTextureSpace
    \nhttps://developer.vectorworks.net/index.php?title=VS:EditTextureSpace/ja
    \nハンドルで指定した3次元図形のマッピングを編集するダイアログを表示します。'''
    return BOOLEAN

def GetTexSpace2DRot(textureSpace):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexSpace2DRot
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexSpace2DRot/ja
    \nハンドルで指定したビットマップのマッピングの回転角度を返します。'''
    return REAL

def SetClTextureR(className, textureRef):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClTextureR
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClTextureR/ja
    \n指定したクラス属性の、壁の右側のテクスチャを設定します。'''
    return None

def SetTexSpaceOrientV(textureSpace, vXAxis, vYAxis, vZAxis):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexSpaceOrientV
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexSpaceOrientV/ja
    \nハンドルで指定したビットマップのＶ軸の座標を設定します。'''
    return None

def GS_EdSh_ConstructLayout(shaderNameCStr, paramsPtr):
    '''https://developer.vectorworks.net/index.php?title=VS:GS_EdSh_ConstructLayout
    \nhttps://developer.vectorworks.net/index.php?title=VS:GS_EdSh_ConstructLayout/ja
    \nシェーダのパラメータ値を編集するダイアログレイアウトを生成します。'''
    return libraryDataPtr

def GetTexSpace2DScale(textureSpace):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexSpace2DScale
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexSpace2DScale/ja
    \nハンドルで指定したビットマップのマッピングの拡大率を返します。'''
    return REAL

def SetClTextureT(className, textureRef):
    '''https://developer.vectorworks.net/index.php?title=VS:SetClTextureT
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetClTextureT/ja
    \n指定したクラス属性の、屋根のテクスチャを設定します。'''
    return None

def SetTexSpaceOrientW(textureSpace, wXAxis, wYAxis, wZAxis):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexSpaceOrientW
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexSpaceOrientW/ja
    \nハンドルで指定したビットマップのＷ軸の座標を設定します。'''
    return None

def GS_EdSh_PopulateMenu(itemID, numStrings, cStringsArray, libraryDataPtr):
    '''https://developer.vectorworks.net/index.php?title=VS:GS_EdSh_PopulateMenu
    \nhttps://developer.vectorworks.net/index.php?title=VS:GS_EdSh_PopulateMenu/ja
    \nシェーダ編集ダイアログのポップアップにメニュー項目を追加します。'''
    return None

def GetTexSpaceEndCap(textureSpace):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexSpaceEndCap
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexSpaceEndCap/ja
    \nハンドルで指定したビットマップで、底面のマッピングが設定されている場合は、TRUEを返します。'''
    return BOOLEAN

def SetCustomRWPrefs():
    '''https://developer.vectorworks.net/index.php?title=VS:SetCustomRWPrefs
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCustomRWPrefs/ja
    \nカスタムRenderworksレンダリング設定を設定します。'''
    return (useTextures, useTransparency, useShadows, useRayTracing, useAntiAliasing, useDithering, tessellationDetail, shadowStyle, rayTracingRecursion)

def SetTexSpaceOrigin(textureSpace, offset):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexSpaceOrigin
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexSpaceOrigin/ja
    \nハンドルで指定したビットマップの原点座標を設定します。'''
    return None

def GS_EdSh_RunDialog(libraryDataPtr):
    '''https://developer.vectorworks.net/index.php?title=VS:GS_EdSh_RunDialog
    \nhttps://developer.vectorworks.net/index.php?title=VS:GS_EdSh_RunDialog/ja
    \nシェーダ編集ダイアログレイアウトを実行します。'''
    return userHitOK

def GetTexSpaceKind(textureSpace):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexSpaceKind
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexSpaceKind/ja
    \nハンドルで指定したビットマップのマッピングの種類を返します。'''
    return INTEGER

def SetDefaultTexMap(h):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDefaultTexMap
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDefaultTexMap/ja
    \nハンドルで指定した図形にデフォルトのテクスチャマッピング情報を設定します。使用するテクスチャリソースは、SetTextureRef で設定します。SetDefaultTextureSpaceの代わりにご利用ください。'''
    return None

def SetTexSpacePartID(textureSpace, partID):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexSpacePartID
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexSpacePartID/ja
    \nハンドルで指定したビットマップの部分番号を設定します。'''
    return None

def GetClTextureC(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClTextureC
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClTextureC/ja
    \n指定したクラスの属性で、壁の中央に設定されているテクスチャの番号を返します。'''
    return LONGINT

def GetTexSpaceOrientU(textureSpace):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexSpaceOrientU
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexSpaceOrientU/ja
    \nハンドルで指定したビットマップのＵ軸の座標を返します。'''
    return (uXAxis, uYAxis, uZAxis)

def SetDefaultTexMapN(h, texPartID, texLayerID):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDefaultTexMapN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDefaultTexMapN/ja
    \nハンドルで指定した図形にデフォルトのテクスチャマッピング情報を設定します。使用するテクスチャリソースは、SetTextureRef で設定します。SetDefaultTexMapの代わりにご利用ください。'''
    return None

def SetTexSpaceStartCap(textureSpace, startCapTextured):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexSpaceStartCap
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexSpaceStartCap/ja
    \nハンドルで指定したビットマップの上面のマッピングの有無を設定します。'''
    return None

def GetClTextureD(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClTextureD
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClTextureD/ja
    \n指定したクラスの属性で、ドーマーに設定されているテクスチャの番号を返します。'''
    return LONGINT

def GetTexSpaceOrientV(textureSpace):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexSpaceOrientV
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexSpaceOrientV/ja
    \nハンドルで指定したビットマップのＶ軸の座標を返します。'''
    return (vXAxis, vYAxis, vZAxis)

def SetDefaultTextureSpace(obj, texSpace, partID):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDefaultTextureSpace
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDefaultTextureSpace/ja
    \nハンドルで指定した3次元図形にテクスチャスペースを設定します。'''
    return None

def SetTextureBitmap(shaderRecord, textureBitmap):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextureBitmap
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextureBitmap/ja
    \nハンドルで指定したテクスチャのビットマップを設定します。図形が存在しない場合はtextureBitmapにNILを返します。'''
    return None

def GetClTextureG(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClTextureG
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClTextureG/ja
    \n指定したクラスの属性に設定されているテクスチャの番号を返します。'''
    return LONGINT

def GetTexSpaceOrientW(textureSpace):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexSpaceOrientW
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexSpaceOrientW/ja
    \nハンドルで指定したビットマップのＷ軸の座標を返します。'''
    return (wXAxis, wYAxis, wZAxis)

def SetImageCropObject(image, crop):
    '''https://developer.vectorworks.net/index.php?title=VS:SetImageCropObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetImageCropObject/ja
    \n指定したイメージと枠へのハンドルを元に、イメージに枠を設定します。'''
    return BOOLEAN

def SetTextureRef(obj, textureRef, partID):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextureRef
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextureRef/ja
    \nハンドルで指定した3次元図形のテクスチャ番号を設定します。'''
    return None

def GetClTextureL(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClTextureL
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClTextureL/ja
    \n指定したクラスの属性で、壁の左側に設定されているテクスチャの番号を返します。'''
    return LONGINT

def GetTexSpaceOrigin(textureSpace):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexSpaceOrigin
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexSpaceOrigin/ja
    \nハンドルで指定したビットマップの原点座標を返します。'''
    return offset

def SetImageCropVisible(obj, isVisible):
    '''https://developer.vectorworks.net/index.php?title=VS:SetImageCropVisible
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetImageCropVisible/ja
    \nイメージ枠の表示を設定します。'''
    return None

def SetTextureRefN(obj, textureRef, texPartID, texLayerID):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextureRefN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextureRefN/ja
    \nハンドルで指定した3次元図形のテクスチャ番号を設定します。'''
    return None

def GetClTextureR(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClTextureR
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClTextureR/ja
    \n指定したクラスの属性で、壁の右側に設定されているテクスチャの番号を返します。'''
    return LONGINT

def GetTexSpacePartID(textureSpace):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexSpacePartID
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexSpacePartID/ja
    \nハンドルで指定したビットマップの部分番号を返します。'''
    return INTEGER

def SetObjExpandTexture(obj, expanded):
    '''https://developer.vectorworks.net/index.php?title=VS:SetObjExpandTexture
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetObjExpandTexture/ja
    \nハンドルで指定した3次元図形のテクスチャを全体に貼り付けるように設定します。'''
    return None

def SetTextureSet(obj, textureSet):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextureSet
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextureSet/ja
    \nオブジェクトのテクスチャセットを設定します。'''
    return None

def GetClTextureT(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClTextureT
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClTextureT/ja
    \n指定したクラスの属性で、屋根に設定されているテクスチャの番号を返します。'''
    return LONGINT

def GetTexSpaceStartCap(textureSpace):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTexSpaceStartCap
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTexSpaceStartCap/ja
    \nハンドルで指定したビットマップで、上面のマッピングが設定されている場合は、TRUEを返します。'''
    return BOOLEAN

def SetOpenGLPrefs():
    '''https://developer.vectorworks.net/index.php?title=VS:SetOpenGLPrefs
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetOpenGLPrefs/ja
    \nOpenGLレンダリングの設定を設定します。'''
    return (useTextures, tessellationDetail, useNURBS)

def SetTextureShader(texture, shaderIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextureShader
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextureShader/ja
    \nハンドルで指定したテクスチャのシェーダ番号を設定します。'''
    return None

def GetClUseTexture(className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClUseTexture
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClUseTexture/ja
    \n指定したクラスの属性で、テクスチャの使用が有効の場合は、TRUEを返します。'''
    return BOOLEAN

def GetTextureBitmap(shaderRecord):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTextureBitmap
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTextureBitmap/ja
    \nハンドルで指定したテクスチャのビットマップを返します。'''
    return HANDLE

def SetTexBFeatureEnd(textureBitmap, featureEndX, featureEndY):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexBFeatureEnd
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexBFeatureEnd/ja
    \nハンドルで指定したビットマップのノードの終点座標を設定します。'''
    return None

def SetTextureShininess(texture, shininess):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextureShininess
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextureShininess/ja
    \nハンドルで指定したテクスチャの反射率をパーセンテージで設定します。反射率の範囲は0から100で、0の場合は鈍い反射です。'''
    return None

def GetImageCropObject(obj):
    '''https://developer.vectorworks.net/index.php?title=VS:GetImageCropObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetImageCropObject/ja
    \nクロップしたイメージの枠を返します。'''
    return HANDLE

def GetTextureRef(obj, partID, resolveByClass):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTextureRef
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTextureRef/ja
    \nハンドルで指定した3次元図形のテクスチャ番号を返します。'''
    return LONGINT

def SetTexBFeatureStart(textureBitmap, featureStartX, featureStartY):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexBFeatureStart
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexBFeatureStart/ja
    \nハンドルで指定したビットマップのノードの始点座標を設定します。'''
    return None

def SetTextureSize(texture, newSize):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextureSize
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextureSize/ja
    \nハンドルで指定したテクスチャの大きさを設定します。'''
    return None

def GetNumTexLayers(obj, texPartID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetNumTexLayers
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNumTexLayers/ja
    \nテクスチャのレイヤ数（基準+デカール）を返します。'''
    return LONGINT

def GetTextureRefN(obj, texPartID, texLayerID, resolveByClass):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTextureRefN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTextureRefN/ja
    \nハンドルで指定した3次元図形のテクスチャ番号を返します。'''
    return LongInt

def SetTexBitFeatureSize(textureBitmap, featureSize):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexBitFeatureSize
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexBitFeatureSize/ja
    \nハンドルで指定したビットマップのノードの大きさを設定します。'''
    return None

def SetTextureTransp(texture, transparency):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTextureTransp
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTextureTransp/ja
    \nハンドルで指定したテクスチャの透明度をパーセンテージで設定します。透明度の範囲は0から100で、0の場合は不透明、100の場合は透明です。'''
    return None

def GetObjExpandTexture(obj):
    '''https://developer.vectorworks.net/index.php?title=VS:GetObjExpandTexture
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetObjExpandTexture/ja
    \nハンドルで指定した3次元図形のテクスチャが全体に貼り付けられている場合は、TRUEを返します。'''
    return BOOLEAN

def GetTextureSet(obj):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTextureSet
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTextureSet/ja
    \nオブジェクトのテクスチャセットを取得します。'''
    return INTEGER

def SetTexBitPaintNode(textureBitmap, paintNode):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexBitPaintNode
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexBitPaintNode/ja
    \nハンドルで指定したビットマップのペイントノードを設定します。'''
    return None

def SetWallHoleTexturePart(obj, part):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWallHoleTexturePart
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWallHoleTexturePart/ja
    \nプラグインオブジェクトや、シンボル定義の壁穴グループの図形の壁テクスチャを設定します。'''
    return None

def GetShaderRecord(texture, family):
    '''https://developer.vectorworks.net/index.php?title=VS:GetShaderRecord
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetShaderRecord/ja
    \n指定した属性のハンドルを返します。（1：色属性／2：反射属性／3：透明属性／4：バンプ属性）'''
    return HANDLE

def GetTextureShader(texture):
    '''https://developer.vectorworks.net/index.php?title=VS:GetTextureShader
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTextureShader/ja
    \nハンドルで指定したテクスチャのシェーダ番号を返します。'''
    return LONGINT

def SetTexBitRepHoriz(textureBitmap, repeatHoriz):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTexBitRepHoriz
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTexBitRepHoriz/ja
    \nハンドルで指定したビットマップの水平方向の繰り返しの有無を設定します。'''
    return None

def ResList_DlgInit(uniqueID, dlgID, ctrlID):
    '''https://developer.vectorworks.net/index.php?title=VS:ResList_DlgInit
    \nhttps://developer.vectorworks.net/index.php?title=VS:ResList_DlgInit/ja
    \nポップアップコントロールまたはリソースのポップアップをリソースリストのデータを識別するuniqueIDと関連付けてダイアログを初期化します。'''
    return None

def vstDrawCoordLineN(pt1X, pt1Y, pt2X, pt2Y, planeRefID):
    '''https://developer.vectorworks.net/index.php?title=VS:vstDrawCoordLineN
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstDrawCoordLineN/ja'''
    return None

def vstGetModeValue(inModeGroup):
    '''https://developer.vectorworks.net/index.php?title=VS:vstGetModeValue
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstGetModeValue/ja'''
    return outValue

def vstSetDataLong(inDataID, inDataVal):
    '''https://developer.vectorworks.net/index.php?title=VS:vstSetDataLong
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstSetDataLong/ja'''
    return result

def vstAddButtonMode(inIconSpecification):
    '''https://developer.vectorworks.net/index.php?title=VS:vstAddButtonMode
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstAddButtonMode/ja'''
    return None

def vstDrawCoordLineN3D(pt1X, pt1Y, pt2X, pt2Y, planeRefID):
    '''https://developer.vectorworks.net/index.php?title=VS:vstDrawCoordLineN3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstDrawCoordLineN3D/ja'''
    return None

def vstGetPickObject():
    '''https://developer.vectorworks.net/index.php?title=VS:vstGetPickObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstGetPickObject/ja'''
    return HANDLE

def vstSetDataReal(inDataID, inDataVal):
    '''https://developer.vectorworks.net/index.php?title=VS:vstSetDataReal
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstSetDataReal/ja'''
    return result

def vstAddPDMenuItem(group, item):
    '''https://developer.vectorworks.net/index.php?title=VS:vstAddPDMenuItem
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstAddPDMenuItem/ja'''
    return None

def vstDrawCoordRect(ptLeftTopX, ptLeftTopY, ptRghtBotX, ptRghtBotY):
    '''https://developer.vectorworks.net/index.php?title=VS:vstDrawCoordRect
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstDrawCoordRect/ja'''
    return None

def vstGetPt2D(inPtIndex, result):
    '''https://developer.vectorworks.net/index.php?title=VS:vstGetPt2D
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstGetPt2D/ja'''
    return (outX, outY)

def vstSetDataString(inDataID, inDataVal):
    '''https://developer.vectorworks.net/index.php?title=VS:vstSetDataString
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstSetDataString/ja'''
    return result

def vstAddPDMenuMode(label):
    '''https://developer.vectorworks.net/index.php?title=VS:vstAddPDMenuMode
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstAddPDMenuMode/ja'''
    return None

def vstEnableMode(inModeNumber, inEnable):
    '''https://developer.vectorworks.net/index.php?title=VS:vstEnableMode
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstEnableMode/ja'''
    return None

def vstGetPt3D(inPtIndex, result):
    '''https://developer.vectorworks.net/index.php?title=VS:vstGetPt3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstGetPt3D/ja'''
    return (outX, outY, outZ)

def vstSetEventInfo(inAction, inMessage1, inMessage1, inRsrcFileID):
    '''https://developer.vectorworks.net/index.php?title=VS:vstSetEventInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstSetEventInfo/ja
    \nVSツールイベントの戻り値を設定します。'''
    return None

def vstAddRadioMode(inInitialSetting, inNumButtons, inImageSpecification1, inImageSpecification2, inImageSpecification3, inImageSpecification4, inImageSpecification5, inImageSpecification6):
    '''https://developer.vectorworks.net/index.php?title=VS:vstAddRadioMode
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstAddRadioMode/ja'''
    return None

def vstGetCurrPt2D():
    '''https://developer.vectorworks.net/index.php?title=VS:vstGetCurrPt2D
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstGetCurrPt2D/ja'''
    return (outX, outY)

def vstGetRsrcFileID():
    '''https://developer.vectorworks.net/index.php?title=VS:vstGetRsrcFileID
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstGetRsrcFileID/ja'''
    return outFileID

def vstSetEventResult(inSetVal):
    '''https://developer.vectorworks.net/index.php?title=VS:vstSetEventResult
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstSetEventResult/ja'''
    return None

def vstAddResPDMenuMode(label, value):
    '''https://developer.vectorworks.net/index.php?title=VS:vstAddResPDMenuMode'''
    return None

def vstGetCurrPt3D(result):
    '''https://developer.vectorworks.net/index.php?title=VS:vstGetCurrPt3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstGetCurrPt3D/ja'''
    return (outX, outY, outZ)

def vstGetString(inStrListID, inStrID):
    '''https://developer.vectorworks.net/index.php?title=VS:vstGetString
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstGetString/ja
    \nツールのリソースファイルに格納された文字列にアクセスします。'''
    return outString

def vstSetHelpString(inHelpStr):
    '''https://developer.vectorworks.net/index.php?title=VS:vstSetHelpString
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstSetHelpString/ja'''
    return None

def vstCustomProcNNA(inEvent, inMode, inDiameter, inSpacing):
    '''https://developer.vectorworks.net/index.php?title=VS:vstCustomProcNNA
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstCustomProcNNA/ja'''
    return (BOOLEAN, outEvtResult)

def vstGetDataLong(inDataID):
    '''https://developer.vectorworks.net/index.php?title=VS:vstGetDataLong
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstGetDataLong/ja'''
    return (outData, result)

def vstGetToolObject():
    '''https://developer.vectorworks.net/index.php?title=VS:vstGetToolObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstGetToolObject/ja
    \nvstSetPtBehaviorは、ツールの完了時にオブジェクトを作成することがあります。この関数は、そのオブジェクトを返します。'''
    return HANDLE

def vstSetModeHelpBase(inTextRsrcIDBase):
    '''https://developer.vectorworks.net/index.php?title=VS:vstSetModeHelpBase
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstSetModeHelpBase/ja'''
    return None

def vstDefault2DToolDraw():
    '''https://developer.vectorworks.net/index.php?title=VS:vstDefault2DToolDraw
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstDefault2DToolDraw/ja'''
    return None

def vstGetDataReal(inDataID):
    '''https://developer.vectorworks.net/index.php?title=VS:vstGetDataReal
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstGetDataReal/ja'''
    return (outData, result)

def vstNameUndoEvent(inUndoEventName):
    '''https://developer.vectorworks.net/index.php?title=VS:vstNameUndoEvent
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstNameUndoEvent/ja'''
    return None

def vstSetPDMenuSel(group, selectedItem):
    '''https://developer.vectorworks.net/index.php?title=VS:vstSetPDMenuSel
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstSetPDMenuSel/ja'''
    return None

def vstDefault3DToolDraw():
    '''https://developer.vectorworks.net/index.php?title=VS:vstDefault3DToolDraw
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstDefault3DToolDraw/ja'''
    return None

def vstGetDataString(inDataID):
    '''https://developer.vectorworks.net/index.php?title=VS:vstGetDataString
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstGetDataString/ja'''
    return (outData, result)

def vstNumPts():
    '''https://developer.vectorworks.net/index.php?title=VS:vstNumPts
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstNumPts/ja'''
    return outNumPts

def vstSetPtBehavior(inStatusType):
    '''https://developer.vectorworks.net/index.php?title=VS:vstSetPtBehavior
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstSetPtBehavior/ja'''
    return None

def vstDrawCoordArcN(ptLeftTopX, ptLeftTopY, ptRghtBotX, ptRghtBotY, startAngle, sweepAngle):
    '''https://developer.vectorworks.net/index.php?title=VS:vstDrawCoordArcN
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstDrawCoordArcN/ja'''
    return None

def vstGetEventInfo():
    '''https://developer.vectorworks.net/index.php?title=VS:vstGetEventInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstGetEventInfo/ja
    \nVSツールイベントパラメータを取得します。'''
    return (outAction, outMessage1, outMessage2)

def vstResPDMenuInit(uniqueID, modeGroup, emptyMsg):
    '''https://developer.vectorworks.net/index.php?title=VS:vstResPDMenuInit
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstResPDMenuInit/ja
    \nツールの初期化で使います。vstAddResPDMenuMode で作られ、ResList_* で初期化された、ツールリソースポップアップを初期化します。uniqueIDでリソースリストのデータを特定します。'''
    return None

def vstSetRsrcFile(inFileName):
    '''https://developer.vectorworks.net/index.php?title=VS:vstSetRsrcFile
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstSetRsrcFile/ja'''
    return None

def vstDrawCoordEllipse(ptLeftTopX, ptLeftTopY, ptRghtBotX, ptRghtBotY):
    '''https://developer.vectorworks.net/index.php?title=VS:vstDrawCoordEllipse
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstDrawCoordEllipse/ja'''
    return None

def vstGetEventResult():
    '''https://developer.vectorworks.net/index.php?title=VS:vstGetEventResult
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstGetEventResult/ja'''
    return outGetVal

def vstRestoreWPHybridTool(message1):
    '''https://developer.vectorworks.net/index.php?title=VS:vstRestoreWPHybridTool
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstRestoreWPHybridTool/ja
    \nハイブリッドツールであるvstSetWPHybridToolの後で、ワーキングプレーンを復元します。'''
    return None

def vstSetWPHybridTool(message1):
    '''https://developer.vectorworks.net/index.php?title=VS:vstSetWPHybridTool
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstSetWPHybridTool/ja
    \nハイブリッドツールに対して、レイヤにワーキングプレーンを設定します。'''
    return None

def vstDrawCoordLine(pt1X, pt1Y, pt2X, pt2Y):
    '''https://developer.vectorworks.net/index.php?title=VS:vstDrawCoordLine
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstDrawCoordLine/ja'''
    return None

def vstGetInitObject(message1):
    '''https://developer.vectorworks.net/index.php?title=VS:vstGetInitObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstGetInitObject/ja
    \nこのツールがコピーする図形のハンドルを返します。「類似オブジェクト作成」'''
    return HANDLE

def vstSetCursorByView():
    '''https://developer.vectorworks.net/index.php?title=VS:vstSetCursorByView
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstSetCursorByView/ja
    \nビューに適したカーソルを設定します。'''
    return None

def vstDrawCoordLine3D(pt1, pt2):
    '''https://developer.vectorworks.net/index.php?title=VS:vstDrawCoordLine3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstDrawCoordLine3D/ja'''
    return None

def vstGetModeHelpBase():
    '''https://developer.vectorworks.net/index.php?title=VS:vstGetModeHelpBase
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstGetModeHelpBase/ja'''
    return outTextRsrcIDBase

def vstSetCustomProc(inRoutineName):
    '''https://developer.vectorworks.net/index.php?title=VS:vstSetCustomProc
    \nhttps://developer.vectorworks.net/index.php?title=VS:vstSetCustomProc/ja'''
    return None

def DLDBeginLoadData(loadDataType):
    '''https://developer.vectorworks.net/index.php?title=VS:DLDBeginLoadData'''
    return None

def OLDConstructMatsCnt():
    '''https://developer.vectorworks.net/index.php?title=VS:OLDConstructMatsCnt'''
    return LONGINT

def OLDGetLoadDataBool(handle, selector, loadIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:OLDGetLoadDataBool'''
    return BOOLEAN

def OLDMassStrToReal(massString):
    '''https://developer.vectorworks.net/index.php?title=VS:OLDMassStrToReal'''
    return (BOOLEAN, realValue)

def DLDEndLoadData():
    '''https://developer.vectorworks.net/index.php?title=VS:DLDEndLoadData'''
    return None

def OLDFindAttachHangPos(handle, loadIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:OLDFindAttachHangPos'''
    return HANDLE

def OLDGetLoadDataReal(handle, selector, loadIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:OLDGetLoadDataReal'''
    return REAL

def OLDSelectTrussSystem(trussHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:OLDSelectTrussSystem'''
    return None

def DLDSetLoadDataBool(selector, value):
    '''https://developer.vectorworks.net/index.php?title=VS:DLDSetLoadDataBool'''
    return None

def OLDForceRealToStr(forceValue):
    '''https://developer.vectorworks.net/index.php?title=VS:OLDForceRealToStr'''
    return STRING

def OLDGetLoadDataStr(handle, selector, loadIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:OLDGetLoadDataStr'''
    return STRING

def OLDSetHangPathHandle(handle, loadIndex, path, height, deletePathHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:OLDSetHangPathHandle'''
    return None

def DLDSetLoadDataReal(selector, value):
    '''https://developer.vectorworks.net/index.php?title=VS:DLDSetLoadDataReal'''
    return None

def OLDForceStrToReal(forceString):
    '''https://developer.vectorworks.net/index.php?title=VS:OLDForceStrToReal'''
    return (BOOLEAN, realValue)

def OLDSetLoadDataBool(handle, selector, value, loadIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:OLDSetLoadDataBool'''
    return None

def DLDSetLoadDataString(selector, value):
    '''https://developer.vectorworks.net/index.php?title=VS:DLDSetLoadDataString'''
    return None

def OLDGetConstructMat(materialIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:OLDGetConstructMat'''
    return (UniversalName, LocalizedName)

def OLDGetPositionTransf(handle, loadIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:OLDGetPositionTransf'''
    return (BOOLEAN, offsetDistance, rotationAngle, hasWitnessLine)

def OLDSetLoadDataReal(handle, selector, value, loadIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:OLDSetLoadDataReal'''
    return None

def HP_AutoAttachLoads(positionHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:HP_AutoAttachLoads'''
    return None

def OLDGetDragSnapPoint():
    '''https://developer.vectorworks.net/index.php?title=VS:OLDGetDragSnapPoint'''
    return (BOOLEAN, point)

def OLDHoistSectionDlg():
    '''https://developer.vectorworks.net/index.php?title=VS:OLDHoistSectionDlg'''
    return (BOOLEAN, crossSection)

def OLDSetLoadDataStr(handle, selector, value, loadIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:OLDSetLoadDataStr'''
    return None

def HP_ConvertToHangPos():
    '''https://developer.vectorworks.net/index.php?title=VS:HP_ConvertToHangPos'''
    return None

def OLDGetHangPointAt(handle, loadIndex, pointIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:OLDGetHangPointAt'''
    return (point, hasLoad)

def OLDMassDistRealToStr(distrMassValue):
    '''https://developer.vectorworks.net/index.php?title=VS:OLDMassDistRealToStr'''
    return STRING

def OLDShowTrussSnapping():
    '''https://developer.vectorworks.net/index.php?title=VS:OLDShowTrussSnapping'''
    return BOOLEAN

def OLDAddLoadHangPoint(handle, loadIndex, point, hasLoad):
    '''https://developer.vectorworks.net/index.php?title=VS:OLDAddLoadHangPoint'''
    return None

def OLDGetHangPointsCnt(handle, loadIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:OLDGetHangPointsCnt'''
    return LONGINT

def OLDMassDistStrToReal(distrMassString):
    '''https://developer.vectorworks.net/index.php?title=VS:OLDMassDistStrToReal'''
    return (BOOLEAN, realValue)

def OLDTrussSectionDlg():
    '''https://developer.vectorworks.net/index.php?title=VS:OLDTrussSectionDlg'''
    return (BOOLEAN, crossSection, height, width, design, chordDiameter)

def OLDClearHangPtsPath(handle, loadIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:OLDClearHangPtsPath'''
    return None

def OLDGetHangingPos(handle, loadIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:OLDGetHangingPos'''
    return HANDLE

def OLDMassRealToStr(massValue):
    '''https://developer.vectorworks.net/index.php?title=VS:OLDMassRealToStr'''
    return STRING

def UpdatePositionParam(positionHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:UpdatePositionParam'''
    return None

def GetPrimaryUnitInfo():
    '''https://developer.vectorworks.net/index.php?title=VS:GetPrimaryUnitInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPrimaryUnitInfo/ja
    \n現在設定されている主単位の情報を返します。'''
    return (style, prec, dimPrec, format, angPrec, showMark, dispFrac)

def GetSecondaryUnitInfo():
    '''https://developer.vectorworks.net/index.php?title=VS:GetSecondaryUnitInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSecondaryUnitInfo/ja
    \n現在設定されている補助単位の情報を返します。'''
    return (style, dimPrec, format, showMark, dispFrac)

def PrimaryUnits(style, prec, dimPrec, format, angPrec, showMark, dispFrac):
    '''https://developer.vectorworks.net/index.php?title=VS:PrimaryUnits
    \nhttps://developer.vectorworks.net/index.php?title=VS:PrimaryUnits/ja
    \n主単位を設定します。'''
    return None

def Units(i):
    '''https://developer.vectorworks.net/index.php?title=VS:Units
    \nhttps://developer.vectorworks.net/index.php?title=VS:Units/ja
    \n現在の単位を設定します。'''
    return None

def GetRoundingBase():
    '''https://developer.vectorworks.net/index.php?title=VS:GetRoundingBase
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetRoundingBase/ja
    \n主単位、寸法（主単位）、寸法（補助単位）の端数丸めの基準（1、2.5、5）を返します。'''
    return (display, primary, secondary)

def GetUnits():
    '''https://developer.vectorworks.net/index.php?title=VS:GetUnits
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetUnits/ja
    \n現在の単位設定の情報を返します。'''
    return (fraction, display, format, upi, name, squareName)

def SecondaryUnits(style, dimPrec, format, showMark, dispFrac):
    '''https://developer.vectorworks.net/index.php?title=VS:SecondaryUnits
    \nhttps://developer.vectorworks.net/index.php?title=VS:SecondaryUnits/ja
    \n補助単位を設定します。'''
    return None

def AutoKey():
    '''https://developer.vectorworks.net/index.php?title=VS:AutoKey
    \nhttps://developer.vectorworks.net/index.php?title=VS:AutoKey/ja
    \nファンクションキー以外のキーが押し続けられていれば、TRUEを返し、同時に押されたキーのASCIIコードを返します。'''
    return (BOOLEAN, asciiCode)

def GetLine(callback):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLine
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLine/ja
    \nマウスで2点を指示されるまで待機し、始点と終点の座標を返します。'''
    return none

def GetRect(callback):
    '''https://developer.vectorworks.net/index.php?title=VS:GetRect
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetRect/ja
    \nマウスで四角形の座標を指示されるまで待機し、四角形の座標を返します。'''
    return None

def SetModeButtonText(modeName, modeType):
    '''https://developer.vectorworks.net/index.php?title=VS:SetModeButtonText
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetModeButtonText/ja
    \nモードバーボタンのヘルプテキストを設定します。'''
    return None

def BeginModeButtonsText():
    '''https://developer.vectorworks.net/index.php?title=VS:BeginModeButtonsText
    \nhttps://developer.vectorworks.net/index.php?title=VS:BeginModeButtonsText/ja
    \nモードバーボタンのヘルプテキストを作成します。'''
    return None

def GetLine3D(useWP, callback):
    '''https://developer.vectorworks.net/index.php?title=VS:GetLine3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetLine3D/ja
    \nマウスで2点を指示されるまで待機し、始点と終点の3D座標を返します。'''
    return None

def GetRect3D(useWP, callback):
    '''https://developer.vectorworks.net/index.php?title=VS:GetRect3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetRect3D/ja
    \nマウスで四角形の座標を指示されるまで待機し、四角形の3D座標を返します。'''
    return None

def SetTempToolHelpStr(helpString):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTempToolHelpStr
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTempToolHelpStr/ja
    \nテンポラリツール関数のヘルプを設定します。'''
    return None

def CallTool(toolID, callback):
    '''https://developer.vectorworks.net/index.php?title=VS:CallTool
    \nhttps://developer.vectorworks.net/index.php?title=VS:CallTool/ja
    \n指定した番号のツールを選択します。ツールが使われた後は、この手続きが実行される前に選択されていたツールを選択します。'''
    return None

def GetMouse():
    '''https://developer.vectorworks.net/index.php?title=VS:GetMouse
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetMouse/ja
    \n現在のマウスの座標を返します。'''
    return p

def KeyDown():
    '''https://developer.vectorworks.net/index.php?title=VS:KeyDown
    \nhttps://developer.vectorworks.net/index.php?title=VS:KeyDown/ja
    \nファンクションキー以外のキーが押された場合、TRUEを返すと同時に押されたキーのASCIIコードを返します。'''
    return (BOOLEAN, asciiCode)

def SetToolHelpMessage(modeText, descriptionText):
    '''https://developer.vectorworks.net/index.php?title=VS:SetToolHelpMessage
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetToolHelpMessage/ja
    \nツールバーのヘルプテキストを新しい標準形式（ツールモード, 使い方のアドバイス）で設定します。'''
    return None

def CapsLock():
    '''https://developer.vectorworks.net/index.php?title=VS:CapsLock
    \nhttps://developer.vectorworks.net/index.php?title=VS:CapsLock/ja
    \nCapsLockキーが押されている場合は、TRUEを返します。'''
    return BOOLEAN

def GetPt(callback):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPt
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPt/ja
    \nマウスがクリックされるまで待機し、クリックされた点の座標を返します。'''
    return None

def MouseDown():
    '''https://developer.vectorworks.net/index.php?title=VS:MouseDown
    \nhttps://developer.vectorworks.net/index.php?title=VS:MouseDown/ja
    \nマウスボタンが押されている場合は、TRUEと座標を返します。'''
    return (bool, (px, py))

def Shift():
    '''https://developer.vectorworks.net/index.php?title=VS:Shift
    \nhttps://developer.vectorworks.net/index.php?title=VS:Shift/ja
    \nShiftキーが押されている場合は、TRUEを返します。'''
    return BOOLEAN

def Command():
    '''https://developer.vectorworks.net/index.php?title=VS:Command
    \nhttps://developer.vectorworks.net/index.php?title=VS:Command/ja
    \nCommand（Control）キーが押されている場合は、TRUEを返します。'''
    return BOOLEAN

def GetPt3D(useWPOnly, callback):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPt3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPt3D/ja
    \nマウスがクリックされるまで待機し、クリックされた点の3D座標を返します。'''
    return None

def Option():
    '''https://developer.vectorworks.net/index.php?title=VS:Option
    \nhttps://developer.vectorworks.net/index.php?title=VS:Option/ja
    \nMacではOptionキー、WindowsではAltキーが押されている場合は、TRUEを返します。'''
    return BOOLEAN

def TrackObject(callback):
    '''https://developer.vectorworks.net/index.php?title=VS:TrackObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:TrackObject/ja
    \nインタラクティブに条件に合致するオブジェクトを選択します。'''
    return (outObj, p)

def EndModeButtonsText():
    '''https://developer.vectorworks.net/index.php?title=VS:EndModeButtonsText
    \nhttps://developer.vectorworks.net/index.php?title=VS:EndModeButtonsText/ja
    \nモードバーボタンのヘルプテキストの作成を終了します。'''
    return None

def GetPtL(callback):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPtL
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPtL/ja
    \n指定した始点から直線が描かれ、マウスで終点が指示されるまで待機します。'''
    return None

def RunTempTool(initialScroll, toolCallback): 
    '''https://developer.vectorworks.net/index.php?title=VS:RunTempTool
    \nhttps://developer.vectorworks.net/index.php?title=VS:RunTempTool/ja
    \nテンポラリツール関数を呼ぶ。ツール関数が終了するまで待機します。コールバック関数へはツールイベントが通知されます。'''
    return None

def TrackObjectN(traverseType, callback):
    '''https://developer.vectorworks.net/index.php?title=VS:TrackObjectN
    \nhttps://developer.vectorworks.net/index.php?title=VS:TrackObjectN/ja
    \nインタラクティブに（ハイライトさせながら）条件に合致したオブジェクトを選択します。'''
    return (outObj, p)

def GetKeyDown():
    '''https://developer.vectorworks.net/index.php?title=VS:GetKeyDown
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetKeyDown/ja
    \nキーを押されるまで待機し、押されたキーのASCIIコードを返します。'''
    return asciiCode

def GetPtL3D(useWPOnly, callback):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPtL3D
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPtL3D/ja
    \n指定した始点から3D線分のラバーバンドが描かれ、マウスで終点が指示されるまで待機します。'''
    return None

def SetCursor(cursor):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCursor
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCursor/ja
    \nカーソルの形状を設定します。'''
    return None

def BeginContext():
    '''https://developer.vectorworks.net/index.php?title=VS:BeginContext
    \nhttps://developer.vectorworks.net/index.php?title=VS:BeginContext/ja
    \nこの手続きを実行した後、EndContextを実行するまでの変化を記録します。'''
    return None

def GetEnabledModules():
    '''https://developer.vectorworks.net/index.php?title=VS:GetEnabledModules
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetEnabledModules/ja
    \n現在利用可能なプロダクトモジュールの組み合わせを返します。'''
    return LONGINT

def PlanarPtToScreenPlanePt(refID, pt2D):
    '''https://developer.vectorworks.net/index.php?title=VS:PlanarPtToScreenPlanePt
    \nhttps://developer.vectorworks.net/index.php?title=VS:PlanarPtToScreenPlanePt/ja
    \n特定の平面上の2D座標をスクリーンプレーンに投影します。'''
    return (BOOLEAN, outPt)

def RunImageComp(FilePath, savedView, SettingsDir, imageWidth, imageHeight):
    '''https://developer.vectorworks.net/index.php?title=VS:RunImageComp'''
    return BOOLEAN

def BeginMultDashConvert():
    '''https://developer.vectorworks.net/index.php?title=VS:BeginMultDashConvert'''
    return None

def GetMainDisplayBounds():
    '''https://developer.vectorworks.net/index.php?title=VS:GetMainDisplayBounds
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetMainDisplayBounds/ja
    \n主画面の境界を返します（Macntoshのみ）'''
    return (outTop, outLeft, outBottom, outRight)

def PrepRelatedObjectForChange(objectAboutToBeChange):
    '''https://developer.vectorworks.net/index.php?title=VS:PrepRelatedObjectForChange
    \nhttps://developer.vectorworks.net/index.php?title=VS:PrepRelatedObjectForChange/ja
    \n行われようとしている変更に関連した図形を準備します。'''
    return None

def ScreenPlanePtToPlanarPt(refID, pt2D):
    '''https://developer.vectorworks.net/index.php?title=VS:ScreenPlanePtToPlanarPt
    \nhttps://developer.vectorworks.net/index.php?title=VS:ScreenPlanePtToPlanarPt/ja
    \nスクリーンプレーン上の2D座標を特定の平面上に投影します。'''
    return outPt

def CallToolByIndex(toolIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:CallToolByIndex
    \nhttps://developer.vectorworks.net/index.php?title=VS:CallToolByIndex/ja
    \nCallToolと同様。ツールの内部IDを引数にとる。'''
    return BOOLEAN

def GetModifierFlags():
    '''https://developer.vectorworks.net/index.php?title=VS:GetModifierFlags'''
    return (optionFlag, cmdFlag, shiftFlag)

def ProgressDlgClose():
    '''https://developer.vectorworks.net/index.php?title=VS:ProgressDlgClose
    \nhttps://developer.vectorworks.net/index.php?title=VS:ProgressDlgClose/ja
    \n進行状況ダイアログを閉じます。'''
    return None

def SetCallBackInval(turnInvalOn):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCallBackInval
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCallBackInval/ja
    \nコールバック関数による画面の更新を無効にするかどうかを設定します。計算のために一時的なオブジェクトを作ったときに、画面の更新をしたくない場合に使われます。'''
    return None

def CallToolByName(toolName):
    '''https://developer.vectorworks.net/index.php?title=VS:CallToolByName
    \nhttps://developer.vectorworks.net/index.php?title=VS:CallToolByName/ja
    \nCallToolと同様。IDの代わりに名前を引数にとる。プラグインツールに対応。（内部ツールには未対応）'''
    return BOOLEAN

def GetNetAdapterInfo(adapterIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetNetAdapterInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNetAdapterInfo/ja
    \nネットワークアダプターの情報を取得します。'''
    return (BOOLEAN, outMacAddr)

def ProgressDlgEnd():
    '''https://developer.vectorworks.net/index.php?title=VS:ProgressDlgEnd
    \nhttps://developer.vectorworks.net/index.php?title=VS:ProgressDlgEnd/ja
    \n進行度の増加を終了します。 開始時に設定した増加率だけ進行状況が推移します。'''
    return None

def SetCurrentObject(h):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCurrentObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCurrentObject/ja
    \nハンドルで指定した図形を、最後に作成された図形とします。'''
    return None

def CallToolWithMode(toolIndex, modeGroup, modeButton, callback):
    '''https://developer.vectorworks.net/index.php?title=VS:CallToolWithMode
    \nhttps://developer.vectorworks.net/index.php?title=VS:CallToolWithMode/ja
    \nアクティブツールとそのモードを設定します。終了すると、その前のアクティブツールに戻ります。'''
    return None

def GetOSVersion():
    '''https://developer.vectorworks.net/index.php?title=VS:GetOSVersion
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetOSVersion/ja
    \n動作しているOSのバージョンを返します。'''
    return (major, minor, incr)

def ProgressDlgHasCancel():
    '''https://developer.vectorworks.net/index.php?title=VS:ProgressDlgHasCancel
    \nhttps://developer.vectorworks.net/index.php?title=VS:ProgressDlgHasCancel/ja
    \nダイアログがキャンセルされたかどうかを返します。 ダイアログ作成時にキャンセルボタンが有効になっている必要があります。'''
    return BOOLEAN

def SetDrawingRect(paperWidth, paperHeight):
    '''https://developer.vectorworks.net/index.php?title=VS:SetDrawingRect
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetDrawingRect/ja
    \n用紙の大きさを設定します。'''
    return None

def ClrMessage():
    '''https://developer.vectorworks.net/index.php?title=VS:ClrMessage
    \nhttps://developer.vectorworks.net/index.php?title=VS:ClrMessage/ja
    \nメッセージウインドウを消去します。'''
    return None

def GetPaletteVisibility(paletteName):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPaletteVisibility
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPaletteVisibility/ja
    \nパレットの表示／非表示を返します。'''
    return BOOLEAN

def ProgressDlgOpen(title, canCancel):
    '''https://developer.vectorworks.net/index.php?title=VS:ProgressDlgOpen
    \nhttps://developer.vectorworks.net/index.php?title=VS:ProgressDlgOpen/ja
    \nスクリプトの進行状況を表示するダイアログを開きます。 ダイアログを閉じるには、 ProgressDlgClose を使用します。'''
    return None

def SetMaximumUndoEvents(events):
    '''https://developer.vectorworks.net/index.php?title=VS:SetMaximumUndoEvents
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetMaximumUndoEvents/ja
    \n取り消し可能な回数を設定します。'''
    return None

def ColorIndexToRGB(color):
    '''https://developer.vectorworks.net/index.php?title=VS:ColorIndexToRGB
    \nhttps://developer.vectorworks.net/index.php?title=VS:ColorIndexToRGB/ja
    \nカラーパレットの色番号から各色の成分を取り出します。値の範囲は0から65535までです。'''
    return (red, green, blue)

def GetPickObjectInfo(p):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPickObjectInfo
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPickObjectInfo/ja
    \n指定した座標の下にある図形のハンドルを返します。座標の下にある図形が、他の図形を内包されている場合（壁に挿入されたシンボルなど）は、内包されている図形のハンドルも返します。'''
    return (BOOLEAN, h, subH, message)

def ProgressDlgOpenDelay(title, canCancel, delaySec):
    '''https://developer.vectorworks.net/index.php?title=VS:ProgressDlgOpenDelay
    \nhttps://developer.vectorworks.net/index.php?title=VS:ProgressDlgOpenDelay/ja
    \nスクリプトの進行状況を表示するダイアログを開きます。 指定した時間(ミリ秒)が経過してからダイアログが表示されます。 ダイアログを閉じるには、 ProgressDlgClose を使用します。'''
    return None

def SetModeString(messageStr):
    '''https://developer.vectorworks.net/index.php?title=VS:SetModeString
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetModeString/ja
    \nモード文字列を設定します。'''
    return None

def ColorIndexToRGBN(color, ignoreBlackBackground):
    '''https://developer.vectorworks.net/index.php?title=VS:ColorIndexToRGBN
    \nhttps://developer.vectorworks.net/index.php?title=VS:ColorIndexToRGBN/ja
    \nカラーパレットの色番号から各色の成分を取り出します。値の範囲は0から65535までです。ignoreBlackBackgroundパラメータは背景色を黒にする設定を無視するか否かを設定します。TRUEに設定すると、白と黒のインデックスは背景色が黒であっても逆にされません。'''
    return (red, green, blue)

def GetPlantToolInitialized():
    '''https://developer.vectorworks.net/index.php?title=VS:GetPlantToolInitialized
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPlantToolInitialized/ja
    \n「植栽シンボル配置」ツールが初期化されているかどうかを返します。'''
    return BOOLEAN

def ProgressDlgSetBotMsg(message):
    '''https://developer.vectorworks.net/index.php?title=VS:ProgressDlgSetBotMsg
    \nhttps://developer.vectorworks.net/index.php?title=VS:ProgressDlgSetBotMsg/ja
    \n進行状況ダイアログの下部のメッセージを設定します。'''
    return None

def SetPaletteVisibility(paletteName, vis):
    '''https://developer.vectorworks.net/index.php?title=VS:SetPaletteVisibility
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetPaletteVisibility/ja
    \nパレットの表示／非表示を設定します。'''
    return None

def CreateUUID():
    '''https://developer.vectorworks.net/index.php?title=VS:CreateUUID
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateUUID/ja
    \nUniversally Unique Identifierを表す文字列を生成します。文字列は次のような形式である：'{00000000-0000-0000-0000-000000000000}''''
    return STRING

def GetPlantToolPlacementMode():
    '''https://developer.vectorworks.net/index.php?title=VS:GetPlantToolPlacementMode
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPlantToolPlacementMode/ja
    \n「植栽シンボル配置」ツールで設定されている配置モードを返します。'''
    return INTEGER

def ProgressDlgSetMeter(message):
    '''https://developer.vectorworks.net/index.php?title=VS:ProgressDlgSetMeter
    \nhttps://developer.vectorworks.net/index.php?title=VS:ProgressDlgSetMeter/ja
    \n進行状況ダイアログのメーター部分のメッセージを設定します。'''
    return None

def SetPlanarTransform(h):
    '''https://developer.vectorworks.net/index.php?title=VS:SetPlanarTransform
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetPlanarTransform/ja
    \n平面マトリックスを取得し、多角形の頂点を移動します。'''
    return HANDLE

def Date(dateFormat, infoFormat):
    '''https://developer.vectorworks.net/index.php?title=VS:Date
    \nhttps://developer.vectorworks.net/index.php?title=VS:Date/ja
    \n現在の日付と時間を文字列で返します。'''
    return STRING

def GetPlantToolPlantName():
    '''https://developer.vectorworks.net/index.php?title=VS:GetPlantToolPlantName
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPlantToolPlantName/ja
    \n「植栽シンボル配置の設定」ダイアログで設定した植栽名を返します。'''
    return STRING

def ProgressDlgSetTopMsg(message):
    '''https://developer.vectorworks.net/index.php?title=VS:ProgressDlgSetTopMsg
    \nhttps://developer.vectorworks.net/index.php?title=VS:ProgressDlgSetTopMsg/ja
    \n進行状況ダイアログの上部のメッセージを設定します。'''
    return None

def SetSavedSetting(category, setting, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetSavedSetting
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetSavedSetting/ja
    \n設定ファイル（SavedSettings.xml）に値を書き込みます。'''
    return None

def DelSavedSetting(category, setting):
    '''https://developer.vectorworks.net/index.php?title=VS:DelSavedSetting
    \nhttps://developer.vectorworks.net/index.php?title=VS:DelSavedSetting/ja
    \n保存された設定を削除します。'''
    return BOOLEAN

def GetPlantToolSpacing():
    '''https://developer.vectorworks.net/index.php?title=VS:GetPlantToolSpacing
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPlantToolSpacing/ja
    \n「植栽シンボル配置の設定」ダイアログで設定した間隔を返します。'''
    return REAL

def ProgressDlgStart(Percentage, LoopCount):
    '''https://developer.vectorworks.net/index.php?title=VS:ProgressDlgStart
    \nhttps://developer.vectorworks.net/index.php?title=VS:ProgressDlgStart/ja
    \n進行度の増加を開始します。 ProgressDlgYeld 呼び出し時に指定するループカウントを定義します。ループカウントにインデックスと増加率を設定します。'''
    return None

def SetToolByIndex(toolIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:SetToolByIndex
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetToolByIndex/ja
    \nSetToolと同様。ツールの内部IDを引数にとる。'''
    return BOOLEAN

def DelSavedSettings(category):
    '''https://developer.vectorworks.net/index.php?title=VS:DelSavedSettings
    \nhttps://developer.vectorworks.net/index.php?title=VS:DelSavedSettings/ja
    \n指定したカテゴリの保存された設定を全て削除します。'''
    return BOOLEAN

def GetProduct():
    '''https://developer.vectorworks.net/index.php?title=VS:GetProduct
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetProduct/ja
    \n製品番号とパッケージ番号を返します。'''
    return (product, modules)

def ProgressDlgYield(count):
    '''https://developer.vectorworks.net/index.php?title=VS:ProgressDlgYield
    \nhttps://developer.vectorworks.net/index.php?title=VS:ProgressDlgYield/ja
    \nインデックスで指定したループカントにより進行度を増加させます。 ProgressDlgStart と ProgressDlgEnd の間で呼ばれます。'''
    return None

def SetToolByName(toolName):
    '''https://developer.vectorworks.net/index.php?title=VS:SetToolByName
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetToolByName/ja
    \nSetToolと同様。IDではなく名前を引数にとる。プラグインツールに対応（内部ツールは未対応）。'''
    return BOOLEAN

def DisableModules(modules):
    '''https://developer.vectorworks.net/index.php?title=VS:DisableModules
    \nhttps://developer.vectorworks.net/index.php?title=VS:DisableModules/ja
    \n動作させないモジュールを設定します。モジュールパラメータは、どのモジュールで動作させないかを指定するビットフィールドです。'''
    return None

def GetPseudoIndFromDash(dashStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPseudoIndFromDash'''
    return (BOOLEAN, outPseudoIndex)

def PythonBeginContext():
    '''https://developer.vectorworks.net/index.php?title=VS:PythonBeginContext
    \nhttps://developer.vectorworks.net/index.php?title=VS:PythonBeginContext/ja
    \nこの関数はPythonExecuteスクリプトが実行されるコンテキストを作成します。'''
    return None

def SetToolWithMode(toolIndex, modeGroup, modeButton):
    '''https://developer.vectorworks.net/index.php?title=VS:SetToolWithMode
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetToolWithMode/ja
    \nツールパレットからツールをモードを指定して選択します。ツールが使われた後も、そのツールを選択したままにします。'''
    return None

def DisplayContextHelpOfCurrentPlugin():
    '''https://developer.vectorworks.net/index.php?title=VS:DisplayContextHelpOfCurrentPlugin
    \nhttps://developer.vectorworks.net/index.php?title=VS:DisplayContextHelpOfCurrentPlugin/ja
    \nアクティブなプラグインのヘルプをウェブブラウザに表示します。'''
    return None

def GetSavedSetting(category, setting):
    '''https://developer.vectorworks.net/index.php?title=VS:GetSavedSetting
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSavedSetting/ja
    \n設定ファイル（SavedSettings.xml）から値を読み込みます。'''
    return (BOOLEAN, value)

def PythonEndContext():
    '''https://developer.vectorworks.net/index.php?title=VS:PythonEndContext
    \nhttps://developer.vectorworks.net/index.php?title=VS:PythonEndContext/ja
    \nPythonBeginContextで開いたPythonコンテキストを閉じます。'''
    return None

def SetWorkingPlane(x, y, z, xRotation, yRotation, zRotation):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWorkingPlane
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWorkingPlane/ja
    \nワーキングプレーンのx,y,zオフセット値とx,y,z平面の回転角度を設定します。'''
    return None

def DisplayContextualHelp(Identifier):
    '''https://developer.vectorworks.net/index.php?title=VS:DisplayContextualHelp
    \nhttps://developer.vectorworks.net/index.php?title=VS:DisplayContextualHelp/ja
    \nコンテクストヘルプマネージャから提供されるGUI要素のID文字列を使用して、関連するコンテクストヘルプを表示します。このヘルプには、WebWorksのウェブページ、インターネットのウェブページ、またはローカルファイルを指定できます。'''
    return BOOLEAN

def GetScreen():
    '''https://developer.vectorworks.net/index.php?title=VS:GetScreen
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetScreen/ja
    \nモニタ画面の左上と右下の座標を返します。'''
    return (x1, y1, x2, y2)

def PythonExecute(script):
    '''https://developer.vectorworks.net/index.php?title=VS:PythonExecute
    \nhttps://developer.vectorworks.net/index.php?title=VS:PythonExecute/ja
    \n与えられたPythonスクリプトを実行します。'''
    return None

def SetWorkingPlaneN(centerPt, normal, uVec):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWorkingPlaneN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWorkingPlaneN/ja
    \nアクティブなワーキングプレーンを設定します。'''
    return None

def DisplayOrganizationDialog(tabToSelect):
    '''https://developer.vectorworks.net/index.php?title=VS:DisplayOrganizationDialog
    \nhttps://developer.vectorworks.net/index.php?title=VS:DisplayOrganizationDialog/ja
    \nデフォルトで選択するタブを指定して「階層」ダイアログを表示します。'''
    return None

def GetTickCount():
    '''https://developer.vectorworks.net/index.php?title=VS:GetTickCount
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTickCount/ja
    \nシステムの時間を返します。'''
    return LONGINT

def PythonGetSearchPath():
    '''https://developer.vectorworks.net/index.php?title=VS:PythonGetSearchPath
    \nhttps://developer.vectorworks.net/index.php?title=VS:PythonGetSearchPath/ja
    \nPythonファイルの検索パスを返します。'''
    return DYNARRAY[] of CHAR

def ShowWebDlg(title, url, buttonText, contextualHelpID):
    '''https://developer.vectorworks.net/index.php?title=VS:ShowWebDlg'''
    return None

def EditCriteriaWithUI(criteria):
    '''https://developer.vectorworks.net/index.php?title=VS:EditCriteriaWithUI
    \nhttps://developer.vectorworks.net/index.php?title=VS:EditCriteriaWithUI/ja
    \n条件編集ダイアログで検索条件を編集します。'''
    return (INTEGER, criteria)

def GetVersion():
    '''https://developer.vectorworks.net/index.php?title=VS:GetVersion
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVersion/ja
    \nVectorWorksのバージョンとOSの種類を返します。'''
    return (major, minor, maintenance, platform)

def PythonSetSearchPath(pathList):
    '''https://developer.vectorworks.net/index.php?title=VS:PythonSetSearchPath
    \nhttps://developer.vectorworks.net/index.php?title=VS:PythonSetSearchPath/ja
    \nPythonファイルの検索パスを設定します。'''
    return None

def SortArray(numtosort, fieldnumber):
    '''https://developer.vectorworks.net/index.php?title=VS:SortArray
    \nhttps://developer.vectorworks.net/index.php?title=VS:SortArray/ja
    \n指定した１次配列を並び替え（ソート）します。配列がレコードのハンドルの場合、指定したフィールド番号で並び替え（ソート）します。配列が構造体の配列の場合、fieldnumber には並び替え（ソート）する構造体の要素を設定します。'''
    return arraytosort

def EncryptAllPlugins():
    '''https://developer.vectorworks.net/index.php?title=VS:EncryptAllPlugins
    \nhttps://developer.vectorworks.net/index.php?title=VS:EncryptAllPlugins/ja
    \nThis will do batch encryption of all VectorScript plug-ins in the Plug-ins folder.'''
    return None

def GetVersionEx():
    '''https://developer.vectorworks.net/index.php?title=VS:GetVersionEx
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVersionEx/ja
    \nVectorWorksのバージョンとビルド番号とOSの種類を返します。'''
    return (major, minor, maintenance, platform, buildNum)

def RGBToColorIndex(red, green, blue):
    '''https://developer.vectorworks.net/index.php?title=VS:RGBToColorIndex
    \nhttps://developer.vectorworks.net/index.php?title=VS:RGBToColorIndex/ja
    \n各色の成分に一番近いカラーパレットの色番号を返します。値の範囲は0から65535までです。'''
    return color

def SysBeep():
    '''https://developer.vectorworks.net/index.php?title=VS:SysBeep
    \nhttps://developer.vectorworks.net/index.php?title=VS:SysBeep/ja
    \n警告音を鳴らします。'''
    return None

def EncryptPlugin(fullPath):
    '''https://developer.vectorworks.net/index.php?title=VS:EncryptPlugin
    \nhttps://developer.vectorworks.net/index.php?title=VS:EncryptPlugin/ja
    \nEncrypt one VectorScript Plug-in file.'''
    return BOOLEAN

def GetWorkingPlane():
    '''https://developer.vectorworks.net/index.php?title=VS:GetWorkingPlane
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWorkingPlane/ja
    \nワーキングプレーンの位置と方向を返します。'''
    return (x, y, z, xRotation, yRotation, zRotation)

def RGBToColorIndexN(red, green, blue, ignoreBlackBackground):
    '''https://developer.vectorworks.net/index.php?title=VS:RGBToColorIndexN
    \nhttps://developer.vectorworks.net/index.php?title=VS:RGBToColorIndexN/ja
    \n各色の成分に一番近いカラーパレットの色番号を返します。値の範囲は0から65535までです。ignoreBlackBackgroundパラメータは背景色を黒にする設定を無視するか否かを設定します。TRUEに設定すると、白と黒のインデックスは背景色が黒であっても逆にされません。'''
    return color

def TBB_AttachRecords():
    '''https://developer.vectorworks.net/index.php?title=VS:TBB_AttachRecords'''
    return TitleBlockBorder

def EndContext(acceptOrReject):
    '''https://developer.vectorworks.net/index.php?title=VS:EndContext
    \nhttps://developer.vectorworks.net/index.php?title=VS:EndContext/ja
    \nBegin/Endブロックの間に、自動的になされたどんな変更にも対応する／しないを設定します。BeginContextとともに使用します。'''
    return None

def GetWorkingPlaneMat(refID):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWorkingPlaneMat
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWorkingPlaneMat/ja
    \n指定したワーキングプレーンマトリックスを取得します。'''
    return (outCenterPt, outNormal, outUVec)

def ReDraw():
    '''https://developer.vectorworks.net/index.php?title=VS:ReDraw
    \nhttps://developer.vectorworks.net/index.php?title=VS:ReDraw/ja
    \n直前に作成または変更された図形を再描画します。'''
    return None

def TBB_GetPageArea(LayerHand):
    '''https://developer.vectorworks.net/index.php?title=VS:TBB_GetPageArea'''
    return (PageWidth, PageHeight)

def EndMultDashConvert():
    '''https://developer.vectorworks.net/index.php?title=VS:EndMultDashConvert'''
    return None

def GetWorkingPlaneN():
    '''https://developer.vectorworks.net/index.php?title=VS:GetWorkingPlaneN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWorkingPlaneN/ja
    \nアクティブなワーキングプレーンを取得します。'''
    return (outCenterPt, outNormal, outUVec)

def ReDrawAll():
    '''https://developer.vectorworks.net/index.php?title=VS:ReDrawAll
    \nhttps://developer.vectorworks.net/index.php?title=VS:ReDrawAll/ja
    \nすべての図形を再描画します。'''
    return None

def TBB_OpenTBBSelDlg(StyleName, SheetSize, TBWidth, TBHeight):
    '''https://developer.vectorworks.net/index.php?title=VS:TBB_OpenTBBSelDlg'''
    return (StyleName, SheetSize, TBWidth, TBHeight)

def ExportImageFile(hHmage, filePath):
    '''https://developer.vectorworks.net/index.php?title=VS:ExportImageFile
    \nhttps://developer.vectorworks.net/index.php?title=VS:ExportImageFile/ja
    \n指定したイメージ図形をイメージファイルとして取り出します。'''
    return BOOLEAN

def ImportImageFile(filePath, importPt):
    '''https://developer.vectorworks.net/index.php?title=VS:ImportImageFile
    \nhttps://developer.vectorworks.net/index.php?title=VS:ImportImageFile/ja
    \n指定したイメージファイルをVectorworksのイメージ図形として取り込みます。'''
    return HANDLE

def RedrawSelection():
    '''https://developer.vectorworks.net/index.php?title=VS:RedrawSelection
    \nhttps://developer.vectorworks.net/index.php?title=VS:RedrawSelection/ja
    \n選択されている図形を再描画します。'''
    return None

def TBB_UpdateOldBorders():
    '''https://developer.vectorworks.net/index.php?title=VS:TBB_UpdateOldBorders'''
    return NumUpdated

def FndError():
    '''https://developer.vectorworks.net/index.php?title=VS:FndError
    \nhttps://developer.vectorworks.net/index.php?title=VS:FndError/ja
    \n直前で実行したプログラムにエラーが発生した場合はTRUEを返します。'''
    return BOOLEAN

def ImportImageFileN(filePath, importPt, mode):
    '''https://developer.vectorworks.net/index.php?title=VS:ImportImageFileN
    \nhttps://developer.vectorworks.net/index.php?title=VS:ImportImageFileN/ja
    \n指定したイメージファイルをVectorworksのイメージ図形として取り込みます。取り込み時にオプションを設定できます。'''
    return HANDLE

def RefreshResManager(updateVWLibs, updateUserLibs, updateWGLibs, updateFavs, UpdateOnlineLibs):
    '''https://developer.vectorworks.net/index.php?title=VS:RefreshResManager'''
    return REAL

def TBB_UpdateOldVAATB():
    '''https://developer.vectorworks.net/index.php?title=VS:TBB_UpdateOldVAATB'''
    return None

def ForEachObjectAtPoint(actionFunc, objOptions, travOptions, loc, pickRadius):
    '''https://developer.vectorworks.net/index.php?title=VS:ForEachObjectAtPoint
    \nhttps://developer.vectorworks.net/index.php?title=VS:ForEachObjectAtPoint/ja
    \n指定した座標の下にある、条件に合致した図形を、指定した手続きで処理します。'''
    return None

def InstallScriptAddPath(fullPath):
    '''https://developer.vectorworks.net/index.php?title=VS:InstallScriptAddPath'''
    return None

def ResetObject(objectHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:ResetObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:ResetObject/ja
    \n現在の設定やパラメータの値を使って指定した図形を更新します。図形のバウンドボックスをリセットします。壁の中の図形であれば、壁もリセットします。'''
    return None

def TestEncryptPlugins():
    '''https://developer.vectorworks.net/index.php?title=VS:TestEncryptPlugins'''
    return None

def ForEachObjectInLayer(actionFunc, objOptions, travOptions, layerOptions):
    '''https://developer.vectorworks.net/index.php?title=VS:ForEachObjectInLayer
    \nhttps://developer.vectorworks.net/index.php?title=VS:ForEachObjectInLayer/ja
    \n指定した条件に合致した図形を、指定した手続きで処理します。'''
    return None

def IsCoPlanar(refID1, refID2):
    '''https://developer.vectorworks.net/index.php?title=VS:IsCoPlanar
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsCoPlanar/ja
    \n2つの平面が同一平面の場合、TRUEを返します。'''
    return BOOLEAN

def Rpstr_GetValueBool(name, defaultValue):
    '''https://developer.vectorworks.net/index.php?title=VS:Rpstr_GetValueBool
    \nhttps://developer.vectorworks.net/index.php?title=VS:Rpstr_GetValueBool/ja
    \nVectorScriptのリポジトリからブール値を取得します。'''
    return BOOLEAN

def UndoOff():
    '''https://developer.vectorworks.net/index.php?title=VS:UndoOff
    \nhttps://developer.vectorworks.net/index.php?title=VS:UndoOff/ja
    \n記録している取り消し操作をすべて破棄し、以降のスクリプト実行について取り消し操作を記録しない。関数の実行後取り消し（undo）システムは元に戻ります。'''
    return None

def ForEachObjectInList(actionFunc, objOptions, travOptions, list):
    '''https://developer.vectorworks.net/index.php?title=VS:ForEachObjectInList
    \nhttps://developer.vectorworks.net/index.php?title=VS:ForEachObjectInList/ja
    \n指定した条件に合致した図形を、指定した手続きで処理します。'''
    return None

def IsPerpPlane(refID1, refID2):
    '''https://developer.vectorworks.net/index.php?title=VS:IsPerpPlane
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsPerpPlane/ja
    \n2つの平面が直交している場合、TRUEを返します。'''
    return BOOLEAN

def Rpstr_GetValueInt(name, defaultValue):
    '''https://developer.vectorworks.net/index.php?title=VS:Rpstr_GetValueInt
    \nhttps://developer.vectorworks.net/index.php?title=VS:Rpstr_GetValueInt/ja
    \nVectorScriptのリポジトリから整数値を取得します。'''
    return INTEGER

def UpdatePIOFromStyle():
    '''https://developer.vectorworks.net/index.php?title=VS:UpdatePIOFromStyle'''
    return pioHandle

def GetActiveSerialNumber():
    '''https://developer.vectorworks.net/index.php?title=VS:GetActiveSerialNumber
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetActiveSerialNumber/ja
    \nアクティブなシリアル番号を返します。'''
    return STRING

def LandmarkMatchSlope(h, h3d, landmarkObj):
    '''https://developer.vectorworks.net/index.php?title=VS:LandmarkMatchSlope
    \nhttps://developer.vectorworks.net/index.php?title=VS:LandmarkMatchSlope/ja
    \n傾斜と造成図形の勾配基準線の角度を、3D多角形に合わせます。'''
    return None

def Rpstr_GetValueReal(name, defaultValue):
    '''https://developer.vectorworks.net/index.php?title=VS:Rpstr_GetValueReal
    \nhttps://developer.vectorworks.net/index.php?title=VS:Rpstr_GetValueReal/ja
    \nVectorScriptのリポジトリからREAL型の値を取得します。'''
    return REAL

def ValidAngStr(str):
    '''https://developer.vectorworks.net/index.php?title=VS:ValidAngStr
    \nhttps://developer.vectorworks.net/index.php?title=VS:ValidAngStr/ja
    \n文字列を角度に変換します。変換できた場合はTRUEを返します。'''
    return (BOOLEAN, value)

def GetArrayDimensions(arrayname):
    '''https://developer.vectorworks.net/index.php?title=VS:GetArrayDimensions
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetArrayDimensions/ja
    \n指定した配列の大きさを返します。'''
    return (rowStart, rowEnd, columnStart, columnEnd)

def Message(z):
    '''https://developer.vectorworks.net/index.php?title=VS:Message
    \nhttps://developer.vectorworks.net/index.php?title=VS:Message/ja
    \nメッセージウインドウに文字列を表示します。'''
    return None

def Rpstr_GetValueStr(name, defaultValue):
    '''https://developer.vectorworks.net/index.php?title=VS:Rpstr_GetValueStr
    \nhttps://developer.vectorworks.net/index.php?title=VS:Rpstr_GetValueStr/ja
    \nVectorScriptのリポジトリからの文字列値を取得します。'''
    return DYNARRAY[] of CHAR

def ValidNumStr(str):
    '''https://developer.vectorworks.net/index.php?title=VS:ValidNumStr
    \nhttps://developer.vectorworks.net/index.php?title=VS:ValidNumStr/ja
    \n文字列を数値に変換します。変換できた場合はTRUEを返します。'''
    return (BOOLEAN, value)

def GetCallBackInval():
    '''https://developer.vectorworks.net/index.php?title=VS:GetCallBackInval
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCallBackInval/ja
    \nコールバック関数による画面の更新を無効にしているかどうかを返します。'''
    return BOOLEAN

def NameUndoEvent(eventName):
    '''https://developer.vectorworks.net/index.php?title=VS:NameUndoEvent
    \nhttps://developer.vectorworks.net/index.php?title=VS:NameUndoEvent/ja
    \nスクリプトの実行開始から構築された取り消し（undo）イベントに名前をつけます。引数eventNameが取り消しイベントの名前となります。'''
    return None

def Rpstr_RemoveValue(name):
    '''https://developer.vectorworks.net/index.php?title=VS:Rpstr_RemoveValue
    \nhttps://developer.vectorworks.net/index.php?title=VS:Rpstr_RemoveValue/ja
    \nVectorScriptのリポジトリから名前付きの値を削除します。'''
    return BOOLEAN

def VerifyLibraryRoutine(routineName):
    '''https://developer.vectorworks.net/index.php?title=VS:VerifyLibraryRoutine
    \nhttps://developer.vectorworks.net/index.php?title=VS:VerifyLibraryRoutine/ja
    \n指定した名前の外部関数が有効の場合はTRUEを返します。'''
    return BOOLEAN

def GetClosestPt(obj, pt):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClosestPt
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClosestPt/ja
    \nハンドルで指定した図形の頂点を返します。頂点が見つからない場合は、0を返します。'''
    return (obj, index, containedObj)

def ObjPropsEditDlg(hObj):
    '''https://developer.vectorworks.net/index.php?title=VS:ObjPropsEditDlg
    \nhttps://developer.vectorworks.net/index.php?title=VS:ObjPropsEditDlg/ja
    \nオブジェクトのプロパティを編集するダイアログを表示します。'''
    return BOOLEAN

def Rpstr_RemoveValues():
    '''https://developer.vectorworks.net/index.php?title=VS:Rpstr_RemoveValues
    \nhttps://developer.vectorworks.net/index.php?title=VS:Rpstr_RemoveValues/ja
    \nVectorScriptのリポジトリからすべての値を削除します。'''
    return None

def Wait(seconds):
    '''https://developer.vectorworks.net/index.php?title=VS:Wait
    \nhttps://developer.vectorworks.net/index.php?title=VS:Wait/ja
    \n指定した秒数が経過するまで、プログラムを停止します。'''
    return None

def GetClosestSide(obj, pt):
    '''https://developer.vectorworks.net/index.php?title=VS:GetClosestSide
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetClosestSide/ja
    \nハンドルで指定した2次元図形で、指定した座標に最も近い頂点の番号を返します。'''
    return (index1, index2)

def OpenScriptResPal(paletteName, open):
    '''https://developer.vectorworks.net/index.php?title=VS:OpenScriptResPal
    \nhttps://developer.vectorworks.net/index.php?title=VS:OpenScriptResPal/ja
    \nスクリプトリソースパレットを開く、あるいは閉じます。'''
    return None

def Rpstr_SetValueBool(name, value):
    '''https://developer.vectorworks.net/index.php?title=VS:Rpstr_SetValueBool
    \nhttps://developer.vectorworks.net/index.php?title=VS:Rpstr_SetValueBool/ja
    \nVectorScriptのリポジトリからブール値を設定します。'''
    return None

def WebDlgEnableConsole(enable):
    '''https://developer.vectorworks.net/index.php?title=VS:WebDlgEnableConsole'''
    return None

def GetCurrentLocalization():
    '''https://developer.vectorworks.net/index.php?title=VS:GetCurrentLocalization
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCurrentLocalization/ja
    \nVectorworksの言語環境をISO 639-3 ドラフト形式の言語IDで返します。sublanguageは現在使われていません。'''
    return (language, subLanguage)

def OpenURL(URLname):
    '''https://developer.vectorworks.net/index.php?title=VS:OpenURL
    \nhttps://developer.vectorworks.net/index.php?title=VS:OpenURL/ja
    \nデフォルトブラウザやAdobe Acrobatを使ってURLを開きます。URLが開けた場合はTRUEを返します。'''
    return BOOLEAN

def Rpstr_SetValueInt(name, value):
    '''https://developer.vectorworks.net/index.php?title=VS:Rpstr_SetValueInt
    \nhttps://developer.vectorworks.net/index.php?title=VS:Rpstr_SetValueInt/ja
    \nVectorScriptのリポジトリから整数値を設定します。'''
    return None

def GetCurrentMode():
    '''https://developer.vectorworks.net/index.php?title=VS:GetCurrentMode
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCurrentMode/ja
    \nアプリケーションの現在のプロテクトモードを返します。'''
    return INTEGER

def PickObject(p):
    '''https://developer.vectorworks.net/index.php?title=VS:PickObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:PickObject/ja
    \n指定した座標の下にある図形のうち、最上位の図形のハンドルを返します。'''
    return HANDLE

def Rpstr_SetValueReal(name, value):
    '''https://developer.vectorworks.net/index.php?title=VS:Rpstr_SetValueReal
    \nhttps://developer.vectorworks.net/index.php?title=VS:Rpstr_SetValueReal/ja
    \nVectorScriptのリポジトリからREAL型の値を設定します。'''
    return None

def GetDashFromPseudoInd(pseudoIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:GetDashFromPseudoInd'''
    return (BOOLEAN, outDashStyle)

def PlanarPtTo3DModelPt(refID, pt2D):
    '''https://developer.vectorworks.net/index.php?title=VS:PlanarPtTo3DModelPt
    \nhttps://developer.vectorworks.net/index.php?title=VS:PlanarPtTo3DModelPt/ja
    \n指定した平面の2D座標を3D座標に変換します。'''
    return (BOOLEAN, outPt3D)

def Rpstr_SetValueStr(name, value):
    '''https://developer.vectorworks.net/index.php?title=VS:Rpstr_SetValueStr
    \nhttps://developer.vectorworks.net/index.php?title=VS:Rpstr_SetValueStr/ja
    \nVectorScriptのリポジトリからの文字列を設定します。'''
    return None

def CreateHLHandle():
    '''https://developer.vectorworks.net/index.php?title=VS:CreateHLHandle
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateHLHandle/ja
    \n新しいVW-陰線レンダリング設定へのハンドルを作ります。'''
    return HLOptionsHandle

def GetHLLineStyle(HLOptionsHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetHLLineStyle'''
    return lineStyle

def RetrieveCustomRWPrefs():
    '''https://developer.vectorworks.net/index.php?title=VS:RetrieveCustomRWPrefs
    \nhttps://developer.vectorworks.net/index.php?title=VS:RetrieveCustomRWPrefs/ja
    \n現在の図面のRenderworksレンダリング設定を取得します。'''
    return (useTextures, useTransparency, useShadows, useRayTracing, useAntiAliasing, useDithering, tessellationDetail, shadowStyle, rayTracingRecursion)

def SetView(xAngle, yAngle, zAngle, xDistance, yDistance, zDistance):
    '''https://developer.vectorworks.net/index.php?title=VS:SetView
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetView/ja
    \n視点を、指定した3次元軸を中心に、指定した角度で回転させます。'''
    return None

def CreateOpenGLHandle():
    '''https://developer.vectorworks.net/index.php?title=VS:CreateOpenGLHandle
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateOpenGLHandle/ja
    \n新しいOpenGL設定へのハンドルを返します。'''
    return GLHandle

def GetProjection(theyLayer):
    '''https://developer.vectorworks.net/index.php?title=VS:GetProjection
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetProjection/ja
    \nレイヤの投影方法の状態を返します。'''
    return INTEGER

def RetrieveHLPrefs():
    '''https://developer.vectorworks.net/index.php?title=VS:RetrieveHLPrefs
    \nhttps://developer.vectorworks.net/index.php?title=VS:RetrieveHLPrefs/ja
    \n現在の図面の隠線消去レンダリング設定を取得します。'''
    return (smoothingAngle, lineStyle, shadeFactorIndex, doIntersections)

def SetViewVector(location, target, up):
    '''https://developer.vectorworks.net/index.php?title=VS:SetViewVector
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetViewVector/ja
    \n3D視点の座標を設定します。'''
    return None

def CreateRWHandle():
    '''https://developer.vectorworks.net/index.php?title=VS:CreateRWHandle
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateRWHandle/ja
    \n新しいRenderWorks設定へのハンドルを返します。'''
    return RWHandle

def GetVCenter():
    '''https://developer.vectorworks.net/index.php?title=VS:GetVCenter
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVCenter/ja
    \nドキュメントウインドウで表示されている中心の座標を返します。'''
    return center

def RetrieveOpenGLPrefs():
    '''https://developer.vectorworks.net/index.php?title=VS:RetrieveOpenGLPrefs
    \nhttps://developer.vectorworks.net/index.php?title=VS:RetrieveOpenGLPrefs/ja
    \n現在の図面のOpenGLレンダリング設定を取得します。'''
    return (useTextures, tessellationDetail, useNURBS)

def SetZoom(zoomfactor):
    '''https://developer.vectorworks.net/index.php?title=VS:SetZoom
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetZoom/ja
    \n画面の拡大／縮小率を設定します。'''
    return None

def CreateRenderworksStyle():
    '''https://developer.vectorworks.net/index.php?title=VS:CreateRenderworksStyle
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateRenderworksStyle/ja'''
    return HANDLE

def GetView():
    '''https://developer.vectorworks.net/index.php?title=VS:GetView
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetView/ja
    \n現在の視点の情報を返します。'''
    return (xAngleR, yAngelR, zAngleR, offset)

def SaveSheet(name, saveView, saveClass, saveLayer):
    '''https://developer.vectorworks.net/index.php?title=VS:SaveSheet
    \nhttps://developer.vectorworks.net/index.php?title=VS:SaveSheet/ja
    \n現在の画面を、指定した名前で登録します。'''
    return None

def VDelete(name):
    '''https://developer.vectorworks.net/index.php?title=VS:VDelete
    \nhttps://developer.vectorworks.net/index.php?title=VS:VDelete/ja
    \n登録されている画面を削除します。'''
    return None

def EditOpenGLPrefs():
    '''https://developer.vectorworks.net/index.php?title=VS:EditOpenGLPrefs
    \nhttps://developer.vectorworks.net/index.php?title=VS:EditOpenGLPrefs/ja
    \nユーザーが現在の書類にOpenGL設定を編集して保存するできるようにします。'''
    return updateRendering

def GetZoom():
    '''https://developer.vectorworks.net/index.php?title=VS:GetZoom
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetZoom/ja
    \n現在の画面の拡大／縮小率を返します。'''
    return REAL

def SetHLLineStyle(HLOptionsHandle, lineStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetHLLineStyle'''
    return None

def VRestore(name):
    '''https://developer.vectorworks.net/index.php?title=VS:VRestore
    \nhttps://developer.vectorworks.net/index.php?title=VS:VRestore/ja
    \n登録されている画面を呼び出して表示します。'''
    return None

def EditRenderWorksPrefs():
    '''https://developer.vectorworks.net/index.php?title=VS:EditRenderWorksPrefs
    \nhttps://developer.vectorworks.net/index.php?title=VS:EditRenderWorksPrefs/ja
    \nユーザーが現在の書類にRenderWorks設定を編集して保存するできるようにします。'''
    return updateRendering

def Projection(proj, rMode, viewDistance, clip1, clip2):
    '''https://developer.vectorworks.net/index.php?title=VS:Projection
    \nhttps://developer.vectorworks.net/index.php?title=VS:Projection/ja
    \n3次元の見え方やレンダリングの種類を設定します。'''
    return None

def SetVCenter(viewCenter):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVCenter
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetVCenter/ja
    \n画面の表示位置を、指定した座標に移動します。'''
    return None

def VSave(name):
    '''https://developer.vectorworks.net/index.php?title=VS:VSave
    \nhttps://developer.vectorworks.net/index.php?title=VS:VSave/ja
    \n現在の画面を、指定した名前で登録します。'''
    return None

def CreateVPClOvrd(viewportHandle, className):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateVPClOvrd
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateVPClOvrd/ja
    \nビューポートのクラスに対してビューポートクラスを作成します。ビューポートクラスには現在のクラス設定が反映されます。'''
    return None

def GetVPClOvrdPenBack(viewportHandle, className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPClOvrdPenBack
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVPClOvrdPenBack/ja
    \nビューポートクラスの線の背景色を返します。色は0~65535の三つのRGB値で返されます。'''
    return (colorRV, colorGV, colorBV)

def GetVPLrOvrdPenFore(viewportHandle, layerHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPLrOvrdPenFore
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVPLrOvrdPenFore/ja
    \nビューポートレイヤの線の前景色を返します。'''
    return (colorRV, colorGV, colorBV)

def SetVPClOvrdPenFore(viewportHandle, className, colorRV, colorGV, colorBV):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVPClOvrdPenFore
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetVPClOvrdPenFore/ja
    \nビューポートクラスの線の前景色を設定します。色は0~65535の三つのRGB値で返されます。'''
    return None

def CreateVPLrOvrd(viewportHandle, layerHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateVPLrOvrd
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateVPLrOvrd/ja
    \n新規のビューポートレイヤを作成し、レイヤの現在のプロパティに設定します。'''
    return None

def GetVPClOvrdPenFore(viewportHandle, className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPClOvrdPenFore
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVPClOvrdPenFore/ja
    \nビューポートクラスの線の前景色を返します。色は0~65535の三つのRGB値で返されます。'''
    return (colorRV, colorGV, colorBV)

def RemoveVPClOvrd(viewportHandle, className):
    '''https://developer.vectorworks.net/index.php?title=VS:RemoveVPClOvrd
    \nhttps://developer.vectorworks.net/index.php?title=VS:RemoveVPClOvrd/ja
    \n指定したビューポートからビューポートクラスを削除します。'''
    return None

def SetVPClOvrdPenOpty(viewportHandle, className, penOpacity):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVPClOvrdPenOpty
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetVPClOvrdPenOpty/ja
    \nビューポートクラスの線の不透明度を設定します。'''
    return None

def GetVPClOvrdCount(viewportHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPClOvrdCount
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVPClOvrdCount/ja
    \n特定のビューポートで使用しているビューポートクラスの数を返します。'''
    return INTEGER

def GetVPClOvrdPenOpty(viewportHandle, className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPClOvrdPenOpty
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVPClOvrdPenOpty/ja
    \nビューポートクラスの線の不透明度を返します。不透明度は 0-100 です。'''
    return INTEGER

def RemoveVPLrOvrd(viewportHandle, layerHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:RemoveVPLrOvrd
    \nhttps://developer.vectorworks.net/index.php?title=VS:RemoveVPLrOvrd/ja
    \nビューポートレイヤを削除します。'''
    return None

def SetVPClOvrdRoofTxt(viewportHandle, className, topMaterial, dormerMaterial):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVPClOvrdRoofTxt'''
    return None

def GetVPClOvrdFillBack(viewportHandle, className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPClOvrdFillBack
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVPClOvrdFillBack/ja
    \nビューポートクラスの背景色を返します。色は0~65535の三つのRGB値で返されます。'''
    return (colorRV, colorGV, colorBV)

def GetVPClOvrdRoofTxt(viewportHandle, className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPClOvrdRoofTxt'''
    return (topMaterial, dormerMaterial)

def SetVPClOvrdFillBack(viewportHandle, className, colorRV, colorGV, colorBV):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVPClOvrdFillBack
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetVPClOvrdFillBack/ja
    \nビューポートクラスの背景色を設定します。色は0~65535の三つのRGB値で返されます。'''
    return None

def SetVPClOvrdWallTxt(viewportHandle, className, leftTexture, centerTexture, rightTexture):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVPClOvrdWallTxt'''
    return None

def GetVPClOvrdFillFore(viewportHandle, className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPClOvrdFillFore
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVPClOvrdFillFore/ja
    \nビューポートクラスの前景色を返します。 色は0~65535の三つのRGB値で返されます。'''
    return (colorRV, colorGV, colorBV)

def GetVPClOvrdWallTxt(viewportHandle, className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPClOvrdWallTxt'''
    return (leftTexture, centerTexture, rightTexture)

def SetVPClOvrdFillFore(viewportHandle, className, colorRV, colorGV, colorBV):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVPClOvrdFillFore
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetVPClOvrdFillFore/ja
    \nビューポートクラスの前景色を設定します。色は0~65535の三つのRGB値で返されます。'''
    return None

def SetVPLrOvrdFillBack(viewportHandle, layerHandle, colorRV, colorGV, colorBV):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVPLrOvrdFillBack
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetVPLrOvrdFillBack/ja
    \nビューポートレイヤの背景色を設定します。'''
    return None

def GetVPClOvrdFillOpty(viewportHandle, className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPClOvrdFillOpty
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVPClOvrdFillOpty/ja
    \nビューポートクラスの面の不透明度を返します。'''
    return INTEGER

def GetVPLrOvrdCount(viewportHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPLrOvrdCount
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVPLrOvrdCount/ja
    \nビューポートレイヤの数を返します。'''
    return INTEGER

def SetVPClOvrdFillOpty(viewportHandle, className, fillOpacity):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVPClOvrdFillOpty
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetVPClOvrdFillOpty/ja
    \nビューポートクラスの面の不透明度を設定します。'''
    return None

def SetVPLrOvrdFillFore(viewportHandle, layerHandle, colorRV, colorGV, colorBV):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVPLrOvrdFillFore
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetVPLrOvrdFillFore/ja
    \nビューポートレイヤの前景色を設定します。'''
    return None

def GetVPClOvrdFillStyle(viewportHandle, className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPClOvrdFillStyle'''
    return LONGINT

def GetVPLrOvrdFillBack(viewportHandle, layerHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPLrOvrdFillBack
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVPLrOvrdFillBack/ja
    \nビューポートレイヤの背景色を返します。'''
    return (colorRV, colorGV, colorBV)

def SetVPClOvrdFillStyle(viewportHandle, className, fillStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVPClOvrdFillStyle'''
    return None

def SetVPLrOvrdOpty(viewportHandle, layerHandle, opacity):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVPLrOvrdOpty
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetVPLrOvrdOpty/ja
    \nビューポートレイヤの不透明度を設定します。'''
    return None

def GetVPClOvrdLineStyle(viewportHandle, className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPClOvrdLineStyle'''
    return LONGINT

def GetVPLrOvrdFillFore(viewportHandle, layerHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPLrOvrdFillFore
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVPLrOvrdFillFore/ja
    \nビューポートレイヤの前景色を返します。'''
    return (colorRV, colorGV, colorBV)

def SetVPClOvrdLineStyle(viewportHandle, className, lineStyle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVPClOvrdLineStyle'''
    return None

def SetVPLrOvrdPenBack(viewportHandle, layerHandle, colorRV, colorGV, colorBV):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVPLrOvrdPenBack
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetVPLrOvrdPenBack/ja
    \nビューポートレイヤの線の背景色を設定します。'''
    return None

def GetVPClOvrdLnWeight(viewportHandle, className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPClOvrdLnWeight'''
    return INTEGER

def GetVPLrOvrdHandle(viewportHandle, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPLrOvrdHandle
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVPLrOvrdHandle/ja
    \nビューポートレイヤ一覧の指定した番号のレイヤのハンドルを返します。'''
    return HANDLE

def SetVPClOvrdLnWeight(viewportHandle, className, LineWeight):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVPClOvrdLnWeight'''
    return None

def SetVPLrOvrdPenFore(viewportHandle, layerHandle, colorRV, colorGV, colorBV):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVPLrOvrdPenFore
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetVPLrOvrdPenFore/ja
    \nビューポートレイヤの線の前景色を設定します。'''
    return None

def GetVPClOvrdName(viewportHandle, index):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPClOvrdName
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVPClOvrdName/ja
    \nビューポートクラス一覧の指定した番号のクラスの名前を返します。'''
    return STRING

def GetVPLrOvrdOpty(viewportHandle, layerHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPLrOvrdOpty
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVPLrOvrdOpty/ja
    \nビューポートレイヤの不透明度を返します。'''
    return INTEGER

def SetVPClOvrdObjTxt(viewportHandle, className, objectTexture):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVPClOvrdObjTxt'''
    return None

def GetVPClOvrdObjTxt(viewportHandle, className):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPClOvrdObjTxt'''
    return INTEGER

def GetVPLrOvrdPenBack(viewportHandle, layerHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetVPLrOvrdPenBack
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetVPLrOvrdPenBack/ja
    \nビューポートレイヤの線の背景色を返します。'''
    return (colorRV, colorGV, colorBV)

def SetVPClOvrdPenBack(viewportHandle, className, colorRV, colorGV, colorBV):
    '''https://developer.vectorworks.net/index.php?title=VS:SetVPClOvrdPenBack
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetVPClOvrdPenBack/ja
    \nビューポートクラスの線の背景色を設定します。色は0~65535の三つのRGB値で返されます。'''
    return None

def ActSSheet():
    '''https://developer.vectorworks.net/index.php?title=VS:ActSSheet
    \nhttps://developer.vectorworks.net/index.php?title=VS:ActSSheet/ja
    \nアクティブなワークシートのハンドルを返します。'''
    return HANDLE

def GetWSColumnWidth(worksheet, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSColumnWidth
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSColumnWidth/ja
    \nハンドルで指定したワークシートの、指定した列の幅を返します。'''
    return width

def IsWSVisible(worksheet):
    '''https://developer.vectorworks.net/index.php?title=VS:IsWSVisible
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsWSVisible/ja
    \nハンドルで指定したワークシートが表示されている場合はTRUEを返します。'''
    return BOOLEAN

def SetWSCurrentCell(worksheet, currentCellRow, currentCellColumn):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCurrentCell
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSCurrentCell/ja
    \nハンドルで指定したワークシートの、指定したセルをアクティブにします。'''
    return None

def AddWSColumnOperator(worksheet, databaseRow, column, operatorType):
    '''https://developer.vectorworks.net/index.php?title=VS:AddWSColumnOperator
    \nhttps://developer.vectorworks.net/index.php?title=VS:AddWSColumnOperator/ja
    \nハンドルで指定したワークシートの、指定したセルに並び替え（ソート）と合計を追加します。'''
    return None

def GetWSFromImage(worksheetImage):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSFromImage
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSFromImage/ja
    \n図形モードのワークシートのハンドルを与えると、そのワークシートのハンドルを返します。'''
    return HANDLE

def LoadCell(ro, col, entry):
    '''https://developer.vectorworks.net/index.php?title=VS:LoadCell
    \nhttps://developer.vectorworks.net/index.php?title=VS:LoadCell/ja
    \nアクティブなワークシートの指定したセルに文字列を入力します。'''
    return None

def SetWSImageScaleF(handle, scaleFactor, redraw):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSImageScaleF
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSImageScaleF/ja
    \n指定したワークシートのイメージの倍率を設定します。'''
    return None

def AreWorksheetGridLinesVisible(h):
    '''https://developer.vectorworks.net/index.php?title=VS:AreWorksheetGridLinesVisible
    \nhttps://developer.vectorworks.net/index.php?title=VS:AreWorksheetGridLinesVisible/ja
    \nグリッドラインが、指定したワークシートで現在有効であるかどうかを返します。'''
    return BOOLEAN

def GetWSImage(worksheet):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSImage
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSImage/ja
    \nワークシートのハンドルを与えると、その図形モードのワークシートのハンドルを返します。'''
    return HANDLE

def MoveWSColumnOperator(worksheet, databaseRow, fromColumn, toColumn, operatorType):
    '''https://developer.vectorworks.net/index.php?title=VS:MoveWSColumnOperator
    \nhttps://developer.vectorworks.net/index.php?title=VS:MoveWSColumnOperator/ja
    \nハンドルで指定したワークシートの、指定した行で並び替え（ソート）や合計のタイプを移動します。'''
    return None

def SetWSImgAngle(worksheet, topRow, leftColumn, bottomRow, rightColumn, angle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSImgAngle
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSImgAngle/ja
    \n指定したワークシートセルのイメージの回転角を設定します。'''
    return None

def AutoFitWSRowHeights(worksheet, fromRow, toRow):
    '''https://developer.vectorworks.net/index.php?title=VS:AutoFitWSRowHeights
    \nhttps://developer.vectorworks.net/index.php?title=VS:AutoFitWSRowHeights/ja
    \nハンドルで指定したワークシート上の指定した行の高さを自動調整します。'''
    return None

def GetWSImageScaleF(handle):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSImageScaleF
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSImageScaleF/ja
    \n指定したワークシートのイメージの倍率を取得します。'''
    return REAL

def NewSprdSheet(name, location, rows, columns, showOnDrawing, openAfterCreate):
    '''https://developer.vectorworks.net/index.php?title=VS:NewSprdSheet
    \nhttps://developer.vectorworks.net/index.php?title=VS:NewSprdSheet/ja
    \n新しいワークシートを作成します。'''
    return None

def SetWSImgComponent(worksheet, topRow, leftColumn, bottomRow, rightColumn, component):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSImgComponent'''
    return None

def CellHasNum(h, row, col):
    '''https://developer.vectorworks.net/index.php?title=VS:CellHasNum
    \nhttps://developer.vectorworks.net/index.php?title=VS:CellHasNum/ja
    \nハンドルで指定したワークシート上のセルに数値が入っている場合は、TRUEを返します。'''
    return BOOLEAN

def GetWSImgAngle(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSImgAngle
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSImgAngle/ja
    \n指定したワークシートセルのイメージの回転角を返します。'''
    return NewParam

def RecalculateWS(worksheet):
    '''https://developer.vectorworks.net/index.php?title=VS:RecalculateWS
    \nhttps://developer.vectorworks.net/index.php?title=VS:RecalculateWS/ja
    \nハンドルで指定したワークシートを再計算します。'''
    return None

def SetWSImgMarginSize(worksheet, topRow, leftColumn, bottomRow, rightColumn, marginSize):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSImgMarginSize
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSImgMarginSize/ja
    \n指定したワークシートセルのイメージの余白サイズを設定します。'''
    return None

def CellHasStr(h, row, col):
    '''https://developer.vectorworks.net/index.php?title=VS:CellHasStr
    \nhttps://developer.vectorworks.net/index.php?title=VS:CellHasStr/ja
    \nハンドルで指定したワークシート上のセルに文字列が入っている場合は、TRUEを返します。'''
    return BOOLEAN

def GetWSImgComponent(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSImgComponent'''
    return component

def RemoveAllWSColumnOperators(worksheet, databaseRow, operatorType):
    '''https://developer.vectorworks.net/index.php?title=VS:RemoveAllWSColumnOperators
    \nhttps://developer.vectorworks.net/index.php?title=VS:RemoveAllWSColumnOperators/ja
    \nハンドルで指定したワークシートの、指定した行の並び替え（ソート）や合計のタイプをすべて削除します。'''
    return None

def SetWSImgRenderMode(worksheet, topRow, leftColumn, bottomRow, rightColumn, renderMode):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSImgRenderMode
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSImgRenderMode/ja
    \n指定したワークシートセルのイメージのレンダリングの種類を設定します。'''
    return None

def CellString(row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:CellString
    \nhttps://developer.vectorworks.net/index.php?title=VS:CellString/ja
    \nアクティブなワークシート上の指定したセルの値を文字列で返します。'''
    return STRING

def GetWSImgMarginSize(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSImgMarginSize
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSImgMarginSize/ja
    \nワークシートセルのイメージの余白のサイズを返します。'''
    return marginSize

def RemoveWSColumnOperator(worksheet, databaseRow, column, operatorType):
    '''https://developer.vectorworks.net/index.php?title=VS:RemoveWSColumnOperator
    \nhttps://developer.vectorworks.net/index.php?title=VS:RemoveWSColumnOperator/ja
    \nハンドルで指定したワークシートの、指定したセルの並び替え（ソート）や合計のタイプを削除します。'''
    return None

def SetWSImgScale(worksheet, topRow, leftColumn, bottomRow, rightColumn, scale):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSImgScale
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSImgScale/ja
    \n指定したワークシートセルのイメージの縮尺を設定します。'''
    return None

def CellValue(row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:CellValue
    \nhttps://developer.vectorworks.net/index.php?title=VS:CellValue/ja
    \nアクティブなワークシート上の指定したセルの値を数値で返します。'''
    return REAL

def GetWSImgRenderMode(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSImgRenderMode
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSImgRenderMode/ja
    \n指定したワークシートセルのイメージのレンダリングの種類を返します。'''
    return renderMode

def SelectSS(h):
    '''https://developer.vectorworks.net/index.php?title=VS:SelectSS
    \nhttps://developer.vectorworks.net/index.php?title=VS:SelectSS/ja
    \nハンドルで指定したワークシートをアクティブにします。'''
    return None

def SetWSImgShowDBHeader(hWorksheetImage, show, redrawImage):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSImgShowDBHeader'''
    return None

def ClearWSCell(worksheet, topRow, leftColumn, bottomRow, rightColumn):
    '''https://developer.vectorworks.net/index.php?title=VS:ClearWSCell
    \nhttps://developer.vectorworks.net/index.php?title=VS:ClearWSCell/ja
    \nハンドルで指定したワークシートの、指定したセル範囲の内容を消去します。'''
    return None

def GetWSImgScale(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSImgScale
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSImgScale/ja
    \nワークシートセルのイメージの縮尺を返します。'''
    return scale

def SetSprdSortSum(sheetHd, row, sortCol1, sortCol2, sortCol3, sumCol):
    '''https://developer.vectorworks.net/index.php?title=VS:SetSprdSortSum
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetSprdSortSum/ja
    \nハンドルで指定したワークシートの内容を並び替え（ソート）します。'''
    return None

def SetWSImgSize(worksheet, topRow, leftColumn, bottomRow, rightColumn, height, width):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSImgSize
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSImgSize/ja
    \n指定したワークシートセルのイメージの大きさを設定します。'''
    return None

def CloseSS(h):
    '''https://developer.vectorworks.net/index.php?title=VS:CloseSS
    \nhttps://developer.vectorworks.net/index.php?title=VS:CloseSS/ja
    \nハンドルで指定したワークシートを閉じます。'''
    return None

def GetWSImgShowDBHeader(hWorksheetImage):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSImgShowDBHeader'''
    return BOOLEAN

def SetSprdSortSumColumns(sheetHd, row, sortCol1, sortCol2, sortCol3, sumCol1, sumCol2, sumCol3):
    '''https://developer.vectorworks.net/index.php?title=VS:SetSprdSortSumColumns
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetSprdSortSumColumns/ja
    \nハンドルで指定したワークシートの並び替え（ソート）の設定します。'''
    return None

def SetWSImgSizeType(worksheet, topRow, leftColumn, bottomRow, rightColumn, imageSizeType):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSImgSizeType
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSImgSizeType/ja
    \nワークシートセルのイメージの大きさの測り方を設定します。'''
    return None

def CreateWS(name, rows, columns):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateWS
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateWS/ja
    \nワークシートを作成します。'''
    return HANDLE

def GetWSImgSize(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSImgSize
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSImgSize/ja
    \n指定したワークシートセルのイメージの大きさを返します。'''
    return (height, width)

def SetTopVisibleWS(worksheet):
    '''https://developer.vectorworks.net/index.php?title=VS:SetTopVisibleWS
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetTopVisibleWS/ja
    \nハンドルで指定したワークシートを最上位に設定します。'''
    return None

def SetWSImgType(worksheet, topRow, leftColumn, bottomRow, rightColumn, type):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSImgType
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSImgType/ja
    \nワークシートセルのイメージタイプを設定します。'''
    return None

def CreateWSImage(worksheet, location):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateWSImage
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateWSImage/ja
    \nハンドルで指定したワークシートを、図形モードとして用紙の上に作成します。'''
    return HANDLE

def GetWSImgSizeType(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSImgSizeType
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSImgSizeType/ja
    \nワークシートセルのイメージの大きさの測り方を返します。'''
    return INTEGER

def SetWSAutoRecalcState(worksheet, state):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSAutoRecalcState
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSAutoRecalcState/ja
    \nハンドルで指定したワークシートがセル編集時に自動再計算する／しないを設定します。'''
    return None

def SetWSImgUseLayScale(worksheet, topRow, leftColumn, bottomRow, rightColumn, useLayerScale):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSImgUseLayScale
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSImgUseLayScale/ja
    \nワークシートセルのイメージの大きさがレイヤの縮尺に基づくかかどうかを設定します。'''
    return None

def DeleteWSColumns(worksheet, startColumn, numColumns):
    '''https://developer.vectorworks.net/index.php?title=VS:DeleteWSColumns
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeleteWSColumns/ja
    \nハンドルで指定したワークシートの、指定した列を削除します。'''
    return None

def GetWSImgType(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSImgType
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSImgType/ja
    \n指定したワークシートセルのイメージタイプを返します。'''
    return type

def SetWSCellAlignment(worksheet, topRow, leftColumn, bottomRow, rightColumn, cellAlignment):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellAlignment
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSCellAlignment/ja
    \nハンドルで指定したワークシートの、指定したセルの位置揃えを設定します。'''
    return None

def SetWSImgUseObjectImg(worksheet, topRow, leftColumn, bottomRow, rightColumn, useObjectImage):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSImgUseObjectImg
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSImgUseObjectImg/ja
    \nワークシートセルがオブジェクトのイメージを使用するかどうかを設定します。'''
    return None

def DeleteWSRows(worksheet, startRow, numRows):
    '''https://developer.vectorworks.net/index.php?title=VS:DeleteWSRows
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeleteWSRows/ja
    \nハンドルで指定したワークシートの、指定した行を削除します。'''
    return None

def GetWSImgUseLayScale(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSImgUseLayScale
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSImgUseLayScale/ja
    \nイメージの大きさがレイヤの縮尺に基づくかかどうかを返します。'''
    return BOOLEAN

def SetWSCellBorder(worksheet, topRow, leftColumn, bottomRow, rightColumn, top, left, bottom, right, outline):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellBorder
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSCellBorder/ja
    \nハンドルで指定したワークシートの、指定したセルの枠線を設定します。'''
    return None

def SetWSImgView(worksheet, topRow, leftColumn, bottomRow, rightColumn, view):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSImgView
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSImgView/ja
    \n指定したワークシートセルのイメージに指定したビューを設定します。'''
    return None

def EnableDrawingWorksheetPalette(enable, worksheet):
    '''https://developer.vectorworks.net/index.php?title=VS:EnableDrawingWorksheetPalette
    \nhttps://developer.vectorworks.net/index.php?title=VS:EnableDrawingWorksheetPalette/ja
    \nハンドルで指定したワークシートまたはすべてのワークシートを描画する／しないを設定します。'''
    return None

def GetWSImgUseObjectImg(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSImgUseObjectImg
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSImgUseObjectImg/ja
    \nセルがオブジェクトのイメージを使用しているかどうかを返します。'''
    return BOOLEAN

def SetWSCellBorders(worksheet, topRow, leftColumn, bottomRow, rightColumn, top, left, bottom, right, OutlineInside):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellBorders
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSCellBorders/ja
    \nハンドルで指定したワークシートの、指定したセルの枠線を設定します。'''
    return None

def SetWSPlacement(worksheet, top, left, bottom, right):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSPlacement
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSPlacement/ja
    \nハンドルで指定したワークシートのウインドウ位置を設定にします。'''
    return None

def GetCAlign(h, row, col):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCAlign
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCAlign/ja
    \nハンドルで指定したワークシート上のセルの位置揃えを返します。'''
    return INTEGER

def GetWSImgView(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSImgView
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSImgView/ja
    \n指定したワークシートセルのイメージのビューを返します。'''
    return view

def SetWSCellBottomBN(worksheet, topRow, leftColumn, bottomRow, rightColumn, style, weight, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellBottomBN'''
    return None

def SetWSRowHeight(worksheet, fromRow, toRow, height, updatePalette, lockHeight):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSRowHeight
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSRowHeight/ja
    \nハンドルで指定したワークシートの、指定した行の高さを設定します。'''
    return None

def GetCWidth(h, row, col):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCWidth
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCWidth/ja
    \nハンドルで指定したワークシート上のセルの幅を返します。'''
    return INTEGER

def GetWSMergedCellRange(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSMergedCellRange
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSMergedCellRange/ja
    \nハンドルで指定したワークシートの、指定したセルをカバーするセルの範囲を取得します。指定されたセルが統合セルならば、TRUEを返します。'''
    return (BOOLEAN, topRow, leftColumn, bottomRow, rightColumn)

def SetWSCellBottomBorder(worksheet, topRow, leftColumn, bottomRow, rightColumn, style, weight, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellBottomBorder
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSCellBottomBorder/ja
    \nハンドルで指定したワークシートの、指定したセルの下側の枠線を設定します。'''
    return None

def SetWSSelection(worksheet, currentCellRow, currentCellColumn, topRangeRow, leftRangeColumn, topRangeSubrow, bottomRangeRow, rightRangeColumn, bottomRangeSubrow):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSSelection
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSSelection/ja
    \nハンドルで指定したワークシートの、指定したセル範囲を選択します。'''
    return None

def GetCellNum(h, row, col):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCellNum
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCellNum/ja
    \nハンドルで指定したワークシート上のセルの数値を返します。'''
    return REAL

def GetWSPlacement(worksheet):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSPlacement
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSPlacement/ja
    \nハンドルで指定したワークシートのウインドウ位置を返します。'''
    return (top, left, bottom, right)

def SetWSCellFill(worksheet, topRow, leftColumn, bottomRow, rightColumn, style, bgcolor, fgcolor, fillpattern):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellFill
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSCellFill/ja
    \nハンドルで指定したワークシートの、指定したセルの模様、及び色属性を設定します。'''
    return None

def SetWSTextAngle(worksheet, topRow, leftColumn, bottomRow, rightColumn, angle):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSTextAngle
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSTextAngle/ja
    \nハンドルで指定したワークシートの、指定したセルの文字の角度を設定します。'''
    return None

def GetCellStr(h, row, col):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCellStr
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCellStr/ja
    \nハンドルで指定したワークシート上のセルの文字列を返します。'''
    return STRING

def GetWSRowColumnCount(worksheet):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSRowColumnCount
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSRowColumnCount/ja
    \nハンドルで指定したワークシートの行数と列数を返します。'''
    return (numRows, numColumns)

def SetWSCellFormula(worksheet, topRow, leftColumn, bottomRow, rightColumn, formula):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellFormula
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSCellFormula/ja
    \nハンドルで指定したワークシートの、指定したセルの式を設定します。'''
    return None

def SetWorksheetGridLinesVisibility(h, visible):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWorksheetGridLinesVisibility
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWorksheetGridLinesVisibility/ja
    \n指定したワークシート内のグリッドラインの表示形式を設定します。'''
    return None

def GetSprdSortSum(sheetHd, row):
    '''https://developer.vectorworks.net/index.php?title=VS:GetSprdSortSum
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSprdSortSum/ja
    \nハンドルで指定したワークシートの並び替え（ソート）の設定を返します。'''
    return (sortCol1, sortCol2, sortCol3, sumCol)

def GetWSRowHLockState(worksheet, row):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSRowHLockState
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSRowHLockState/ja
    \nハンドルで指定したワークシートの指定した行のロック状態を返します。'''
    return lockState

def SetWSCellFormulaN(worksheet, topRow, leftColumn, bottomRow, rightColumn, formula):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellFormulaN
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSCellFormulaN/ja
    \nハンドルで指定したワークシートの、指定したセルの式を設定します。'''
    return None

def ShowWS(worksheet, show):
    '''https://developer.vectorworks.net/index.php?title=VS:ShowWS
    \nhttps://developer.vectorworks.net/index.php?title=VS:ShowWS/ja
    \nハンドルで指定したワークシートの、表示／非表示を設定します。'''
    return None

def GetSprdSortSumColumns(sheetHd, row):
    '''https://developer.vectorworks.net/index.php?title=VS:GetSprdSortSumColumns
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetSprdSortSumColumns/ja
    \nハンドルで指定したワークシートの並び替え（ソート）の設定を返します。'''
    return (sortCol1, sortCol2, sortCol3, sumCol1, sumCol2, sumCol3)

def GetWSRowHeight(worksheet, row):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSRowHeight
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSRowHeight/ja
    \nハンドルで指定したワークシートの、指定した行の高さを返します。'''
    return height

def SetWSCellInsideHorizBorder(worksheet, topRow, leftColumn, bottomRow, rightColumn, style, weight, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellInsideHorizBorder
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSCellInsideHorizBorder/ja
    \nハンドルで指定したワークシートの、指定したセルの内側水平方向の枠線を設定します。'''
    return None

def ShowWSDialog(dialogType):
    '''https://developer.vectorworks.net/index.php?title=VS:ShowWSDialog
    \nhttps://developer.vectorworks.net/index.php?title=VS:ShowWSDialog/ja
    \nアクティブなワークシートに対する設定ダイアログを表示します。'''
    return None

def GetTopVisibleWS():
    '''https://developer.vectorworks.net/index.php?title=VS:GetTopVisibleWS
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetTopVisibleWS/ja
    \n表示されている最上位のワークシートのハンドルを返します。'''
    return HANDLE

def GetWSSelection(worksheet):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSSelection
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSSelection/ja
    \nハンドルで指定したワークシートの、選択されているセルの範囲を返します。'''
    return (currentCellRow, currentCellColumn, topRangeRow, leftRangeColumn, topRangeSubrow, bottomRangeRow, rightRangeColumn, bottomRangeSubrow)

def SetWSCellInsideHzBN(worksheet, topRow, leftColumn, bottomRow, rightColumn, style, weight, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellInsideHzBN'''
    return None

def SprdAlign(align):
    '''https://developer.vectorworks.net/index.php?title=VS:SprdAlign
    \nhttps://developer.vectorworks.net/index.php?title=VS:SprdAlign/ja
    \nワークシートのセルの位置揃えを設定します。'''
    return None

def GetWSAutoRecalcState(worksheet):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSAutoRecalcState
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSAutoRecalcState/ja
    \nハンドルで指定したワークシートがセル編集時に自動再計算する設定かどうかを返します。'''
    return BOOLEAN

def GetWSSubrowActualCellString(worksheet, row, column, subrow):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSSubrowActualCellString
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSSubrowActualCellString/ja
    \nハンドルで指定したワークシートの、データベース設定されている行の文字列を返します。'''
    return cellString

def SetWSCellInsideVertBorder(worksheet, topRow, leftColumn, bottomRow, rightColumn, style, weight, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellInsideVertBorder
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSCellInsideVertBorder/ja
    \nハンドルで指定したワークシートの、指定したセルの内側垂直方向の枠線を設定します。'''
    return None

def SprdBorder(top, left, bot, right):
    '''https://developer.vectorworks.net/index.php?title=VS:SprdBorder
    \nhttps://developer.vectorworks.net/index.php?title=VS:SprdBorder/ja
    \nアクティブなワークシートのセルに枠線を設定します。'''
    return None

def GetWSCellAlignment(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSCellAlignment
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSCellAlignment/ja
    \nハンドルで指定したワークシートの、指定したセルの位置揃えを返します。'''
    return cellAlignment

def GetWSSubrowActualStringN(worksheet, row, column, subrow):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSSubrowActualStringN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSSubrowActualStringN/ja
    \nハンドルで指定したワークシートの、データベース設定されている行の文字列を返します。'''
    return cellString

def SetWSCellInsideVtBN(worksheet, topRow, leftColumn, bottomRow, rightColumn, style, weight, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellInsideVtBN'''
    return None

def SprdFormat(numForm, acc, ldr, trailr):
    '''https://developer.vectorworks.net/index.php?title=VS:SprdFormat
    \nhttps://developer.vectorworks.net/index.php?title=VS:SprdFormat/ja
    \nアクティブなワークシートのセルの数字の表示形式を設定します。'''
    return None

def GetWSCellBorder(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSCellBorder
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSCellBorder/ja
    \nハンドルで指定したワークシートの、指定したセルの枠線情報を返します。'''
    return (top, left, bottom, right)

def GetWSSubrowCellStrN(worksheet, row, column, subrow):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSSubrowCellStrN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSSubrowCellStrN/ja
    \nハンドルで指定したワークシートの、データベース設定されている行の文字列を返します。GetWSSubrowCellStringNの代わりに使います。'''
    return cellString

def SetWSCellLeftBN(worksheet, topRow, leftColumn, bottomRow, rightColumn, style, weight, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellLeftBN'''
    return None

def SprdSize(h):
    '''https://developer.vectorworks.net/index.php?title=VS:SprdSize
    \nhttps://developer.vectorworks.net/index.php?title=VS:SprdSize/ja
    \nハンドルで指定したワークシートの行と列の数を返します。'''
    return (row, col)

def GetWSCellFill(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSCellFill
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSCellFill/ja
    \nハンドルで指定したワークシートの、指定したセルの模様、及び色属性を返します。'''
    return (style, bgcolor, fgcolor, fillpattern)

def GetWSSubrowCellString(worksheet, row, column, subrow):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSSubrowCellString
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSSubrowCellString/ja
    \nハンドルで指定したワークシートの、データベース設定されている行の文字列を返します。'''
    return cellString

def SetWSCellLeftBorder(worksheet, topRow, leftColumn, bottomRow, rightColumn, style, weight, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellLeftBorder
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSCellLeftBorder/ja
    \nハンドルで指定したワークシートの、指定したセルの左側の枠線を設定します。'''
    return None

def SprdWidth(width):
    '''https://developer.vectorworks.net/index.php?title=VS:SprdWidth
    \nhttps://developer.vectorworks.net/index.php?title=VS:SprdWidth/ja
    \nワークシートのセル幅を設定します。'''
    return None

def GetWSCellFormula(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSCellFormula
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSCellFormula/ja
    \nハンドルで指定したワークシートの、指定したセルの式を返します。'''
    return formula

def GetWSSubrowCellValue(worksheet, row, column, subrow):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSSubrowCellValue
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSSubrowCellValue/ja
    \nハンドルで指定したワークシートの、データベース設定されている行の数値を返します。'''
    return cellValue

def SetWSCellNumberFormat(worksheet, topRow, leftColumn, bottomRow, rightColumn, style, accuracy, leaderString, trailerString):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellNumberFormat
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSCellNumberFormat/ja
    \nハンドルで指定したワークシートの、指定したセルの数字の表示形式を設定します。'''
    return None

def TargetSprdSheet(h):
    '''https://developer.vectorworks.net/index.php?title=VS:TargetSprdSheet
    \nhttps://developer.vectorworks.net/index.php?title=VS:TargetSprdSheet/ja
    \nハンドルで指定したワークシートをアクティブにします。'''
    return None

def GetWSCellFormulaN(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSCellFormulaN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSCellFormulaN/ja
    \nハンドルで指定したワークシートの、指定したセルの式を返します。'''
    return formula

def GetWSSubrowCount(worksheet, databaseRow):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSSubrowCount
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSSubrowCount/ja
    \nハンドルで指定したワークシートの、データベース設定されている行の補助行数を返します。'''
    return numSubrows

def SetWSCellOutlineBN(worksheet, topRow, leftColumn, bottomRow, rightColumn, style, weight, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellOutlineBN'''
    return None

def WSScript_AddHandle(h):
    '''https://developer.vectorworks.net/index.php?title=VS:WSScript_AddHandle'''
    return None

def GetWSCellNumberFormat(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSCellNumberFormat
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSCellNumberFormat/ja
    \nハンドルで指定したワークシートの、指定したセルの数字の表示形式を返します。'''
    return (style, accuracy, leaderString, trailerString)

def GetWSSubrowHeight(worksheet, databaserow, subrow):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSSubrowHeight
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSSubrowHeight/ja
    \nハンドルで指定したワークシートのデータベース行の高さを取得します。'''
    return height

def SetWSCellOutlineBorder(worksheet, topRow, leftColumn, bottomRow, rightColumn, style, weight, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellOutlineBorder
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSCellOutlineBorder/ja
    \nハンドルで指定したワークシートの、指定したセルの外側の枠線を設定します。'''
    return None

def WSScript_AddHandleId(h, id):
    '''https://developer.vectorworks.net/index.php?title=VS:WSScript_AddHandleId'''
    return None

def GetWSCellString(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSCellString
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSCellString/ja
    \nハンドルで指定したワークシートの、指定したセルの文字列を返します。'''
    return cellString

def HasWSColumnOperator(worksheet, databaseRow, column, operatorType):
    '''https://developer.vectorworks.net/index.php?title=VS:HasWSColumnOperator
    \nhttps://developer.vectorworks.net/index.php?title=VS:HasWSColumnOperator/ja
    \nハンドルで指定したワークシートの、指定したセルの並び替え（ソート）や合計のタイプを照会します。'''
    return BOOLEAN

def SetWSCellRightBN(worksheet, topRow, leftColumn, bottomRow, rightColumn, style, weight, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellRightBN'''
    return None

def WSScript_GetEdit():
    '''https://developer.vectorworks.net/index.php?title=VS:WSScript_GetEdit'''
    return (BOOLEAN, outNewValue)

def GetWSCellStringN(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSCellStringN
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSCellStringN/ja
    \nハンドルで指定したワークシートの、指定したセルの文字列を返します。'''
    return cellString

def InsertWSColumns(worksheet, beforeColumn, numColumns):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertWSColumns
    \nhttps://developer.vectorworks.net/index.php?title=VS:InsertWSColumns/ja
    \nハンドルで指定したワークシートに、指定した列数を挿入します。'''
    return None

def SetWSCellRightBorder(worksheet, topRow, leftColumn, bottomRow, rightColumn, style, weight, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellRightBorder
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSCellRightBorder/ja
    \nハンドルで指定したワークシートの、指定したセルの右側の枠線を設定します。'''
    return None

def WSScript_GetEditObj(objIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:WSScript_GetEditObj'''
    return (BOOLEAN, outObj)

def GetWSCellTextAngle(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSCellTextAngle
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSCellTextAngle/ja
    \nハンドルで指定したワークシートの、指定したセルの文字の角度を返します。'''
    return angle

def InsertWSRows(worksheet, beforeRow, numRows):
    '''https://developer.vectorworks.net/index.php?title=VS:InsertWSRows
    \nhttps://developer.vectorworks.net/index.php?title=VS:InsertWSRows/ja
    \nハンドルで指定したワークシートに、指定した行数を挿入します。'''
    return None

def SetWSCellTextColor(worksheet, topRow, leftColumn, bottomRow, rightColumn, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellTextColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSCellTextColor/ja
    \nハンドルで指定したワークシートの、指定したセルの文字色を設定します。'''
    return None

def WSScript_GetObject():
    '''https://developer.vectorworks.net/index.php?title=VS:WSScript_GetObject
    \nhttps://developer.vectorworks.net/index.php?title=VS:WSScript_GetObject/ja
    \nこの関数は 'RunScript' ワークシート式で呼び出すワークシートスクリプト内で使用してください。スクリプト実行時にワークシート検索条件で処理されているオブジェクトを返します。'''
    return HANDLE

def GetWSCellTextColor(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSCellTextColor
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSCellTextColor/ja
    \nハンドルで指定したワークシートの、指定したセルの文字色を返します。'''
    return color

def IsValidWSCell(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:IsValidWSCell
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsValidWSCell/ja
    \nハンドルで指定したワークシートの、指定したセルが有効の場合はTRUEを返します。'''
    return BOOLEAN

def SetWSCellTextFormat(worksheet, topRow, leftColumn, bottomRow, rightColumn, fontIndex, size, style):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellTextFormat
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSCellTextFormat/ja
    \nハンドルで指定したワークシートの、指定したセルの文字属性を設定します。'''
    return None

def WSScript_GetPrmInt(paramIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:WSScript_GetPrmInt
    \nhttps://developer.vectorworks.net/index.php?title=VS:WSScript_GetPrmInt/ja
    \nこの関数は 'RunScript' ワークシート式で呼び出すワークシートスクリプト内で使用してください。指定したパラメータの整数値を返します。'''
    return INTEGER

def GetWSCellTextFormat(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSCellTextFormat
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSCellTextFormat/ja
    \nハンドルで指定したワークシートの、指定したセルの文字属性を返します。'''
    return (fontIndex, size, style)

def IsValidWSRange(worksheet, topRow, leftColumn, bottomRow, rightColumn):
    '''https://developer.vectorworks.net/index.php?title=VS:IsValidWSRange
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsValidWSRange/ja
    \nハンドルで指定したワークシートの、指定したセル範囲が有効の場合はTRUEを返します。'''
    return BOOLEAN

def SetWSCellTopBN(worksheet, topRow, leftColumn, bottomRow, rightColumn, style, weight, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellTopBN'''
    return None

def WSScript_GetPrmReal(paramIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:WSScript_GetPrmReal
    \nhttps://developer.vectorworks.net/index.php?title=VS:WSScript_GetPrmReal/ja
    \nこの関数は 'RunScript' ワークシート式で呼び出すワークシートスクリプト内で使用してください。指定したパラメータの実数値を返します。'''
    return REAL

def GetWSCellValue(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSCellValue
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSCellValue/ja
    \nハンドルで指定したワークシートの、指定したセルの数値を返します。'''
    return cellValue

def IsValidWSSubrowCell(worksheet, row, column, subrow):
    '''https://developer.vectorworks.net/index.php?title=VS:IsValidWSSubrowCell
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsValidWSSubrowCell/ja
    \nハンドルで指定したワークシートの、指定したデータベース行が有効の場合はTRUEを返します。'''
    return BOOLEAN

def SetWSCellTopBorder(worksheet, topRow, leftColumn, bottomRow, rightColumn, style, weight, color):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellTopBorder
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSCellTopBorder/ja
    \nハンドルで指定したワークシートの、指定したセルの上側の枠線を設定します。'''
    return None

def WSScript_GetPrmStr(paramIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:WSScript_GetPrmStr
    \nhttps://developer.vectorworks.net/index.php?title=VS:WSScript_GetPrmStr/ja
    \nこの関数は 'RunScript' ワークシート式で呼び出すワークシートスクリプト内で使用してください。指定したパラメータのストリング値を返します。'''
    return STRING

def GetWSCellVertAlignment(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSCellVertAlignment
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSCellVertAlignment/ja
    \nハンドルで指定したワークシートの、指定したセルの垂直方向の位置揃えを返します。'''
    return vAlignment

def IsWSCellNumber(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:IsWSCellNumber
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsWSCellNumber/ja
    \nハンドルで指定したワークシートの、指定したセルの内容が数値の場合はTRUEを返します。'''
    return BOOLEAN

def SetWSCellVertAlignment(worksheet, topRow, leftColumn, bottomRow, rightColumn, vAlignment):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellVertAlignment
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSCellVertAlignment/ja
    \nハンドルで指定したワークシートの、指定したセルの垂直方向の位置揃えを設定します。'''
    return None

def WSScript_SetResImage(h):
    '''https://developer.vectorworks.net/index.php?title=VS:WSScript_SetResImage
    \nhttps://developer.vectorworks.net/index.php?title=VS:WSScript_SetResImage/ja
    \nこの関数は 'RunScript' ワークシート式で呼び出すワークシートスクリプト内で使用してください。セル内のイメージとして使用されるオブジェクトのワークシートスクリプト結果を設定します。'''
    return None

def GetWSCellWrapTextFlag(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSCellWrapTextFlag
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSCellWrapTextFlag/ja
    \nハンドルで指定したワークシートの、指定したセルのラップテキストの状態を返します。'''
    return wrapTextFlag

def IsWSCellString(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:IsWSCellString
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsWSCellString/ja
    \nハンドルで指定したワークシートの、指定したセルの内容が文字列の場合はTRUEを返します。'''
    return BOOLEAN

def SetWSCellWrapTextFlag(worksheet, topRow, leftColumn, bottomRow, rightColumn, wrapTextFlag):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellWrapTextFlag
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSCellWrapTextFlag/ja
    \nハンドルで指定したワークシートの、指定したセルのラップテキストの状態を設定します。'''
    return None

def WSScript_SetResInt(resultCellValue):
    '''https://developer.vectorworks.net/index.php?title=VS:WSScript_SetResInt
    \nhttps://developer.vectorworks.net/index.php?title=VS:WSScript_SetResInt/ja
    \nこの関数は 'RunScript' ワークシート式で呼び出すワークシートスクリプト内で使用してください。指定した整数値のワークシートスクリプトの結果を設定します。'''
    return None

def GetWSCellsImgDPIRes(worksheet):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSCellsImgDPIRes
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSCellsImgDPIRes/ja
    \n指定したワークシートのイメージのDPI解像度を取得します。'''
    return dpiResolution

def IsWSDatabaseRow(worksheet, databaseRow):
    '''https://developer.vectorworks.net/index.php?title=VS:IsWSDatabaseRow
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsWSDatabaseRow/ja
    \nハンドルで指定したワークシートの、指定した行がデータベース行の場合はTRUEを返します。'''
    return BOOLEAN

def SetWSCellsImgDPIRes(worksheet, dpiResolution):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSCellsImgDPIRes
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSCellsImgDPIRes/ja
    \n指定したワークシートのイメージのDPI解像度を設定します。'''
    return None

def WSScript_SetResReal(resultCellValue):
    '''https://developer.vectorworks.net/index.php?title=VS:WSScript_SetResReal
    \nhttps://developer.vectorworks.net/index.php?title=VS:WSScript_SetResReal/ja
    \nこの関数は 'RunScript' ワークシート式で呼び出すワークシートスクリプト内で使用してください。指定した実数値のワークシートスクリプトの結果を設定します。'''
    return None

def GetWSColumnOperators(worksheet, row):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSColumnOperators
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSColumnOperators/ja
    \nハンドルで指定したワークシートの、指定した行の並び替え（ソート）と合計を返します。'''
    return (sort1, sort2, sort3, sum1, sum2, sum3)

def IsWSImg(worksheet, row, column):
    '''https://developer.vectorworks.net/index.php?title=VS:IsWSImg
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsWSImg/ja
    \nワークシートのセルがイメージを表示させる設定かどうかを返します。'''
    return BOOLEAN

def SetWSColumnOperators(worksheet, row, sort1, sort2, sort3, sum1, sum2, sum3):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSColumnOperators
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSColumnOperators/ja
    \nハンドルで指定したワークシートの、指定した行の並び替え（ソート）と合計を設定します。'''
    return None

def WSScript_SetResStr(resultCellValue):
    '''https://developer.vectorworks.net/index.php?title=VS:WSScript_SetResStr
    \nhttps://developer.vectorworks.net/index.php?title=VS:WSScript_SetResStr/ja
    \nこの関数は 'RunScript' ワークシート式で呼び出すワークシートスクリプト内で使用してください。指定したストリング値のワークシートスクリプトの結果を設定します。'''
    return None

def GetWSColumnSortPrecedence(worksheet, databaseRow, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSColumnSortPrecedence
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSColumnSortPrecedence/ja
    \nハンドルで指定したワークシートの、指定したデータベース行のソート優先順位を返します。'''
    return INTEGER

def IsWSSubrowCellNumber(worksheet, row, column, subrow):
    '''https://developer.vectorworks.net/index.php?title=VS:IsWSSubrowCellNumber
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsWSSubrowCellNumber/ja
    \nハンドルで指定したワークシートの、指定したデータベース行が数値の場合はTRUEを返します。'''
    return BOOLEAN

def SetWSColumnSortType(worksheet, databaseRow, column, sortType):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSColumnSortType
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSColumnSortType/ja
    \nハンドルで指定したワークシートの、指定したデータベース行のソート順を設定します。'''
    return None

def WorksheetMergeCells(worksheet, topRow, leftColumn, bottomRow, rightColumn):
    '''https://developer.vectorworks.net/index.php?title=VS:WorksheetMergeCells
    \nhttps://developer.vectorworks.net/index.php?title=VS:WorksheetMergeCells/ja
    \nハンドルで指定したワークシートの、指定した複数のセルを1つのセルに統合します。'''
    return BOOLEAN

def GetWSColumnSortType(worksheet, databaseRow, column):
    '''https://developer.vectorworks.net/index.php?title=VS:GetWSColumnSortType
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetWSColumnSortType/ja
    \nハンドルで指定したワークシートの、指定したデータベース行のソート順を返します。'''
    return INTEGER

def IsWSSubrowCellString(worksheet, row, column, subrow):
    '''https://developer.vectorworks.net/index.php?title=VS:IsWSSubrowCellString
    \nhttps://developer.vectorworks.net/index.php?title=VS:IsWSSubrowCellString/ja
    \nハンドルで指定したワークシートの、指定したデータベース行が文字列の場合はTRUEを返します。'''
    return BOOLEAN

def SetWSColumnWidth(worksheet, fromColumn, toColumn, width):
    '''https://developer.vectorworks.net/index.php?title=VS:SetWSColumnWidth
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetWSColumnWidth/ja
    \nハンドルで指定したワークシートの、指定した列の幅を設定します。'''
    return None

def WorksheetSplitCells(worksheet, topRow, leftColumn, bottomRow, rightColumn):
    '''https://developer.vectorworks.net/index.php?title=VS:WorksheetSplitCells
    \nhttps://developer.vectorworks.net/index.php?title=VS:WorksheetSplitCells/ja
    \nハンドルで指定したワークシートの、指定したセルを分離して個別のセルに戻します。'''
    return BOOLEAN

def ws2AddMenuGroup(menuPath, newUnivName, newDisplayName, beforeIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:ws2AddMenuGroup'''
    return BOOLEAN

def ws2DelMenuAt(menuPath, index):
    '''https://developer.vectorworks.net/index.php?title=VS:ws2DelMenuAt'''
    return BOOLEAN

def ws2GetToolAt(toolPath, index):
    '''https://developer.vectorworks.net/index.php?title=VS:ws2GetToolAt'''
    return DYNARRAY[] of CHAR

def wsEditAddTool(toolName, toolType):
    '''https://developer.vectorworks.net/index.php?title=VS:wsEditAddTool'''
    return None

def ws2AddMenuItem(menuPath, newMenuUnivName, beforeIndex):
    '''https://developer.vectorworks.net/index.php?title=VS:ws2AddMenuItem'''
    return BOOLEAN

def ws2DelTool(toolPath):
    '''https://developer.vectorworks.net/index.php?title=VS:ws2DelTool'''
    return BOOLEAN

def ws2GetToolInfo(toolPath):
    '''https://developer.vectorworks.net/index.php?title=VS:ws2GetToolInfo'''
    return (BOOLEAN, outDisplayName, outShortcutKey, outShortcutKeyModifier, outResourceID)

def wsEditAddTool2(toolName, underToolName, toolType):
    '''https://developer.vectorworks.net/index.php?title=VS:wsEditAddTool2'''
    return None

def ws2CommitChanges(restart, reload):
    '''https://developer.vectorworks.net/index.php?title=VS:ws2CommitChanges'''
    return None

def ws2FindMenuIndex(menuPath, findMenuUnivName):
    '''https://developer.vectorworks.net/index.php?title=VS:ws2FindMenuIndex'''
    return INTEGER

def ws2GetToolsCnt(toolPath):
    '''https://developer.vectorworks.net/index.php?title=VS:ws2GetToolsCnt'''
    return INTEGER

def wsEditBegin(companyName):
    '''https://developer.vectorworks.net/index.php?title=VS:wsEditBegin'''
    return None

def ws2CreateTool(toolPath, univName, resourceID):
    '''https://developer.vectorworks.net/index.php?title=VS:ws2CreateTool'''
    return BOOLEAN

def ws2FindToolIndex(toolPath, findUnivName):
    '''https://developer.vectorworks.net/index.php?title=VS:ws2FindToolIndex'''
    return INTEGER

def ws2SetMenuInfo(menuPath, displayName, hasShortcutKey, shortcutKey, shortcutKeyModifier):
    '''https://developer.vectorworks.net/index.php?title=VS:ws2SetMenuInfo'''
    return None

def wsEditBeginN(companyName, companyToolSetIconFilePath):
    '''https://developer.vectorworks.net/index.php?title=VS:wsEditBeginN'''
    return None

def ws2CreateToolPalette(univName, displayName):
    '''https://developer.vectorworks.net/index.php?title=VS:ws2CreateToolPalette'''
    return BOOLEAN

def ws2GetMenuAt(menuPath, index):
    '''https://developer.vectorworks.net/index.php?title=VS:ws2GetMenuAt'''
    return DYNARRAY[] of CHAR

def ws2SetToolInfo(toolPath, displayName, shortcutKey, shortcutKeyModifier, resourceID):
    '''https://developer.vectorworks.net/index.php?title=VS:ws2SetToolInfo'''
    return None

def wsEditEnd(restart):
    '''https://developer.vectorworks.net/index.php?title=VS:wsEditEnd'''
    return BOOLEAN

def ws2CreateToolSet(toolPath, univName, displayName, iconFullFilePath):
    '''https://developer.vectorworks.net/index.php?title=VS:ws2CreateToolSet'''
    return BOOLEAN

def ws2GetMenuInfo(menuPath):
    '''https://developer.vectorworks.net/index.php?title=VS:ws2GetMenuInfo'''
    return (DYNARRAY[] of CHAR, outHasShortcutKey, outShortcutKey, outShortcutKeyModifier)

def wsDelete(companyName, restart, reload):
    '''https://developer.vectorworks.net/index.php?title=VS:wsDelete'''
    return None

def wsInstallCanceled(canceled):
    '''https://developer.vectorworks.net/index.php?title=VS:wsInstallCanceled'''
    return None

def ws2DelMenu(menuPath):
    '''https://developer.vectorworks.net/index.php?title=VS:ws2DelMenu'''
    return BOOLEAN

def ws2GetMenusCnt(menuPath):
    '''https://developer.vectorworks.net/index.php?title=VS:ws2GetMenusCnt'''
    return INTEGER

def wsEditAddMenu(menuPath):
    '''https://developer.vectorworks.net/index.php?title=VS:wsEditAddMenu'''
    return None

def wsInstallFailed(failed):
    '''https://developer.vectorworks.net/index.php?title=VS:wsInstallFailed'''
    return None

def CreateNewXMLDocument(XMLHandle, rootElementName):
    '''https://developer.vectorworks.net/index.php?title=VS:CreateNewXMLDocument
    \nhttps://developer.vectorworks.net/index.php?title=VS:CreateNewXMLDocument/ja
    \n新しいXML書類を作成します。'''
    return INTEGER

def GetAttributeValue(XMLHandle, elementPath, attribute):
    '''https://developer.vectorworks.net/index.php?title=VS:GetAttributeValue
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetAttributeValue/ja
    \n属性の値を取得します'''
    return (INTEGER, value)

def InitXML():
    '''https://developer.vectorworks.net/index.php?title=VS:InitXML
    \nhttps://developer.vectorworks.net/index.php?title=VS:InitXML/ja
    \nXMLシステムを初期化します'''
    return LONGINT

def SetElementValue(XMLHandle, elementPath, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetElementValue
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetElementValue/ja
    \n与えられたパスの要素の値を設定します。.'''
    return INTEGER

def DeleteAttribute(XMLHandle, elementPath, attribute):
    '''https://developer.vectorworks.net/index.php?title=VS:DeleteAttribute
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeleteAttribute/ja
    \n属性を一つ削除します。'''
    return INTEGER

def GetCDATA(XMLHandle, elementPath):
    '''https://developer.vectorworks.net/index.php?title=VS:GetCDATA
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetCDATA/ja
    \nCDATAセクションを取得します'''
    return (INTEGER, returnVal)

def ReadXMLFile(XMLHandle, whichPath, filename):
    '''https://developer.vectorworks.net/index.php?title=VS:ReadXMLFile
    \nhttps://developer.vectorworks.net/index.php?title=VS:ReadXMLFile/ja
    \nXMLファイルを開いて読み込む'''
    return INTEGER

def WriteXMLFile(XMLHandle, whichPath, filename):
    '''https://developer.vectorworks.net/index.php?title=VS:WriteXMLFile
    \nhttps://developer.vectorworks.net/index.php?title=VS:WriteXMLFile/ja
    \nXMLファイルを書き出す。'''
    return INTEGER

def DeleteCDATA(XMLHandle, elementPath):
    '''https://developer.vectorworks.net/index.php?title=VS:DeleteCDATA
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeleteCDATA/ja
    \nCDATAセクションを削除します'''
    return INTEGER

def GetElementValue(XMLHandle, elementPath):
    '''https://developer.vectorworks.net/index.php?title=VS:GetElementValue
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetElementValue/ja
    \nパスで示される要素の値を取得します。'''
    return (INTEGER, value)

def ReadXMLMemory(XMLHandle, XMLData):
    '''https://developer.vectorworks.net/index.php?title=VS:ReadXMLMemory
    \nhttps://developer.vectorworks.net/index.php?title=VS:ReadXMLMemory/ja
    \nメモリ上のXMLデータをパースします'''
    return INTEGER

def WriteXMLMemory(XMLHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:WriteXMLMemory
    \nhttps://developer.vectorworks.net/index.php?title=VS:WriteXMLMemory/ja
    \n内部のDOMツリーからXMLデータを作成します'''
    return (INTEGER, XMLData)

def DeleteElement(XMLHandle, elementPath):
    '''https://developer.vectorworks.net/index.php?title=VS:DeleteElement
    \nhttps://developer.vectorworks.net/index.php?title=VS:DeleteElement/ja
    \nパスで指定された位置の要素を削除します。'''
    return INTEGER

def GetFirstChild(XMLHandle, elementPath):
    '''https://developer.vectorworks.net/index.php?title=VS:GetFirstChild
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetFirstChild/ja
    \n与えられた要素の最初の子を返します'''
    return (INTEGER, value)

def ReleaseXML(XMLHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:ReleaseXML
    \nhttps://developer.vectorworks.net/index.php?title=VS:ReleaseXML/ja
    \nXMLパーサが利用する内部メモリを解放します'''
    return INTEGER

def FindAttribute(XMLHandle, startElementPath, searchAttribute):
    '''https://developer.vectorworks.net/index.php?title=VS:FindAttribute
    \nhttps://developer.vectorworks.net/index.php?title=VS:FindAttribute/ja
    \n名前で特定の属性を検索します。'''
    return (INTEGER, foundPath, attributeValue)

def GetNextElement(XMLHandle, elementPath):
    '''https://developer.vectorworks.net/index.php?title=VS:GetNextElement
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetNextElement/ja
    \n与えられた要素の次（兄弟）の要素を返します。'''
    return (INTEGER, value)

def SetAttributeValue(XMLHandle, elementPath, attribute, value):
    '''https://developer.vectorworks.net/index.php?title=VS:SetAttributeValue
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetAttributeValue/ja
    \n属性の値を設定します'''
    return INTEGER

def FindElement(XMLHandle, startElementPath, searchElement):
    '''https://developer.vectorworks.net/index.php?title=VS:FindElement
    \nhttps://developer.vectorworks.net/index.php?title=VS:FindElement/ja
    \n名前で特定の要素を検索します。'''
    return (INTEGER, foundPath)

def GetPreviousElement(XMLHandle, elementPath):
    '''https://developer.vectorworks.net/index.php?title=VS:GetPreviousElement
    \nhttps://developer.vectorworks.net/index.php?title=VS:GetPreviousElement/ja
    \n与えられた要素の前（兄弟）の要素を返します。'''
    return (INTEGER, value)

def SetCDATA(XMLHandle, elementPath, data):
    '''https://developer.vectorworks.net/index.php?title=VS:SetCDATA
    \nhttps://developer.vectorworks.net/index.php?title=VS:SetCDATA/ja
    \nCDATAセクションを設定する.'''
    return INTEGER

def XMLSAXAddNodeAttr(XMLHandle, nodeAttrName, nodeAttrValue):
    '''https://developer.vectorworks.net/index.php?title=VS:XMLSAXAddNodeAttr
    \nhttps://developer.vectorworks.net/index.php?title=VS:XMLSAXAddNodeAttr/ja
    \nSAXを利用してXMLを書く。XMLSAXBeginNodeで始まるノードに属性ノードを追加します。'''
    return INTEGER

def XMLSAXBeginDocMemory(XMLHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:XMLSAXBeginDocMemory
    \nhttps://developer.vectorworks.net/index.php?title=VS:XMLSAXBeginDocMemory/ja
    \nSAXを利用してXMLを書く。メモリ上の書類を開始します。XMLSAXEndDocMemoryで終了します。'''
    return INTEGER

def XMLSAXEndDocMemory(XMLHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:XMLSAXEndDocMemory
    \nhttps://developer.vectorworks.net/index.php?title=VS:XMLSAXEndDocMemory/ja
    \nSAXを利用してXMLを書く。書類の終了。書類の開始はXMLSAXBeginDocMemory'''
    return (INTEGER, XMLData)

def XMLSAXParseMemory(XMLHandle, XMLData, nodeCallback):
    '''https://developer.vectorworks.net/index.php?title=VS:XMLSAXParseMemory
    \nhttps://developer.vectorworks.net/index.php?title=VS:XMLSAXParseMemory/ja
    \nSAXを利用してメモリ上のXMLをパースします。'''
    return INTEGER

def XMLSAXAddNodeValue(XMLHandle, nodeValue):
    '''https://developer.vectorworks.net/index.php?title=VS:XMLSAXAddNodeValue
    \nhttps://developer.vectorworks.net/index.php?title=VS:XMLSAXAddNodeValue/ja
    \nSAXを利用してXMLを書く。XMLSAXBeginNodeで始まるノードに要素ノードを追加します。'''
    return INTEGER

def XMLSAXBeginNode(XMLHandle, nodeName):
    '''https://developer.vectorworks.net/index.php?title=VS:XMLSAXBeginNode
    \nhttps://developer.vectorworks.net/index.php?title=VS:XMLSAXBeginNode/ja
    \nSAXを利用してXMLを書く。ノードの開始。XMLSAXEndNodeで終了します。'''
    return INTEGER

def XMLSAXEndNode(XMLHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:XMLSAXEndNode
    \nhttps://developer.vectorworks.net/index.php?title=VS:XMLSAXEndNode/ja
    \nSAXを利用してXMLを書く。ノードの終了。ノードの開始はXMLSAXBeginNode'''
    return INTEGER

def XMLSAXBeginDocFile(XMLHandle, whichPath, filename):
    '''https://developer.vectorworks.net/index.php?title=VS:XMLSAXBeginDocFile
    \nhttps://developer.vectorworks.net/index.php?title=VS:XMLSAXBeginDocFile/ja
    \nSAXを利用してXMLを書く。ファイル上の書類の開始。XMLSAXEndDocで終了します。'''
    return INTEGER

def XMLSAXEndDoc(XMLHandle):
    '''https://developer.vectorworks.net/index.php?title=VS:XMLSAXEndDoc
    \nhttps://developer.vectorworks.net/index.php?title=VS:XMLSAXEndDoc/ja
    \nSAXを利用してXMLを書く。書類の終了。書類の開始はXMLSAXBeginDocFile'''
    return INTEGER

def XMLSAXParseFile(XMLHandle, whichPath, filename, nodeCallback):
    '''https://developer.vectorworks.net/index.php?title=VS:XMLSAXParseFile
    \nhttps://developer.vectorworks.net/index.php?title=VS:XMLSAXParseFile/ja
    \nSAXを利用してXMLをパースします。'''
    return INTEGER

