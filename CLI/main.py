"""
import Special.sunday as sunday
import Special

print( sunday.filename )
sunday.hello("Masa")

## __path__ 属性はフォルダにのみ存在する。ファイルに対してはエラーとなる。
print( Special.__path__ )
"""

from Farewell2016.Greet import farewell
farewell()