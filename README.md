# Octoprint 中文简体语言包
>  翻译过程采用Google翻译生成，部分进行人工修改优化。


## 翻译说明

- 第一版翻译：利用 `tools/potrans.py`脚本自动使用google翻译生成，然后人工修改部分记录，最后使用`poedit`工具生成 mo 文件。


## 使用方法


克隆本项目后，将本项目的`zh_Hans_CN`目录，直接放到 `$HOME/.octoprint/translations`
```bash
git clone https://github.com/Awkee/Octoprint-i18n-zh_Hans_CN.git

cd Octoprint-i18n-zh_Hans_CN && cp -r Octoprint-i18n-zh_Hans_CN/zh_Hans_CN $HOME/.octoprint/translations

```

在Octoprint的WEB页面中`重新加载UI`，启用中文语音包方法：

- 通过URL地址设置: `http://rpi3:5000/?l10n=zh_Hans_CN` 
- 在设置`settings` -> `appearance` 中修改 `Default Language`为中文，点击保存后刷新页面生效。



更为通用的方法（加载zip压缩包win/linux/mac）：
- 下载 Octoprint_i18n_zh_Hans_CN.zip 文件.
- 在设置`settings` -> `appearance` 中 **Language Packs** 点击**Manager**按钮，将 **Octoprint_i18n_zh_Hans_CN.zip**文件上传后，点击保存，刷新页面后即可生效。




## 最后

机器翻译内容可能存在言不及义的情况，如果你希望让这个语言包更好，请多多提供建议和意见。

