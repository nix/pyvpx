from ctypes import *

STRING = c_char_p
_libraries = {}
_libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'] = CDLL('/xtra/libvpx/x86_build/libvpx.so.0.9.6')
WSTRING = c_wchar_p


VP8_GOOD_QUALITY_ENCODING = 1
VPX_IMG_FMT_YV12 = 769
IMG_FMT_YV12 = VPX_IMG_FMT_YV12 # alias
VP8_DEBUG_TXT_RATE_INFO = 64
# NULL = __null # alias
VP8E_SET_STATIC_THRESHOLD = 17
VP8_SET_DBG_DISPLAY_MV = 7
VP8_TWO_TOKENPARTITION = 1
# def __LDBL_REDIR1(name,proto,alias): return name proto # macro
# def VPX_CTRL_USE_TYPE_DEPRECATED(id,typ): return DECLSPEC_DEPRECATED static vpx_codec_err_t vpx_codec_control_ ##id(vpx_codec_ctx_t*, int, typ) DEPRECATED UNUSED; DECLSPEC_DEPRECATED static vpx_codec_err_t vpx_codec_control_ ##id(vpx_codec_ctx_t *ctx, int ctrl_id, typ data) { return vpx_codec_control_(ctx, ctrl_id, data); } # macro

# values for enumeration 'vpx_img_fmt'
VPX_IMG_FMT_NONE = 0
VPX_IMG_FMT_RGB24 = 1
VPX_IMG_FMT_RGB32 = 2
VPX_IMG_FMT_RGB565 = 3
VPX_IMG_FMT_RGB555 = 4
VPX_IMG_FMT_UYVY = 5
VPX_IMG_FMT_YUY2 = 6
VPX_IMG_FMT_YVYU = 7
VPX_IMG_FMT_BGR24 = 8
VPX_IMG_FMT_RGB32_LE = 9
VPX_IMG_FMT_ARGB = 10
VPX_IMG_FMT_ARGB_LE = 11
VPX_IMG_FMT_RGB565_LE = 12
VPX_IMG_FMT_RGB555_LE = 13
VPX_IMG_FMT_I420 = 258
VPX_IMG_FMT_VPXYV12 = 771
VPX_IMG_FMT_VPXI420 = 260
vpx_img_fmt = c_int # enum
vpx_img_fmt_t = vpx_img_fmt
img_fmt_t = vpx_img_fmt_t # alias
VPX_PLANE_ALPHA = 3 # Variable c_int '3'
PLANE_ALPHA = VPX_PLANE_ALPHA # alias
VP8_TUNE_SSIM = 1
def __attribute_format_arg__(x): return __attribute__ ((__format_arg__ (x))) # macro
VP8E_SET_TOKEN_PARTITIONS = 18
VP8_COMMON_CTRL_ID_MAX = 8
VP8_FOUR_TOKENPARTITION = 2
VPX_IMG_FMT_HAS_ALPHA = 1024 # Variable c_int '1024'
IMG_FMT_HAS_ALPHA = VPX_IMG_FMT_HAS_ALPHA # alias
IMG_FMT_RGB24 = VPX_IMG_FMT_RGB24 # alias
VPX_CODEC_LIST_END = 9
def vpx_codec_version_major(): return ((vpx_codec_version()>>16)&0xff) # macro
def __attribute_format_strfmon__(a,b): return __attribute__ ((__format__ (__strfmon__, a, b))) # macro
VP8E_GET_LAST_QUANTIZER = 19
IMG_FMT_RGB565 = VPX_IMG_FMT_RGB565 # alias
VP8_DECODER_CTRL_ID_START = 256
VP8_EIGHT_TOKENPARTITION = 3
IMG_FMT_RGB32_LE = VPX_IMG_FMT_RGB32_LE # alias
VPX_DEC_CORRUPT_FRAME = 7
VP8E_GET_LAST_QUANTIZER_64 = 20
VP8E_SET_SHARPNESS = 16
IMG_FMT_NONE = VPX_IMG_FMT_NONE # alias
VPX_PLANE_PACKED = 0 # Variable c_int '0'
PLANE_PACKED = VPX_PLANE_PACKED # alias
def vpx_codec_control(ctx,id,data): return vpx_codec_control_ ##id(ctx,id,data) # macro
def vpx_codec_version_minor(): return ((vpx_codec_version()>>8)&0xff) # macro
def __bos0(ptr): return __builtin_object_size (ptr, 0) # macro
VP8E_SET_ARNR_MAXFRAMES = 21
VP8_SET_DBG_COLOR_B_MODES = 6
# def __LDBL_REDIR1_NTH(name,proto,alias): return name proto __THROW # macro
VPX_CODEC_OK = 0
VPX_DEC_INVALID_PARAM = 8
VPX_PLANE_Y = 0 # Variable c_int '0'
PLANE_Y = VPX_PLANE_Y # alias
# def __nonnull(params): return __attribute__ ((__nonnull__ params)) # macro
VP8E_SET_ARNR_STRENGTH = 22
IMG_FMT_RGB565_LE = VPX_IMG_FMT_RGB565_LE # alias
VPX_IMG_FMT_PLANAR = 256 # Variable c_int '256'
IMG_FMT_PLANAR = VPX_IMG_FMT_PLANAR # alias
VPX_RC_ONE_PASS = 0
VPX_CODEC_ERROR = 1
VP8_SET_POSTPROC = 3
VP8_SET_DBG_COLOR_MB_MODES = 5
# def VPX_CTRL_VOID(id): return static vpx_codec_err_t vpx_codec_control_ ##id(vpx_codec_ctx_t*, int) UNUSED; static vpx_codec_err_t vpx_codec_control_ ##id(vpx_codec_ctx_t *ctx, int ctrl_id) { return vpx_codec_control_(ctx, ctrl_id); } # macro
# __gwchar_t = wchar_t # alias
IMG_FMT_I420 = VPX_IMG_FMT_I420 # alias
VP8E_SET_ARNR_TYPE = 23
VPX_VBR = 0
VP8E_UPD_ENTROPY = 5
VPX_RC_FIRST_PASS = 1
def vpx_dec_init(ctx,iface): return vpx_dec_init_ver(ctx, iface, VPX_DECODER_ABI_VERSION) # macro
VP8_ONE_TOKENPARTITION = 0
VPX_DEC_OK = 0
VP8_LAST_FRAME = 1
# __wur = __attribute_warn_unused_result__ # alias
VPX_CODEC_CX_FRAME_PKT = 0
VPX_IMG_FMT_UV_FLIP = 512 # Variable c_int '512'
IMG_FMT_UV_FLIP = VPX_IMG_FMT_UV_FLIP # alias
VPX_DEC_ERROR = 1
# def __LDBL_REDIR_NTH(name,proto): return name proto __THROW # macro
VPX_CBR = 1
VP8E_UPD_REFERENCE = 6
VPX_RC_LAST_PASS = 2
def vpx_codec_version_patch(): return ((vpx_codec_version()>>0)&0xff) # macro
VPX_CODEC_ABI_MISMATCH = 3
def VPX_VERSION_PATCH(v): return ((v>>0)&0xff) # macro
VP8_GOLD_FRAME = 2
VPX_CODEC_STATS_PKT = 1
def offsetof(TYPE,MEMBER): return __builtin_offsetof (TYPE, MEMBER) # macro
VP8E_SET_CQ_LEVEL = 25
IMG_FMT_UYVY = VPX_IMG_FMT_UYVY # alias
# def __NTH(fct): return fct throw () # macro
img_fmt = vpx_img_fmt # alias
VP8E_USE_REFERENCE = 7
VPX_PLANE_U = 1 # Variable c_int '1'
PLANE_U = VPX_PLANE_U # alias
VPX_CODEC_INCAPABLE = 4
VP8E_ONETWO = 3
# def __warndecl(name,msg): return extern void name (void) # macro
def __CONCAT(x,y): return x ## y # macro
VPX_CODEC_CORRUPT_FRAME = 7
VPX_DEC_MEM_ERROR = 2
VP8_ALTR_FRAME = 4
VPX_CODEC_PSNR_PKT = 2
VP8_NOFILTERING = 0
VPX_DEC_ABI_MISMATCH = 3
def __P(args): return args # macro
VP8_DEBUG_TXT_DC_DIFF = 32
VP8E_SET_ROI_MAP = 8
IMG_FMT_RGB32 = VPX_IMG_FMT_RGB32 # alias
VPX_CODEC_UNSUP_BITSTREAM = 5
def __ASMNAME(cname): return __ASMNAME2 (__USER_LABEL_PREFIX__, cname) # macro
def vpx_dec_xma_init(ctx,iface): return vpx_dec_xma_init_ver(ctx, iface, VPX_DECODER_ABI_VERSION) # macro
VPX_CQ = 2
IMG_FMT_YVYU = VPX_IMG_FMT_YVYU # alias
VPX_CODEC_CUSTOM_PKT = 256
def __bos(ptr): return __builtin_object_size (ptr, __USE_FORTIFY_LEVEL > 1) # macro
VP8_DEBLOCK = 1
IMG_FMT_VPXI420 = VPX_IMG_FMT_VPXI420 # alias
def __PMT(args): return args # macro
VP8D_GET_LAST_REF_UPDATES = 256
VP8E_SET_ACTIVEMAP = 9
VP8_SET_REFERENCE = 1
VPX_CODEC_UNSUP_FEATURE = 6
# def __ASMNAME2(prefix,cname): return __STRING (prefix) cname # macro
VPX_DEC_UNSUP_BITSTREAM = 5
VPX_KF_FIXED = 0
IMG_FMT_RGB555_LE = VPX_IMG_FMT_RGB555_LE # alias
VP8_DEMACROBLOCK = 2
# def __REDIRECT(name,proto,alias): return name proto __asm__ (__ASMNAME (#alias)) # macro
VP8D_GET_FRAME_CORRUPTED = 257
VPX_CODEC_MEM_ERROR = 2
VP8E_SET_SCALEMODE = 11
VP8_COPY_REFERENCE = 2
VPX_DEC_UNSUP_FEATURE = 6
VP8_BEST_QUALITY_ENCODING = 0
VPX_KF_AUTO = 1
# def VPX_CTRL_USE_TYPE(id,typ): return static vpx_codec_err_t vpx_codec_control_ ##id(vpx_codec_ctx_t*, int, typ) UNUSED; static vpx_codec_err_t vpx_codec_control_ ##id(vpx_codec_ctx_t *ctx, int ctrl_id, typ data) { return vpx_codec_control_(ctx, ctrl_id, data); } # macro
def vpx_codec_dec_init(ctx,iface,cfg,flags): return vpx_codec_dec_init_ver(ctx, iface, cfg, flags, VPX_DECODER_ABI_VERSION) # macro
VP8_ADDNOISE = 4
IMG_FMT_VPXYV12 = VPX_IMG_FMT_VPXYV12 # alias
IMG_FMT_RGB555 = VPX_IMG_FMT_RGB555 # alias
VP8_DECODER_CTRL_ID_MAX = 258
VPX_CODEC_INVALID_PARAM = 8
IMG_FMT_ARGB_LE = VPX_IMG_FMT_ARGB_LE # alias
VPX_KF_DISABLED = 0
VP8_DEBUG_TXT_FRAME_INFO = 8
IMG_FMT_YUY2 = VPX_IMG_FMT_YUY2 # alias
VP8E_SET_CPUUSED = 13
def VPX_VERSION_MINOR(v): return ((v>>8)&0xff) # macro
# def __REDIRECT_NTH(name,proto,alias): return name proto __THROW __asm__ (__ASMNAME (#alias)) # macro
VP8E_SET_ENABLEAUTOALTREF = 14
VP8_SET_DBG_COLOR_REF_FRAME = 4
VPX_PLANE_V = 2 # Variable c_int '2'
PLANE_V = VPX_PLANE_V # alias
def __GLIBC_PREREQ(maj,min): return ((__GLIBC__ << 16) + __GLIBC_MINOR__ >= ((maj) << 16) + (min)) # macro
VP8_REAL_TIME_ENCODING = 2
VP8E_NORMAL = 0
VP8_DEBUG_TXT_MBLK_MODES = 16
VP8E_SET_NOISE_SENSITIVITY = 15
def __GNUC_PREREQ(maj,min): return ((__GNUC__ << 16) + __GNUC_MINOR__ >= ((maj) << 16) + (min)) # macro
VP8E_THREEFIVE = 2
IMG_FMT_BGR24 = VPX_IMG_FMT_BGR24 # alias
IMG_FMT_ARGB = VPX_IMG_FMT_ARGB # alias
VPX_DEC_LIST_END = 9
VP8E_FOURFIVE = 1
def vpx_codec_enc_init(ctx,iface,cfg,flags): return vpx_codec_enc_init_ver(ctx, iface, cfg, flags, VPX_ENCODER_ABI_VERSION) # macro
def __STRING(x): return #x # macro
VP8E_SET_TUNING = 24
def VPX_VERSION_MAJOR(v): return ((v>>16)&0xff) # macro
# def __LDBL_REDIR(name,proto): return name proto # macro
VP8_TUNE_PSNR = 0
VPX_CODEC_ABI_VERSION = 3 # Variable c_int '3'
VPX_FRAME_IS_KEY = 1 # Variable c_int '1'
_ATFILE_SOURCE = 1 # Variable c_int '1'
VPX_CODEC_CAP_XMA = 4 # Variable c_int '4'
PRId32 = 'd' # Variable STRING '(const char*)"d"'
_SVID_SOURCE = 1 # Variable c_int '1'
__USE_ATFILE = 1 # Variable c_int '1'
PRIxLEAST32 = 'x' # Variable STRING '(const char*)"x"'
SCNuFAST64 = 'lu' # Variable STRING '(const char*)"lu"'
PRIoLEAST32 = 'o' # Variable STRING '(const char*)"o"'
__USE_XOPEN = 1 # Variable c_int '1'
__USE_LARGEFILE64 = 1 # Variable c_int '1'
SCNoFAST16 = 'lo' # Variable STRING '(const char*)"lo"'
SCNxLEAST32 = 'x' # Variable STRING '(const char*)"x"'
VPX_DEC_MEM_WRONLY = 2 # Variable c_int '2'
VPX_DECODER_ABI_VERSION = 5 # Variable c_int '5'
SCNo16 = 'ho' # Variable STRING '(const char*)"ho"'
PRIuFAST32 = 'lu' # Variable STRING '(const char*)"lu"'
SCNx64 = 'lx' # Variable STRING '(const char*)"lx"'
PRIX64 = 'lX' # Variable STRING '(const char*)"lX"'
PRId16 = 'd' # Variable STRING '(const char*)"d"'
VPX_DEC_CAP_PUT_FRAME = 2 # Variable c_int '2'
VPX_CODEC_CAP_POSTPROC = 262144 # Variable c_int '262144'
SCNi64 = 'li' # Variable STRING '(const char*)"li"'
SCNoFAST8 = 'hho' # Variable STRING '(const char*)"hho"'
PRIu16 = 'u' # Variable STRING '(const char*)"u"'
PRIdFAST32 = 'ld' # Variable STRING '(const char*)"ld"'
PRIXLEAST16 = 'X' # Variable STRING '(const char*)"X"'
VP8_EFLAG_NO_REF_ARF = 2097152 # Variable c_int '2097152'
PRIo64 = 'lo' # Variable STRING '(const char*)"lo"'
SCNd16 = 'hd' # Variable STRING '(const char*)"hd"'
VP8_EFLAG_NO_UPD_LAST = 262144 # Variable c_int '262144'
VPX_IMAGE_ABI_VERSION = 1 # Variable c_int '1'
__STDC_IEC_559__ = 1 # Variable c_int '1'
VPX_DEC_MEM_ZERO = 1 # Variable c_int '1'
SCNxFAST64 = 'lx' # Variable STRING '(const char*)"lx"'
SCNo8 = 'hho' # Variable STRING '(const char*)"hho"'
PRIdLEAST64 = 'ld' # Variable STRING '(const char*)"ld"'
PRIdFAST64 = 'ld' # Variable STRING '(const char*)"ld"'
__GLIBC_HAVE_LONG_LONG = 1 # Variable c_int '1'
SCNdFAST16 = 'ld' # Variable STRING '(const char*)"ld"'
SCNuPTR = 'lu' # Variable STRING '(const char*)"lu"'
SCNuLEAST16 = 'hu' # Variable STRING '(const char*)"hu"'
__GNU_LIBRARY__ = 6 # Variable c_int '6'
PRIoFAST64 = 'lo' # Variable STRING '(const char*)"lo"'
PRIuLEAST64 = 'lu' # Variable STRING '(const char*)"lu"'
VPX_CODEC_USE_XMA = 1 # Variable c_int '1'
SCNuFAST16 = 'lu' # Variable STRING '(const char*)"lu"'
PRIXFAST32 = 'lX' # Variable STRING '(const char*)"lX"'
VPX_CODEC_CAP_PUT_SLICE = 65536 # Variable c_int '65536'
PRIiMAX = 'li' # Variable STRING '(const char*)"li"'
PRIxFAST8 = 'x' # Variable STRING '(const char*)"x"'
PRIiLEAST64 = 'li' # Variable STRING '(const char*)"li"'
_POSIX_SOURCE = 1 # Variable c_int '1'
PRIiLEAST8 = 'i' # Variable STRING '(const char*)"i"'
VPX_CODEC_USE_PSNR = 65536 # Variable c_int '65536'
_ISOC99_SOURCE = 1 # Variable c_int '1'
PRIo16 = 'o' # Variable STRING '(const char*)"o"'
__USE_POSIX = 1 # Variable c_int '1'
PRIiLEAST16 = 'i' # Variable STRING '(const char*)"i"'
PRIxMAX = 'lx' # Variable STRING '(const char*)"lx"'
SCNiFAST16 = 'li' # Variable STRING '(const char*)"li"'
SCNoLEAST32 = 'o' # Variable STRING '(const char*)"o"'
SCNdPTR = 'ld' # Variable STRING '(const char*)"ld"'
PRId8 = 'd' # Variable STRING '(const char*)"d"'
SCNdFAST8 = 'hhd' # Variable STRING '(const char*)"hhd"'
__PRI64_PREFIX = 'l' # Variable STRING '(const char*)"l"'
PRIoLEAST16 = 'o' # Variable STRING '(const char*)"o"'
PRIdFAST16 = 'ld' # Variable STRING '(const char*)"ld"'
__USE_LARGEFILE = 1 # Variable c_int '1'
VPX_DEC_MEM_FAST = 4 # Variable c_int '4'
SCNdLEAST16 = 'hd' # Variable STRING '(const char*)"hd"'
PRIuFAST16 = 'lu' # Variable STRING '(const char*)"lu"'
SCNdFAST64 = 'ld' # Variable STRING '(const char*)"ld"'
__USE_POSIX199309 = 1 # Variable c_int '1'
SCNd8 = 'hhd' # Variable STRING '(const char*)"hhd"'
_BITS_WCHAR_H = 1 # Variable c_int '1'
__GLIBC_MINOR__ = 5 # Variable c_int '5'
SCNiLEAST16 = 'hi' # Variable STRING '(const char*)"hi"'
SCNoLEAST64 = 'lo' # Variable STRING '(const char*)"lo"'
SCNo32 = 'o' # Variable STRING '(const char*)"o"'
PRIXLEAST32 = 'X' # Variable STRING '(const char*)"X"'
__strtol_internal_defined = 1 # Variable c_int '1'
PRIuLEAST16 = 'u' # Variable STRING '(const char*)"u"'
SCNiFAST64 = 'li' # Variable STRING '(const char*)"li"'
PRIiFAST64 = 'li' # Variable STRING '(const char*)"li"'
VPX_DL_GOOD_QUALITY = 1000000 # Variable c_int '1000000'
PRIi64 = 'li' # Variable STRING '(const char*)"li"'
PRIxPTR = 'lx' # Variable STRING '(const char*)"lx"'
SCNuLEAST8 = 'hhu' # Variable STRING '(const char*)"hhu"'
VP8_EFLAG_NO_REF_GF = 131072 # Variable c_int '131072'
VP8_EFLAG_NO_UPD_GF = 4194304 # Variable c_int '4194304'
VPX_CODEC_CAP_PUT_FRAME = 131072 # Variable c_int '131072'
SCNuFAST8 = 'hhu' # Variable STRING '(const char*)"hhu"'
SCNd32 = 'd' # Variable STRING '(const char*)"d"'
__USE_XOPEN2K = 1 # Variable c_int '1'
PRIoFAST16 = 'lo' # Variable STRING '(const char*)"lo"'
PRIxLEAST64 = 'lx' # Variable STRING '(const char*)"lx"'
PRIX32 = 'X' # Variable STRING '(const char*)"X"'
PRIuMAX = 'lu' # Variable STRING '(const char*)"lu"'
SCNxFAST16 = 'lx' # Variable STRING '(const char*)"lx"'
SCNu16 = 'hu' # Variable STRING '(const char*)"hu"'
PRIuLEAST8 = 'u' # Variable STRING '(const char*)"u"'
__wcstol_internal_defined = 1 # Variable c_int '1'
PRIXFAST16 = 'lX' # Variable STRING '(const char*)"lX"'
SCNi8 = 'hhi' # Variable STRING '(const char*)"hhi"'
__USE_GNU = 1 # Variable c_int '1'
PRIdPTR = 'ld' # Variable STRING '(const char*)"ld"'
__USE_POSIX2 = 1 # Variable c_int '1'
__USE_BSD = 1 # Variable c_int '1'
SCNoFAST64 = 'lo' # Variable STRING '(const char*)"lo"'
PRIuFAST64 = 'lu' # Variable STRING '(const char*)"lu"'
PRIiFAST16 = 'li' # Variable STRING '(const char*)"li"'
PRIx32 = 'x' # Variable STRING '(const char*)"x"'
SCNi32 = 'i' # Variable STRING '(const char*)"i"'
PRIiLEAST32 = 'i' # Variable STRING '(const char*)"i"'
SCNx8 = 'hhx' # Variable STRING '(const char*)"hhx"'
PRIuFAST8 = 'u' # Variable STRING '(const char*)"u"'
SCNoMAX = 'lo' # Variable STRING '(const char*)"lo"'
_LARGEFILE_SOURCE = 1 # Variable c_int '1'
_POSIX_C_SOURCE = 200112 # Variable c_long '200112l'
VP8_EFLAG_NO_UPD_ARF = 8388608 # Variable c_int '8388608'
PRIxFAST16 = 'lx' # Variable STRING '(const char*)"lx"'
VP8_EFLAG_NO_REF_LAST = 65536 # Variable c_int '65536'
PRIdLEAST16 = 'd' # Variable STRING '(const char*)"d"'
SCNxFAST8 = 'hhx' # Variable STRING '(const char*)"hhx"'
SCNi16 = 'hi' # Variable STRING '(const char*)"hi"'
SCNdLEAST8 = 'hhd' # Variable STRING '(const char*)"hhd"'
_INTTYPES_H = 1 # Variable c_int '1'
PRId64 = 'ld' # Variable STRING '(const char*)"ld"'
PRIiFAST32 = 'li' # Variable STRING '(const char*)"li"'
__USE_SVID = 1 # Variable c_int '1'
__USE_UNIX98 = 1 # Variable c_int '1'
__USE_ANSI = 1 # Variable c_int '1'
SCNuMAX = 'lu' # Variable STRING '(const char*)"lu"'
SCNx16 = 'hx' # Variable STRING '(const char*)"hx"'
__USE_MISC = 1 # Variable c_int '1'
SCNiLEAST8 = 'hhi' # Variable STRING '(const char*)"hhi"'
PRIxLEAST8 = 'x' # Variable STRING '(const char*)"x"'
PRIo8 = 'o' # Variable STRING '(const char*)"o"'
SCNiLEAST32 = 'i' # Variable STRING '(const char*)"i"'
PRIxFAST32 = 'lx' # Variable STRING '(const char*)"lx"'
VPX_CODEC_MEM_FAST = 4 # Variable c_int '4'
PRIiFAST8 = 'i' # Variable STRING '(const char*)"i"'
SCNuLEAST32 = 'u' # Variable STRING '(const char*)"u"'
PRIxFAST64 = 'lx' # Variable STRING '(const char*)"lx"'
__USE_ISOC99 = 1 # Variable c_int '1'
PRIoPTR = 'lo' # Variable STRING '(const char*)"lo"'
VPX_DL_REALTIME = 1 # Variable c_int '1'
PRIoFAST8 = 'o' # Variable STRING '(const char*)"o"'
PRIXLEAST8 = 'X' # Variable STRING '(const char*)"X"'
SCNiFAST8 = 'hhi' # Variable STRING '(const char*)"hhi"'
PRIoFAST32 = 'lo' # Variable STRING '(const char*)"lo"'
__USE_FORTIFY_LEVEL = 2 # Variable c_int '2'
VPX_DEC_CAP_XMA = 4 # Variable c_int '4'
PRIuLEAST32 = 'u' # Variable STRING '(const char*)"u"'
VPX_EFLAG_FORCE_KF = 1 # Variable c_int '1'
VPX_CODEC_CAP_DECODER = 1 # Variable c_int '1'
PRIi8 = 'i' # Variable STRING '(const char*)"i"'
VPX_CODEC_MEM_ZERO = 1 # Variable c_int '1'
SCNdFAST32 = 'ld' # Variable STRING '(const char*)"ld"'
VP8_EFLAG_NO_UPD_ENTROPY = 1048576 # Variable c_int '1048576'
__STDC_ISO_10646__ = 200009 # Variable c_long '200009l'
VPX_CODEC_MEM_WRONLY = 2 # Variable c_int '2'
PRIX16 = 'X' # Variable STRING '(const char*)"X"'
PRIoLEAST64 = 'lo' # Variable STRING '(const char*)"lo"'
__STDC_IEC_559_COMPLEX__ = 1 # Variable c_int '1'
PRIuPTR = 'lu' # Variable STRING '(const char*)"lu"'
__USE_XOPEN_EXTENDED = 1 # Variable c_int '1'
VP8_EFLAG_FORCE_ARF = 16777216 # Variable c_int '16777216'
SCNuFAST32 = 'lu' # Variable STRING '(const char*)"lu"'
VPX_ENCODER_ABI_VERSION = 5 # Variable c_int '5'
PRIi16 = 'i' # Variable STRING '(const char*)"i"'
PRIu64 = 'lu' # Variable STRING '(const char*)"lu"'
VPX_FRAME_IS_DROPPABLE = 2 # Variable c_int '2'
SCNiFAST32 = 'li' # Variable STRING '(const char*)"li"'
PRIXLEAST64 = 'lX' # Variable STRING '(const char*)"lX"'
VP8_EFLAG_FORCE_GF = 524288 # Variable c_int '524288'
__USE_EXTERN_INLINES = 1 # Variable c_int '1'
PRIXFAST64 = 'lX' # Variable STRING '(const char*)"lX"'
_FEATURES_H = 1 # Variable c_int '1'
SCNxMAX = 'lx' # Variable STRING '(const char*)"lx"'
PRIdMAX = 'ld' # Variable STRING '(const char*)"ld"'
PRIXPTR = 'lX' # Variable STRING '(const char*)"lX"'
PRIx16 = 'x' # Variable STRING '(const char*)"x"'
PRIu8 = 'u' # Variable STRING '(const char*)"u"'
SCNdLEAST32 = 'd' # Variable STRING '(const char*)"d"'
SCNxPTR = 'lx' # Variable STRING '(const char*)"lx"'
SCNxLEAST64 = 'lx' # Variable STRING '(const char*)"lx"'
VPX_DL_BEST_QUALITY = 0 # Variable c_int '0'
PRIdLEAST32 = 'd' # Variable STRING '(const char*)"d"'
SCNx32 = 'x' # Variable STRING '(const char*)"x"'
VPX_CODEC_CAP_PSNR = 65536 # Variable c_int '65536'
SCNxFAST32 = 'lx' # Variable STRING '(const char*)"lx"'
SCNiPTR = 'li' # Variable STRING '(const char*)"li"'
PRIo32 = 'o' # Variable STRING '(const char*)"o"'
__wcstoul_internal_defined = 1 # Variable c_int '1'
__WORDSIZE_COMPAT32 = 1 # Variable c_int '1'
__PRIPTR_PREFIX = 'l' # Variable STRING '(const char*)"l"'
VPX_FRAME_IS_INVISIBLE = 4 # Variable c_int '4'
__WCHAR_MAX = 2147483647 # Variable c_int '2147483647'
SCNiMAX = 'li' # Variable STRING '(const char*)"li"'
____gwchar_t_defined = 1 # Variable c_int '1'
SCNdMAX = 'ld' # Variable STRING '(const char*)"ld"'
SCNd64 = 'ld' # Variable STRING '(const char*)"ld"'
PRIXMAX = 'lX' # Variable STRING '(const char*)"lX"'
PRIxLEAST16 = 'x' # Variable STRING '(const char*)"x"'
_STDINT_H = 1 # Variable c_int '1'
SCNoLEAST16 = 'ho' # Variable STRING '(const char*)"ho"'
__WCHAR_MIN = -2147483648 # Variable c_int '-0x00000000080000000'
SCNoFAST32 = 'lo' # Variable STRING '(const char*)"lo"'
VPX_CODEC_CAP_ENCODER = 2 # Variable c_int '2'
SCNu64 = 'lu' # Variable STRING '(const char*)"lu"'
_XOPEN_SOURCE_EXTENDED = 1 # Variable c_int '1'
SCNoLEAST8 = 'hho' # Variable STRING '(const char*)"hho"'
__strtoul_internal_defined = 1 # Variable c_int '1'
PRIXFAST8 = 'X' # Variable STRING '(const char*)"X"'
__WORDSIZE = 64 # Variable c_int '64'
VPX_CODEC_USE_POSTPROC = 65536 # Variable c_int '65536'
PRIu32 = 'u' # Variable STRING '(const char*)"u"'
PRIX8 = 'X' # Variable STRING '(const char*)"X"'
_SYS_CDEFS_H = 1 # Variable c_int '1'
PRIiPTR = 'li' # Variable STRING '(const char*)"li"'
SCNu8 = 'hhu' # Variable STRING '(const char*)"hhu"'
_LARGEFILE64_SOURCE = 1 # Variable c_int '1'
PRIoLEAST8 = 'o' # Variable STRING '(const char*)"o"'
_XOPEN_SOURCE = 600 # Variable c_int '600'
PRIx64 = 'lx' # Variable STRING '(const char*)"lx"'
__USE_POSIX199506 = 1 # Variable c_int '1'
SCNxLEAST16 = 'hx' # Variable STRING '(const char*)"hx"'
__GLIBC__ = 2 # Variable c_int '2'
SCNdLEAST64 = 'ld' # Variable STRING '(const char*)"ld"'
PRIoMAX = 'lo' # Variable STRING '(const char*)"lo"'
SCNu32 = 'u' # Variable STRING '(const char*)"u"'
PRIx8 = 'x' # Variable STRING '(const char*)"x"'
SCNo64 = 'lo' # Variable STRING '(const char*)"lo"'
PRIdFAST8 = 'd' # Variable STRING '(const char*)"d"'
PRIi32 = 'i' # Variable STRING '(const char*)"i"'
SCNuLEAST64 = 'lu' # Variable STRING '(const char*)"lu"'
SCNiLEAST64 = 'li' # Variable STRING '(const char*)"li"'
_BSD_SOURCE = 1 # Variable c_int '1'
VPX_DEC_CAP_PUT_SLICE = 1 # Variable c_int '1'
SCNxLEAST8 = 'hhx' # Variable STRING '(const char*)"hhx"'
SCNoPTR = 'lo' # Variable STRING '(const char*)"lo"'
PRIdLEAST8 = 'd' # Variable STRING '(const char*)"d"'
class imaxdiv_t(Structure):
    pass
imaxdiv_t._fields_ = [
    ('quot', c_long),
    ('rem', c_long),
]
intmax_t = c_long
imaxabs = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].imaxabs
imaxabs.restype = intmax_t
imaxabs.argtypes = [intmax_t]
imaxabs.__doc__ = \
"""intmax_t imaxabs(intmax_t __n)
/usr/include/inttypes.h:298"""
imaxdiv = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].imaxdiv
imaxdiv.restype = imaxdiv_t
imaxdiv.argtypes = [intmax_t, intmax_t]
imaxdiv.__doc__ = \
"""imaxdiv_t imaxdiv(intmax_t __numer, intmax_t __denom)
/usr/include/inttypes.h:302"""
__strtol_internal = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].__strtol_internal
__strtol_internal.restype = c_long
__strtol_internal.argtypes = [STRING, POINTER(STRING), c_int, c_int]
__strtol_internal.__doc__ = \
"""long int __strtol_internal(unknown __nptr, unknown __endptr, int __base, int __group)
/usr/include/inttypes.h:330"""
strtoimax = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].strtoimax
strtoimax.restype = intmax_t
strtoimax.argtypes = [STRING, POINTER(STRING), c_int]
strtoimax.__doc__ = \
"""intmax_t strtoimax(unknown nptr, unknown endptr, int base)
/usr/include/inttypes.h:334"""
__strtoul_internal = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].__strtoul_internal
__strtoul_internal.restype = c_ulong
__strtoul_internal.argtypes = [STRING, POINTER(STRING), c_int, c_int]
__strtoul_internal.__doc__ = \
"""long unsigned int __strtoul_internal(unknown __nptr, unknown __endptr, int __base, int __group)
/usr/include/inttypes.h:345"""
uintmax_t = c_ulong
strtoumax = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].strtoumax
strtoumax.restype = uintmax_t
strtoumax.argtypes = [STRING, POINTER(STRING), c_int]
strtoumax.__doc__ = \
"""uintmax_t strtoumax(unknown nptr, unknown endptr, int base)
/usr/include/inttypes.h:349"""
__wcstol_internal = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].__wcstol_internal
__wcstol_internal.restype = c_long
__wcstol_internal.argtypes = [WSTRING, POINTER(WSTRING), c_int, c_int]
__wcstol_internal.__doc__ = \
"""long int __wcstol_internal(unknown __nptr, unknown __endptr, int __base, int __group)
/usr/include/inttypes.h:359"""
wcstoimax = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].wcstoimax
wcstoimax.restype = intmax_t
wcstoimax.argtypes = [WSTRING, POINTER(WSTRING), c_int]
wcstoimax.__doc__ = \
"""intmax_t wcstoimax(unknown nptr, unknown endptr, int base)
/usr/include/inttypes.h:363"""
__wcstoul_internal = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].__wcstoul_internal
__wcstoul_internal.restype = c_ulong
__wcstoul_internal.argtypes = [WSTRING, POINTER(WSTRING), c_int, c_int]
__wcstoul_internal.__doc__ = \
"""long unsigned int __wcstoul_internal(unknown __nptr, unknown __endptr, int __base, int __group)
/usr/include/inttypes.h:376"""
wcstoumax = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].wcstoumax
wcstoumax.restype = uintmax_t
wcstoumax.argtypes = [WSTRING, POINTER(WSTRING), c_int]
wcstoumax.__doc__ = \
"""uintmax_t wcstoumax(unknown nptr, unknown endptr, int base)
/usr/include/inttypes.h:380"""
int8_t = c_int8
int16_t = c_int16
int32_t = c_int32
int64_t = c_int64
uint8_t = c_uint8
uint16_t = c_uint16
uint32_t = c_uint32
uint64_t = c_uint64
int_least8_t = c_byte
int_least16_t = c_short
int_least32_t = c_int
int_least64_t = c_long
uint_least8_t = c_ubyte
uint_least16_t = c_ushort
uint_least32_t = c_uint
uint_least64_t = c_ulong
int_fast8_t = c_byte
int_fast16_t = c_long
int_fast32_t = c_long
int_fast64_t = c_long
uint_fast8_t = c_ubyte
uint_fast16_t = c_ulong
uint_fast32_t = c_ulong
uint_fast64_t = c_ulong
intptr_t = c_long
uintptr_t = c_ulong
ptrdiff_t = c_long
size_t = c_ulong

# values for enumeration 'vp8_com_control_id'
vp8_com_control_id = c_int # enum

# values for enumeration 'vp8_postproc_level'
vp8_postproc_level = c_int # enum
class vp8_postproc_cfg(Structure):
    pass
vp8_postproc_cfg._fields_ = [
    ('post_proc_flag', c_int),
    ('deblocking_level', c_int),
    ('noise_level', c_int),
]
vp8_postproc_cfg_t = vp8_postproc_cfg

# values for enumeration 'vpx_ref_frame_type'
vpx_ref_frame_type = c_int # enum
vpx_ref_frame_type_t = vpx_ref_frame_type
class vpx_ref_frame(Structure):
    pass
class vpx_image(Structure):
    pass
vpx_image._fields_ = [
    ('fmt', vpx_img_fmt_t),
    ('w', c_uint),
    ('h', c_uint),
    ('d_w', c_uint),
    ('d_h', c_uint),
    ('x_chroma_shift', c_uint),
    ('y_chroma_shift', c_uint),
    ('planes', POINTER(c_ubyte) * 4),
    ('stride', c_int * 4),
    ('bps', c_int),
    ('user_priv', c_void_p),
    ('img_data', POINTER(c_ubyte)),
    ('img_data_owner', c_int),
    ('self_allocd', c_int),
]
vpx_image_t = vpx_image
vpx_ref_frame._fields_ = [
    ('frame_type', vpx_ref_frame_type_t),
    ('img', vpx_image_t),
]
vpx_ref_frame_t = vpx_ref_frame
class vpx_codec_iface(Structure):
    pass
vpx_codec_iface._fields_ = [
]
vpx_codec_iface_t = vpx_codec_iface
vpx_codec_vp8_cx_algo = (vpx_codec_iface_t).in_dll(_libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'], 'vpx_codec_vp8_cx_algo')
vpx_codec_vp8_cx = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_vp8_cx
vpx_codec_vp8_cx.restype = POINTER(vpx_codec_iface_t)
vpx_codec_vp8_cx.argtypes = []
vpx_codec_vp8_cx.__doc__ = \
"""vpx_codec_iface_t * vpx_codec_vp8_cx()
/xtra/libvpx/vpx/vp8cx.h:34"""

# values for enumeration 'vp8e_enc_control_id'
vp8e_enc_control_id = c_int # enum

# values for enumeration 'vpx_scaling_mode_1d'
vpx_scaling_mode_1d = c_int # enum
VPX_SCALING_MODE = vpx_scaling_mode_1d
class vpx_roi_map(Structure):
    pass
vpx_roi_map._fields_ = [
    ('roi_map', POINTER(c_ubyte)),
    ('rows', c_uint),
    ('cols', c_uint),
    ('delta_q', c_int * 4),
    ('delta_lf', c_int * 4),
    ('static_threshold', c_uint * 4),
]
vpx_roi_map_t = vpx_roi_map
class vpx_active_map(Structure):
    pass
vpx_active_map._fields_ = [
    ('active_map', POINTER(c_ubyte)),
    ('rows', c_uint),
    ('cols', c_uint),
]
vpx_active_map_t = vpx_active_map
class vpx_scaling_mode(Structure):
    pass
vpx_scaling_mode._fields_ = [
    ('h_scaling_mode', VPX_SCALING_MODE),
    ('v_scaling_mode', VPX_SCALING_MODE),
]
vpx_scaling_mode_t = vpx_scaling_mode

# values for enumeration 'vp8e_encoding_mode'
vp8e_encoding_mode = c_int # enum

# values for enumeration 'vp8e_token_partitions'
vp8e_token_partitions = c_int # enum

# values for enumeration 'vp8e_tuning'
vp8e_tuning = c_int # enum
vpx_codec_vp8_dx_algo = (vpx_codec_iface_t).in_dll(_libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'], 'vpx_codec_vp8_dx_algo')
vpx_codec_vp8_dx = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_vp8_dx
vpx_codec_vp8_dx.restype = POINTER(vpx_codec_iface_t)
vpx_codec_vp8_dx.argtypes = []
vpx_codec_vp8_dx.__doc__ = \
"""vpx_codec_iface_t * vpx_codec_vp8_dx()
/xtra/libvpx/vpx/vp8dx.h:34"""

# values for enumeration 'vp8_dec_control_id'
vp8_dec_control_id = c_int # enum

# values for enumeration 'vpx_codec_err_t'
vpx_codec_err_t = c_int # enum
vpx_codec_caps_t = c_long
vpx_codec_flags_t = c_long
class vpx_codec_priv(Structure):
    pass
vpx_codec_priv_t = vpx_codec_priv
vpx_codec_priv._fields_ = [
]
vpx_codec_iter_t = c_void_p
class vpx_codec_ctx(Structure):
    pass
class N13vpx_codec_ctx3DOT_2E(Union):
    pass
class vpx_codec_dec_cfg(Structure):
    pass
class vpx_codec_enc_cfg(Structure):
    pass
N13vpx_codec_ctx3DOT_2E._fields_ = [
    ('dec', POINTER(vpx_codec_dec_cfg)),
    ('enc', POINTER(vpx_codec_enc_cfg)),
    ('raw', c_void_p),
]
vpx_codec_ctx._fields_ = [
    ('name', STRING),
    ('iface', POINTER(vpx_codec_iface_t)),
    ('err', vpx_codec_err_t),
    ('err_detail', STRING),
    ('init_flags', vpx_codec_flags_t),
    ('config', N13vpx_codec_ctx3DOT_2E),
    ('priv', POINTER(vpx_codec_priv_t)),
]
vpx_codec_ctx_t = vpx_codec_ctx
vpx_codec_version = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_version
vpx_codec_version.restype = c_int
vpx_codec_version.argtypes = []
vpx_codec_version.__doc__ = \
"""int vpx_codec_version()
/xtra/libvpx/vpx/vpx_codec.h:227"""
vpx_codec_version_str = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_version_str
vpx_codec_version_str.restype = STRING
vpx_codec_version_str.argtypes = []
vpx_codec_version_str.__doc__ = \
"""unknown * vpx_codec_version_str()
/xtra/libvpx/vpx/vpx_codec.h:249"""
vpx_codec_version_extra_str = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_version_extra_str
vpx_codec_version_extra_str.restype = STRING
vpx_codec_version_extra_str.argtypes = []
vpx_codec_version_extra_str.__doc__ = \
"""unknown * vpx_codec_version_extra_str()
/xtra/libvpx/vpx/vpx_codec.h:258"""
vpx_codec_build_config = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_build_config
vpx_codec_build_config.restype = STRING
vpx_codec_build_config.argtypes = []
vpx_codec_build_config.__doc__ = \
"""unknown * vpx_codec_build_config()
/xtra/libvpx/vpx/vpx_codec.h:267"""
vpx_codec_iface_name = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_iface_name
vpx_codec_iface_name.restype = STRING
vpx_codec_iface_name.argtypes = [POINTER(vpx_codec_iface_t)]
vpx_codec_iface_name.__doc__ = \
"""unknown * vpx_codec_iface_name(vpx_codec_iface_t * iface)
/xtra/libvpx/vpx/vpx_codec.h:277"""
vpx_codec_err_to_string = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_err_to_string
vpx_codec_err_to_string.restype = STRING
vpx_codec_err_to_string.argtypes = [vpx_codec_err_t]
vpx_codec_err_to_string.__doc__ = \
"""unknown * vpx_codec_err_to_string(vpx_codec_err_t err)
/xtra/libvpx/vpx/vpx_codec.h:290"""
vpx_codec_error = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_error
vpx_codec_error.restype = STRING
vpx_codec_error.argtypes = [POINTER(vpx_codec_ctx_t)]
vpx_codec_error.__doc__ = \
"""unknown * vpx_codec_error(vpx_codec_ctx_t * ctx)
/xtra/libvpx/vpx/vpx_codec.h:303"""
vpx_codec_error_detail = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_error_detail
vpx_codec_error_detail.restype = STRING
vpx_codec_error_detail.argtypes = [POINTER(vpx_codec_ctx_t)]
vpx_codec_error_detail.__doc__ = \
"""unknown * vpx_codec_error_detail(vpx_codec_ctx_t * ctx)
/xtra/libvpx/vpx/vpx_codec.h:316"""
vpx_codec_destroy = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_destroy
vpx_codec_destroy.restype = vpx_codec_err_t
vpx_codec_destroy.argtypes = [POINTER(vpx_codec_ctx_t)]
vpx_codec_destroy.__doc__ = \
"""vpx_codec_err_t vpx_codec_destroy(vpx_codec_ctx_t * ctx)
/xtra/libvpx/vpx/vpx_codec.h:336"""
vpx_codec_get_caps = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_get_caps
vpx_codec_get_caps.restype = vpx_codec_caps_t
vpx_codec_get_caps.argtypes = [POINTER(vpx_codec_iface_t)]
vpx_codec_get_caps.__doc__ = \
"""vpx_codec_caps_t vpx_codec_get_caps(vpx_codec_iface_t * iface)
/xtra/libvpx/vpx/vpx_codec.h:346"""
vpx_codec_control_ = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_control_
vpx_codec_control_.restype = vpx_codec_err_t
vpx_codec_control_.argtypes = [POINTER(vpx_codec_ctx_t), c_int]
vpx_codec_control_.__doc__ = \
"""vpx_codec_err_t vpx_codec_control_(vpx_codec_ctx_t * ctx, int ctrl_id)
/xtra/libvpx/vpx/vpx_codec.h:375"""
class vpx_codec_mmap(Structure):
    pass
vpx_codec_mmap._fields_ = [
    ('id', c_uint),
    ('sz', c_ulong),
    ('align', c_uint),
    ('flags', c_uint),
    ('base', c_void_p),
    ('dtor', CFUNCTYPE(None, POINTER(vpx_codec_mmap))),
    ('priv', c_void_p),
]
vpx_codec_mmap_t = vpx_codec_mmap
vpx_codec_get_mem_map = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_get_mem_map
vpx_codec_get_mem_map.restype = vpx_codec_err_t
vpx_codec_get_mem_map.argtypes = [POINTER(vpx_codec_ctx_t), POINTER(vpx_codec_mmap_t), POINTER(vpx_codec_iter_t)]
vpx_codec_get_mem_map.__doc__ = \
"""vpx_codec_err_t vpx_codec_get_mem_map(vpx_codec_ctx_t * ctx, vpx_codec_mmap_t * mmap, vpx_codec_iter_t * iter)
/xtra/libvpx/vpx/vpx_codec.h:519"""
vpx_codec_set_mem_map = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_set_mem_map
vpx_codec_set_mem_map.restype = vpx_codec_err_t
vpx_codec_set_mem_map.argtypes = [POINTER(vpx_codec_ctx_t), POINTER(vpx_codec_mmap_t), c_uint]
vpx_codec_set_mem_map.__doc__ = \
"""vpx_codec_err_t vpx_codec_set_mem_map(vpx_codec_ctx_t * ctx, vpx_codec_mmap_t * mmaps, unsigned int num_maps)
/xtra/libvpx/vpx/vpx_codec.h:545"""
class vpx_codec_stream_info(Structure):
    pass
vpx_codec_stream_info._fields_ = [
    ('sz', c_uint),
    ('w', c_uint),
    ('h', c_uint),
    ('is_kf', c_uint),
]
vpx_codec_stream_info_t = vpx_codec_stream_info
vpx_codec_dec_cfg._fields_ = [
    ('threads', c_uint),
    ('w', c_uint),
    ('h', c_uint),
]
vpx_codec_dec_cfg_t = vpx_codec_dec_cfg
vpx_codec_dec_init_ver = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_dec_init_ver
vpx_codec_dec_init_ver.restype = vpx_codec_err_t
vpx_codec_dec_init_ver.argtypes = [POINTER(vpx_codec_ctx_t), POINTER(vpx_codec_iface_t), POINTER(vpx_codec_dec_cfg_t), vpx_codec_flags_t, c_int]
vpx_codec_dec_init_ver.__doc__ = \
"""vpx_codec_err_t vpx_codec_dec_init_ver(vpx_codec_ctx_t * ctx, vpx_codec_iface_t * iface, vpx_codec_dec_cfg_t * cfg, vpx_codec_flags_t flags, int ver)
/xtra/libvpx/vpx/vpx_decoder.h:126"""
vpx_codec_peek_stream_info = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_peek_stream_info
vpx_codec_peek_stream_info.restype = vpx_codec_err_t
vpx_codec_peek_stream_info.argtypes = [POINTER(vpx_codec_iface_t), POINTER(uint8_t), c_uint, POINTER(vpx_codec_stream_info_t)]
vpx_codec_peek_stream_info.__doc__ = \
"""vpx_codec_err_t vpx_codec_peek_stream_info(vpx_codec_iface_t * iface, unknown * data, unsigned int data_sz, vpx_codec_stream_info_t * si)
/xtra/libvpx/vpx/vpx_decoder.h:156"""
vpx_codec_get_stream_info = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_get_stream_info
vpx_codec_get_stream_info.restype = vpx_codec_err_t
vpx_codec_get_stream_info.argtypes = [POINTER(vpx_codec_ctx_t), POINTER(vpx_codec_stream_info_t)]
vpx_codec_get_stream_info.__doc__ = \
"""vpx_codec_err_t vpx_codec_get_stream_info(vpx_codec_ctx_t * ctx, vpx_codec_stream_info_t * si)
/xtra/libvpx/vpx/vpx_decoder.h:173"""
vpx_codec_decode = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_decode
vpx_codec_decode.restype = vpx_codec_err_t
vpx_codec_decode.argtypes = [POINTER(vpx_codec_ctx_t), POINTER(uint8_t), c_uint, c_void_p, c_long]
vpx_codec_decode.__doc__ = \
"""vpx_codec_err_t vpx_codec_decode(vpx_codec_ctx_t * ctx, unknown * data, unsigned int data_sz, void * user_priv, long int deadline)
/xtra/libvpx/vpx/vpx_decoder.h:203"""
vpx_codec_get_frame = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_get_frame
vpx_codec_get_frame.restype = POINTER(vpx_image_t)
vpx_codec_get_frame.argtypes = [POINTER(vpx_codec_ctx_t), POINTER(vpx_codec_iter_t)]
vpx_codec_get_frame.__doc__ = \
"""vpx_image_t * vpx_codec_get_frame(vpx_codec_ctx_t * ctx, vpx_codec_iter_t * iter)
/xtra/libvpx/vpx/vpx_decoder.h:222"""
vpx_codec_put_frame_cb_fn_t = CFUNCTYPE(None, c_void_p, POINTER(vpx_image_t))
vpx_codec_register_put_frame_cb = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_register_put_frame_cb
vpx_codec_register_put_frame_cb.restype = vpx_codec_err_t
vpx_codec_register_put_frame_cb.argtypes = [POINTER(vpx_codec_ctx_t), vpx_codec_put_frame_cb_fn_t, c_void_p]
vpx_codec_register_put_frame_cb.__doc__ = \
"""vpx_codec_err_t vpx_codec_register_put_frame_cb(vpx_codec_ctx_t * ctx, vpx_codec_put_frame_cb_fn_t cb, void * user_priv)
/xtra/libvpx/vpx/vpx_decoder.h:260"""
class vpx_image_rect(Structure):
    pass
vpx_image_rect_t = vpx_image_rect
vpx_codec_put_slice_cb_fn_t = CFUNCTYPE(None, c_void_p, POINTER(vpx_image_t), POINTER(vpx_image_rect_t), POINTER(vpx_image_rect_t))
vpx_codec_register_put_slice_cb = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_register_put_slice_cb
vpx_codec_register_put_slice_cb.restype = vpx_codec_err_t
vpx_codec_register_put_slice_cb.argtypes = [POINTER(vpx_codec_ctx_t), vpx_codec_put_slice_cb_fn_t, c_void_p]
vpx_codec_register_put_slice_cb.__doc__ = \
"""vpx_codec_err_t vpx_codec_register_put_slice_cb(vpx_codec_ctx_t * ctx, vpx_codec_put_slice_cb_fn_t cb, void * user_priv)
/xtra/libvpx/vpx/vpx_decoder.h:302"""

# values for enumeration 'vpx_dec_err_t'
vpx_dec_err_t = c_int # enum
vpx_dec_caps_t = c_int
vpx_dec_stream_info_t = vpx_codec_stream_info_t
vpx_dec_iface_t = vpx_codec_iface
vpx_dec_priv_t = vpx_codec_priv
vpx_dec_iter_t = vpx_codec_iter_t
vpx_dec_ctx_t = vpx_codec_ctx_t
vpx_dec_put_frame_cb_fn_t = CFUNCTYPE(None, c_void_p, POINTER(vpx_image_t))
vpx_dec_put_slice_cb_fn_t = CFUNCTYPE(None, c_void_p, POINTER(vpx_image_t), POINTER(vpx_image_rect_t), POINTER(vpx_image_rect_t))
vpx_dec_mmap_t = vpx_codec_mmap
class vpx_fixed_buf(Structure):
    pass
vpx_fixed_buf._fields_ = [
    ('buf', c_void_p),
    ('sz', size_t),
]
vpx_fixed_buf_t = vpx_fixed_buf
vpx_codec_pts_t = int64_t
vpx_codec_frame_flags_t = uint32_t

# values for enumeration 'vpx_codec_cx_pkt_kind'
vpx_codec_cx_pkt_kind = c_int # enum
class vpx_codec_cx_pkt(Structure):
    pass
class N16vpx_codec_cx_pkt3DOT_6E(Union):
    pass
class N16vpx_codec_cx_pkt3DOT_63DOT_7E(Structure):
    pass
N16vpx_codec_cx_pkt3DOT_63DOT_7E._fields_ = [
    ('buf', c_void_p),
    ('sz', size_t),
    ('pts', vpx_codec_pts_t),
    ('duration', c_ulong),
    ('flags', vpx_codec_frame_flags_t),
]
class vpx_psnr_pkt(Structure):
    pass
vpx_psnr_pkt._fields_ = [
    ('samples', c_uint * 4),
    ('sse', uint64_t * 4),
    ('psnr', c_double * 4),
]
N16vpx_codec_cx_pkt3DOT_6E._fields_ = [
    ('frame', N16vpx_codec_cx_pkt3DOT_63DOT_7E),
    ('twopass_stats', vpx_fixed_buf),
    ('psnr', vpx_psnr_pkt),
    ('raw', vpx_fixed_buf),
    ('pad', c_char * 124),
]
vpx_codec_cx_pkt._fields_ = [
    ('kind', vpx_codec_cx_pkt_kind),
    ('data', N16vpx_codec_cx_pkt3DOT_6E),
]
vpx_codec_cx_pkt_t = vpx_codec_cx_pkt
class vpx_rational(Structure):
    pass
vpx_rational._fields_ = [
    ('num', c_int),
    ('den', c_int),
]
vpx_rational_t = vpx_rational

# values for enumeration 'vpx_enc_pass'
vpx_enc_pass = c_int # enum

# values for enumeration 'vpx_rc_mode'
vpx_rc_mode = c_int # enum

# values for enumeration 'vpx_kf_mode'
vpx_kf_mode = c_int # enum
vpx_enc_frame_flags_t = c_long
vpx_codec_enc_cfg._fields_ = [
    ('g_usage', c_uint),
    ('g_threads', c_uint),
    ('g_profile', c_uint),
    ('g_w', c_uint),
    ('g_h', c_uint),
    ('g_timebase', vpx_rational),
    ('g_error_resilient', c_uint),
    ('g_pass', vpx_enc_pass),
    ('g_lag_in_frames', c_uint),
    ('rc_dropframe_thresh', c_uint),
    ('rc_resize_allowed', c_uint),
    ('rc_resize_up_thresh', c_uint),
    ('rc_resize_down_thresh', c_uint),
    ('rc_end_usage', vpx_rc_mode),
    ('rc_twopass_stats_in', vpx_fixed_buf),
    ('rc_target_bitrate', c_uint),
    ('rc_min_quantizer', c_uint),
    ('rc_max_quantizer', c_uint),
    ('rc_undershoot_pct', c_uint),
    ('rc_overshoot_pct', c_uint),
    ('rc_buf_sz', c_uint),
    ('rc_buf_initial_sz', c_uint),
    ('rc_buf_optimal_sz', c_uint),
    ('rc_2pass_vbr_bias_pct', c_uint),
    ('rc_2pass_vbr_minsection_pct', c_uint),
    ('rc_2pass_vbr_maxsection_pct', c_uint),
    ('kf_mode', vpx_kf_mode),
    ('kf_min_dist', c_uint),
    ('kf_max_dist', c_uint),
]
vpx_codec_enc_cfg_t = vpx_codec_enc_cfg
vpx_codec_enc_init_ver = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_enc_init_ver
vpx_codec_enc_init_ver.restype = vpx_codec_err_t
vpx_codec_enc_init_ver.argtypes = [POINTER(vpx_codec_ctx_t), POINTER(vpx_codec_iface_t), POINTER(vpx_codec_enc_cfg_t), vpx_codec_flags_t, c_int]
vpx_codec_enc_init_ver.__doc__ = \
"""vpx_codec_err_t vpx_codec_enc_init_ver(vpx_codec_ctx_t * ctx, vpx_codec_iface_t * iface, vpx_codec_enc_cfg_t * cfg, vpx_codec_flags_t flags, int ver)
/xtra/libvpx/vpx/vpx_encoder.h:581"""
vpx_codec_enc_config_default = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_enc_config_default
vpx_codec_enc_config_default.restype = vpx_codec_err_t
vpx_codec_enc_config_default.argtypes = [POINTER(vpx_codec_iface_t), POINTER(vpx_codec_enc_cfg_t), c_uint]
vpx_codec_enc_config_default.__doc__ = \
"""vpx_codec_err_t vpx_codec_enc_config_default(vpx_codec_iface_t * iface, vpx_codec_enc_cfg_t * cfg, unsigned int usage)
/xtra/libvpx/vpx/vpx_encoder.h:613"""
vpx_codec_enc_config_set = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_enc_config_set
vpx_codec_enc_config_set.restype = vpx_codec_err_t
vpx_codec_enc_config_set.argtypes = [POINTER(vpx_codec_ctx_t), POINTER(vpx_codec_enc_cfg_t)]
vpx_codec_enc_config_set.__doc__ = \
"""vpx_codec_err_t vpx_codec_enc_config_set(vpx_codec_ctx_t * ctx, unknown * cfg)
/xtra/libvpx/vpx/vpx_encoder.h:631"""
vpx_codec_get_global_headers = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_get_global_headers
vpx_codec_get_global_headers.restype = POINTER(vpx_fixed_buf_t)
vpx_codec_get_global_headers.argtypes = [POINTER(vpx_codec_ctx_t)]
vpx_codec_get_global_headers.__doc__ = \
"""vpx_fixed_buf_t * vpx_codec_get_global_headers(vpx_codec_ctx_t * ctx)
/xtra/libvpx/vpx/vpx_encoder.h:645"""
vpx_codec_encode = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_encode
vpx_codec_encode.restype = vpx_codec_err_t
vpx_codec_encode.argtypes = [POINTER(vpx_codec_ctx_t), POINTER(vpx_image_t), vpx_codec_pts_t, c_ulong, vpx_enc_frame_flags_t, c_ulong]
vpx_codec_encode.__doc__ = \
"""vpx_codec_err_t vpx_codec_encode(vpx_codec_ctx_t * ctx, unknown * img, vpx_codec_pts_t pts, long unsigned int duration, vpx_enc_frame_flags_t flags, long unsigned int deadline)
/xtra/libvpx/vpx/vpx_encoder.h:695"""
vpx_codec_set_cx_data_buf = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_set_cx_data_buf
vpx_codec_set_cx_data_buf.restype = vpx_codec_err_t
vpx_codec_set_cx_data_buf.argtypes = [POINTER(vpx_codec_ctx_t), POINTER(vpx_fixed_buf_t), c_uint, c_uint]
vpx_codec_set_cx_data_buf.__doc__ = \
"""vpx_codec_err_t vpx_codec_set_cx_data_buf(vpx_codec_ctx_t * ctx, unknown * buf, unsigned int pad_before, unsigned int pad_after)
/xtra/libvpx/vpx/vpx_encoder.h:744"""
vpx_codec_get_cx_data = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_get_cx_data
vpx_codec_get_cx_data.restype = POINTER(vpx_codec_cx_pkt_t)
vpx_codec_get_cx_data.argtypes = [POINTER(vpx_codec_ctx_t), POINTER(vpx_codec_iter_t)]
vpx_codec_get_cx_data.__doc__ = \
"""unknown * vpx_codec_get_cx_data(vpx_codec_ctx_t * ctx, vpx_codec_iter_t * iter)
/xtra/libvpx/vpx/vpx_encoder.h:771"""
vpx_codec_get_preview_frame = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_codec_get_preview_frame
vpx_codec_get_preview_frame.restype = POINTER(vpx_image_t)
vpx_codec_get_preview_frame.argtypes = [POINTER(vpx_codec_ctx_t)]
vpx_codec_get_preview_frame.__doc__ = \
"""unknown * vpx_codec_get_preview_frame(vpx_codec_ctx_t * ctx)
/xtra/libvpx/vpx/vpx_encoder.h:786"""
vpx_image_rect._fields_ = [
    ('x', c_uint),
    ('y', c_uint),
    ('w', c_uint),
    ('h', c_uint),
]
vpx_img_alloc = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_img_alloc
vpx_img_alloc.restype = POINTER(vpx_image_t)
vpx_img_alloc.argtypes = [POINTER(vpx_image_t), vpx_img_fmt_t, c_uint, c_uint, c_uint]
vpx_img_alloc.__doc__ = \
"""vpx_image_t * vpx_img_alloc(vpx_image_t * img, vpx_img_fmt_t fmt, unsigned int d_w, unsigned int d_h, unsigned int align)
/xtra/libvpx/vpx/vpx_image.h:173"""
vpx_img_wrap = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_img_wrap
vpx_img_wrap.restype = POINTER(vpx_image_t)
vpx_img_wrap.argtypes = [POINTER(vpx_image_t), vpx_img_fmt_t, c_uint, c_uint, c_uint, POINTER(c_ubyte)]
vpx_img_wrap.__doc__ = \
"""vpx_image_t * vpx_img_wrap(vpx_image_t * img, vpx_img_fmt_t fmt, unsigned int d_w, unsigned int d_h, unsigned int align, unsigned char * img_data)
/xtra/libvpx/vpx/vpx_image.h:199"""
vpx_img_set_rect = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_img_set_rect
vpx_img_set_rect.restype = c_int
vpx_img_set_rect.argtypes = [POINTER(vpx_image_t), c_uint, c_uint, c_uint, c_uint]
vpx_img_set_rect.__doc__ = \
"""int vpx_img_set_rect(vpx_image_t * img, unsigned int x, unsigned int y, unsigned int w, unsigned int h)
/xtra/libvpx/vpx/vpx_image.h:219"""
vpx_img_flip = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_img_flip
vpx_img_flip.restype = None
vpx_img_flip.argtypes = [POINTER(vpx_image_t)]
vpx_img_flip.__doc__ = \
"""void vpx_img_flip(vpx_image_t * img)
/xtra/libvpx/vpx/vpx_image.h:229"""
vpx_img_free = _libraries['/xtra/libvpx/x86_build/libvpx.so.0.9.6'].vpx_img_free
vpx_img_free.restype = None
vpx_img_free.argtypes = [POINTER(vpx_image_t)]
vpx_img_free.__doc__ = \
"""void vpx_img_free(vpx_image_t * img)
/xtra/libvpx/vpx/vpx_image.h:237"""
__all__ = ['VPX_RC_ONE_PASS', 'vpx_fixed_buf_t', '_ATFILE_SOURCE',
           'int_fast32_t', 'SCNuFAST64', 'SCNdPTR',
           'vpx_enc_frame_flags_t', 'VP8_COPY_REFERENCE',
           'IMG_FMT_YV12', 'vp8_postproc_cfg', 'uint8_t',
           'vp8e_enc_control_id', 'VPX_KF_FIXED',
           'vpx_ref_frame_type', 'VPX_DEC_CAP_PUT_FRAME',
           'VPX_CODEC_CAP_POSTPROC', 'SCNoFAST8', 'vpx_img_wrap',
           'VPX_DL_REALTIME', 'vpx_codec_cx_pkt', 'IMG_FMT_YVYU',
           'VPX_CODEC_INVALID_PARAM', 'VP8E_SET_ENABLEAUTOALTREF',
           'vpx_codec_cx_pkt_t', 'SCNdFAST16', '__GLIBC_PREREQ',
           'PRIxLEAST32', 'VP8E_SET_ARNR_STRENGTH', '__ASMNAME',
           'SCNuFAST16', 'VPX_CODEC_CAP_PUT_SLICE', 'int_least16_t',
           '_POSIX_SOURCE', 'vp8_postproc_cfg_t', 'uint_fast16_t',
           'uint_least8_t', 'vpx_img_set_rect',
           'VPX_IMG_FMT_HAS_ALPHA', '____gwchar_t_defined',
           '__USE_POSIX199309', 'vpx_codec_control', 'VPX_CQ',
           'PRIu32', 'VP8_DEBUG_TXT_MBLK_MODES', 'SCNiLEAST16',
           'vpx_codec_enc_cfg_t', 'SCNo32', 'PRIXLEAST32',
           'vpx_codec_iface', '__strtol_internal_defined',
           'SCNiFAST64', 'vpx_codec_dec_init', 'PRIxPTR',
           'VPX_CODEC_INCAPABLE', 'IMG_FMT_UYVY', 'SCNd32', 'PRIX32',
           'SCNxLEAST32', 'vpx_dec_xma_init', 'VPX_IMG_FMT_UV_FLIP',
           '__wcstol_internal_defined', 'PRIXFAST16',
           'vpx_codec_ctx_t', 'IMG_FMT_RGB32',
           'vpx_codec_frame_flags_t', 'SCNx8', 'PRIuFAST8',
           'vp8e_token_partitions', 'VP8_REAL_TIME_ENCODING', '__PMT',
           'VPX_IMG_FMT_RGB565', 'PRId64', 'VPX_CODEC_CAP_PSNR',
           'PRIdLEAST16', 'VPX_IMG_FMT_ARGB',
           'VP8_BEST_QUALITY_ENCODING', '__USE_POSIX199506',
           'VPX_DEC_UNSUP_FEATURE', 'vpx_codec_build_config',
           'VPX_CODEC_LIST_END', 'SCNdLEAST32', 'vpx_scaling_mode',
           'vpx_codec_flags_t', 'PRIoPTR', 'wcstoimax',
           'int_least64_t', 'VP8E_NORMAL', 'VPX_VBR',
           'VPX_CODEC_CORRUPT_FRAME',
           'N16vpx_codec_cx_pkt3DOT_63DOT_7E', 'vpx_codec_priv_t',
           '__USE_FORTIFY_LEVEL', 'PRIi8', 'VPX_PLANE_PACKED',
           '__USE_XOPEN_EXTENDED', 'VPX_FRAME_IS_DROPPABLE',
           'VPX_RC_FIRST_PASS', '__PRIPTR_PREFIX', 'PRIiLEAST64',
           'IMG_FMT_PLANAR', 'vpx_dec_ctx_t', 'VPX_DL_BEST_QUALITY',
           'PRIxFAST32', 'VPX_CODEC_PSNR_PKT', 'vpx_codec_iface_name',
           'VPX_KF_AUTO', 'vpx_active_map_t',
           'vpx_codec_version_extra_str', 'VPX_DEC_OK',
           'IMG_FMT_VPXYV12', 'PRIx32', 'SCNu64', 'VP8E_SET_TUNING',
           '__WORDSIZE', 'VP8_DECODER_CTRL_ID_START', 'vpx_kf_mode',
           'SCNu8', '_XOPEN_SOURCE', 'vpx_codec_peek_stream_info',
           'vpx_scaling_mode_t', 'VPX_IMG_FMT_RGB32_LE', '__GLIBC__',
           '__USE_ISOC99', 'SCNu32', 'SCNo64', 'PRIdFAST8',
           'vpx_codec_encode', 'PRIi32', 'SCNiLEAST64',
           'vpx_codec_version_major', 'VP8_SET_DBG_COLOR_MB_MODES',
           'VPX_CODEC_ABI_VERSION', 'vpx_codec_caps_t',
           'IMG_FMT_RGB555', 'VP8_ONE_TOKENPARTITION',
           'vpx_rational_t', '_INTTYPES_H', 'vpx_roi_map_t',
           'IMG_FMT_ARGB_LE', 'size_t', '__USE_XOPEN', 'SCNoFAST16',
           'N16vpx_codec_cx_pkt3DOT_6E',
           'vpx_codec_register_put_frame_cb',
           'VPX_DECODER_ABI_VERSION', 'VP8_SET_DBG_COLOR_REF_FRAME',
           'PRIuFAST32', 'PRIX64', 'VP8E_SET_TOKEN_PARTITIONS',
           'uint_least16_t', 'vpx_dec_stream_info_t',
           'VPX_IMG_FMT_BGR24', 'VPX_IMG_FMT_RGB555',
           'VP8_EFLAG_FORCE_ARF', 'PRIo64', 'VP8_EFLAG_NO_UPD_LAST',
           'IMG_FMT_RGB555_LE', 'SCNoLEAST16', 'SCNxFAST64',
           'PRIdLEAST64', '__USE_ATFILE', 'PLANE_ALPHA',
           'VPX_DEC_MEM_ZERO', 'vpx_scaling_mode_1d',
           'VPX_FRAME_IS_INVISIBLE', 'PRIo16', '__USE_POSIX',
           'SCNxFAST16', 'PRIxMAX', 'PRIiFAST16', 'vpx_codec_dec_cfg',
           'VPX_CODEC_ERROR', 'VPX_IMG_FMT_RGB565_LE',
           'vpx_codec_vp8_dx_algo', 'SCNdFAST8', '__PRI64_PREFIX',
           'PRIoLEAST16', 'vpx_image_rect_t', 'VP8_LAST_FRAME',
           'vpx_ref_frame', 'SCNdFAST64', 'int_fast64_t',
           'vpx_dec_put_frame_cb_fn_t', '_BITS_WCHAR_H', 'PLANE_V',
           'VP8E_GET_LAST_QUANTIZER_64', 'PLANE_Y', 'VPX_KF_DISABLED',
           'VPX_VERSION_MINOR', 'PRIuLEAST16',
           'vpx_codec_err_to_string', 'VP8E_SET_ROI_MAP',
           'SCNuLEAST16', 'SCNuLEAST8', 'VP8_EFLAG_NO_REF_GF',
           'SCNoLEAST64', 'PRIoFAST16', 'PRIxLEAST64',
           'vpx_codec_cx_pkt_kind', 'vpx_codec_err_t',
           'vp8_com_control_id', '__P', 'vpx_codec_version',
           'VP8E_SET_SCALEMODE', 'VP8_GOLD_FRAME',
           '__strtol_internal', '__USE_GNU', 'VP8_TWO_TOKENPARTITION',
           'SCNiFAST16', 'PRIiLEAST32', 'VP8E_UPD_ENTROPY',
           'VPX_DEC_UNSUP_BITSTREAM', '__attribute_format_arg__',
           'VPX_DEC_LIST_END', 'vpx_img_free', '_POSIX_C_SOURCE',
           'VP8_EFLAG_NO_UPD_ARF', 'VP8_DEBUG_TXT_DC_DIFF',
           'VP8_EFLAG_NO_REF_LAST', 'VPX_CODEC_UNSUP_FEATURE',
           'PRIdFAST32', 'SCNi16', 'SCNdLEAST8', '__USE_SVID',
           'VPX_IMG_FMT_VPXYV12', 'vpx_rational', '__USE_ANSI',
           'SCNx16', 'SCNxLEAST8', 'vpx_codec_control_',
           'VPX_SCALING_MODE', 'PRIiFAST8', 'IMG_FMT_RGB24',
           'vpx_image_rect', 'vpx_codec_get_mem_map',
           'vpx_dec_put_slice_cb_fn_t', 'VPX_VERSION_MAJOR',
           'SCNdLEAST64', 'PRIoFAST8', 'PRIXLEAST8', 'SCNiFAST8',
           'VPX_DEC_CORRUPT_FRAME', 'VPX_CODEC_CAP_DECODER',
           'IMG_FMT_RGB565', 'VPX_CODEC_CUSTOM_PKT',
           '__STDC_ISO_10646__', 'VPX_CODEC_MEM_WRONLY', 'PRIdFAST16',
           'vpx_img_flip', 'VPX_CODEC_UNSUP_BITSTREAM',
           'VPX_ENCODER_ABI_VERSION', 'vpx_dec_iface_t',
           '__USE_LARGEFILE', 'VP8E_SET_CQ_LEVEL', 'PRIXFAST64',
           '_FEATURES_H', 'vpx_dec_init', 'VP8_GOOD_QUALITY_ENCODING',
           'uint64_t', 'vpx_dec_mmap_t', 'VPX_IMG_FMT_YV12',
           'vpx_dec_priv_t', 'VPX_IMG_FMT_RGB555_LE',
           'VPX_DEC_MEM_FAST', 'SCNiPTR', 'uintptr_t',
           '__WORDSIZE_COMPAT32', 'vpx_codec_error_detail',
           'vpx_codec_dec_cfg_t', 'vpx_codec_get_stream_info',
           'vpx_codec_set_mem_map', 'IMG_FMT_YUY2',
           'VP8_DEBUG_TXT_FRAME_INFO', 'vpx_codec_vp8_dx',
           'vpx_fixed_buf', 'VPX_CODEC_CAP_ENCODER',
           '_XOPEN_SOURCE_EXTENDED', 'SCNd8',
           'VPX_CODEC_USE_POSTPROC', 'vpx_img_fmt', 'PRIxLEAST8',
           'vpx_codec_iter_t', 'vpx_codec_enc_init', 'uint32_t',
           'PRIXFAST8', 'PRIx64', 'VPX_IMG_FMT_VPXI420',
           'VP8E_SET_CPUUSED', 'vpx_codec_get_global_headers',
           'vpx_codec_enc_config_default', 'VPX_CODEC_MEM_ERROR',
           'VPX_EFLAG_FORCE_KF', 'SCNdFAST32', '_BSD_SOURCE',
           'VPX_DEC_CAP_PUT_SLICE', 'VPX_CBR',
           'vpx_codec_enc_init_ver', 'VPX_CODEC_CAP_XMA',
           'vpx_ref_frame_t', 'VPX_DEC_INVALID_PARAM',
           '__GNU_LIBRARY__', 'SCNdLEAST16', '__USE_LARGEFILE64',
           'vpx_codec_get_caps', 'vpx_codec_decode', 'SCNo16',
           'VPX_CODEC_CX_FRAME_PKT', 'VP8E_USE_REFERENCE',
           'VPX_IMG_FMT_I420', 'PRId16', 'PRIu16', 'PRIXLEAST16',
           'intptr_t', 'SCNd16', 'vpx_codec_version_minor',
           'int_fast8_t', 'SCNo8', 'PRIdFAST64',
           'vpx_codec_get_cx_data', 'vp8_dec_control_id',
           '__GLIBC_HAVE_LONG_LONG', 'SCNuPTR', 'VP8_ADDNOISE',
           'IMG_FMT_HAS_ALPHA', 'PRIoLEAST8', 'IMG_FMT_UV_FLIP',
           '__attribute_format_strfmon__', 'VP8_DECODER_CTRL_ID_MAX',
           '__bos', 'PRId8', 'vpx_codec_iface_t',
           'VP8_SET_DBG_COLOR_B_MODES', 'VPX_IMG_FMT_RGB24',
           'VPX_IMG_FMT_UYVY', '__USE_EXTERN_INLINES',
           '__strtoul_internal_defined', 'VPX_IMG_FMT_YUY2',
           'vpx_codec_mmap_t', 'VP8_SET_POSTPROC', 'PRIiFAST64',
           'VPX_RC_LAST_PASS', 'VP8_EFLAG_NO_UPD_GF', 'IMG_FMT_NONE',
           'VPX_CODEC_CAP_PUT_FRAME', 'SCNuFAST8', '__USE_XOPEN2K',
           'VP8E_THREEFIVE', 'vpx_roi_map',
           'VP8_EIGHT_TOKENPARTITION', 'SCNxFAST8', 'SCNu16', 'PRIo8',
           'VP8_NOFILTERING', 'SCNuFAST32', '__USE_POSIX2',
           'vpx_codec_priv', 'uint16_t', 'wcstoumax',
           'vpx_codec_stream_info', 'vpx_codec_vp8_cx_algo',
           'PRIxFAST16', 'vpx_img_alloc', 'int32_t',
           'vpx_codec_register_put_slice_cb', 'vp8e_tuning',
           'VP8_COMMON_CTRL_ID_MAX', 'SCNuMAX', '__USE_MISC',
           'SCNiLEAST8', 'vpx_dec_err_t', 'SCNiLEAST32',
           'IMG_FMT_I420', 'VPX_CODEC_MEM_FAST', 'vpx_codec_mmap',
           'vpx_enc_pass', 'vpx_codec_version_str', 'PRIxFAST64',
           '__wcstol_internal', 'strtoimax', 'vpx_codec_destroy',
           'VP8_EFLAG_NO_REF_ARF', 'SCNi64', 'strtoumax',
           'VP8_ALTR_FRAME', '_STDINT_H', 'vpx_codec_enc_config_set',
           'VPX_CODEC_MEM_ZERO', 'VP8_EFLAG_NO_UPD_ENTROPY', 'PRIX16',
           'vpx_codec_dec_init_ver', 'VPX_DEC_ABI_MISMATCH',
           'PRIXFAST32', 'PRIi16', 'imaxabs', 'VP8_EFLAG_FORCE_GF',
           'IMG_FMT_RGB32_LE', 'SCNxMAX', 'VP8E_ONETWO', 'SCNxPTR',
           'PRIiFAST32', 'PRIdLEAST32', 'SCNxFAST32', 'PRIo32',
           'VPX_DEC_ERROR', 'uintmax_t', 'vpx_codec_stream_info_t',
           '__WCHAR_MAX', 'SCNiMAX', 'int_fast16_t', 'SCNdMAX',
           'VPX_PLANE_ALPHA', 'SCNd64', 'VPX_IMG_FMT_ARGB_LE',
           'SCNoLEAST8', 'VPX_CODEC_USE_PSNR', 'VP8_DEMACROBLOCK',
           '_SYS_CDEFS_H', 'PRIiPTR', 'VP8_FOUR_TOKENPARTITION',
           'VP8_DEBLOCK', 'PRIXPTR', 'VP8E_SET_STATIC_THRESHOLD',
           'uint_fast64_t', 'SCNuLEAST64', 'VP8E_SET_ACTIVEMAP',
           'uint_fast8_t', 'VP8E_GET_LAST_QUANTIZER',
           'VPX_DEC_MEM_ERROR', '_LARGEFILE_SOURCE', 'VP8_TUNE_SSIM',
           'PRIoLEAST32', 'uint_least32_t', 'VPX_CODEC_ABI_MISMATCH',
           'vpx_image', 'VP8E_SET_NOISE_SENSITIVITY', 'vpx_image_t',
           'VPX_VERSION_PATCH', 'img_fmt', 'IMG_FMT_ARGB',
           'VPX_DEC_MEM_WRONLY', 'vpx_codec_version_patch',
           'img_fmt_t', 'vpx_dec_caps_t', 'vp8e_encoding_mode',
           'SCNx64', 'int_least32_t', 'VPX_IMAGE_ABI_VERSION',
           '__STDC_IEC_559__', 'PRIuLEAST64', 'VPX_CODEC_USE_XMA',
           'vpx_codec_put_slice_cb_fn_t', 'VP8_DEBUG_TXT_RATE_INFO',
           'VPX_IMG_FMT_YVYU', 'VP8E_UPD_REFERENCE',
           'vpx_codec_vp8_cx', 'vpx_codec_error', 'PRIxFAST8',
           'vpx_codec_enc_cfg', 'PRIiLEAST8', '_ISOC99_SOURCE',
           'VP8E_FOURFIVE', 'PRIiMAX', 'SCNoLEAST32', 'int16_t',
           'SCNi32', 'VP8D_GET_FRAME_CORRUPTED', 'intmax_t', 'PRIu8',
           'vpx_codec_put_frame_cb_fn_t', 'PRIuFAST16', 'PRIXMAX',
           'IMG_FMT_RGB565_LE', 'int_least8_t', 'PRIi64',
           'VPX_PLANE_V', 'VPX_PLANE_U', '_SVID_SOURCE',
           'VPX_PLANE_Y', '__strtoul_internal', 'VPX_IMG_FMT_RGB32',
           'PRIuMAX', 'PRIiLEAST16', 'PRIuLEAST8', 'vpx_codec_pts_t',
           'SCNi8', 'PRIdPTR', '__USE_BSD', 'SCNoFAST64',
           'PRIuFAST64', '__CONCAT', 'ptrdiff_t', 'SCNoMAX',
           'vpx_codec_set_cx_data_buf', 'uint_least64_t',
           'VP8_TUNE_PSNR', '__USE_UNIX98', 'VPX_DL_GOOD_QUALITY',
           'VP8_SET_REFERENCE', 'SCNoFAST32', 'VPX_IMG_FMT_NONE',
           'SCNuLEAST32', 'vpx_codec_get_frame', 'PRIuLEAST32',
           'VPX_IMG_FMT_PLANAR', 'PRIX8', 'PRIoFAST32', 'PRIoMAX',
           'VPX_DEC_CAP_XMA', 'PRIx8', 'int8_t', 'vpx_rc_mode',
           'VPX_CODEC_STATS_PKT', 'PRIoLEAST64',
           '__STDC_IEC_559_COMPLEX__', '__wcstoul_internal',
           'PRIuPTR', 'PRIu64', 'SCNiFAST32', 'PRIXLEAST64',
           'imaxdiv', 'PRIdMAX', 'PRIx16', 'vpx_ref_frame_type_t',
           'vpx_dec_iter_t', 'SCNxLEAST64', 'SCNx32', 'PRIoFAST64',
           'vpx_codec_get_preview_frame', 'vpx_codec_ctx',
           '__wcstoul_internal_defined', '__STRING', 'int64_t',
           'IMG_FMT_VPXI420', '__WCHAR_MIN', 'uint_fast32_t',
           'PRIxLEAST16', '__GNUC_PREREQ', 'imaxdiv_t',
           'VP8E_SET_ARNR_TYPE', 'VPX_FRAME_IS_KEY', 'PRId32',
           'IMG_FMT_BGR24', 'VPX_CODEC_OK', '_LARGEFILE64_SOURCE',
           'VP8_SET_DBG_DISPLAY_MV', 'vpx_psnr_pkt', 'SCNxLEAST16',
           '__bos0', 'VP8E_SET_ARNR_MAXFRAMES',
           'N13vpx_codec_ctx3DOT_2E', 'PLANE_PACKED', 'PLANE_U',
           'VP8E_SET_SHARPNESS', 'vpx_img_fmt_t', '__GLIBC_MINOR__',
           'vp8_postproc_level', 'VP8D_GET_LAST_REF_UPDATES',
           'vpx_active_map', 'offsetof', 'SCNoPTR', 'PRIdLEAST8']
