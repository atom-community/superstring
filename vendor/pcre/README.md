Superstring contains a copy of the [PCRE](http://www.pcre.org/) regex engine.

Downloaded from:

https://github.com/PCRE2Project/pcre2/releases

The file that `superstring` uses to compile PCRE, `pcre.gyp`, was created using the `configure` script added to this folder:

```
cd ./vendor/pcre/pcre2-10.40
cmake -S ./ -B ./build -DPCRE2_BUILD_PCRE2_16=ON -DPCRE2_BUILD_PCRE2_8=OFF -DPCRE2_STATIC_PIC=ON
cp ./build/pcre2.h ../include/
cp ./build/config.h ../include/
cp ./build/pcre2_chartables.c ../
cd ../../../
```