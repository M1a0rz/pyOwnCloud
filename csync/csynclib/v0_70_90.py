'''Wrapper for csync0.70.90.h

Generated with:
/home/hefee/.local/bin/ctypesgen.py csync0.70.90.h -o v0_70_90.py --no-macros --exclude csync_version -I .

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

from .preamble import *
from .pre import _lib

__uid_t = c_uint # /usr/include/x86_64-linux-gnu/bits/types.h: 134

__gid_t = c_uint # /usr/include/x86_64-linux-gnu/bits/types.h: 135

__mode_t = c_uint # /usr/include/x86_64-linux-gnu/bits/types.h: 138

__time_t = c_long # /usr/include/x86_64-linux-gnu/bits/types.h: 148

gid_t = __gid_t # /usr/include/unistd.h: 232

uid_t = __uid_t # /usr/include/unistd.h: 237

mode_t = __mode_t # /usr/include/x86_64-linux-gnu/sys/types.h: 70

time_t = __time_t # /usr/include/time.h: 75

enum_csync_error_codes_e = c_int # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_NONE = 0 # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_LOG = (CSYNC_ERR_NONE + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_LOCK = (CSYNC_ERR_LOG + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_STATEDB_LOAD = (CSYNC_ERR_LOCK + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_STATEDB_WRITE = (CSYNC_ERR_STATEDB_LOAD + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_MODULE = (CSYNC_ERR_STATEDB_WRITE + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_TIMESKEW = (CSYNC_ERR_MODULE + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_FILESYSTEM = (CSYNC_ERR_TIMESKEW + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_TREE = (CSYNC_ERR_FILESYSTEM + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_MEM = (CSYNC_ERR_TREE + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_PARAM = (CSYNC_ERR_MEM + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_UPDATE = (CSYNC_ERR_PARAM + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_RECONCILE = (CSYNC_ERR_UPDATE + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_PROPAGATE = (CSYNC_ERR_RECONCILE + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_ACCESS_FAILED = (CSYNC_ERR_PROPAGATE + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_REMOTE_CREATE = (CSYNC_ERR_ACCESS_FAILED + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_REMOTE_STAT = (CSYNC_ERR_REMOTE_CREATE + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_LOCAL_CREATE = (CSYNC_ERR_REMOTE_STAT + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_LOCAL_STAT = (CSYNC_ERR_LOCAL_CREATE + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_PROXY = (CSYNC_ERR_LOCAL_STAT + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_LOOKUP = (CSYNC_ERR_PROXY + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_AUTH_SERVER = (CSYNC_ERR_LOOKUP + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_AUTH_PROXY = (CSYNC_ERR_AUTH_SERVER + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_CONNECT = (CSYNC_ERR_AUTH_PROXY + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_TIMEOUT = (CSYNC_ERR_CONNECT + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_HTTP = (CSYNC_ERR_TIMEOUT + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_PERM = (CSYNC_ERR_HTTP + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_NOT_FOUND = (CSYNC_ERR_PERM + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_EXISTS = (CSYNC_ERR_NOT_FOUND + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_NOSPC = (CSYNC_ERR_EXISTS + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_QUOTA = (CSYNC_ERR_NOSPC + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_SERVICE_UNAVAILABLE = (CSYNC_ERR_QUOTA + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_FILE_TOO_BIG = (CSYNC_ERR_SERVICE_UNAVAILABLE + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_ABORTED = (CSYNC_ERR_FILE_TOO_BIG + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERR_UNSPEC = (CSYNC_ERR_ABORTED + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 53

CSYNC_ERROR_CODE = enum_csync_error_codes_e # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 91

enum_csync_instructions_e = c_int # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 97

CSYNC_INSTRUCTION_NONE = 0 # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 97

CSYNC_INSTRUCTION_EVAL = 1 # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 97

CSYNC_INSTRUCTION_REMOVE = 2 # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 97

CSYNC_INSTRUCTION_RENAME = 4 # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 97

CSYNC_INSTRUCTION_NEW = 8 # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 97

CSYNC_INSTRUCTION_CONFLICT = 16 # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 97

CSYNC_INSTRUCTION_IGNORE = 32 # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 97

CSYNC_INSTRUCTION_SYNC = 64 # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 97

CSYNC_INSTRUCTION_STAT_ERROR = 128 # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 97

CSYNC_INSTRUCTION_ERROR = 256 # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 97

CSYNC_INSTRUCTION_DELETED = 512 # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 97

CSYNC_INSTRUCTION_UPDATED = 1024 # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 97

enum_csync_ftw_type_e = c_int # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 113

CSYNC_FTW_TYPE_FILE = 0 # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 113

CSYNC_FTW_TYPE_SLINK = (CSYNC_FTW_TYPE_FILE + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 113

CSYNC_FTW_TYPE_DIR = (CSYNC_FTW_TYPE_SLINK + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 113

CSYNC_FTW_TYPE_SKIP = (CSYNC_FTW_TYPE_DIR + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 113

# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 133
class struct_csync_tree_walk_file_s(Structure):
    pass

struct_csync_tree_walk_file_s.__slots__ = [
    'path',
    'modtime',
    'uid',
    'gid',
    'mode',
    'type',
    'instruction',
    'rename_path',
    'md5',
    'error_string',
]
struct_csync_tree_walk_file_s._fields_ = [
    ('path', String),
    ('modtime', time_t),
    ('uid', uid_t),
    ('gid', gid_t),
    ('mode', mode_t),
    ('type', enum_csync_ftw_type_e),
    ('instruction', enum_csync_instructions_e),
    ('rename_path', String),
    ('md5', String),
    ('error_string', String),
]

TREE_WALK_FILE = struct_csync_tree_walk_file_s # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 152

# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 157
class struct_csync_s(Structure):
    pass

CSYNC = struct_csync_s # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 157

csync_auth_callback = CFUNCTYPE(UNCHECKED(c_int), String, String, c_size_t, c_int, c_int, POINTER(None)) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 159

csync_log_callback = CFUNCTYPE(UNCHECKED(None), POINTER(CSYNC), c_int, String, String, POINTER(None)) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 162

# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 175
if hasattr(_lib, 'csync_create'):
    csync_create = _lib.csync_create
    csync_create.argtypes = [POINTER(POINTER(CSYNC)), String, String]
    csync_create.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 186
if hasattr(_lib, 'csync_init'):
    csync_init = _lib.csync_init
    csync_init.argtypes = [POINTER(CSYNC)]
    csync_init.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 195
if hasattr(_lib, 'csync_update'):
    csync_update = _lib.csync_update
    csync_update.argtypes = [POINTER(CSYNC)]
    csync_update.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 204
if hasattr(_lib, 'csync_reconcile'):
    csync_reconcile = _lib.csync_reconcile
    csync_reconcile.argtypes = [POINTER(CSYNC)]
    csync_reconcile.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 213
if hasattr(_lib, 'csync_propagate'):
    csync_propagate = _lib.csync_propagate
    csync_propagate.argtypes = [POINTER(CSYNC)]
    csync_propagate.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 222
if hasattr(_lib, 'csync_commit'):
    csync_commit = _lib.csync_commit
    csync_commit.argtypes = [POINTER(CSYNC)]
    csync_commit.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 233
if hasattr(_lib, 'csync_destroy'):
    csync_destroy = _lib.csync_destroy
    csync_destroy.argtypes = [POINTER(CSYNC)]
    csync_destroy.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 269
if hasattr(_lib, 'csync_add_exclude_list'):
    csync_add_exclude_list = _lib.csync_add_exclude_list
    csync_add_exclude_list.argtypes = [POINTER(CSYNC), String]
    csync_add_exclude_list.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 278
if hasattr(_lib, 'csync_get_config_dir'):
    csync_get_config_dir = _lib.csync_get_config_dir
    csync_get_config_dir.argtypes = [POINTER(CSYNC)]
    if sizeof(c_int) == sizeof(c_void_p):
        csync_get_config_dir.restype = ReturnString
    else:
        csync_get_config_dir.restype = String
        csync_get_config_dir.errcheck = ReturnString


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 289
if hasattr(_lib, 'csync_set_config_dir'):
    csync_set_config_dir = _lib.csync_set_config_dir
    csync_set_config_dir.argtypes = [POINTER(CSYNC), String]
    csync_set_config_dir.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 298
if hasattr(_lib, 'csync_remove_config_dir'):
    csync_remove_config_dir = _lib.csync_remove_config_dir
    csync_remove_config_dir.argtypes = [POINTER(CSYNC)]
    csync_remove_config_dir.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 307
if hasattr(_lib, 'csync_enable_statedb'):
    csync_enable_statedb = _lib.csync_enable_statedb
    csync_enable_statedb.argtypes = [POINTER(CSYNC)]
    csync_enable_statedb.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 316
if hasattr(_lib, 'csync_disable_statedb'):
    csync_disable_statedb = _lib.csync_disable_statedb
    csync_disable_statedb.argtypes = [POINTER(CSYNC)]
    csync_disable_statedb.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 325
if hasattr(_lib, 'csync_is_statedb_disabled'):
    csync_is_statedb_disabled = _lib.csync_is_statedb_disabled
    csync_is_statedb_disabled.argtypes = [POINTER(CSYNC)]
    csync_is_statedb_disabled.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 335
if hasattr(_lib, 'csync_get_userdata'):
    csync_get_userdata = _lib.csync_get_userdata
    csync_get_userdata.argtypes = [POINTER(CSYNC)]
    csync_get_userdata.restype = POINTER(None)


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 347
if hasattr(_lib, 'csync_set_userdata'):
    csync_set_userdata = _lib.csync_set_userdata
    csync_set_userdata.argtypes = [POINTER(CSYNC), POINTER(None)]
    csync_set_userdata.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 357
if hasattr(_lib, 'csync_get_auth_callback'):
    csync_get_auth_callback = _lib.csync_get_auth_callback
    csync_get_auth_callback.argtypes = [POINTER(CSYNC)]
    csync_get_auth_callback.restype = csync_auth_callback


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 368
if hasattr(_lib, 'csync_set_auth_callback'):
    csync_set_auth_callback = _lib.csync_set_auth_callback
    csync_set_auth_callback.argtypes = [POINTER(CSYNC), csync_auth_callback]
    csync_set_auth_callback.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 379
if hasattr(_lib, 'csync_set_log_verbosity'):
    csync_set_log_verbosity = _lib.csync_set_log_verbosity
    csync_set_log_verbosity.argtypes = [POINTER(CSYNC), c_int]
    csync_set_log_verbosity.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 388
if hasattr(_lib, 'csync_get_log_verbosity'):
    csync_get_log_verbosity = _lib.csync_get_log_verbosity
    csync_get_log_verbosity.argtypes = [POINTER(CSYNC)]
    csync_get_log_verbosity.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 398
if hasattr(_lib, 'csync_get_log_callback'):
    csync_get_log_callback = _lib.csync_get_log_callback
    csync_get_log_callback.argtypes = [POINTER(CSYNC)]
    csync_get_log_callback.restype = csync_log_callback


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 409
if hasattr(_lib, 'csync_set_log_callback'):
    csync_set_log_callback = _lib.csync_set_log_callback
    csync_set_log_callback.argtypes = [POINTER(CSYNC), csync_log_callback]
    csync_set_log_callback.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 418
if hasattr(_lib, 'csync_get_statedb_file'):
    csync_get_statedb_file = _lib.csync_get_statedb_file
    csync_get_statedb_file.argtypes = [POINTER(CSYNC)]
    if sizeof(c_int) == sizeof(c_void_p):
        csync_get_statedb_file.restype = ReturnString
    else:
        csync_get_statedb_file.restype = String
        csync_get_statedb_file.errcheck = ReturnString


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 427
if hasattr(_lib, 'csync_enable_conflictcopys'):
    csync_enable_conflictcopys = _lib.csync_enable_conflictcopys
    csync_enable_conflictcopys.argtypes = [POINTER(CSYNC)]
    csync_enable_conflictcopys.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 436
if hasattr(_lib, 'csync_set_local_only'):
    csync_set_local_only = _lib.csync_set_local_only
    csync_set_local_only.argtypes = [POINTER(CSYNC), c_uint8]
    csync_set_local_only.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 443
if hasattr(_lib, 'csync_get_local_only'):
    csync_get_local_only = _lib.csync_get_local_only
    csync_get_local_only.argtypes = [POINTER(CSYNC)]
    csync_get_local_only.restype = c_uint8


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 446
if hasattr(_lib, 'csync_get_status'):
    csync_get_status = _lib.csync_get_status
    csync_get_status.argtypes = [POINTER(CSYNC)]
    csync_get_status.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 449
if hasattr(_lib, 'csync_set_status'):
    csync_set_status = _lib.csync_set_status
    csync_set_status.argtypes = [POINTER(CSYNC), c_int]
    csync_set_status.restype = c_int


csync_treewalk_visit_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(TREE_WALK_FILE), POINTER(None)) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 451

# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 462
if hasattr(_lib, 'csync_walk_local_tree'):
    csync_walk_local_tree = _lib.csync_walk_local_tree
    csync_walk_local_tree.argtypes = [POINTER(CSYNC), POINTER(csync_treewalk_visit_func), c_int]
    csync_walk_local_tree.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 473
if hasattr(_lib, 'csync_walk_remote_tree'):
    csync_walk_remote_tree = _lib.csync_walk_remote_tree
    csync_walk_remote_tree.argtypes = [POINTER(CSYNC), POINTER(csync_treewalk_visit_func), c_int]
    csync_walk_remote_tree.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 482
if hasattr(_lib, 'csync_set_iconv_codec'):
    csync_set_iconv_codec = _lib.csync_set_iconv_codec
    csync_set_iconv_codec.argtypes = [String]
    csync_set_iconv_codec.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 489
if hasattr(_lib, 'csync_get_error'):
    csync_get_error = _lib.csync_get_error
    csync_get_error.argtypes = [POINTER(CSYNC)]
    csync_get_error.restype = CSYNC_ERROR_CODE


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 496
if hasattr(_lib, 'csync_get_error_string'):
    csync_get_error_string = _lib.csync_get_error_string
    csync_get_error_string.argtypes = [POINTER(CSYNC)]
    if sizeof(c_int) == sizeof(c_void_p):
        csync_get_error_string.restype = ReturnString
    else:
        csync_get_error_string.restype = String
        csync_get_error_string.errcheck = ReturnString


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 509
if hasattr(_lib, 'csync_set_module_property'):
    csync_set_module_property = _lib.csync_set_module_property
    csync_set_module_property.argtypes = [POINTER(CSYNC), String, POINTER(None)]
    csync_set_module_property.restype = c_int


enum_csync_notify_type_e = c_int # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 511

CSYNC_NOTIFY_START_DOWNLOAD = 0 # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 511

CSYNC_NOTIFY_START_UPLOAD = (CSYNC_NOTIFY_START_DOWNLOAD + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 511

CSYNC_NOTIFY_PROGRESS = (CSYNC_NOTIFY_START_UPLOAD + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 511

CSYNC_NOTIFY_FINISHED_DOWNLOAD = (CSYNC_NOTIFY_PROGRESS + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 511

CSYNC_NOTIFY_FINISHED_UPLOAD = (CSYNC_NOTIFY_FINISHED_DOWNLOAD + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 511

CSYNC_NOTIFY_ERROR = (CSYNC_NOTIFY_FINISHED_UPLOAD + 1) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 511

csync_progress_callback = CFUNCTYPE(UNCHECKED(None), String, enum_csync_notify_type_e, c_longlong, c_longlong, POINTER(None)) # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 515

# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 524
if hasattr(_lib, 'csync_set_progress_callback'):
    csync_set_progress_callback = _lib.csync_set_progress_callback
    csync_set_progress_callback.argtypes = [POINTER(CSYNC), csync_progress_callback]
    csync_set_progress_callback.restype = c_int


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 531
if hasattr(_lib, 'csync_request_abort'):
    csync_request_abort = _lib.csync_request_abort
    csync_request_abort.argtypes = [POINTER(CSYNC)]
    csync_request_abort.restype = None


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 538
if hasattr(_lib, 'csync_resume'):
    csync_resume = _lib.csync_resume
    csync_resume.argtypes = [POINTER(CSYNC)]
    csync_resume.restype = None


# /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 545
if hasattr(_lib, 'csync_abort_requested'):
    csync_abort_requested = _lib.csync_abort_requested
    csync_abort_requested.argtypes = [POINTER(CSYNC)]
    csync_abort_requested.restype = c_int


csync_tree_walk_file_s = struct_csync_tree_walk_file_s # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 133

csync_s = struct_csync_s # /home/hefee/hg/pyOwnCloud/csync0.70.90.h: 157

# No inserted files

