use anyhow::Context;
use bstr::{BStr, ByteSlice};
use os_str_bytes::RawOsStr;
use std::ffi::OsString;

fn main() -> anyhow::Result<()> {
    let dirpath = std::env::args_os().nth(1).unwrap_or(OsString::from("."));
    for entry in std::fs::read_dir(dirpath).context("Error reading directory")? {
        match entry {
            Ok(entry) => {
                let fname = entry.file_name();
                println!("- Filename: {fname:?}");
                let raw = RawOsStr::new(&fname);
                println!("  RawOsStr: {raw:?}");
                println!("  RawOsStr.as_raw_bytes(): {:?}", BStr::new(raw.as_raw_bytes()));
                match <[u8]>::from_os_str(&fname) {
                    Some(bs) => println!("  bstr: {:?}", BStr::new(bs)),
                    None => println!("  bstr: ERROR"),
                }
            }
            Err(e) => eprintln!("Error getting DirEntry: {e}"),
        }
    }
    Ok(())
}
