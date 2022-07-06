{
    "targets": [
        {
            "target_name": "pcre",
            "type": "static_library",
            "sources": [
                "pcre2_chartables.c",
                "pcre2-10.40/src/pcre2_auto_possess.c",
                "pcre2-10.40/src/pcre2_compile.c",
                "pcre2-10.40/src/pcre2_config.c",
                "pcre2-10.40/src/pcre2_context.c",
                "pcre2-10.40/src/pcre2_dfa_match.c",
                "pcre2-10.40/src/pcre2_error.c",
                "pcre2-10.40/src/pcre2_find_bracket.c",
                "pcre2-10.40/src/pcre2_jit_compile.c",
                "pcre2-10.40/src/pcre2_maketables.c",
                "pcre2-10.40/src/pcre2_match.c",
                "pcre2-10.40/src/pcre2_match_data.c",
                "pcre2-10.40/src/pcre2_newline.c",
                "pcre2-10.40/src/pcre2_ord2utf.c",
                "pcre2-10.40/src/pcre2_pattern_info.c",
                "pcre2-10.40/src/pcre2_serialize.c",
                "pcre2-10.40/src/pcre2_string_utils.c",
                "pcre2-10.40/src/pcre2_study.c",
                "pcre2-10.40/src/pcre2_substitute.c",
                "pcre2-10.40/src/pcre2_substring.c",
                "pcre2-10.40/src/pcre2_tables.c",
                "pcre2-10.40/src/pcre2_ucd.c",
                "pcre2-10.40/src/pcre2_valid_utf.c",
                "pcre2-10.40/src/pcre2_xclass.c",
            ],
            "include_dirs": [
                "include",
                "pcre2-10.40/src"
            ],
            "defines": [
                "HAVE_CONFIG_H",
                "PCRE2_CODE_UNIT_WIDTH=16",
                "SUPPORT_JIT",
            ],
            "cflags": [
                "-Wno-unused-function"
            ],
            'xcode_settings': {
                'OTHER_CFLAGS': [
                    '-Wno-unused-function'
                ],
            },
            "direct_dependent_settings": {
                "include_dirs": [
                    "include"
                ],
                "defines": [
                    "PCRE2_CODE_UNIT_WIDTH=16",
                ]
            },
        "cflags_cc": [ "-std=c++17" ],
        "conditions": [
            ['OS=="mac"', {
                "xcode_settings": {
                    'CLANG_CXX_LANGUAGE_STANDARD':'c++17',
                    'MACOSX_DEPLOYMENT_TARGET': "10.15"
                }
            }],
            ['OS=="win"', {
                "msvs_settings": {
                    "VCCLCompilerTool": {
                        "AdditionalOptions": [
                            "/std:c++17",
                        ]
                    }
              }
            }]
        ]}
    ]
}