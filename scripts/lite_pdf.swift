// Usage: swift lite.swift in.pdf out.pdf scale quality
// Light copy for sending: every page becomes one JPEG image (embedded as JPEG, not re-encoded).
import Foundation
import PDFKit
import AppKit
let a = CommandLine.arguments
let doc = PDFDocument(url: URL(fileURLWithPath: a[1]))!
let scale = CGFloat(Double(a[3])!), q = Double(a[4])!
var box = doc.page(at: 0)!.bounds(for: .mediaBox)
let ctx = CGContext(URL(fileURLWithPath: a[2]) as CFURL, mediaBox: &box, nil)!
for i in 0..<doc.pageCount {
    let page = doc.page(at: i)!
    let r = page.bounds(for: .mediaBox)
    let w = Int(r.width * scale), h = Int(r.height * scale)
    let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: w, pixelsHigh: h, bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false, colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)!
    NSGraphicsContext.saveGraphicsState()
    let g = NSGraphicsContext(bitmapImageRep: rep)!
    NSGraphicsContext.current = g
    g.cgContext.setFillColor(NSColor.black.cgColor); g.cgContext.fill(CGRect(x: 0, y: 0, width: w, height: h))
    g.cgContext.scaleBy(x: scale, y: scale)
    page.draw(with: .mediaBox, to: g.cgContext)
    NSGraphicsContext.restoreGraphicsState()
    let jpg = rep.representation(using: .jpeg, properties: [.compressionFactor: q])!
    let img = CGImage(jpegDataProviderSource: CGDataProvider(data: jpg as CFData)!, decode: nil, shouldInterpolate: true, intent: .defaultIntent)!
    ctx.beginPDFPage(nil); ctx.draw(img, in: box); ctx.endPDFPage()
}
ctx.closePDF()
print("pages", doc.pageCount)
