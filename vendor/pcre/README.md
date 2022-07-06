Superstring contains a copy of the [PCRE](http://www.pcre.org/) regex engine.

Downloaded from:

https://github.com/PCRE2Project/pcre2/releases

The file that `superstring` uses to compile PCRE, `pcre.gyp`, was created using the `source ./vendor/pcre/configure` script added to this folder:

```
cd ./vendor/pcre/pcre2-10.40
cmake -S ./ -B ./build -DPCRE2_BUILD_PCRE2_8=ON -DPCRE2_BUILD_PCRE2_16=ON -DPCRE2_BUILD_PCRE2_32=ON -DPCRE2_STATIC_PIC=ON -DPCRE2_SUPPORT_JIT=ON -DPCRE2_BUILD_TESTS=OFF -DPCRE2_BUILD_PCRE2GREP=OFF -DINSTALL_MSVC_PDB=ON -DPCRE2_SUPPORT_BSR_ANYCRLF=ON
cp ./build/pcre2.h ../include/
cp ./build/config.h ../include/
cp ./build/pcre2_chartables.c ../
cd ../../../
```

Then modified `./include/config.h` to support both Windows and Unix using
```h
#ifdef _WIN32
#define HAVE_WINDOWS_H 1
#else
#undef HAVE_UNISTD_H
#endif

```