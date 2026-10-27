// Usage: swift pdf_pages.swift deck.pdf out_dir [scale]
// Renders every PDF page to out_dir/pN.jpg (default scale 1.3) so the slides can be looked at.
import Foundation
import PDFKit
import AppKit

let args = CommandLine.arguments
let doc = PDFDocument(url: URL(fileURLWithPath: args[1]))!
let scale: CGFloat = args.count > 3 ? CGFloat(Double(args[3])!) : 1.3
print("pages:", doc.pageCount)
for i in 0..<doc.pageCount {
    let page = doc.page(at: i)!
    let box = page.bounds(for: .mediaBox)
    let img = NSImage(size: NSSize(width: box.width * scale, height: box.height * scale))
    img.lockFocus()
    NSColor.white.set(); NSRect(x: 0, y: 0, width: box.width * scale, height: box.height * scale).fill()
    let ctx = NSGraphicsContext.current!.cgContext
    ctx.scaleBy(x: scale, y: scale)
    page.draw(with: .mediaBox, to: ctx)
    img.unlockFocus()
    let rep = NSBitmapImageRep(data: img.tiffRepresentation!)!
    let jpg = rep.representation(using: .jpeg, properties: [.compressionFactor: 0.6])!
    try! jpg.write(to: URL(fileURLWithPath: "\(args[2])/p\(i + 1).jpg"))
}
