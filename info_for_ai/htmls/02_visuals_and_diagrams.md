# Visuals, diagrams, plots, and structured geometry

Open this module when an HTML artifact contains diagrams, charts, plots, matrices, coordinate maps, structured tables, timelines with meaningful geometry, or comparable visual structures.

Apply `htmls/00_core.md` and `htmls/01_generation_and_interaction.md` first. Before delivery, also apply `htmls/05_verification.md`.

## Geometric integrity for diagrams, plots, and tables

**Invariant:** Diagrams, plots, matrices, tables, and other structured visual components must preserve their geometry and remain legible across responsive sizes and interactive states.

**Invariant:** A diagram or schematic must also be semantically valid and visually interpretable, not merely a collection of well-aligned shapes. Every visible node, connector, label, region, icon, or marker must have a clear role in the concept being explained. Do not ship placeholder geometry, arbitrary boxes or circles, detached labels, decorative connectors, or pseudo-diagrams whose meaning a viewer has to guess. Before delivery, inspect the rendered visual and confirm that the intended entities, relationships, direction, grouping, and emphasis are actually communicated. If the visual does not explain the concept clearly, redesign it or replace it with a simpler representation.

**Invariant:** When interaction changes points, annotations, labels, highlighted regions, series, selections, or explanatory detail around a shared chart, plot, matrix, map, or diagram, the outer visual frame must keep the same width, height, aspect ratio, and coordinate geometry across equivalent states. A sibling detail panel or longer text state must not be allowed to resize the visual through content-dependent grid or flex sizing. Change the visual footprint only when the changed dimensions themselves carry deliberate meaning.

- Give interactive visuals a stable parent footprint. Use techniques such as explicit `aspect-ratio`, bounded dimensions, `min-width:0`, `minmax(0, ...)` grid tracks, non-stretching alignment, or stacked state layers when they prevent sibling content from changing the visual size.
- For diagrams built with CSS, SVG, canvas, or generated markup, inspect the actual rendered result rather than inferring correctness from the source. Confirm that connectors terminate on the intended elements, labels clearly belong to the intended object or relation, flow direction is unambiguous, and no unexplained shape appears to carry meaning accidentally.
- In charts, matrices, coordinate maps, and similar visuals, render axes, grid lines, quadrant dividers, and other structural guides on a background layer behind points, labels, annotations, controls, and explanatory text. Structural lines must not cut through foreground text.
- Prevent visible overlap between labels, annotations, markers, controls, and other foreground elements. If the available space is insufficient, reposition, wrap, abbreviate, reveal progressively, or redesign the component rather than allowing collisions.
- Preserve the intended aspect ratio of geometric primitives. A circle must remain circular rather than becoming an oval, and squares, icons, markers, or nodes must not deform because of flex or grid stretching. Use explicit equal dimensions, `aspect-ratio`, non-stretching alignment, or equivalent constraints where appropriate.
- Active, inactive, selected, hover, and focus states must not change an element's bounding geometry unless the size change itself carries meaning. Prefer color, border, fill, or other non-geometric state cues so selecting one item does not distort neighboring shapes or move axes.
- When interactive states share the same coordinate system, keep the plot area, axes, origin, quadrant boundaries, and scale geometry fixed across selections. Change those only when the underlying scale or coordinate system genuinely changes, and make that change explicit to the user.
- Tables and table-like grids must keep their intended outer boundary and row/column separators straight, aligned, visually continuous, and complete. Prefer semantic tables or one shared CSS grid with common tracks and consistent borders rather than independent line fragments or decorative offsets.

### Connectors between boxes and process steps

**Invariant:** Arrows, chevrons, lines, or other connectors between adjacent boxes, cards, nodes, or process steps must occupy deliberate relation space, connect the intended elements clearly, and avoid intruding into readable content.

- Prefer a dedicated Grid/Flex track, gap region, or connector layer whose footprint is independent from the boxes it connects. Center the connector on the relevant horizontal or vertical axis using layout primitives rather than guessed pixel offsets.
- When a horizontal process reflows into a vertical stack, reorient the connector and keep it centered in the relation space between the two boxes. The responsive state must not leave a detached connector or ambiguous direction.
- If a connector represents a true edge in a node-link diagram rather than a simple interstitial process arrow, its endpoints may meet the node boundary, but the line and arrowhead must still terminate deliberately and must not intrude into the node's readable content area.

**Invariant:** Numeric markers used for ordered steps, sequences, timelines, cards, or similar enumerations must remain legible, geometrically stable, and clearly centered inside their enclosing shape across supported viewports and states. Use audience-appropriate numbering and verify the rendered marker rather than relying on incidental font metrics.

## Visual verification

**Invariant:** Render and visually inspect every diagram or schematic before delivery. Verify semantic correctness as well as geometry: each node, connector, label, grouping, direction, and visual emphasis must match the intended explanation, with no arbitrary or unexplained geometry.

For interactive visuals with a shared frame, compare rendered bounding boxes and aspect ratios across every selectable state when browser tooling permits. Width, height, aspect ratio, axes, origin, and plot frame must remain stable within normal rendering tolerance unless a size or scale change is explicitly intentional.
