"""todo 常用数据结构之字符串"""
'''转义字符 \ '''
# 我们可以在字符串中使用`\`（反斜杠）来表示转义，也就是说`\`后面的字符不再是它原来的意义，
# 例如：`\n`不是代表字符`\`和字符`n`，而是表示换行；
# `\t`也不是代表字符`\`和字符`t`，而是表示制表符。
# 所以如果字符串本身又包含了`'`、`"`、`\`这些特殊的字符，必须要通过`\`进行转义处理。
s1 = '\'hello, world!\''
s2 = '\\hello, world!\\'
print(s1)
print(s2)

'''原始字符串:R或者r'''
# 中有一种以`r`或`R`开头的字符串，这种字符串被称为原始字符串，意思是字符串中的每个字符都是它本来的含义，没有所谓的转义字符。
# 例如，在字符串`'hello\n'`中，`\n`表示换行；而在`r'hello\n'`中，`\n`不再表示换行，就是字符`\`和字符`n`。大家可以运行下面的代码，看看会输出什么。
s1 = '\it \is \time \to \read \now'
s2 = r'\it \is \time \to \read \now'
print(s1)
print(s2)

'''字符的特殊表示'''
# Python 中还允许在`\`后面还可以跟一个八进制或者十六进制数来表示字符，
# 例如`\141`和`\x61`都代表小写字母`a`，前者是八进制的表示法，后者是十六进制的表示法。
# 另外一种表示字符的方式是在`\u`后面跟 Unicode 字符编码，例如`\u9a86\u660a`代表的是中文“骆昊”。运行下面的代码，看看输出了什么。
s1 = 'abc\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1)
print(s2)

s = 'abc123456'
n = len(s)
print(s[0], s[-n])  # a a
print(s[n - 1], s[-1])  # 6 6
print(s[2], s[-7])  # c c
print(s[5], s[-4])  # 3 3
print(s[2:5])  # c12
print(s[-7:-4])  # c12
print(s[2:])  # c123456
print(s[:2])  # ab
print(s[::2])  # ac246
print(s[::-1])  # 654321cba  反向以步长为1取数

s1 = 'hello, world!'
# 字符串首字母大写
print(s1.capitalize())  # Hello, world!
# 字符串每个单词首字母大写
print(s1.title())  # Hello, World!
# 字符串变大写
print(s1.upper())  # HELLO, WORLD!
s2 = 'GOODBYE'
# 字符串变小写
print(s2.lower())  # goodbye
# 检查s1和s2的值
print(s1)  # hello, world
print(s2)  # GOODBYE

# todo 编码和解码
'Python 中除了字符串`str`类型外，还有一种表示二进制数据的字节串类型（`bytes`）。所谓字节串，就是**由零个或多个字节组成的有限序列**。'
'通过字符串的`encode`方法，我们可以按照某种编码方式将字符串编码为字节串，我们也可以使用字节串的`decode`方法，将字节串解码为字符串，代码如下所示。'

a = '骆昊'
b = a.encode('utf-8')
c = a.encode('gbk')
print(b)  # b'\xe9\xaa\x86\xe6\x98\x8a'
print(c)  # b'\xc2\xe6\xea\xbb'
print(b.decode('utf-8'))  # 骆昊
print(c.decode('gbk'))  # 骆昊
