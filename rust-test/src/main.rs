use anyhow::Context;
use bstr::{BStr, ByteSlice};
use os_str_bytes::RawOsStr;
use std::ffi::{OsStr, OsString};

fn main() -> anyhow::Result<()> {
    let dirpath = std::env::args_os().nth(1).unwrap_or(OsString::from("."));
    for entry in std::fs::read_dir(dirpath).context("Error reading directory")? {
        match entry {
            Ok(entry) => {
                let fname = entry.file_name();
                println!("- Filename: {fname:?}");
                let raw = RawOsStr::new(&fname);
                println!("  RawOsStr: {raw:?}");
                println!(
                    "  RawOsStr.as_raw_bytes(): {:?}",
                    BStr::new(raw.as_raw_bytes())
                );
                match <[u8]>::from_os_str(&fname) {
                    Some(bs) => println!("  bstr: {:?}", BStr::new(bs)),
                    None => println!("  bstr: ERROR"),
                }
                show_wide(&fname);
            }
            Err(e) => eprintln!("Error getting DirEntry: {e}"),
        }
    }
    Ok(())
}

#[cfg(windows)]
fn show_wide(s: &OsStr) {
    use std::os::windows::ffi::OsStrExt;
    print!("  Wide: \"");
    for wc in s.encode_wide() {
        match char::from_u32(u32::from(wc)) {
            Some(c) => print!("{}", c.escape_debug()),
            None => print!("\\wc{{{:04x}}}", wc),
        }
    }
    println!("\"");
}

#[cfg(not(windows))]
fn show_wide(_: &OsStr) {}
